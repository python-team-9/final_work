# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resume.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(413, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 361, 591))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("background:#fff;\n"
"border-radius:30px;"
"border:1px solid #000")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 20, 16, 16))
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
        self.pushButton_1.setGeometry(QtCore.QRect(310, 20, 16, 16))
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
        self.label_2.setGeometry(QtCore.QRect(57, 110, 71, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(57, 60, 71, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(57, 160, 71, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(57, 210, 71, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(57, 260, 71, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 50, 221, 31))
        self.lineEdit.setStyleSheet("border:none;\n"
"border-bottom: 1px solid #000;\n"
"background:#fff;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 150, 221, 31))
        self.lineEdit_2.setStyleSheet("border:none;\n"
"border-bottom: 1px solid #000;\n"
"background:#fff;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 200, 221, 31))
        self.lineEdit_3.setStyleSheet("border:none;\n"
"border-bottom: 1px solid #000;\n"
"background:#fff;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 250, 221, 31))
        self.lineEdit_4.setStyleSheet("border:none;\n"
"border-bottom: 1px solid #000;\n"
"background:#fff;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(140, 110, 51, 31))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(190, 110, 51, 31))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(57, 360, 91, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 400, 291, 151))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"background:#fff;\n"
"border:1px solid #000;\n"
"border-radius:10px;\n"
"}\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(57, 310, 71, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 300, 221, 31))
        self.lineEdit_5.setStyleSheet("border:none;\n"
"border-bottom: 1px solid #000;\n"
"background:#fff;")
        self.lineEdit_5.setObjectName("lineEdit_5")
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
        self.label_2.setText(_translate("MainWindow", "性别："))
        self.label_1.setText(_translate("MainWindow", "姓名："))
        self.label_3.setText(_translate("MainWindow", "年龄："))
        self.label_4.setText(_translate("MainWindow", "学历："))
        self.label_5.setText(_translate("MainWindow", "专业："))
        self.radioButton.setText(_translate("MainWindow", "男"))
        self.radioButton_2.setText(_translate("MainWindow", "女"))
        self.label_6.setText(_translate("MainWindow", "工作经历："))
        self.label_7.setText(_translate("MainWindow", "院校："))
