# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detail.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1006, 491)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 951, 461))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("background:#E8E8E8;\n"
"border-radius:30px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(930, 20, 16, 16))
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
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(900, 20, 16, 16))
        self.pushButton_1.setStyleSheet("QPushButton{\n"
"    border-radius:8px;\n"
"    background-color: #336666;\n"
"}\n"
"QPushButton:hover{\n"
"    border-radius:8px;\n"
"    background-color: #CCCCCC;\n"
"}\n"
"\n"
"")
        self.pushButton_1.setText("")
        self.pushButton_1.setObjectName("pushButton_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(57, 130, 71, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(57, 60, 81, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(57, 200, 71, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(57, 270, 81, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(57, 340, 81, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 50, 301, 31))
        self.lineEdit.setStyleSheet("border:none;\n"
"border-bottom: 1px solid #000;\n"
"background:#E8E8E8;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 120, 301, 31))
        self.lineEdit_2.setStyleSheet("border:none;\n"
"border-bottom: 1px solid #000;\n"
"background:#E8E8E8;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 190, 301, 31))
        self.lineEdit_3.setStyleSheet("border:none;\n"
"border-bottom: 1px solid #000;\n"
"background:#E8E8E8;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 260, 301, 31))
        self.lineEdit_4.setStyleSheet("border:none;\n"
"border-bottom: 1px solid #000;\n"
"background:#E8E8E8;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(490, 60, 91, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(493, 100, 451, 331))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"background:#E8E8E8;\n"
"border:1px solid #000;\n"
"border-radius:10px;\n"
"}\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(57, 410, 81, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 330, 301, 31))
        self.lineEdit_5.setStyleSheet("border:none;\n"
"border-bottom: 1px solid #000;\n"
"background:#E8E8E8;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(140, 400, 301, 31))
        self.lineEdit_6.setStyleSheet("border:none;\n"
"border-bottom: 1px solid #000;\n"
"background:#E8E8E8;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close) # type: ignore
        self.pushButton_1.clicked.connect(MainWindow.showMinimized) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "公司："))
        self.label_1.setText(_translate("MainWindow", "职位名称："))
        self.label_3.setText(_translate("MainWindow", "月薪："))
        self.label_4.setText(_translate("MainWindow", "工作地点："))
        self.label_5.setText(_translate("MainWindow", "学历要求："))
        self.label_6.setText(_translate("MainWindow", "简介："))
        self.label_7.setText(_translate("MainWindow", "工作经验："))
