import json
import sys
import _thread

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from TCPmodule import m_recv
from jianli import *
from PyQt5 import QtCore
import socket

class addjianli(QMainWindow):
    addsuccess = QtCore.pyqtSignal(str)  # 上传完成信号
    def __init__(self, client, userid, identity):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.userid = userid
        self.identity = identity
        self.mode = False  # mode为false说明第一次上传简历 ，为true说明时修改简历

        print("启动user窗口")

        # 隐藏窗口
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()
        self.client = client
        self.ui.pushButton_3.clicked.connect(self.addresume)

        try:
            _thread.start_new_thread(self.getresumm, ())
        except:
            print('获取简历失败')

    def getresumm(self):
        sql = "SELECT * FROM personalResume WHERE id=\'{}\';".format(self.userid)
        jdata = [{'request': 'getJobDetailSQL', 'sql': sql}]
        self.client.send(json.dumps(jdata).encode())
        jres = json.loads(m_recv(self.client))
        print("jres[0]['num']", jres[0]['num'])
        num = jres[0]['num']
        if num == 0:
            self.mode = False
            print("mode是", self.mode)
        else:
            self.mode = True
            print("mode是", self.mode)
            datas = jres[1]
            print("已有简历", datas)
            self.ui.lineEdit.setText(datas['name'])
            self.ui.lineEdit_2.setText(str(datas['age']))
            self.ui.lineEdit_3.setText(datas['education'])
            self.ui.lineEdit_4.setText(datas['major'])
            self.ui.lineEdit_5.setText(datas['school'])
            print(datas['experience'])
            self.ui.textEdit.append(datas['experience'])
            print("a")
            if datas['sex'] == 'm':
                print("b")
                self.ui.radioButton.setChecked(True)
                print("c")
            else:
                print("d")
                self.ui.radioButton_2.setChecked(True)
                print("e")

    def addresume(self):
        name = self.ui.lineEdit.text()
        age = int(self.ui.lineEdit_2.text())
        print('age', age)
        education = self.ui.lineEdit_3.text()
        print(1)
        major = self.ui.lineEdit_4.text()
        print(2)
        school = self.ui.lineEdit_5.text()
        print(3)
        experience = self.ui.textEdit.toPlainText()
        print(4)
        if self.ui.radioButton.isChecked():
            print(5)
            sex = 'm'
        elif self.ui.radioButton_2.isChecked():
            print(6)
            sex = 'f'
        else:
            print(7)
            sex = ''
        print("输入信息为{}，{}，{}，{}，{}，{}，{}，{}".format(name, age, education, major, school, experience, sex, self.userid))
        if name == '' or age == '' or education == '' or major == '' or school == '' or experience == '' or sex == '':
            print('waring')
            QMessageBox.warning(self, 'ERROR', '信息不完整')
        else:
            print('send')
            if self.mode:  # 更新简历
                sql = "UPDATE personalResume SET name=\'{}\', age={}, education=\'{}\', major=\'{}\', school=\'{}\', experience=\'{}\', sex=\'{}\' WHERE id=\'{}\';".format(name, age, education, major, school, experience, sex, self.userid)
            else:
                sql = "INSERT INTO personalResume VALUES ( '{}\',\'{}\',\'{}\',{},\'{}\',\'{}\',\'{}\',\'{}\');".format(self.userid, name, sex, age, education, major, school, experience)
            jdata = [{'request': 'getJobDetailSQL', 'sql': sql}]
            self.client.send(json.dumps(jdata).encode())
            jres = json.loads(m_recv(self.client))
            print('上传简历', jres[0]['num'])
            self.addsuccess.emit("上传简历成功！")

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = addjianli()
    sys.exit(app.exec_())
