import pymysql
import sys
import pyqtgraph
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import Qt
import csv

form_widget = uic.loadUiType('bicon11.ui')[0]
class Search(QWidget, form_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        if self.home_login_pb.text() == '로그인':
            self.home_login_pb.clicked.connect(self.gologin)
            self.login_student_pb.clicked.connect(self.login)
        elif self.home_login_pb.text() == '로그아웃':
            self.home_login_pb.clicked.connect(self.logout)

    # 시그널 연결
    def gohome(self):
        self.login_SW.setCurrentIndex(0)
    def gologin(self):
        self.login_SW.setCurrentIndex(1)
        self.login_id_lineEdit.clear()
        self.login_pw_lineEdit.clear()


    def login(self):
        if self.login_id_lineEdit.text() == "":
            QMessageBox.critical(self, "로그인 오류", "정보를 입력하세요")
            return
        self.id = self.login_id_lineEdit.text()
        pw = self.login_pw_lineEdit.text()
        check = False
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='0000',
                               db='attendance check')
        a = conn.cursor()
        sql ="SELECT * FROM `attendance check`.data_ai where ID like '%s'"%self.id
        a.execute(sql)
        id_check = a.fetchall()     # 이중 튜플 형태(( ))
        print(id_check)

        if self.id != id_check[0][1]:       # id_check[0][1] = id
            QMessageBox.critical(self, "로그인 오류", "ID를 다시 입력하세요")
        elif pw != id_check[0][2]:     # id_check[0][2] = pw

            QMessageBox.critical(self, "로그인 오류", "비밀번호를 다시 입력하세요")
        elif pw == '':
            QMessageBox.critical(self, "로그인 오류", "비밀번호를 입력하세요")

        else:
            self.check = True
            self.gohome()   # 홈으로 가는 메서드 호출
            self.loginsuccess()     # 메서드 호출
            return True    # 로그인 성공


    # 로그인 성공 시 버튼 텍스트를 로그아웃으로 바꾸는 메서드
    def loginsuccess(self):
        self.home_login_pb.setText('로그아웃')

    def logout(self):
        if self.check == True:
            self.check = False
            self.home_login_pb.setText('로그인')


if __name__ == "__main__":

    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    mainWindow = Search()

    widget.addWidget(mainWindow)

    widget.setFixedHeight(800)
    widget.setFixedWidth(600)
    widget.show()
    app.exec_()