# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'boosUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 762)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 0, 161, 25))
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
        self.pushButton_4.setGeometry(QtCore.QRect(260, 0, 111, 25))
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
        self.line.setGeometry(QtCore.QRect(240, 0, 16, 31))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 40, 441, 561))
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 30, 311, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("#pushButton_5{\n"
"border:none;\n"
"}\n"
"#pushButton_5:focus{\n"
"color:rgb(186,186,186);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 90, 71, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("#pushButton_5{\n"
"border:none;\n"
"}\n"
"#pushButton_5:focus{\n"
"color:rgb(186,186,186);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 90, 301, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 150, 71, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("#pushButton_5{\n"
"border:none;\n"
"}\n"
"#pushButton_5:focus{\n"
"color:rgb(186,186,186);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 210, 71, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("#pushButton_5{\n"
"border:none;\n"
"}\n"
"#pushButton_5:focus{\n"
"color:rgb(186,186,186);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.widget)
        self.pushButton_10.setGeometry(QtCore.QRect(20, 270, 81, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("#pushButton_5{\n"
"border:none;\n"
"}\n"
"#pushButton_5:focus{\n"
"color:rgb(186,186,186);\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 150, 301, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 210, 301, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(110, 260, 291, 281))
        self.textEdit.setObjectName("textEdit")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 441, 561))
        self.widget_2.setObjectName("widget_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit_3.setGeometry(QtCore.QRect(120, 80, 291, 221))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton_16 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_16.setGeometry(QtCore.QRect(10, 30, 101, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("QPushButton{\n"
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
        self.pushButton_16.setObjectName("pushButton_16")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(120, 30, 291, 41))
        self.lineEdit_10.setStyleSheet("border:none;\n"
"border-bottom:2px solid #000;\n"
"")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pushButton_17 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_17.setGeometry(QtCore.QRect(10, 360, 101, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("QPushButton{\n"
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
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_18.setGeometry(QtCore.QRect(10, 430, 101, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("QPushButton{\n"
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
        self.pushButton_18.setObjectName("pushButton_18")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(120, 310, 291, 41))
        self.lineEdit_11.setStyleSheet("border:none;\n"
"border-bottom:2px solid #000;\n"
"")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.textEdit_4 = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit_4.setGeometry(QtCore.QRect(120, 360, 291, 191))
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton_19 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_19.setGeometry(QtCore.QRect(10, 300, 101, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("QPushButton{\n"
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
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_20.setGeometry(QtCore.QRect(10, 100, 101, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("QPushButton{\n"
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
        self.pushButton_20.setObjectName("pushButton_20")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_5.setText(_translate("MainWindow", "发布招聘"))
        self.pushButton_4.setText(_translate("MainWindow", "我的招聘"))
        self.pushButton_6.setText(_translate("MainWindow", "职位名称"))
        self.pushButton_7.setText(_translate("MainWindow", "薪资"))
        self.pushButton_8.setText(_translate("MainWindow", "工作地"))
        self.pushButton_9.setText(_translate("MainWindow", "人数"))
        self.pushButton_10.setText(_translate("MainWindow", "职位描述"))
        self.pushButton_16.setText(_translate("MainWindow", "查询"))
        self.pushButton_17.setText(_translate("MainWindow", "同意"))
        self.pushButton_18.setText(_translate("MainWindow", "取消"))
        self.pushButton_19.setText(_translate("MainWindow", "查询"))
        self.pushButton_20.setText(_translate("MainWindow", "取消"))
