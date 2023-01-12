import datetime

import pymysql
import sys
import pyqtgraph
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from datetime import *
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
        self.out = 0    # 퇴실 이후 또 퇴실버튼 누를 시, 퇴실 누르지 않았을 시 필요. 퇴실 버튼 상태 저장
        self.outback = 0  # 외출, 복귀 할 때 필요, 외출 상태 저장

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
        self.statusboard()  # 메서드 호출(나의 출결현황)

    def goschedule(self):
        self.login_SW.setCurrentIndex(3)
        self.textEdit.clear()
        self.textBrowser.clear()

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
        sql ="SELECT * FROM `attendance check`.data_ai2nd where ID like '%s'"%self.student_id
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
                a.execute(f"UPDATE `attendance check`.data_ai2nd SET 로그인여부 = 'O' WHERE ID = '{id_check[0][1]}'")
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
        sql = "SELECT * FROM `attendance check`.data_ai2nd where ID like '%s'" % self.teacher_id
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
                a.execute(f"UPDATE `attendance check`.data_ai2nd SET 로그인여부 = 'O' WHERE ID = '{id_check[0][1]}'")
                conn.commit()
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
        sql = "SELECT * FROM `attendance check`.data_ai2nd where 로그인여부 like '%s'" %'O'
        a.execute(sql)
        login_check = a.fetchall()  # 이중 튜플 형태(( ))

        for i in range(len(login_check)):
            if self.student_id == login_check[i][1]:
                temp = 1
                f"update data_ai2nd set 로그인여부 = 'X' where ID = '{self.student_id}'"
                conn.commit()

            elif self.teacher_id == login_check[i][1]:
                temp = 2
                f"update data_ai2nd set 로그인여부 = 'X' where ID = '{self.teacher_id}'"
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
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000',
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
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000',
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
        # 퇴실
        if self.out == 1:   # 이미 퇴실버튼 눌렀을 때
            QMessageBox.critical(self, "오류", "이미 퇴실 처리 되었습니다")
        elif self.inout == 1:     # init에서 불러온 변수, 입실한 상태
            if self.outing_label.text() == '' or self.comeback_label.text() == '':  # 외출, 복귀 안했을 경우
                self.showexpulsion()    # 메서드 호출, 퇴실
                self.att_outback_Button.hide()
                self.countattendance()  # 메서드 호출(출석계산)
                self.countleave()  # 메서드 호출(조퇴계산)
            else:
                self.showexpulsion()  # 메서드 호출, 퇴실
                self.att_outback_Button.hide()
                self.countattendance()  # 메서드 호출(출석계산)

        # 입실
        else:
            entrance_datetime = datetime.now()
            self.entrance_time = entrance_datetime.strftime('%H.%M.%S')
            self.att_inout_Button.setText('퇴실')
            self.entrance_label.setText(self.entrance_time)
            self.countlate()  # 메서드 호출(지각계산)
            self.inout = 1
            self.att_outback_Button.show()


    def showexpulsion(self):    # def showentrance에 호출 됨
        expulsion_datetime = datetime.now()
        self.expulsion_time = expulsion_datetime.strftime('%H.%M.%S')
        self.att_inout_Button.setText('입실')
        self.expulsion_label.setText(self.expulsion_time)
        self.out = 1


    def showouting(self):
        if self.outback == 1:
            self.showcomeback()
        else:
            self.outing_datetime = datetime.now()
            self.outing_time = self.outing_datetime.strftime('%H.%M.%S')
            self.att_outback_Button.setText('복귀')
            self.outing_label.setText(self.outing_time)
            self.outback = 1

    def showcomeback(self):
        self.comeback_datetime = datetime.now()
        self.comeback_time = self.comeback_datetime.strftime('%H.%M.%S')
        self.att_outback_Button.setText('외출')
        self.comeback_label.setText(self.comeback_time)
        self.countouting()  # 메서드 호출(외출계산)

    def statusboard(self):
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000',
                               db='attendance check')
        a = conn.cursor()
        sql = f"SELECT * FROM data_ai2nd where ID like '{self.student_id}'"
        a.execute(sql)
        appear = a.fetchall()  # 이중 튜플 형태(( ))
        self.myatt_label.setText(str(appear[0][11]))     # 출석
        self.mylate_label.setText(str(appear[0][12]))    # 지각
        self.myleave_label.setText(str(appear[0][13]))   # 조퇴
        self.myouting_label.setText(str(appear[0][14]))  # 외출
        self.myabsent_label.setText(str(appear[0][15]))  # 결석

    def countattendance(self):    # def showexplusion에 추가할 메서드
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000',
                               db='attendance check')
        a = conn.cursor()
        sql = f"SELECT * FROM data_ai2nd where ID like '{self.student_id}'"
        a.execute(sql)
        user_info = a.fetchall()  # 이중 튜플 형태(( ))
        print(user_info)
        if self.entrance_time < '09.21.00' and self.expulsion_time >= '17.01.00' and user_info[0][7] != '' and user_info[0][10] != '':
            calatt= int(user_info[0][11]) + 1
            print(calatt)
            a.execute(f"UPDATE data_ai2nd SET 출석횟수 = {calatt} WHERE ID = '{self.student_id}'")
            conn.commit()
            print("****")
        # else:
        #     print("조건 불만족")

    def countlate(self):
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='0000',
                               db='attendance check')
        a = conn.cursor()
        sql = f"SELECT * FROM data_ai2nd where ID like '{self.student_id}'"
        a.execute(sql)
        user_info = a.fetchall()  # 이중 튜플 형태(( ))
        if self.entrance_time > '09.20.59':
            callate = int(user_info[0][12]) + 1
            a.execute(f"UPDATE data_ai2nd SET 지각횟수 = {callate} WHERE ID = '{self.student_id}'")
            conn.commit()

    def countleave(self):
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000',
                               db='attendance check')
        a = conn.cursor()
        sql = f"SELECT * FROM data_ai2nd where ID like '{self.student_id}'"
        a.execute(sql)
        user_info = a.fetchall()  # 이중 튜플 형태(( ))
        two_hour_later = self.outing_datetime + timedelta(hours=2)  #외출 후 2시간 경과
        if (self.expulsion_time >'13.00.00' and self.expulsion_time < '17.01.00') or self.comeback_datetime > two_hour_later or user_info[0][8] == '0':
            calleave = int(user_info[0][13]) + 1
            a.execute(f"UPDATE data_ai2nd SET 조퇴횟수 = {calleave} WHERE ID = '{self.student_id}'")
            conn.commit()

    def countouting(self):
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='0000',
                               db='attendance check')
        a = conn.cursor()
        sql = f"SELECT * FROM data_ai2nd where ID like '{self.student_id}'"
        a.execute(sql)
        user_info = a.fetchall()  # 이중 튜플 형태(( ))
        two_hour_later = self.outing_datetime + timedelta(hours=2)
        if self.att_inout_Button.text() == '퇴실' and self.comeback_datetime <= two_hour_later:
            calouting = int(user_info[0][14]) + 1
            a.execute(f"UPDATE data_ai2nd SET 외출횟수 = {calouting} WHERE ID = '{self.student_id}'")
            conn.commit()

    def countabsent(self):
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000',
                               db='attendance check')
        a = conn.cursor()
        sql = f"SELECT * FROM data_ai2nd where ID like '{self.student_id}'"
        a.execute(sql)
        user_info = a.fetchall()  # 이중 튜플 형태(( ))
        if (user_info[0][7] == '' or self.entrance_time > '13.00.00') or (user_info[0][10] == '0' or self.expulsion_time < '13.00.00'):
            calabsent = int(user_info[0][15]) + 1
            a.execute(f"UPDATE data_ai2nd SET 결석 = {calabsent} WHERE ID = '{self.student_id}'")
            conn.commit()










if __name__ == "__main__":

    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    mainWindow = Search()

    widget.addWidget(mainWindow)

    widget.setFixedHeight(921)
    widget.setFixedWidth(601)
    widget.show()
    app.exec_()