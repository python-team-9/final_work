from loading import *
from Logup.login_db import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

userid = ''
password = ''
ismanager = False


class LoadingWindow(QMainWindow):
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
        self.ismanager = self.ui.radioButton_2.isChecked()
        print(self.ismanager)
        if self.userid=='':
            self.massage = '用户名为空！'
            self.show_error()

        a = login(self.userid, self.password, self.ismanager)
        if a > 0:
            print('登录成功！')
        else:
            self.massage = '用户名或密码错误！'
            print('用户名或密码错误！')
            self.show_error()


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
            self.ismanager = self.ui.radioButton_3.isChecked()
            print(self.ismanager)

            a = login(self.userid, self.password, self.ismanager)
            if a > 0:
                self.massage = '该用户已存在！'
                print('该用户已存在！')
                self.show_error()
            else:
                register(self.userid, self.password, self.ismanager)
                print('注册成功！')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoadingWindow()
    sys.exit(app.exec_())


