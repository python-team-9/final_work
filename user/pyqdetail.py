import json
import sys
import _thread

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QCursor, QFont, QPainter

from TCPmodule import m_recv
from detail import *
from PyQt5 import QtCore

class pyqdetail(QMainWindow):
    def __init__(self, detail):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit.setText(detail['jobName'])
        self.ui.lineEdit_2.setText(detail['jobCompany'])
        self.ui.lineEdit_3.setText(detail['jobSalary'])
        self.ui.lineEdit_4.setText(detail['jobPlace'])
        self.ui.lineEdit_5.setText(detail['jobEducation'])
        self.ui.lineEdit_6.setText(detail['jobExperience'])
        self.ui.textEdit.setText(detail['jobDescribe'])

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