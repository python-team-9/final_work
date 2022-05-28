# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdministratorUI1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1221, 939)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 0, 1101, 31))
        self.label_8.setStyleSheet("background:rgb(218,218,218);\n"
"border-top-left-radius:30px;\n"
"border-top-right-radius:30px;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(70, 60, 101, 41))
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
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 60, 891, 41))
        self.lineEdit_4.setStyleSheet("border:none;\n"
"border-bottom:2px solid #000;\n"
"")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 640, 911, 61))
        self.label.setStyleSheet("background-color:#FFFFCC;\n"
"border-top-right-radius:30px;\n"
"border-bottom-right-radius:30px;\n"
"border-top-left-radius:30px;\n"
"border-bottom-left-radius:30px;")
        self.label.setObjectName("label")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(200, 220, 911, 481))
        self.tableView.setStyleSheet("")
        self.tableView.setObjectName("tableView")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1030, 10, 16, 16))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    border-radius:8px;\n"
"    background-color: #336666;\n"
"}\n"
"QPushButton:hover{\n"
"    border-radius:8px;\n"
"    background-color: #CCCCCC;\n"
"}\n"
"\n"
"")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1060, 10, 16, 16))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    border-radius:8px;\n"
"    background-color: #336666;\n"
"}\n"
"QPushButton:hover{\n"
"    border-radius:8px;\n"
"    background-color: #CCCCCC;\n"
"}\n"
"\n"
"")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 1101, 841))
        self.label_2.setStyleSheet("background:#FFF;\n"
"border-radius:30px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(210, 140, 891, 41))
        self.lineEdit_5.setStyleSheet("border:none;\n"
"border-bottom:2px solid #000;\n"
"")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(70, 140, 101, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
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
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 720, 911, 101))
        self.label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setObjectName("label_3")
        self.label_2.raise_()
        self.label_8.raise_()
        self.pushButton_6.raise_()
        self.lineEdit_4.raise_()
        self.label.raise_()
        self.tableView.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.lineEdit_5.raise_()
        self.pushButton_7.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1221, 22))
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
        self.pushButton_6.setText(_translate("MainWindow", "查询"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_7.setText(_translate("MainWindow", "删除"))
        self.label_3.setText(_translate("MainWindow", "招聘信息总数："))

