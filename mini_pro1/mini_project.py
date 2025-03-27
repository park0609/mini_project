import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtGui, uic
import cx_Oracle
import uuid

#DB연결
#매니저 연결
sid_m = 'XE'
host_m = 'localhost'
port_m = 1521
username_m = 'sampleuser'
password_m = '12345'


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

id = ['sumin0759@gmail.com','dongho7736@gmail.com','guppy135@naver.com','rudwnzlxl6@naver.com']
pwd = ['123456']

#MainWindow(편의점 시스템)실행
class MainWindow(QDialog,QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

        

    def initUI(self):
        uic.loadUi('./mini_pro1/mini_main2.ui', self)
        self.setWindowTitle('편의점 물품 관리 시스템')
    
        self.btn_login.clicked.connect(self.btn_login_click)

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
        elif (login_id == '') or (login_pwd == ''):
            QMessageBox.warning(self,'경고','아이디나 비밀번호가 일치하지 않습니다.')
            return
        elif login_id in id and login_pwd in pwd:
            self.btn_main_to_second()
        
        else: pass

    def btn_main_to_second(self): #상품서비스창과 메인과 연결되있는 버튼 코드
        self.hide()                     
        self.prod = ProdWindow()    
        self.prod.exec()             
        self.show()

            #print('DB입력 진행')
            #values = (login_id, login_pwd) # 변수값 3개를 튜플로 묶어서 
            #self.addData(values) # 튜플을 파라미터로 전달
            #if self.addData(values) == True:
            #    QMessageBox.about(self,'로그인성공','어서오세요!')
            #else:
            #    QMessageBox.about(self,'로그인실패','관리자에게!')
            #self.loadData() #다시 컬럼을 테이블위젯에 띄우기
            #self.clearInput() #input값 삭제 함수


    def create_session(username, role):
    
    #로그인 성공 시, 랜덤한 세션 ID를 생성하여 데이터베이스에 저장한다.
    
        session_id = str(uuid.uuid4())  # 랜덤한 세션 ID 생성
        conn = cx_Oracle.connect("your_user/your_password@your_db")
        cursor = conn.cursor()
    
        query = '''
        INSERT INTO sessions (session_id, username, role) VALUES (:1, :2, :3)
        '''
        cursor.execute(query, (session_id, username, role))
        conn.commit()
    
        return session_id


class ProdWindow(QDialog,QWidget): # 제품관리 시스템 코드
    def __init__(self):
        super(ProdWindow,self).__init__()
        self.initUi()
        self.show()
    
    def initUi(self):
        uic.loadUi('./mini_pro1/mini_prod.ui',self)
        self.setWindowTitle('상품 관리')

    def btn_second_to_third(self): #상품서비스와 발주서비스가 연결되있는 버튼 코드
         self.hide()                     
         self.prod_deli = DeliveryWindow()    
         self.prod_deli.exec()             
         self.show()

    def btn_second_to_main(self): #상품서비스와 발주서비스가 연결되있는 버튼 코드
         self.hide()                     
         self.prod_main = MainWindow()    
         self.prod_main.exec()             
         self.show()
    



class DeliveryWindow(QDialog,QWidget): #발주 시스템 코드
    # 테이블 생성하지 않음 QT디자이너로 완성 하면서 연결 예정 3.26 11시 54분
    def __init__(self):
        super(DeliveryWindow,self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        uic.loadUi('./mini_pro1/mini_delivery.ui',self)
        self.setWindowTitle('발주 신청 및 관리')

    def btn_third_to_second(self): #발주서비스와 상품서비스가 연결되있는 버튼 코드
        self.hide()                     
        self.deli_prod = ProdWindow()    
        self.deli_prod.exec()             
        self.show()

    



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()

#==============================================================================

    #        self.btn_search.clicked.connect(self.btn_search_click)

#   def clearInput(self):
#       self.input_prod_name.clear()
#       self.input_prod_order.clear()
#       self.input_prod_delivery.clear()
        

#    def btn_search_click(self):
#        prod_name = self.input_prod_name.text()
#        if prod_name == '':
#            QMessageBox.about(self,'경고','제품명은 필수입니다!')
#        else:
#            values = (prod_name)
#            self.searchData(values)
#            self.loadData()
#            self.clearInput()

#    def searchData(self, tuples):
#        isSuccede = False #성공여부 플랴그 변수
#        conn = oci.connect(f'{username}/{password}@{host}:{port}/{sid}')
#        cursor = conn.cursor()

 #       try:
 #           conn.begin() # begin 트랜잭션 시작

            #쿼리 작성
 #           query = '''SELECT prod_name,prod_order,prod_delivery
 #                        FROM DELIVERY
 #                       WHERE prod_name = :v_prod_name
 #                   '''
 #           cursor.execute(query, tuples)
 #           conn.commit() 
 #           last_id = cursor.lastrowid
 #           print(last_id) 
 #           isSuccede = True 
 #       except Exception as e:
 #           print(e)
 #           conn.rollback() 
 #           isSuccede = False
 #       finally:
 #           cursor.close()
 #           conn.close()

 #       return isSuccede # 