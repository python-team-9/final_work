# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loading.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(993, 713)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 110, 341, 411))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-top-right-radius:30px;\n"
"border-bottom-right-radius:30px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 110, 291, 411))
        self.label_2.setStyleSheet("border-image: url(:/images/images/woshou.jpg);\n"
"border-top-left-radius:30px;\n"
"border-bottom-left-radius:30px;\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 120, 16, 16))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border-radius:8px;\n"
"    background-color: #336666;\n"
"}\n"
"QPushButton:hover{\n"
"    border-radius:8px;\n"
"    background-color: #CCCCCC;\n"
"}\n"
"\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 120, 16, 16))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    border-radius:8px;\n"
"    background-color: #336666;\n"
"}\n"
"QPushButton:hover{\n"
"    border-radius:8px;\n"
"    background-color: #CCCCCC;\n"
"}\n"
"\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(481, 160, 61, 25))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("#pushButton_5{\n"
"border:none;\n"
"}\n"
"#pushButton_5:focus{\n"
"color:rgb(186,186,186);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(560, 160, 51, 25))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("#pushButton_4{\n"
"border:none;\n"
"}\n"
"#pushButton_4:focus{\n"
"color:rgb(186,186,186);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(540, 160, 16, 31))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(410, 210, 291, 281))
        self.widget.setObjectName("widget")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 220, 101, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0,         x2:1, y2:1, stop:0 #663300, stop:1 #333333);\n"
"    color:#fff;\n"
"    border-radius:5px;\n"
"    border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:15px;\n"
"    padding-left:15px;\n"
"}\n"
"\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(30, 80, 61, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(160, 150, 71, 21))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setGeometry(QtCore.QRect(40, 150, 71, 21))
        self.radioButton.setObjectName("radioButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 90, 191, 31))
        self.lineEdit_2.setStyleSheet("border:none;\n"
"border-bottom:2px solid #000;\n"
"")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 61, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 30, 191, 31))
        self.lineEdit.setStyleSheet("border:none;\n"
"border-bottom:2px solid #000;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.radioButton_5 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_5.setGeometry(QtCore.QRect(100, 150, 71, 21))
        self.radioButton_5.setObjectName("radioButton_5")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(410, 200, 291, 281))
        self.widget_2.setObjectName("widget_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 230, 101, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0,         x2:1, y2:1, stop:0 #663300, stop:1 #333333);\n"
"    color:#fff;\n"
"    border-radius:5px;\n"
"    border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:15px;\n"
"    padding-left:15px;\n"
"}\n"
"\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 81, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_4.setGeometry(QtCore.QRect(40, 190, 71, 21))
        self.radioButton_4.setObjectName("radioButton_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 60, 191, 31))
        self.lineEdit_3.setStyleSheet("border:none;\n"
"border-bottom:2px solid #000;\n"
"")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(40, 10, 41, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 20, 191, 31))
        self.lineEdit_4.setStyleSheet("border:none;\n"
"border-bottom:2px solid #000;\n"
"")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 100, 191, 31))
        self.lineEdit_5.setStyleSheet("border:none;\n"
"border-bottom:2px solid #000;\n"
"")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(10, 90, 81, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.radioButton_6 = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_6.setGeometry(QtCore.QRect(100, 190, 71, 21))
        self.radioButton_6.setObjectName("radioButton_6")
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(40, 130, 41, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(90, 140, 191, 31))
        self.lineEdit_6.setStyleSheet("border:none;\n"
"border-bottom:2px solid #000;\n"
"")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 490, 291, 16))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255,0,0);")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_5.setText(_translate("MainWindow", "登录"))
        self.pushButton_4.setText(_translate("MainWindow", "注册"))
        self.pushButton_3.setText(_translate("MainWindow", "登录"))
        self.label_5.setText(_translate("MainWindow", "密码:"))
        self.radioButton_2.setText(_translate("MainWindow", "管理员"))
        self.radioButton.setText(_translate("MainWindow", "求职"))
        self.label_4.setText(_translate("MainWindow", "账号:"))
        self.radioButton_5.setText(_translate("MainWindow", "招聘"))
        self.pushButton_6.setText(_translate("MainWindow", "注册"))
        self.label_6.setText(_translate("MainWindow", "密码设置:"))
        self.radioButton_4.setText(_translate("MainWindow", "求职"))
        self.label_7.setText(_translate("MainWindow", "账号:"))
        self.label_8.setText(_translate("MainWindow", "确认密码:"))
        self.radioButton_6.setText(_translate("MainWindow", "招聘"))
        self.label_9.setText(_translate("MainWindow", "昵称:"))
        self.label_3.setText(_translate("MainWindow", "错误！"))
import res_rc
