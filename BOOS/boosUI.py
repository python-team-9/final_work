# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'boosUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1177, 890)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(760, 31, 111, 25))
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
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 70, 551, 801))
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 30, 430, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(90, 300, 430, 381))
        self.textEdit.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 68, 15))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 85, 68, 15))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(10, 130, 68, 15))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(10, 175, 68, 15))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(10, 310, 68, 15))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(10, 220, 68, 15))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setGeometry(QtCore.QRect(10, 265, 68, 15))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 75, 430, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 120, 430, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 165, 430, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 210, 430, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setGeometry(QtCore.QRect(90, 255, 430, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(409, 710, 101, 41))
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
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 710, 111, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    border-top: 5px solid qlineargradient(y0:0, y1:1,stop: 0 #ececef, stop: 1 white);\n"
"border-left: 5px solid qlineargradient(x0:0, x1:1,stop: 0 #ececef, stop: 1 white);\n"
" border-bottom: 5px solid qlineargradient(y0:0, y1:1,stop: 0 white, stop: 1  #ececef);\n"
"border-right: 5px solid qlineargradient(x0:0, x1:1,stop:  0 white, stop: 1 #ececef);\n"
"background-color: rgb(255,255,255);\n"
"    color:#aaa\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:15px;\n"
"    padding-left:15px;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 1101, 31))
        self.label_8.setStyleSheet("background:rgb(218,218,218);\n"
"border-top-left-radius:30px;\n"
"border-top-right-radius:30px;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1030, 10, 16, 16))
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
        self.pushButton_2.setGeometry(QtCore.QRect(1060, 10, 16, 16))
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
        self.pushButton_5.setGeometry(QtCore.QRect(330, 31, 161, 25))
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
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(590, 70, 501, 751))
        self.tableView.setStyleSheet("")
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1101, 841))
        self.label.setStyleSheet("background:#FFF;\n"
"border-radius:30px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 68, 15))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 40, 281, 16))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label.raise_()
        self.pushButton_4.raise_()
        self.widget.raise_()
        self.label_8.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_5.raise_()
        self.tableView.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1177, 22))
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
        self.pushButton_4.setText(_translate("MainWindow", "求职申请"))
        self.label_5.setText(_translate("MainWindow", "职位名称"))
        self.label_6.setText(_translate("MainWindow", "薪资"))
        self.label_7.setText(_translate("MainWindow", "工作地点"))
        self.label_9.setText(_translate("MainWindow", "招聘人数"))
        self.label_10.setText(_translate("MainWindow", "职位描述"))
        self.label_11.setText(_translate("MainWindow", "学历要求"))
        self.label_12.setText(_translate("MainWindow", "经验要求"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "请输入一个范围如4000-5000"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "请输入几年"))
        self.pushButton_6.setText(_translate("MainWindow", "发布"))
        self.pushButton_7.setText(_translate("MainWindow", "注销账号"))
        self.pushButton_5.setText(_translate("MainWindow", "发布招聘"))
        self.label_3.setText(_translate("MainWindow", "欢迎"))
        self.label_4.setText(_translate("MainWindow", "南宁市瑞薪电子科技有限公司"))

