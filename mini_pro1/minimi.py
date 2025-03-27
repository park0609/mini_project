import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtGui, uic
import cx_Oracle
import uuid

class login(QDialog):
    def __init__(self):
        super(login, self).__init__()
        uic.loadUi('C:\Source\java-database-2025\mini_pro1\mini_main2.ui', self)
        self.btn_login.clicked.connet(self.loginfunction)
        self.login_pwd.setEchoMode(QWidget.QlineEdit.login_pwd)

    def loginfunction(self):
        login_id = self.input_prod_id.text()
        login_pwd = self.input_prod_pwd.text()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = login()
    win.show()
    app.exec()