import datetime
import pymysql
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from datetime import *
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import font_manager, rc
# 한글 폰트 사용을 위해서 세팅, 폰트 경로 설정
font_path = "C:\\Windows\\Fonts\\gulim.ttc"
# 폰트 패스를 통해 폰트 세팅해 폰트 이름 반환받아 font 변수에 삽입
font = font_manager.FontProperties(fname=font_path).get_name()
# 폰트 설정
rc('font', family=font)

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
        self.home_message_pb.clicked.connect(self.gomessage)
        self.message_Home_Button.clicked.connect(self.gohome)
        self.message_Home_Button_2.clicked.connect(self.gohome)

        self.login_student_pb.clicked.connect(self.studentlogin)
        self.login_teacher_pb.clicked.connect(self.teacherlogin)
        self.calendarWidget.clicked.connect(self.choicedate)
        self.addschedule_pb.clicked.connect(self.addschedule)
        self.att_inout_Button.clicked.connect(self.showentrance)
        self.att_outback_Button.clicked.connect(self.showouting)
        self.send_pb.clicked.connect(self.sendmessage)
        self.comboBox2.currentIndexChanged.connect(self.sendmessage)
        self.send_pb_2.clicked.connect(self.psendmessage)
        self.comboBox3.currentIndexChanged.connect(self.psendmessage)
        self.att_graph_Button.clicked.connect(self.studentgraph)
        self.att_graph_Button2.clicked.connect(self.classgraph)


        # tableWidget 열 넓이 조절
        self.tableWidget.setColumnWidth(2, 130)
        self.tableWidget.setColumnWidth(3, 200)

        #graph
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.fig2 = plt.Figure()
        self.canvas2 = FigureCanvas(self.fig2)


    # 시그널 연결
    def gohome(self):
        self.login_SW.setCurrentIndex(0)
    def gologin(self):
        # 로그아웃
        if self.log == 1 or self.log == 2:  # init에서 불러온 변수, 로그인 된 상태
            self.logout()
            self.login_SW.setCurrentIndex(0)
        else:
            self.login_SW.setCurrentIndex(1)    # 로그인 페이지로 가기
            # self.login_id_lineEdit.clear()
            # self.login_pw_lineEdit.clear()

    def goattendance(self):
        if self.log == 0:
            QMessageBox.information(self, "알림", "로그인 후 이용 가능합니다")
            self.login_SW.setCurrentIndex(0)
        else:
            now = datetime.now()
            now1 = now.strftime('%Y-%m-%d')     # 오늘 날짜
            # MySQL에서 import 해오기
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000',
                                   db='attendance check')
            a = conn.cursor()
            sql = f"INSERT INTO attendance (id, date, check_in, check_out, outing, comeback) values ('{self.id}', '{now1}', '', '', '', '')"
            a.execute(sql)
            conn.commit()
            self.login_SW.setCurrentIndex(2)
            # 메서드 호출
            self.countattendance() # 출석 계산
            self.countlate()    # 지각 계산
            #self.countleave()   # 조퇴 계산
            # self.countouting()  # 외출 계산
            self.countabsent()  # 결석 계산
            self.statusboard()  # 나의 출결 현황

    def goschedule(self):
        if self.log == 0:
            QMessageBox.information(self, "알림", "로그인 후 이용 가능합니다")
            self.login_SW.setCurrentIndex(0)
        else:
            self.login_SW.setCurrentIndex(3)
            self.textEdit.clear()
            self.textBrowser.clear()

    def gomessage(self):
        if self.log == 0:
            QMessageBox.information(self, "알림", "로그인 후 이용 가능합니다")
            self.login_SW.setCurrentIndex(0)
        else:
            if self.log == 1:
                self.login_SW.setCurrentIndex(5)
            elif self.log == 2:
                self.login_SW.setCurrentIndex(6)


# 로그인 / 로그아웃
    def studentlogin(self):
        self.id = self.login_id_lineEdit.text()
        pw = self.login_pw_lineEdit.text()

        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000',
                               db='attendance check')
        a = conn.cursor()
        sql ="SELECT * FROM `attendance check`.data_ai2nd where ID like '%s'"%self.id
        a.execute(sql)
        id_check = a.fetchall()     # 이중 튜플 형태(( ))

        if id_check[0][4] == '학생':
            if self.login_id_lineEdit.text() == "":
                QMessageBox.critical(self, "로그인 오류", "정보를 입력하세요")
                return

            if self.id != id_check[0][1]:       # id_check[0][1] = id
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
        self.id = self.login_id_lineEdit.text()
        pw = self.login_pw_lineEdit.text()
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='0000',
                               db='attendance check')
        a = conn.cursor()
        sql = "SELECT * FROM `attendance check`.data_ai2nd where ID like '%s'" % self.id
        a.execute(sql)
        id_check = a.fetchall()  # 이중 튜플 형태(( ))
        if id_check[0][4] == '교수':
            if self.login_id_lineEdit.text() == "":
                QMessageBox.critical(self, "로그인 오류", "정보를 입력하세요")
                return

            if self.id != id_check[0][1]:  # id_check[0][1] = id
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
                self.log = 2  # init에서 불러온 변수(로그인 상태 저장)
                return True
            a.close()
        else:
            QMessageBox.critical(self, "로그인 오류", "교사가 아닙니다")

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
            if self.id == login_check[i][1]:
                self.log = 0
                f"update data_ai2nd set 로그인여부 = 'X' where ID = '{self.id}'"
                conn.commit()
        QMessageBox.information(self, "로그아웃", "로그아웃 됐습니다")
        self.home_login_pb.setText('로그인')
        a.close()

# 일정 추가
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

# 츌결
    def showentrance(self):
        now = datetime.now()
        now1 = now.strftime('%Y-%m-%d')
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000',
                               db='attendance check')
        a = conn.cursor()
        # 퇴실
        if self.out == 1:   # 이미 퇴실버튼 눌렀을 때
            QMessageBox.critical(self, "오류", "이미 퇴실 처리 되었습니다")
        elif self.inout == 1:     # init에서 불러온 변수, 입실한 상태
            if self.outing_label.text() == '' or self.comeback_label.text() == '':  # 외출, 복귀 안했을 경우
                self.showexpulsion()    # 메서드 호출, 퇴실
                self.att_outback_Button.hide()
            else:
                self.showexpulsion()  # 메서드 호출, 퇴실
                self.att_outback_Button.hide()

        # 입실
        else:
            entrance_datetime = datetime.now()
            self.entrance_time = entrance_datetime.strftime('%H:%M')
            sql = f"UPDATE attendance SET check_in = '{self.entrance_time}' where id = '{self.id}' and date = '{now1}'"
            a.execute(sql)
            conn.commit()
            self.att_inout_Button.setText('퇴실')
            self.entrance_label.setText(self.entrance_time)
            self.inout = 1
            self.att_outback_Button.show()

    def showexpulsion(self):    # def showentrance에 호출 됨
        now = datetime.now()
        now1 = now.strftime('%Y-%m-%d')
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000',
                               db='attendance check')
        a = conn.cursor()
        expulsion_datetime = datetime.now()
        self.expulsion_time = expulsion_datetime.strftime('%H:%M')
        self.countleave()  # 조퇴 계산
        sql = f"UPDATE attendance SET check_out = '{self.expulsion_time}' where id = '{self.id}' and date = '{now1}'"
        a.execute(sql)
        conn.commit()
        self.att_inout_Button.setText('입실')
        self.expulsion_label.setText(self.expulsion_time)
        self.out = 1

    def showouting(self):
        now = datetime.now()
        now1 = now.strftime('%Y-%m-%d')
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000',
                               db='attendance check')
        a = conn.cursor()
        if self.outback == 1:
            self.showcomeback()
        else:
            self.outing_datetime = datetime.now()
            self.outing_time = self.outing_datetime.strftime('%H.%M')
            sql = f"UPDATE attendance SET outing = '{self.outing_time}' where id = '{self.id}' and date = '{now1}'"
            a.execute(sql)
            conn.commit()
            conn.close()
            self.att_outback_Button.setText('복귀')
            self.outing_label.setText(self.outing_time)
            self.outback = 1

    def showcomeback(self):
        now = datetime.now()
        now1 = now.strftime('%Y-%m-%d')
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000',
                               db='attendance check')
        a = conn.cursor()
        self.comeback_datetime = datetime.now()
        self.comeback_time = self.comeback_datetime.strftime('%H.%M')
        self.countouting()  # 외출 계산
        sql = f"UPDATE attendance SET comeback = '{self.comeback_time}' where id = '{self.id}' and date = '{now1}'"
        a.execute(sql)
        conn.commit()
        conn.close()
        self.att_outback_Button.hide()
        self.comeback_label.setText(self.comeback_time)

    def statusboard(self):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000',
                               db='attendance check')
        a = conn.cursor()
        sql = f"SELECT * FROM data_ai2nd where id like '{self.id}'"
        a.execute(sql)
        user_info = a.fetchall()
        self.myatt_label.setText(str(user_info[0][11]))     # 출석
        self.mylate_label.setText(str(user_info[0][12]))    # 지각
        self.myleave_label.setText(str(user_info[0][13]))   # 조퇴
        self.myouting_label.setText(str(user_info[0][14]))  # 외출
        self.myabsent_label.setText(str(user_info[0][15]))  # 결석

    def countattendance(self):    # def showexplusion에 추가할 메서드
        now = datetime.now()
        now1 = now.strftime('%Y-%m-%d')
        yesterday = now - timedelta(days=1)

        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000',
                               db='attendance check')
        a = conn.cursor()
        sql = f"SELECT * FROM attendance where id like '{self.id}' and date != '{now1}'"
        a.execute(sql)
        user_info = a.fetchall()  # 이중 튜플 형태((id, date, check_in, check_out, outing, comeback), )
        self.calatt = 0
        for i in user_info:
             if i[2] < '09:21' and i[3] >= '17:01' and i[2] != '' and i[3] != '':
                self.calatt += 1
        save = f"UPDATE data_ai2nd set 출석횟수 = {self.calatt} where ID like '{self.id}'"
        a.execute(save)
        conn.commit()

    def countlate(self):
        now = datetime.now()
        now1 = now.strftime('%Y-%m-%d')
        yesterday = now - timedelta(days=1)
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000',
                               db='attendance check')
        a = conn.cursor()
        sql = f"SELECT * FROM attendance where id like '{self.id}' and date != '{now1}'"
        a.execute(sql)
        user_info = a.fetchall()  # 이중 튜플 형태(( ))
        self.callate = 0
        for i in user_info:
            if i[2] >= '09.21':
                self.callate += 1
        save = f"UPDATE data_ai2nd set 지각횟수 = {self.callate} where ID like '{self.id}'"
        a.execute(save)
        conn.commit()

    def countleave(self):
        now = datetime.now()
        now1 = now.strftime('%Y-%m-%d')
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000',
                               db='attendance check')
        a = conn.cursor()
        sql = f"SELECT * FROM attendance where ID like '{self.id}' and date != '{now1}'"
        a.execute(sql)
        user_info = a.fetchall()  # 이중 튜플 형태(( ))
        if self.outing_label.text() != '':
            two_hours_later = self.outing_datetime + timedelta(hours=2)  #외출 후 2시간 경과
            self.calleave = 0
            for i in user_info:
                if (i[3] >'13.00' and i[3] < '17.01') or i[4] > two_hours_later.strftime('%H.%M') or i[4] == '':
                    self.calleave += 1
            save = f"UPDATE data_ai2nd set 조퇴횟수 = {self.calleave} where ID like '{self.id}'"
            a.execute(save)
            conn.commit()

    def countouting(self):
        now = datetime.now()
        now1 = now.strftime('%Y-%m-%d')
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000',
                               db='attendance check')
        a = conn.cursor()
        sql = f"SELECT * FROM attendance where ID like '{self.id}' and date != '{now1}'"
        a.execute(sql)
        user_info = a.fetchall()  # 이중 튜플 형태(( ))
        two_hour_later = self.outing_datetime + timedelta(hours=2)
        self.calouting = 0
        for i in user_info:
            if i[2] != '' and i[4] <= two_hour_later.strftime('%H.%M'):
                self.calouting += 1
        save = f"UPDATE data_ai2nd set 외출횟수 = {self.calouting} where ID like '{self.id}'"
        a.execute(save)
        conn.commit()

    def countabsent(self):
        now = datetime.now()
        now1 = now.strftime('%Y-%m-%d')
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000',
                               db='attendance check')
        a = conn.cursor()
        sql = f"SELECT * FROM attendance where ID like '{self.id}' and date != '{now1}'"
        a.execute(sql)
        user_info = a.fetchall()  # 이중 튜플 형태(( ))
        self.calabsent = 0
        for i in user_info:
            if (i[2] == '' or i[2] > '13.00') or (i[3] == '' or i[3] < '13.00'):
                self.calabsent += 1
        save = f"UPDATE data_ai2nd set 결석 = {self.calabsent} where ID like '{self.id}'"
        a.execute(save)
        conn.commit()

# 메세지
    def sendmessage(self):
        contents = self.message_lineEdit.text()
        professor = self.comboBox2.currentText()
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000',
                               db='attendance check')
        a = conn.cursor()
        # DB에 메세지 저장
        sql = f"SELECT * FROM data_ai2nd where ID like '{self.id}'"
        a.execute(sql)
        user_info = a.fetchall()  # 이중 튜플 형태(( ))
        sql1 = f"INSERT INTO message (sender, recipient, date2, letter) VALUES ('{user_info[0][3]}', '{professor}', '{now}', '{contents}')"
        a.execute(sql1)
        conn.commit()
        # DB에서 메세지 로드
        sql2 = f"SELECT * FROM message where sender = '{user_info[0][3]}' and recipient = '{professor}'"
        a.execute(sql2)
        message_info = a.fetchall()
        row = 0
        self.tableWidget.setRowCount(len(message_info))
        for i in message_info:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(i[0]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(i[1]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(i[2]))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(i[3]))
            row += 1

    def psendmessage(self):
        contents = self.message_lineEdit_2.text()
        student = self.comboBox3.currentText()
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000',
                               db='attendance check')
        a = conn.cursor()
        # DB에 메세지 저장
        sql = f"SELECT * FROM data_ai2nd where ID like '{self.id}'"
        a.execute(sql)
        user_info = a.fetchall()  # 이중 튜플 형태(( ))
        sql1 = f"INSERT INTO message (sender, recipient, date2, letter) VALUES ('{user_info[0][3]}', '{student}', '{now}', '{contents}')"
        a.execute(sql1)
        conn.commit()
        # DB에서 메세지 로드
        sql2 = f"SELECT * FROM message where (sender = '{user_info[0][3]}' and recipient = '{student}') or (sender = '{student}' and recipient = '{user_info[0][3]}')"
        a.execute(sql2)
        message_info = a.fetchall()
        row = 0
        self.tableWidget_2.setRowCount(len(message_info))
        for i in message_info:
            self.tableWidget_2.setItem(row, 0, QTableWidgetItem(i[0]))
            self.tableWidget_2.setItem(row, 1, QTableWidgetItem(i[1]))
            self.tableWidget_2.setItem(row, 2, QTableWidgetItem(i[2]))
            self.tableWidget_2.setItem(row, 3, QTableWidgetItem(i[3]))
            row += 1
# 추가기능(그래프)
    def studentgraph(self):
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000',
                               db='attendance check')
        a = conn.cursor()
        sql = f"SELECT * FROM attendance1 where ID like '{self.id}' and date in ('2023-01-02', '2023-01-03', '2023-01-04','2023-01-05', '2023-01-06')"
        a.execute(sql)
        user_info = a.fetchall()  # 이중 튜플 형태(( ))
        calatt = 0
        callate = 0
        calleave = 0
        calouting = 0
        calabsent = 0
        for i in user_info:
            if i[2] < '09:21' and i[3] >= '17:01' and i[2] != '' and i[3] != '':
                calatt += 1
            if i[2] >= '09.21':
                callate += 1
            if (i[3] > '13.00' and i[3] < '17.01') or i[4] == '':
                calleave += 1
            if i[2] != '' and i[4]:
                calouting += 1
            if (i[2] == '' or i[2] > '13.00') or (i[3] == '' or i[3] < '13.00'):
                calabsent += 1

        x = ['출석', '지각', '조퇴', '외출', '결석']
        y = [calatt,calatt,calleave,calouting,calabsent]
        self.verticalLayout.addWidget(self.canvas)
        ax = self.fig.add_subplot(111)
        ax.bar(x, y)
        ax.set_xlabel("x")
        ax.set_xlabel("y")
        ax.set_title("나의 출석 현황")
        self.canvas.draw()

    def classgraph(self):
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000',
                               db='attendance check')
        a = conn.cursor()
        sql = f"SELECT * FROM attendance1 where date in ('2023-01-02', '2023-01-03', '2023-01-04','2023-01-05', '2023-01-06')"
        a.execute(sql)
        user_info = a.fetchall()  # 이중 튜플 형태(( ))
        calatt = 0
        callate = 0
        calleave = 0
        calouting = 0
        calabsent = 0
        for i in user_info:
            if i[2] < '09:21' and i[3] >= '17:01' and i[2] != '' and i[3] != '':
                calatt += 1
            if i[2] >= '09.21':
                callate += 1
            if (i[3] > '13.00' and i[3] < '17.01') or i[4] == '':
                calleave += 1
            if i[2] != '' and i[4]:
                calouting += 1
            if (i[2] == '' or i[2] > '13.00') or (i[3] == '' or i[3] < '13.00'):
                calabsent += 1

        labels = ['출석', '외출', '지각', '조퇴',  '결석']
        ratio = [calatt/27, calouting/27, calatt/27, calleave/27, calabsent/27]

        # plt.pie(ratio, labels=labels, autopct='%.1f%%')
        # plt.show()

        self.verticalLayout_2.addWidget(self.canvas2)
        ax = self.fig2.add_subplot(111)
        ax.pie(ratio, labels=labels, autopct='%.2f%%', startangle=160, counterclock=False)
        ax.set_title("반 전체 출석 현황")
        self.canvas2.draw()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    mainWindow = Search()

    widget.addWidget(mainWindow)

    widget.setFixedHeight(921)
    widget.setFixedWidth(601)
    widget.show()
    app.exec_()