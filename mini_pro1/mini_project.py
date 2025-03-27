import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtGui, uic
import cx_Oracle as oci
import uuid

#DB연결
#매니저 연결
sid_m = 'XE'
host_m = 'localhost'
port_m = 1521
username_m = 'system'
password_m = 'oracle'


#스태프 연결
sid_s = 'XE'
host_s = 'localhost'
port_s = 1521
username_s = 'staff'
password_s = '12345'


#배달기사 연결
sid_d = 'XE'
host_d = 'localhost'
port_d = 1521
username_d = 'deliver'
password_d = '12345'

#아래 상태창
basic_msg = '편의점 물품 관리 시스템 v 1.0'

main_id = ['sumin0759@gmail.com','dongho7736@gmail.com','a']
deli_id = ['guppy135@naver.com','rudwnzlxl6@naver.com']
pwd = ['123456']

#MainWindow(편의점 시스템)실행
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

        

    def initUI(self):
        uic.loadUi('./mini_pro1/mini_main2.ui',self)
        self.setWindowTitle('편의점 물품 관리 시스템')
    
        self.btn_login.clicked.connect(self.btn_login_click)
        # self.btn_add.clicked.connect(self.btn_add_click)
        # self.btn_mod.clicked.connect(self.btn_mod_click)
        # self.btn_del.clicked.connect(self.btn_del_click)


    def btn_login_click(self):
        login_id = self.input_prod_id.text()
        login_pwd = self.input_prod_pwd.text()


        if (login_id == '') and (login_pwd == ''):
            QMessageBox.about(self,'경고','아이디와 비밀번호 모두 기입하시오!')           
            return # 함수 빠져나가기
        
        elif login_id == '':
            QMessageBox.warning(self,'경고','아이디를 입력하시오!')
            return
        elif login_pwd == '':
            QMessageBox.warning(self,'경고','비밀번호를 입력하시오!')
            return
        
        elif login_id in deli_id and login_pwd in pwd:
            self.btn_main_to_sub()

        elif login_id in main_id and login_pwd in pwd:
            self.btn_main_to_second()
        
        else: pass

    def btn_main_to_second(self): #상품서비스창과 메인과 연결되있는 버튼 코드
        self.hide()                     
        self.prod = ProdWindow()    
        self.prod.exec()             
        self.show()

    
    def btn_main_to_sub(self): #상품서비스창이 배달기사 전용 화면으로 연결되있는 버튼 코드
        self.hide()                     
        self.prod = ProdSubWindow()    
        self.prod.exec()             
        self.show()


# 매니저, 스태프 화면

class ProdWindow(QDialog,QWidget): # 제품관리 시스템 코드
    def __init__(self):
        super(ProdWindow,self).__init__()
        self.initUi()
        self.show()
    
    def initUi(self):
        uic.loadUi('./mini_pro1/final.ui',self)
        self.setWindowTitle('상품 확인 및 관리 시스템')
        self.loadData()
        self.btn_search.clicked.connect(self.btn_search_click)
        self.teamprod.doubleClicked.connect(self.teamprodDoubleClick)

    def btn_second_to_third(self): #상품서비스와 발주서비스가 연결되있는 버튼 코드
         self.hide()                     
         self.prod_deli = DeliveryWindow()    
         self.prod_deli.exec()             
         self.show()

    def clearInput(self):
        self.prod_number.clear()
        self.prod_category.clear()
        self.prod_name.clear()
        self.prod_price.clear()
        self.prod_adult.clear()
        self.prod_amount.clear()

    def makeTable(self, teamprod): # 수정 필요 최종 UI뜨면 맞춰 수정 3월27일 오후5시30분
            self.teamprod.setSelectionMode(QAbstractItemView.SingleSelection) # 단일 row선택모드
            self.teamprod.setEditTriggers(QAbstractItemView.NoEditTriggers) #컬럼수 변경금지
            self.teamprod.setColumnCount(6)
            self.teamprod.setRowCount(len(teamprod))# 커서에 들어있는 데이터 길이만큼 row 생성
            self.teamprod.setHorizontalHeaderLabels(['상품번호','상품카테고리','상품명','상품가격','구매연령제한','상품수량'])

            # 전달받은 cursor를 반복문으로 테이블 위젯에 뿌리는 작업
            for i, (prod_number,prod_category,prod_name,prod_price,prod_adult,prod_amount) in enumerate(teamprod):
                self.teamprod.setItem(i, 0, QTableWidgetItem(str(prod_number))) # oracle number타입은 뿌릴때 str()로 형변환 필요!
                self.teamprod.setItem(i, 1, QTableWidgetItem(prod_category))
                self.teamprod.setItem(i, 2, QTableWidgetItem(prod_name))
                self.teamprod.setItem(i, 3, QTableWidgetItem(str(prod_price)))
                self.teamprod.setItem(i, 4, QTableWidgetItem(prod_adult))
                self.teamprod.setItem(i, 5, QTableWidgetItem(str(prod_amount)))

    def teamprodDoubleClick(self):
        #QMessageBox.about(self,'더블클릭','동작합니다!')
        selected = self.teamprod.currentRow() #현재 선택된 row의 index를 반환하는함수
        number = self.teamprod.item(selected,0).text()
        category = self.teamprod.item(selected,1).text()
        name = self.teamprod.item(selected,2).text()
        price = self.teamprod.item(selected,3).text()
        adult = self.teamprod.item(selected,4).text()
        amount = self.teamprod.item(selected,5).text()

        QMessageBox.about(self,'더블클릭',f'{number},{category},{name},{price},{adult},{amount}')

        self.prod_number.setText(number)
        self.prod_category.setText(category)
        self.prod_name.setText(name)
        self.prod_price.setText(price)
        self.prod_adult.setText(adult)
        self.prod_amount.setText(amount)

    def btn_search_click(self):
        number = self.prod_number.text()
        category = self.prod_category.text()
        name = self.prod_name.text()
        
        

        if name == '' and category == '' and number == '':
            self.loadData()
            return # 함수 빠져나가기
        else: 
            self.searchData(name,number,category) # 튜플을 파라미터로 전달
            if self.searchData(name,number,category) == True:
                return
            else:
                QMessageBox.about(self,'저장실패','관리자에게 문의해주세요!')
            self.loadData() #다시 컬럼을 테이블위젯에 띄우기
            self.clearInput() #input값 삭제 함수

           
    

    # def btn_add_click(self):
    #     std_id = self.input_std_id.text()
    #     std_name = self.input_std_name.text()
    #     std_mobile = self.input_std_mobile.text()
    #     std_regyear = self.input_std_regyear.text()
    #     print(std_name,std_mobile,std_regyear)



    # def btn_mod_click(self):
    #     std_id = self.input_std_id.text()
    #     std_name = self.input_std_name.text()
    #     std_mobile = self.input_std_mobile.text()
    #     std_regyear = self.input_std_regyear.text()
    #     print(std_name,std_mobile,std_regyear)
    


    # def btn_del_click(self):
    #     std_id = self.input_std_id.text()
    #     std_name = self.input_std_name.text()
    #     std_mobile = self.input_std_mobile.text()
    #     std_regyear = self.input_std_regyear.text()
    #     print(std_name,std_mobile,std_regyear)

    def loadData(self):
        # DB연결
        try:
            conn = oci.connect(f'{username_m}/{password_m}@{host_m}:{port_m}/{sid_m}')
            cursor = conn.cursor()

            query = '''
            SELECT *
            FROM MINIPROJECT.TEAMPROD
            '''
            cursor.execute(query)
            teamprod = cursor.fetchall()  # 모든 결과를 가져옵니다.

            self.makeTable(teamprod)  # 새로 생성한 리스트를 파라미터로 전달
        except oci.DatabaseError as e:
            QMessageBox.critical(self, 'DB 오류', f'DB 작업 중 오류 발생: {e}')
        finally:
            cursor.close()
            conn.close()

    def searchData(self, name, number,category):
        # DB연결
        try:
            conn = oci.connect(f'{username_m}/{password_m}@{host_m}:{port_m}/{sid_m}')
            cursor = conn.cursor()

            query = '''
            SELECT *
            FROM MINIPROJECT.TEAMPROD
            where prod_name = :v_name or prod_number = :v_number or prod_category = :v_category
            '''
            cursor.execute(query, {'v_name': name,'v_number':number,'v_category':category})
            teamprod = cursor.fetchall()  # 모든 결과를 가져옵니다.

            if teamprod:  # 데이터가 존재하면
                self.makeTable(teamprod)
                return True
            else:
                return False

            self.makeTable(teamprod)  # 새로 생성한 리스트를 파라미터로 전달
        except oci.DatabaseError as e:
            QMessageBox.critical(self, 'DB 오류', f'DB 작업 중 오류 발생: {e}')
        finally:
            cursor.close()
            conn.close()
    
    # def btn_add_click(self):
    #     std_id = self.input_std_id.text()
    #     std_name = self.input_std_name.text()
    #     std_mobile = self.input_std_mobile.text()
    #     std_regyear = self.input_std_regyear.text()
    #     print(std_name,std_mobile,std_regyear)

    #     # 입력검증 필수(Validation Check)
    #     if std_name == '' or std_regyear == '':
    #         QMessageBox.about(self,'경고','학생이름 또는 입학년도는 필수입니다!')
    #         return # 함수 빠져나가기
    #     elif std_id != '':
    #         QMessageBox.warning(self,'경고','기학생정보를 다시 등록할 수 없습니다!')
    #         return
    #     else:
    #         print('DB입력 진행')
    #         values = (std_name, std_mobile, std_regyear) # 변수값 3개를 튜플로 묶어서 
    #         self.addData(values) # 튜플을 파라미터로 전달
    #         if self.addData(values) == True:
    #             QMessageBox.about(self,'저장성공','학생정보 등록완료!')
    #         else:
    #             QMessageBox.about(self,'저장실패','관리자에게 문의해주세요!')
    #         self.loadData() #다시 컬럼을 테이블위젯에 띄우기
    #         self.clearInput() #input값 삭제 함수

    # def btn_mod_click(self):
    #     std_id = self.input_std_id.text()
    #     std_name = self.input_std_name.text()
    #     std_mobile = self.input_std_mobile.text()
    #     std_regyear = self.input_std_regyear.text()
    #     #print(std_id, std_name,std_mobile,std_regyear)

    #     if std_id == '' or std_name == '' or std_mobile == '' or std_regyear == '':
    #         QMessageBox.about(self,'경고','학생이름 또는 입학년도는 필수입니다!')
    #         return 
    #     else:
    #         print('DB수정진행')    
    #         values = (std_name,std_mobile,std_regyear,std_id)
    #         if self.modData(values) == True:
    #             QMessageBox.about(self,'수정성공','학생정보 수정완료!')
    #         else:
    #             QMessageBox.about(self,'수정실패','관리자에게 문의해주세요!')

    #         self.loadData() 
    #         self.clearInput()
    
    # def btn_del_click(self):
    #     std_id = self.input_std_id.text()
        
    #     if std_id == '':
    #         QMessageBox.warning(self,'경고','학생이름 또는 입학년도는 필수입니다!')
    #         return 
    #     else:
    #         print('DB삭제진행')
    #         # Oracle은 파라미터 타입에 민감. 정확한 타입을 사용해야함
    #         values = (int(std_id),)
    #         if self.delData(values) == True:
    #             QMessageBox.about(self,'삭제성공','학생정보 삭제완료!')
    #         else:
    #             QMessageBox.about(self,'삭제실패','관리자에게 문의해주세요!')

    #         self.loadData() 
    #         self.clearInput()
    
    


# 배달기사 전용 화면
    
class ProdSubWindow(QDialog,QWidget): # 제품관리 시스템 코드
    def __init__(self):
        super(ProdSubWindow,self).__init__()
        self.initUi()
        self.show()
    
    def initUi(self):
        uic.loadUi('./mini_pro1/mini_sub.ui',self)
        self.setWindowTitle('상품 확인 시스템(배달기사 전용)')


class DeliveryWindow(QDialog,QWidget): #발주 시스템 코드
    # 테이블 생성하지 않음 QT디자이너로 완성 하면서 연결 예정 3.26 11시 54분
    def __init__(self):
        super(DeliveryWindow,self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        uic.loadUi('./mini_pro1/order.ui',self)
        self.setWindowTitle('발주 신청 및 관리')
        self.loadData()

    def btn_third_to_second(self): #발주서비스와 상품서비스가 연결되있는 버튼 코드
        self.hide()                     
        self.deli_prod = ProdWindow()    
        self.deli_prod.exec()             
        self.show()
    
    def makeTable(self, delivery): # 수정 필요 최종 UI뜨면 맞춰 수정 3월27일 오후5시30분
            self.delivery.setSelectionMode(QAbstractItemView.SingleSelection) # 단일 row선택모드
            self.delivery.setEditTriggers(QAbstractItemView.NoEditTriggers) #컬럼수 변경금지
            self.delivery.setColumnCount(3)
            self.delivery.setRowCount(len(delivery))# 커서에 들어있는 데이터 길이만큼 row 생성
            self.delivery.setHorizontalHeaderLabels(['상품명','주문일자','입고일자'])

            # 전달받은 cursor를 반복문으로 테이블 위젯에 뿌리는 작업
            for i, (prod_name,prod_order,prod_delivery) in enumerate(delivery):
                self.delivery.setItem(i, 0, QTableWidgetItem(prod_name)) # oracle number타입은 뿌릴때 str()로 형변환 필요!
                self.delivery.setItem(i, 1, QTableWidgetItem(prod_order))
                self.delivery.setItem(i, 2, QTableWidgetItem(prod_delivery))
                

    def loadData(self):
        # DB연결
        try:
            conn = oci.connect(f'{username_m}/{password_m}@{host_m}:{port_m}/{sid_m}')
            cursor = conn.cursor()

            query = '''
            SELECT *
            FROM MINIPROJECT.DELIVERY
            '''
            cursor.execute(query)
            delivery = cursor.fetchall()  # 모든 결과를 가져옵니다.

            self.makeTable(delivery)  # 새로 생성한 리스트를 파라미터로 전달

            if delivery:  # 데이터가 존재하면
                self.makeTable(delivery)
                return True
            else:
                return False

        except oci.DatabaseError as e:
            QMessageBox.critical(self, 'DB 오류', f'DB 작업 중 오류 발생: {e}')
        finally:
            cursor.close()
            conn.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()






