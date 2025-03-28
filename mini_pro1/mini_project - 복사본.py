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
deli_id = ['guppy135@naver.com','rudwnzlxl6@naver.com',"b"]
pwd = ['123456']

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

        

    def initUI(self):
        uic.loadUi('./mini_pro1/mini_main2.ui',self)
        self.setWindowTitle('편의점 물품 관리 시스템')
    
        self.btn_login.clicked.connect(self.btn_login_click)


    def btn_login_click(self):
        login_id = self.input_prod_id.text()
        login_pwd = self.input_prod_pwd.text()


        if (login_id == '') and (login_pwd == ''):
            QMessageBox.about(self,'경고','아이디와 비밀번호 모두 기입하시오!')           
            return 
        
        elif login_id == '':
            QMessageBox.warning(self,'경고','아이디를 입력하시오!')
            return
        elif login_pwd == '':
            QMessageBox.warning(self,'경고','비밀번호를 입력하시오!')
            return
        
        elif login_id in main_id and login_pwd in pwd:
            self.btn_main_to_second()
            return
        
        elif login_id in deli_id and login_pwd in pwd:
            self.btn_main_to_sub()
            return
        
        else: pass

    def btn_main_to_second(self): 
        self.hide()                     
        self.prod = ProdWindow()    
        self.prod.exec()             
        self.show()

    
    def btn_main_to_sub(self): 
        self.hide()                     
        self.prod = ProdSubWindow()    
        self.prod.exec()             
        self.show()

class ProdWindow(QDialog,QWidget): 
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

    def btn_second_to_third(self): 
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

    def makeTable(self, teamprod): 
            self.teamprod.setSelectionMode(QAbstractItemView.SingleSelection) 
            self.teamprod.setEditTriggers(QAbstractItemView.NoEditTriggers) 
            self.teamprod.setColumnCount(6)
            self.teamprod.setRowCount(len(teamprod))
            self.teamprod.setHorizontalHeaderLabels(['상품번호','상품카테고리','상품명','상품가격','구매연령제한','상품수량'])

           
            for i, (prod_number,prod_category,prod_name,prod_price,prod_adult,prod_amount) in enumerate(teamprod):
                self.teamprod.setItem(i, 0, QTableWidgetItem(str(prod_number)))
                self.teamprod.setItem(i, 1, QTableWidgetItem(prod_category))
                self.teamprod.setItem(i, 2, QTableWidgetItem(prod_name))
                self.teamprod.setItem(i, 3, QTableWidgetItem(str(prod_price)))
                self.teamprod.setItem(i, 4, QTableWidgetItem(prod_adult))
                self.teamprod.setItem(i, 5, QTableWidgetItem(str(prod_amount)))

    def teamprodDoubleClick(self):
        
        selected = self.teamprod.currentRow() 
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
            return 
        else: 
            self.searchData(name,number,category) 
            if self.searchData(name,number,category) == True:
                return
            else:
                QMessageBox.about(self,'검색실패','관리자에게 문의해주세요!')
            self.loadData() 
            self.clearInput() 


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
            teamprod = cursor.fetchall()  

            self.makeTable(teamprod) 
        except oci.DatabaseError as e:
            QMessageBox.critical(self, 'DB 오류', f'DB 작업 중 오류 발생: {e}')
        finally:
            cursor.close()
            conn.close()

    def searchData(self, name, number,category):
       
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

            self.makeTable(teamprod) 
        except oci.DatabaseError as e:
            QMessageBox.critical(self, 'DB 오류', f'DB 작업 중 오류 발생: {e}')
        finally:
            cursor.close()
            conn.close()
    


# 배달기사 전용 화면
    
class ProdSubWindow(QDialog,QWidget): # 제품관리 시스템 코드
    def __init__(self):
        super(ProdSubWindow,self).__init__()
        self.initUi()
        self.show()
    
    def initUi(self):
        uic.loadUi('./mini_pro1/delivery.ui',self)
        self.setWindowTitle('상품 확인 시스템(배달기사 전용)')
        self.btn_search_d.clicked.connect(self.btn_search_d_click)

    # 검색 버튼 
    def btn_search_d_click(self):
        deliverydate = self.prod_delivery.text().strip()  # 공백 제거

        # 입력값 검증
        if not deliverydate:
            QMessageBox.warning(self, '경고', '발주현황 조회시 도착일 입력은 필수입니다!')
            return

        # 날짜 형식 확인
        from datetime import datetime
        try:
            datetime.strptime(deliverydate, '%Y-%m-%d')  # 'YYYY-MM-DD' 형식 확인
        except ValueError:
            QMessageBox.warning(self, '경고', '도착일은 YYYY-MM-DD 형식으로 입력해야 합니다!')
            return
        success = self.searchDeliveryData(deliverydate)
        if success:
            QMessageBox.information(self, '성공', '조회가 성공적으로 완료되었습니다!')
        else:
            QMessageBox.about(self, '검색실패', '관리자에게 문의해주세요!')
            self.DeliveryloadData()

    def DeliveryloadData(self):
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
        except oci.DatabaseError as e:
            QMessageBox.critical(self, 'DB 오류', f'DB 작업 중 오류 발생: {e}')
        finally:
            cursor.close()
            conn.close()

    def searchDeliveryData(self,deliverydate):
        # DB연결
        try:
            conn = oci.connect(f'{username_m}/{password_m}@{host_m}:{port_m}/{sid_m}')
            cursor = conn.cursor()

            query = '''
            SELECT *
            FROM MINIPROJECT.DELIVERY
            WHERE PROD_DELIVERY = TO_DATE(:v_deliverydate, 'YYYY-MM-DD')
            '''
            cursor.execute(query, {'v_deliverydate': deliverydate})
            delivery = cursor.fetchall()  # 모든 결과를 가져옵니다.

            if delivery:  # 데이터가 존재하면
                self.makeTable(delivery)
                return True
            else:
                return False

            self.makeTable(delivery)  # 새로 생성한 리스트를 파라미터로 전달
        except oci.DatabaseError as e:
            QMessageBox.critical(self, 'DB 오류', f'DB 작업 중 오류 발생: {e}')
        finally:
            cursor.close()
            conn.close()

    def makeTable(self, delivery): # 수정 필요 최종 UI뜨면 맞춰 수정 3월27일 오후5시30분
            self.delivery.setSelectionMode(QAbstractItemView.SingleSelection) # 단일 row선택모드
            self.delivery.setEditTriggers(QAbstractItemView.NoEditTriggers) #컬럼수 변경금지
            self.delivery.setColumnCount(3)
            self.delivery.setRowCount(len(delivery))# 커서에 들어있는 데이터 길이만큼 row 생성
            self.delivery.setHorizontalHeaderLabels(['상품명','주문일','도착예정일'])

            # 전달받은 cursor를 반복문으로 테이블 위젯에 뿌리는 작업
            for i, (prod_name,prod_order,prod_delivery) in enumerate(delivery):
                self.delivery.setItem(i, 0, QTableWidgetItem(prod_name)) # oracle number타입은 뿌릴때 str()로 형변환 필요!
                self.delivery.setItem(i, 1, QTableWidgetItem(str(prod_order)))
                self.delivery.setItem(i, 2, QTableWidgetItem(str(prod_delivery)))  

class DeliveryWindow(QDialog,QWidget):
    def __init__(self):
        super(DeliveryWindow,self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        uic.loadUi('./mini_pro1/order.ui',self)
        self.setWindowTitle('발주 신청 및 관리')
        self.loadData()
        self.btn_search.clicked.connect(self.btn_search_click)
        self.btn_add.clicked.connect(self.addData)
        self.initTable()
        

    def btn_third_to_second(self): 
        self.hide()                     
        self.deli_prod = ProdWindow()    
        self.deli_prod.exec()             
        self.show()
    
    def initTable(self):
        self.delivery.setColumnCount(4)
        self.delivery.setHorizontalHeaderLabels(['상품명', '주문일자', '입고일자','발주수량'])
        self.delivery.setEditTriggers(self.delivery.NoEditTriggers)
    
    def initTable(self):
        """QTableWidget 초기화"""
        self.delivery.setColumnCount(4)  
        self.delivery.setHorizontalHeaderLabels(['상품명', '주문일자', '입고일자', '발주수량'])
        self.delivery.setEditTriggers(QTableWidget.NoEditTriggers) 
        self.delivery.setSelectionMode(QTableWidget.SingleSelection)
    
    def makeTable(self, delivery): 
            self.delivery.setSelectionMode(QAbstractItemView.SingleSelection)
            self.delivery.setEditTriggers(QAbstractItemView.NoEditTriggers) 
            self.delivery.setColumnCount(4)
            self.delivery.setRowCount(len(delivery))
            self.delivery.setHorizontalHeaderLabels(['상품명','주문일자','입고일자','발주수량'])

            
            for i, (prod_name,prod_order,prod_delivery,amount) in enumerate(delivery):
                self.delivery.setItem(i, 0, QTableWidgetItem(str(prod_name))) 
                self.delivery.setItem(i, 1, QTableWidgetItem(prod_order))
                self.delivery.setItem(i, 2, QTableWidgetItem(prod_delivery))
                self.delivery.setItem(i, 3, QTableWidgetItem(str(amount)))
    
    def btn_search_click(self):
        name = self.prod_name.text()
        order = self.prod_orderdate.text()
        delivery_d = self.prod_delidate.text()
        

        if name == '' and order == '' and delivery_d == '':
            self.loadData()
            return 
        else: 
            self.searchData(name) 
            if self.searchData(name) == True:
                return
            else:
                QMessageBox.about(self,'검색실패','관리자에게 문의해주세요!')
            self.loadData() 

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
            delivery = cursor.fetchall() 

            self.makeTable(delivery)  

            if delivery: 
                self.makeTable(delivery)
                return True
            else:
                return False

        except oci.DatabaseError as e:
            QMessageBox.critical(self, 'DB 오류', f'DB 작업 중 오류 발생: {e}')
        finally:
            cursor.close()
            conn.close()

    def searchData(self, name):
        # DB연결
        try:
            conn = oci.connect(f'{username_m}/{password_m}@{host_m}:{port_m}/{sid_m}')
            cursor = conn.cursor()

            query = '''
            SELECT prod_name, SYSDATE AS order_date, SYSDATE + 3 AS delivery_date
                FROM MINIPROJECT.DELIVERY
              WHERE prod_name = :v_name 
            '''
            cursor.execute(query, {'v_name': name})
            delivery = cursor.fetchall()  

            if delivery:
                self.makeTable(delivery)
                return True
            else:
                return False

        except oci.DatabaseError as e:
            QMessageBox.critical(self, 'DB 오류', f'DB 작업 중 오류 발생: {e}')
        finally:
            cursor.close()
            conn.close()

    def addData(self):
        prod_name = self.prod_name.text()  
        amount = self.prod_amount.text()  

        if not prod_name or not amount:
            QMessageBox.warning(self, "경고", "상품명과 수량을 입력하세요!")
            return

        try:
            # Oracle DB 연결
            conn = oci.connect(f'{username_m}/{password_m}@{host_m}:{port_m}/{sid_m}')
            cursor = conn.cursor()

            # 테이블 업데이트 쿼리 작성
            query = '''
            INSERT INTO MINIPROJECT.DELIVERY 
		        (prod_name,prod_order,prod_delivery,amount)
	        VALUES (:v_prod_name,sysdate,sysdate+3,:v_amount)
            '''
            cursor.execute(query, {'v_prod_name': prod_name, 'v_amount': amount})
            conn.commit()  # 트랜잭션 커밋

            query = '''
            SELECT prod_name, prod_order, prod_delivery, amount
            FROM MINIPROJECT.delivery
            WHERE prod_name = :v_prod_name
            '''
            cursor.execute(query, {'v_prod_name': prod_name})
            updated_rows = cursor.fetchall()  # 업데이트된 데이터 가져오기

            if updated_rows:
                self.displayUpdates(updated_rows)
                QMessageBox.information(self, "성공", "주문이 성공적으로 업데이트되었습니다!")
            else:
                QMessageBox.information(self, "정보", "해당 상품명이 존재하지 않습니다.")

        except oci.DatabaseError as e:
            QMessageBox.critical(self, "DB 오류", f"오류: {e}")
        finally:
            cursor.close()
            conn.close()

    def displayUpdates(self, rows):

        self.delivery.setRowCount(len(rows))  
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                self.delivery.setItem(i, j, QTableWidgetItem(str(value)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()