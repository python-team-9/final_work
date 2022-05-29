# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChartView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1501, 968)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1501, 931))
        self.label.setStyleSheet("background:#FFF;\n"
"border-radius:30px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1320, 10, 16, 16))
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
        self.pushButton_2.setGeometry(QtCore.QRect(1350, 10, 16, 16))
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
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(1000, 80, 491, 831))
        self.tableView.setObjectName("tableView")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(990, 50, 68, 15))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 68, 15))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 68, 15))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 50, 68, 15))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 80, 151, 16))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.tableView_2 = QtWidgets.QTableView(self.centralwidget)
        self.tableView_2.setGeometry(QtCore.QRect(10, 160, 501, 321))
        self.tableView_2.setObjectName("tableView_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 130, 68, 15))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 1501, 31))
        self.label_8.setStyleSheet("background:rgb(218,218,218);\n"
"border-top-left-radius:30px;\n"
"border-top-right-radius:30px;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.chartview = QChartView(self.centralwidget)
        self.chartview.setGeometry(QtCore.QRect(0, 500, 411, 411))
        self.chartview.setObjectName("chartview")
        self.chartview_2 = QChartView(self.centralwidget)
        self.chartview_2.setGeometry(QtCore.QRect(410, 500, 591, 411))
        self.chartview_2.setObjectName("chartview_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(860, 110, 111, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:15px;\n"
"    color:#fff;\n"
"    background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #99CCCC, stop:1 #336699)\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:15px;\n"
"    padding-left:15px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(530, 160, 451, 321))
        self.listView.setObjectName("listView")
        self.label.raise_()
        self.tableView.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.tableView_2.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.chartview.raise_()
        self.chartview_2.raise_()
        self.pushButton_3.raise_()
        self.listView.raise_()
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
        self.label_2.setText(_translate("MainWindow", "招聘信息"))
        self.label_3.setText(_translate("MainWindow", "用户："))
        self.label_4.setText(_translate("MainWindow", "账号："))
        self.label_5.setText(_translate("MainWindow", "小龙团"))
        self.label_6.setText(_translate("MainWindow", "2020211754"))
        self.label_7.setText(_translate("MainWindow", "已投递"))
        self.pushButton_3.setText(_translate("MainWindow", "投递"))

