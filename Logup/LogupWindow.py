from loading import *
import login_db
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
import socket


class LoadingWindow(QMainWindow):
    switch = QtCore.pyqtSignal()  # 切换窗口信号
    def switch_widget2(self):
        self.ui.widget.hide()
        self.hide_error()
        self.ui.widget_2.show()

    def switch_widget(self):
        self.ui.widget_2.hide()
        self.hide_error()
        self.ui.widget.show()

    def show_error(self):
        self.ui.label_3.setText(self.massage)
        self.ui.label_3.show()

    def hide_error(self):
        self.ui.label_3.hide()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.widget_2.hide()
        self.ui.label_3.hide()
        self.ui.pushButton_5.clicked.connect(self.switch_widget)
        self.ui.pushButton_4.clicked.connect(self.switch_widget2)
        self.ui.pushButton_3.clicked.connect(self.logining)
        self.ui.pushButton_6.clicked.connect(self.registering)

        # 连接服务器
        self.client = socket.socket()
        host = '47.99.201.114'
        port = 1010
        self.client.connect((host, port))


        # 隐藏窗口
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def logining(self):
        self.userid = self.ui.lineEdit.text()
        print(self.userid)
        self.password = self.ui.lineEdit_2.text()
        print(self.password)
        if self.ui.radioButton.isChecked():
            self.identity = 'users'
        elif self.ui.radioButton_2.isChecked():
            self.identity = 'managers'
        elif self.ui.radioButton_5.isChecked():
            self.identity = 'bosses'
        else:
            self.massage = '未选择身份！'
            self.show_error()
        if self.userid=='':
            self.massage = '用户名为空！'
            self.show_error()
        print("账号输入",self.userid,self.password,self.identity)
        print('login_db')
        a = login_db.login(self.client, self.userid, self.password, self.identity)
        print('a等于', a)

        if a[0] == '用户未注册或账号错误':
            self.massage = '用户未注册或账号错误！'
            print('用户未注册或账号错误！')
            self.show_error()
        elif a[0] == '密码错误':
            self.massage = '密码错误！'
            print('密码错误！')
            self.show_error()

        else:
            self.userid = a[1][0]
            self.password = a[1][1]
            self.username = a[1][2]
            print('登录成功！', self.identity)
            self.switch.emit()

        # if a > 0:
        #     print('登录成功！')
        # else:
        #     self.massage = '用户名或密码错误！'
        #     print('用户名或密码错误！')
        #     self.show_error()


    def registering(self):
        self.userid = self.ui.lineEdit_4.text()
        print(self.userid)
        if self.userid == '':
            self.massage='用户名为空！'
            self.show_error()
        self.password = self.ui.lineEdit_3.text()
        print(self.password)
        self.password_2 = self.ui.lineEdit_5.text()
        if self.password != self.password_2:
            print('确认密码错误！')
            self.massage = '确认密码错误！'
            self.show_error()
            return
        else:
            if self.ui.radioButton_4.isChecked():
                self.identity = 'users'
            elif self.ui.radioButton_6.isChecked():
                self.identity = 'bosses'
            else:
                print('未选择身份')
                self.massage = '未选择身份'
                self.show_error()

            self.username = self.ui.lineEdit_6.text()
            print("昵称", self.username)

            a = login_db.register(self.client, self.userid, self.password, self.username, self.identity)
            if a == '注册成功':
                self.massage = '注册成功！'
                self.show_error()
            else:
                self.massage = 'ERROR注册失败！'
                self.show_error()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoadingWindow()
    sys.exit(app.exec_())


