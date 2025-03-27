import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtGui, uic
import cx_Oracle as oci

#DB연결
sid = 'XE'
host = 'localhost'
port = 1521
username = 'sampleuser'
password = '12345'
basic_msg = '편의점 물품 관리 시스템 v 1.0'

#MainWindow(편의점 시스템)실행
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

        #상태바
        self.statusbar.showMessage(basic_msg)

    def initUI(self):
        uic.loadUi('./mini_pro1/mini_main.ui', self)
        self.setWindowTitle('편의점 물품 관리 시스템')

    def btn_main_to_second(self): #발주서비스창과 연결되있는 버튼 코드
        self.hide()                     
        self.second = DeliveryWindow()    
        self.second.exec()             
        self.show()

    def btn_main_to_third(self):
        self.hide()                     
        self.third = ProdWindow()    
        self.third.exec()             
        self.show()

class ProdWindow(QDialog,QWidget): # 제품관리 시스템 코드
    def __init__(self):
        super(ProdWindow,self).__init__()
        self.initUi()
        self.show()
    
    def initUi(self):
        uic.loadUi('./mini_pro1/mini_prod.ui',self)
        self.setWindowTitle('제품 관리')

    def btn_third_to_main(self):
        self.close()




class DeliveryWindow(QDialog,QWidget): #발주 시스템 코드
    # 테이블 생성하지 않음 QT디자이너로 완성 하면서 연결 예정 3.26 11시 54분
    def __init__(self):
        super(DeliveryWindow,self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        uic.loadUi('./mini_pro1/mini_delivery.ui',self)
        self.setWindowTitle('발주 신청 및 관리')

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


    def btn_second_to_main(self):
        self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()