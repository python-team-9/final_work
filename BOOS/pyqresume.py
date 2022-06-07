import json
import sys
import _thread

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QCursor, QFont, QPainter

from TCPmodule import m_recv
from resume import *
from PyQt5 import QtCore

class pyqresume(QMainWindow):
    def __init__(self, self_resume):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.self_resume = self_resume
        self.ui.lineEdit.setText(self_resume['name'])
        self.ui.lineEdit_2.setText(str(self_resume['age']))
        self.ui.lineEdit_3.setText(self_resume['education'])
        self.ui.lineEdit_4.setText(self_resume['major'])
        self.ui.lineEdit_5.setText(self_resume['school'])
        self.ui.textEdit.setText(self_resume['experience'])
        if self_resume['sex'] == 'm':
            self.ui.radioButton.setChecked(True)
        elif self_resume['sex'] == 'f':
            self.ui.radioButton_2.setChecked(True)



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