import pymysql
import sys
import pyqtgraph
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import Qt
import csv

form_widget = uic.loadUiType('bicon11.ui')[0]
class Search(QWidget, form_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.log = 0  # 로그인 ,로그 아웃 할 때 필요, 로그인 상태 저장
        self.inout = 0  # 입실, 퇴실 할 때 필요, 입실 상태 저장

        self.login_SW.setCurrentIndex(0)
        self.att_outback_Button.hide()

        # 페이지 이동
        self.home_schedule_pb.clicked.connect(self.goschedule)
        self.home_login_pb.clicked.connect(self.gologin)
        self.home_attendance_pb.clicked.connect(self.goattendance)
        self.login_Home_Button.clicked.connect(self.gohome)
        self.att_Home_Button.clicked.connect(self.gohome)
        self.calendar_Home_Button1.clicked.connect(self.gohome)
        self.calendar_Home_Button2.clicked.connect(self.gohome)

        self.login_student_pb.clicked.connect(self.studentlogin)
        self.login_teacher_pb.clicked.connect(self.teacherlogin)
        self.calendarWidget.clicked.connect(self.choicedate)
        self.addschedule_pb.clicked.connect(self.addschedule)
        self.att_inout_Button.clicked.connect(self.showentrance)
        self.att_outback_Button.clicked.connect(self.showouting)


    # 시그널 연결
    def gohome(self):
        self.login_SW.setCurrentIndex(0)
    def gologin(self):
        # 로그아웃
        if self.log == 1:  # init에서 불러온 변수, 로그인 된 상태
            self.logout()
            self.login_SW.setCurrentIndex(0)
        else:
            self.login_SW.setCurrentIndex(1)    # 로그인 페이지로 가기
            self.login_id_lineEdit.clear()
            self.login_pw_lineEdit.clear()

    def goattendance(self):
        self.login_SW.setCurrentIndex(2)

    def goschedule(self):
        self.login_SW.setCurrentIndex(3)
        self.textEdit.clear()
        self.textBrowser.clear()
        #self.att_outback_Button.hide()

    def studentlogin(self):
        self.student_id = self.login_id_lineEdit.text()
        pw = self.login_pw_lineEdit.text()

        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='0000',
                               db='attendance check')
        a = conn.cursor()
        sql ="SELECT * FROM `attendance check`.data_ai where ID like '%s'"%self.student_id
        a.execute(sql)
        id_check = a.fetchall()     # 이중 튜플 형태(( ))

        if id_check[0][4] == '학생':
            if self.login_id_lineEdit.text() == "":
                QMessageBox.critical(self, "로그인 오류", "정보를 입력하세요")
                return

            if self.student_id != id_check[0][1]:       # id_check[0][1] = id
                QMessageBox.critical(self, "로그인 오류", "ID를 다시 입력하세요")
            elif pw != id_check[0][2]:     # id_check[0][2] = pw

                QMessageBox.critical(self, "로그인 오류", "비밀번호를 다시 입력하세요")
            elif pw == '':
                QMessageBox.critical(self, "로그인 오류", "비밀번호를 입력하세요")

            else:
                # 로그인 성공
                a.execute(f"UPDATE `attendance check`.data_ai SET 로그인여부 = 'O' WHERE ID = '{id_check[0][1]}'")
                conn.commit()
                self.gohome()   # 홈으로 가는 메서드 호출
                self.home_login_pb.setText('로그아웃')
                self.log = 1    # init에서 불러온 변수(로그인 상태 저장)
                return True
            a.close()
        else:
            QMessageBox.critical(self, "로그인 오류", "학생이 아닙니다")

    def teacherlogin(self):
        self.teacher_id = self.login_id_lineEdit.text()
        pw = self.login_pw_lineEdit.text()
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='0000',
                               db='attendance check')
        a = conn.cursor()
        sql = "SELECT * FROM `attendance check`.data_ai where ID like '%s'" % self.teacher_id
        a.execute(sql)
        id_check = a.fetchall()  # 이중 튜플 형태(( ))
        if id_check[0][4] == '교수':
            if self.login_id_lineEdit.text() == "":
                QMessageBox.critical(self, "로그인 오류", "정보를 입력하세요")
                return

            if self.teacher_id != id_check[0][1]:  # id_check[0][1] = id
                QMessageBox.critical(self, "로그인 오류", "ID를 다시 입력하세요")
            elif pw != id_check[0][2]:  # id_check[0][2] = pw

                QMessageBox.critical(self, "로그인 오류", "비밀번호를 다시 입력하세요")
            elif pw == '':
                QMessageBox.critical(self, "로그인 오류", "비밀번호를 입력하세요")

            else:
                # 로그인 성공
                a.execute(f"UPDATE `attendance check`.data_ai SET 로그인여부 = 'O' WHERE ID = '{id_check[0][1]}'")
                conn.commit()
                print(id_check[0][26])
                self.gohome()  # 홈으로 가는 메서드 호출
                self.home_login_pb.setText('로그아웃')
                self.log = 1  # init에서 불러온 변수(로그인 상태 저장)
                return True
            a.close()
        else:
            QMessageBox.critical(self, "로그인 오류", "교사가 아닙니다")


    # 로그인 성공 시 버튼 텍스트를 로그아웃으로 바꾸는 메서드
    # def loginsuccess(self):     # 굳이 메서드로 안 만들어도 될듯.....?
    #     self.home_login_pb.setText('로그아웃')

    def logout(self):
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='0000',
                               db='attendance check')
        a = conn.cursor()
        sql = "SELECT * FROM `attendance check`.data_ai where 로그인여부 like '%s'" %'O'
        a.execute(sql)
        login_check = a.fetchall()  # 이중 튜플 형태(( ))

        for i in range(len(login_check)):
            if self.student_id == login_check[i][1]:
                temp = 1
                f"update data_ai set 로그인여부 = 'X' where ID = '{self.student_id}'"
                conn.commit()

            elif self.teacher_id == login_check[i][1]:
                temp = 2
                f"update data_ai set 로그인여부 = 'X' where ID = '{self.teacher_id}'"
                conn.commit()

        QMessageBox.information(self, "로그아웃", "로그아웃 됐습니다")
        self.home_login_pb.setText('로그인')
        a.close()

    def choicedate(self):
        self.textBrowser.clear()    # 페이지 나갔다 들어올 때 빈 칸으로 보이기 위함
        # addschedule에서 필요한 값이기 때문에 self 붙여줌
        self.date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")   # 선택한 날짜 정보 문자열로 반환
        self.cb_name = self.comboBox.currentText()

        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='0000',
                               db='attendance check')
        a = conn.cursor()
        a.execute(f"SELECT memo FROM `attendance check`.schedule where name like '{self.cb_name}' and date1 like '{self.date}'")
        all_memo = a.fetchall()  # 이중 튜플 형태(( ))
        print(all_memo)
        for i in all_memo:
            self.textBrowser.append(str(i[0]))


    def addschedule(self):
        self.choicedate()   # 메서드 호출

        # 일정 페이지로 넘어올 때 clear 헤주려고 self 붙여줌
        self.memo_data = self.textEdit.toPlainText()
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='0000',
                               db='attendance check')
        a = conn.cursor()
        sql = f"SELECT * FROM `attendance check`.schedule where name like '{self.cb_name}'"
        a.execute(sql)
        add_memo = a.fetchall()  # 이중 튜플 형태(( ))
        if str(self.cb_name) == add_memo[0][0]:
            a.execute(f"INSERT INTO schedule (name, ID, date1, memo) VALUES ('{self.cb_name}','{add_memo[0][1]}','{self.date}','{self.memo_data}')")
            conn.commit()
        self.textBrowser.append(self.memo_data)
        a.close()

    def showentrance(self):
        if self.inout == 1:     # init에서 불러온 변수, 입실한 상태
            self.showexpulsion()    # 메서드 호출, 퇴실
        else:
            entrance_time = QTime.currentTime().toString('hh.mm.ss')
            self.att_inout_Button.setText('퇴실')
            self.entrance_label.setText(entrance_time)
            self.inout = 1
            self.att_outback_Button.show()

    def showexpulsion(self):    # def showentrance에 호출 됨
        expulsion_time = QTime.currentTime().toString('hh.mm.ss')
        self.att_inout_Button.setText('입실')
        self.expulsion_label.setText(expulsion_time)

    def showouting(self):
        outing_time = QTime.currentTime().toString('hh.mm.ss')
        self.att_outback_Button.setText('복귀')
        self.outing_label.setText(outing_time)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    mainWindow = Search()

    widget.addWidget(mainWindow)

    widget.setFixedHeight(800)
    widget.setFixedWidth(600)
    widget.show()
    app.exec_()