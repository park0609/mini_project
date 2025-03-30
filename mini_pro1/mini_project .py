import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtGui, uic
from datetime import datetime
import cx_Oracle as oci
import uuid
from prod import prodname

#DB연결
sid_m = 'XE'
host_m = '210.119.14.67'
port_m = 1521
username_m = 'MINIPRO'
password_m = '12345'
basic_msg = '편의점 물품 관리 시스템 v 1.0'
main_id = ['sumin0759@gmail.com','dongho7736@gmail.com','a']
deli_id = ['guppy135@naver.com','rudwnzlxl6@naver.com',"b"]
pwd = ['123456']
# 로그인 실패 횟수 제한
login_attempts = 0
max_attempts = 5

# 자동 로그인 세션 저장용
session = {'user_id': None, 'role': None}

# 상태 메시지
basic_msg = '편의점 물품 관리 시스템 v1.0'

# 로그인 화면 창
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('./mini_pro1/main.ui',self)
        self.setWindowTitle('편의점 물품 관리 시스템')
        self.btn_login.clicked.connect(self.btn_login_click)
        # 버튼 클릭 이벤트 연결

        # 엔터 키로 로그인 실행 (비밀번호 입력칸 기준)
        self.input_pwd.returnPressed.connect(self.btn_login_click)

        # # 자동 로그인 체크
        # if session['user_id']:
        #     self.open_product_window(session['user_id'], session['role'])
        

    def clearInput(self):
        self.input_id.clear() 
        self.input_pwd.clear()  

    def btn_login_click(self):
        login_id = self.input_id.text()
        login_pwd = self.input_pwd.text()
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
        T_ID = self.input_id.text()
        T_PW = self.input_pwd.text()

        if T_ID == '' or T_PW == '':
            QMessageBox.warning(self, '경고', '아이디,비밀번호 입력은 필수 입니다!')
            return  
        else:
            print('로그인 진행!') 
            values = (T_ID, T_PW)
            if self.addData(values) == True:  
                QMessageBox.about(self, '로그인 성공!', '선생님 어서오세요! ')
            else: 
                QMessageBox.about(self, '로그인 실패!', '로그인 실패, 관리자에게 문의하세요.')
        self.clearInput()

    # def addData(self, values):
    #     isSucceed = False  
    #     conn = oci.connect(f'{username_m}/{password_m}@{host_m}:{port_m}/{sid_m}')
    #     cursor = conn.cursor()
    #     try:
    #         query = '''
    #                 SELECT COUNT(*)
    #                   FROM MINIPRO.cmemberlist
    #                  WHERE USER_ID = :v_T_ID
    #                    AND USER_PW = :v_T_PW
    #                 '''
    #         cursor.execute(query, {'v_T_ID': values[0], 'v_T_PW': values[1]})
    #         result = cursor.fetchone()
    #         if result[0] > 0:
    #             isSucceed = True
    #     except Exception as e:
    #         print(f"❌ 오류 발생: {e}")
    #     finally:
    #         cursor.close()
    #         conn.close()
    #     return isSucceed  
    
 

    # def btn_login_click(self):
    #     global login_attempts

    #     login_id = self.input_id.text()
    #     login_pwd = self.input_pwd.text()

    #     # 로그인 입력 검증
    #     if not login_id or not login_pwd:
    #         QMessageBox.warning(self, '경고', '아이디와 비밀번호를 모두 입력하세요!')
    #         return

    #     # 로그인 확인 및 역할 부여
    #     if login_id in main_id and login_pwd in pwd:
    #         QMessageBox.information(self, '로그인 성공', f'어서오세요, {login_id}님!')
    #         role = 'manager'  # 매니저 역할 부여
    #         session['user_id'] = login_id
    #         session['role'] = role
    #         self.open_product_window(login_id, role)

    #     elif login_id in deli_id and login_pwd in pwd:
    #         QMessageBox.information(self, '로그인 성공', f'어서오세요, {login_id}님!')
    #         role = 'deliver'  # 배달기사 역할 부여
    #         session['user_id'] = login_id
    #         session['role'] = role
    #         self.open_sub_window()#login_id, role)

    #     else:
    #         login_attempts += 1
    #         if login_attempts >= max_attempts:
    #             QMessageBox.critical(self, '로그인 차단', '로그인 시도 5회를 초과하여 차단되었습니다.')
    #             self.close()
    #         else:
    #             QMessageBox.warning(self, '경고', f'아이디나 비밀번호가 일치하지 않습니다. ({max_attempts - login_attempts}회 남음)')

    # def open_product_window(self, user_id, role):
    #     self.hide()
    #     self.prod_window = ProdWindow(user_id, role)  # user_id와 role 전달
    #     self.prod_window.exec()
    #     self.show()
    
    # def open_sub_window(self, user_id, role):
    #     self.hide()
    #     self.prod_sub_window = DeliveryWindow(user_id, role)

    
    def btn_main_to_second(self):
        self.prod = ProdWindow()
        self.prod.show()                
        self.close()                     
        self.deleteLater()

    def btn_main_to_sub(self): 
        self.prod_deli = ProdSubWindow()  
        self.prod_deli.show()
        self.close()                       
        self.deleteLater() 

# 제품조회 창
class ProdWindow(QDialog,QWidget): 
    def __init__(self):
        super(ProdWindow,self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        uic.loadUi('./mini_pro1/teamprod.ui',self)
        self.setWindowTitle('상품 확인 및 관리 시스템')
        self.loadData()
        self.btn_search.clicked.connect(self.btn_search_click)
        self.teamprod.doubleClicked.connect(self.teamprodDoubleClick)
        self.btn_search.setIcon(QIcon('C:\\Source\\mini_project\\mini_pro1\\200image\\find.png'))
        self.pushButton_2.setIcon(QIcon('C:\\Source\\mini_project\\mini_pro1\\200image\\order2.png'))
        self.pushButton_3.setIcon(QIcon('C:\\Source\\mini_project\\mini_pro1\\200image\\sell.png'))
        
    def btn_second_to_third(self): 
        self.prod_deli = DeliveryWindow()  
        self.prod_deli.show()
        self.close()                       
        self.deleteLater()

    def btn_second_to_forth(self): 
        self.prod_deli = HistoryWindow()  
        self.prod_deli.show()
        self.close()                       
        self.deleteLater()

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
        self.prod_number.setText(number)
        self.prod_category.setText(category)
        self.prod_name.setText(name)
        self.prod_price.setText(price)
        self.prod_adult.setText(adult)
        self.prod_amount.setText(amount)
        self.label.setPixmap(QtGui.QPixmap(prodname[name])) 

    def btn_search_click(self):
        number = self.prod_number.text()
        category = self.prod_category.text()
        name = self.prod_name.text()
        if name == '' and category == '' and number == '':
            self.loadData()
            return 
        else: 
            if self.searchData(name,number,category) == True:
                if name == '':
                    self.label.setPixmap(QtGui.QPixmap(prodname[number])) 
                elif number == '':    
                    self.label.setPixmap(QtGui.QPixmap(prodname[name]))
                else: pass 
                return
            else:
                QMessageBox.about(self,'검색실패','관리자에게 문의해주세요!')
            self.loadData() 
            self.clearInput() 

    def loadData(self):
        try:
            conn = oci.connect(f'{username_m}/{password_m}@{host_m}:{port_m}/{sid_m}')
            cursor = conn.cursor()
            query = '''
            SELECT *
            FROM MINIPRO.TEAMPROD
            '''
            cursor.execute(query)
            teamprod = cursor.fetchall()  
            self.makeTable(teamprod)
            self.label.setPixmap(QtGui.QPixmap('C:\\Source\\mini_project\\mini_pro1\\200image\\normal.png')) 
        except oci.DatabaseError as e:
            QMessageBox.critical(self, 'DB 오류', f'DB 작업 중 오류 발생: {e}')
        finally:
            cursor.close()
            conn.close()

    def searchData(self, name, number, category):
        try:
            conn = oci.connect(f'{username_m}/{password_m}@{host_m}:{port_m}/{sid_m}')
            cursor = conn.cursor()
            query = '''
            SELECT *
            FROM MINIPRO.TEAMPROD
            where prod_name = :v_name or prod_number = :v_number or prod_category = :v_category
            '''
            cursor.execute(query, {'v_name': name,'v_number':number,'v_category':category})
            teamprod = cursor.fetchall()  
            if teamprod:  
                self.makeTable(teamprod)
                return True
            else:
                return False
        except oci.DatabaseError as e:
            QMessageBox.critical(self, 'DB 오류', f'DB 작업 중 오류 발생: {e}')
        finally:
            cursor.close()
            conn.close()
    
# 배달기사 전용 화면
class ProdSubWindow(QDialog,QWidget): 
    def __init__(self):
        super(ProdSubWindow,self).__init__()
        self.initUi()
        self.show()
    
    def initUi(self):
        uic.loadUi('./mini_pro1/delivery.ui',self)
        self.setWindowTitle('상품 확인 시스템(배달기사 전용)')
        self.btn_search_d.clicked.connect(self.btn_search_d_click)
        self.setWindowIcon(QIcon('C:\\Source\\mini_project\\mini_pro1\\200image\\deli.png'))
        self.btn_search_d.setIcon(QIcon('C:\\Source\\mini_project\\mini_pro1\\200image\\find.png'))

    def btn_search_d_click(self, deliverydate):
        deliverydate = self.prod_delivery.text()  
        if not deliverydate:
            QMessageBox.warning(self, '경고', '발주현황 조회시 도착일 입력은 필수입니다!')
            return
        try:
            datetime.strptime(deliverydate, '%Y-%m-%d')  
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
        try:
            conn = oci.connect(f'{username_m}/{password_m}@{host_m}:{port_m}/{sid_m}')
            cursor = conn.cursor()
            query = '''
            SELECT *
            FROM MINIPRO.DELIVERY
            '''
            cursor.execute(query)
            delivery = cursor.fetchall()  
            self.makeTable(delivery)  
        except oci.DatabaseError as e:
            QMessageBox.critical(self, 'DB 오류', f'DB 작업 중 오류 발생: {e}')
        finally:
            cursor.close()
            conn.close()

    def searchDeliveryData(self, deliverydate):
        try:
            conn = oci.connect(f'{username_m}/{password_m}@{host_m}:{port_m}/{sid_m}')
            cursor = conn.cursor()
            query = '''
            SELECT prod_name, prod_order, substr(to_char(prod_delivery, 'YYYY-MM-DD'), 1, 10), amount
            FROM MINIPRO.DELIVERY
            WHERE PROD_DELIVERY = TO_date(:v_deliverydate , 'YYYY-MM-DD')
            '''
            cursor.execute(query, {'v_deliverydate': deliverydate})
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

    def makeTable(self, delivery): 
            self.delivery.setSelectionMode(QAbstractItemView.SingleSelection) 
            self.delivery.setEditTriggers(QAbstractItemView.NoEditTriggers) 
            self.delivery.setColumnCount(4)
            self.delivery.setRowCount(len(delivery))
            self.delivery.setHorizontalHeaderLabels(['상품명','주문일','도착예정일','발주수량'])

            for i, (prod_name,prod_order,prod_delivery,amount) in enumerate(delivery):
                self.delivery.setItem(i, 0, QTableWidgetItem(prod_name)) 
                self.delivery.setItem(i, 1, QTableWidgetItem(str(prod_order)))
                self.delivery.setItem(i, 2, QTableWidgetItem(str(prod_delivery)))
                self.delivery.setItem(i, 3, QTableWidgetItem(str(amount)))  

# 발주조회 창
class DeliveryWindow(QDialog,QWidget):
    def __init__(self):
        super(DeliveryWindow,self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        uic.loadUi('./mini_pro1/order.ui',self)
        self.setWindowTitle('발주 신청 및 관리')
        self.loadData()
        self.btn_search_2.clicked.connect(self.btn_search_click)
        self.btn_add.clicked.connect(self.addData)
        self.btn_mod.clicked.connect(self.btn_mod_click)
        self.btn_del.clicked.connect(self.btn_del_click)
        self.initTable()
        self.btn_search_2.setIcon(QIcon('C:\\Source\\mini_project\\mini_pro1\\200image\\find.png'))
        self.btn_add.setIcon(QIcon('C:\\Source\\mini_project\\mini_pro1\\200image\\plus.png'))
        self.btn_mod.setIcon(QIcon('C:\\Source\\mini_project\\mini_pro1\\200image\\mod.png'))
        self.btn_del.setIcon(QIcon('C:\\Source\\mini_project\\mini_pro1\\200image\\del.png'))
        self.pushButton_2.setIcon(QIcon('C:\\Source\\mini_project\\mini_pro1\\200image\\order.png'))
        
    def btn_third_to_second(self): 
        self.deli_prod = ProdWindow()                     
        self.deli_prod.show()
        self.close()                
        self.deleteLater()

    def initTable(self):
        self.delivery.setColumnCount(4)
        self.delivery.setHorizontalHeaderLabels(['상품명', '주문일자', '입고일자','발주수량'])
        self.delivery.setEditTriggers(self.delivery.NoEditTriggers)
    
    def initTable(self):
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
                self.delivery.setItem(i, 1, QTableWidgetItem(str(prod_order)))
                self.delivery.setItem(i, 2, QTableWidgetItem(str(prod_delivery)))
                self.delivery.setItem(i, 3, QTableWidgetItem(str(amount)))
    
    def btn_search_click(self):
        name = self.prod_name.text()
        if name == '':
            self.loadData()
            return 
        else: 
            self.searchData(name) 
            if self.searchData(name) == True:
                return
            else:
                QMessageBox.about(self,'검색실패','관리자에게 문의해주세요!')
            self.loadData() 

    def btn_mod_click(self):
        name = self.prod_name.text()
        amount = self.prod_amount.text()
        if name == '' and amount == '':
            self.loadData()
            return 
        else: 
            if self.modData(name,amount) == True:
                return
            else: 
                QMessageBox.about(self,'수정성공!','발주수량이 변경되었습니다!')
            self.loadData()

    def btn_del_click(self):
        name = self.prod_name.text()
        if name == '':
            self.loadData()
            return 
        else:
            if self.delData(name) == True:
                QMessageBox.about(self,'삭제성공','학생정보 삭제완료!')
            else:
                QMessageBox.about(self,'삭제실패','관리자에게 문의해주세요!')
            self.loadData() 

    def loadData(self):
        try:
            conn = oci.connect(f'{username_m}/{password_m}@{host_m}:{port_m}/{sid_m}')
            cursor = conn.cursor()
            query = '''
            SELECT prod_name, prod_order, substr(to_char(prod_delivery, 'YYYY-MM-DD'),1 , 10), amount
            FROM MINIPRO.DELIVERY
            '''
            cursor.execute(query)
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

    def searchData(self, name):
        try:
            conn = oci.connect(f'{username_m}/{password_m}@{host_m}:{port_m}/{sid_m}')
            cursor = conn.cursor()
            query = '''
            SELECT *
                FROM MINIPRO.DELIVERY
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
            conn = oci.connect(f'{username_m}/{password_m}@{host_m}:{port_m}/{sid_m}')
            cursor = conn.cursor()
            query = '''
            INSERT INTO MINIPRO.DELIVERY
		        (prod_name,prod_order,prod_delivery,amount)
	        VALUES (:v_prod_name,trunc(sysdate),trunc(sysdate+3),:v_amount)
            '''
            cursor.execute(query, {'v_prod_name': prod_name, 'v_amount': amount})
            conn.commit()  
            query = '''
            SELECT prod_name, prod_order, to_char(prod_delivery, 'YYYY-MM-DD'), amount
            FROM MINIPRO.delivery
            WHERE prod_name = :v_prod_name
            '''
            cursor.execute(query, {'v_prod_name': prod_name})
            updated_rows = cursor.fetchall()  
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

    def modData(self, name, amount):
        name = self.prod_name.text()  
        amount = self.prod_amount.text()  
        if not name or not amount:
            QMessageBox.warning(self, "경고", "상품명과 수량을 입력하세요!")
            return
        try:
            conn = oci.connect(f'{username_m}/{password_m}@{host_m}:{port_m}/{sid_m}')
            cursor = conn.cursor()
            query = '''
            UPDATE MINIPRO.DELIVERY SET
  	             amount = :v_amount
                , prod_order = sysdate 
                , prod_delivery = sysdate + 3
             WHERE prod_name = :v_name
            '''
            cursor.execute(query, {'v_name': name, 'v_amount': amount})
            conn.commit()
        except oci.DatabaseError as e:
            QMessageBox.critical(self, "DB 오류", f"오류: {e}")
        finally:
            cursor.close()
            conn.close()

    def delData(self,name):
        name = self.prod_name.text()
        isSuccede = False 
        conn = oci.connect(f'{username_m}/{password_m}@{host_m}:{port_m}/{sid_m}')
        cursor = conn.cursor()
        try:
            conn.begin() 
            query = '''
                    UPDATE MINIPRO.DELIVERY SET
  	                      amount = null
                        , prod_order = null
                        , prod_delivery = null
                    WHERE prod_name = :v_name
                    '''
            cursor.execute(query, {'v_name':name})
            conn.commit() 
            isSuccede = True 
        except Exception as e:
            print(e)
            conn.rollback() 
            isSuccede = False
        finally:
            cursor.close()
            conn.close()
        return isSuccede

    def displayUpdates(self, rows):
        self.delivery.setRowCount(len(rows))  
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                self.delivery.setItem(i, j, QTableWidgetItem(str(value)))

# 판매 화면 창
class HistoryWindow(QDialog, QWidget):
    def __init__(self):
        super(HistoryWindow, self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        uic.loadUi('./mini_pro1/history.ui', self)
        self.setWindowTitle('상품판매 시스템')
        self.loadData()
        self.btn_add.clicked.connect(self.btn_add_click)
        self.btn_del.clicked.connect(self.btn_del_click)
        self.btn_add.setIcon(QIcon('C:\\Source\\mini_project\\mini_pro1\\200image\\plus.png'))
        self.btn_del.setIcon(QIcon('C:\\Source\\mini_project\\mini_pro1\\200image\\del.png'))
        self.pushButton_3.setIcon(QIcon('C:\\Source\\mini_project\\mini_pro1\\200image\\sell.png'))
        self.pushButton_4.setIcon(QIcon('C:\\Source\\mini_project\\mini_pro1\\200image\\order2.png'))
    
    def btn_forth_to_second(self): 
        self.deli_prod = ProdWindow()                     
        self.deli_prod.show()
        self.close()                
        self.deleteLater()

    def btn_forth_to_third(self): 
        self.deli_prod = DeliveryWindow()                     
        self.deli_prod.show()
        self.close()                
        self.deleteLater()

    def makeTable(self, history):
            self.history.setSelectionMode(QAbstractItemView.SingleSelection)
            self.history.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.history.setColumnCount(5)
            self.history.setRowCount(len(history))
            self.history.setHorizontalHeaderLabels(['판매날짜','상품카테고리','상품명','상품수량','상품가격'])
            for i, (cell_date,prod_category,prod_name,cell_amount,cell_price) in enumerate(history):
                self.history.setItem(i, 0, QTableWidgetItem(str(cell_date))) 
                self.history.setItem(i, 1, QTableWidgetItem(str(prod_category)))
                self.history.setItem(i, 2, QTableWidgetItem(str(prod_name)))
                self.history.setItem(i, 3, QTableWidgetItem(str(cell_amount)))
                self.history.setItem(i, 4, QTableWidgetItem(str(cell_price)))

    def btn_add_click(self):
        category = self.prod_category.text()
        name = self.prod_name.text()
        amount = self.cell_amount.text()
        price = self.cell_price.text()
        if  category == '' and name == ''and price == ''and amount == '':
            self.loadData()
            return 
        else: 
            if self.addData(category,name,price,amount) == True:
                return
            else:
                pass
            self.loadData() 

    def btn_del_click(self):
        name = self.prod_name.text()
        if name == '':
            QMessageBox.warning(self,'경고','제품이름은 필수입니다!')
            return 
        else:
            if self.delData(name) == True:
                self.loadData()
            else: pass
            
    def loadData(self):
        try:
            conn = oci.connect(f'{username_m}/{password_m}@{host_m}:{port_m}/{sid_m}')
            cursor = conn.cursor()
            query = '''
            SELECT *
            FROM MINIPRO.HISTORY
            '''
            cursor.execute(query)
            history = cursor.fetchall() 
            if history: 
                self.makeTable(history)
                return True
            else:
                return False
        except oci.DatabaseError as e:
            QMessageBox.critical(self, 'DB 오류', f'DB 작업 중 오류 발생: {e}')
        finally:
            cursor.close()
            conn.close()

    def addData(self,category,name,price,amount):
        category = self.prod_category.text()
        name = self.prod_name.text()
        amount = self.cell_amount.text()  
        price = self.cell_price.text()
        if  not category or not name or not amount or not price:
            QMessageBox.warning(self, "경고", "상품명과 수량을 입력하세요!")
            return
        try:
            conn = oci.connect(f'{username_m}/{password_m}@{host_m}:{port_m}/{sid_m}')
            cursor = conn.cursor()
            query = '''
            INSERT INTO MINIPRO.HISTORY 
              (cell_date,prod_category,prod_name,cell_amount,cell_price)
           VALUES (sysdate,:v_prod_category,:v_prod_name,:v_cell_amount,:v_cell_price)
            '''
            cursor.execute(query, {'v_prod_category' : category,'v_prod_name': name, 'v_cell_amount': amount, 'v_cell_price' : price})
            conn.commit()  
            query = '''
            SELECT *
            FROM MINIPRO.HISTORY
            WHERE prod_name = :v_prod_name
            '''
            cursor.execute(query, {'v_prod_name': name})
            updated_rows = cursor.fetchall() 
            if updated_rows:
                self.makeTable(updated_rows)
                QMessageBox.information(self, "성공", "주문이 성공적으로 업데이트되었습니다!")
            else:
                QMessageBox.information(self, "정보", "해당 상품명이 존재하지 않습니다.")
        except oci.DatabaseError as e:
            QMessageBox.critical(self, "DB 오류", f"오류: {e}")
        finally:
            cursor.close()
            conn.close()

    def delData(self, name):
        name = self.prod_name.text()    
        conn = oci.connect(f'{username_m}/{password_m}@{host_m}:{port_m}/{sid_m}')
        cursor = conn.cursor()
        try:
            conn.begin() 
            query = '''
                    DELETE FROM MINIPRO.history
                     WHERE prod_name= :v_prod_name
                    '''
            cursor.execute(query, {'v_prod_name': name})
            conn.commit() 
        except Exception as e:
            print(e)
            conn.rollback()    
        finally:
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())



