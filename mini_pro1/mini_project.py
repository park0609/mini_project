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

main_id = ['sumin0759@gmail.com','dongho7736@gmail.com']
deli_id = ['guppy135@naver.com','rudwnzlxl6@naver.com']
pwd = ['123456']

#MainWindow(편의점 시스템)실행
class MainWindow(QDialog,QWidget):
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
        uic.loadUi('./mini_pro1/mini_prod.ui',self)
        self.setWindowTitle('상품 확인 및 관리 시스템')

    def btn_second_to_third(self): #상품서비스와 발주서비스가 연결되있는 버튼 코드
         self.hide()                     
         self.prod_deli = DeliveryWindow()    
         self.prod_deli.exec()             
         self.show()


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
