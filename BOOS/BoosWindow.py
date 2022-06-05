from TCPmodule import m_recv
from boosUI import *
from TCPmodule import m_recv
import pymysql
import sys
import json
import _thread
import time
"""from PyQt5.QtWidgets import QWidget, QTableView, QAbstractItemView, QToolTip, qApp, QPushButton, QLabel, QVBoxLayout, \
    QHBoxLayout, QApplication, QMainWindow, QHeaderView

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QCursor, QFont"""
from PyQt5.QtWidgets import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
import socket




class BoosWindow(QMainWindow):
    def __init__(self, client, company):
        super().__init__()
        print('init boss')
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 隐藏窗口
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()

        self.client = client
        # host = '47.99.201.114'
        # port = 1010
        # self.client.connect((host, port))



        # self.table_view.setColumnWidth(0, 100)
        # self.table_view.setColumnWidth(1, 130)
        # self.table_view.setColumnWidth(2, 150)
        # self.table_view.setColumnWidth(3, 150)
        # self.table_view.setColumnWidth(4, 160)
        # self.table_view.setColumnWidth(5, 165)
        # 调节列宽度


        self.ui.pushButton.clicked.connect(self.min_window_clicked)
        self.ui.pushButton_2.clicked.connect(self.close_window_clicked)
        self.ui.pushButton_6.clicked.connect(self.releaseJobInformation)
        """
        self.ui.pushButton_6.clicked.connect(self.search)
        self.ui.pushButton_4.clicked.connect(self.min_window_clicked)
        self.ui.lineEdit_4.returnPressed.connect(self.search)
        self.ui.lineEdit_5.returnPressed.connect(self.deleteJob)"""
        self.company = company
        self.ui.label_4.setText(self.company)
        sql = """
                SELECT id,name,jobName FROM al join accoujobOfferinformation.jobOfferDetail natural join jobOfferinformation.resume naturnt.users where jobCompany = \""""\
              +self.company+"""\""""
        try:
            _thread.start_new_thread(self.getdata, (self.client,sql))
        except:
            print("启动线程失败")


    def getdata(self, client,sql):
        # 直接访问数据库
        # conn = pymysql.connect(host="47.99.201.114", port=3306, user ="root", password ="Aa123456",database ="jobOfferinformation",charset ="utf8")
        # 得到一个可以执行SQL语句的光标对象
        # cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
        # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 执行SQL语句
        # print(sql)
        # num = cursor.execute(sql)
        # data = cursor.fetchall()
        # 关闭光标对象
        # cursor.close()
        # 关闭数据库连接
        # conn.close()

        # 服务器返回所有申请本公司职位的信息
        # print('login')
        # jdata = [{'request': 'login', 'passwd': '1', 'id': '1', 'identity':'bosses'}]
        # client.send(json.dumps(jdata).encode())
        # jres = json.loads(m_recv(client))
        # print(jres)
        # print('get')
        jdata = [{'request':'getApplicant', 'identity':'bosses', 'company':self.company}]
        client.send(json.dumps(jdata).encode())
        jres = json.loads(m_recv(client))
        print(jres)

        num = jres[0]['num']
        data = jres[1:]
        print(num)
        print(data)
        """防止最后数据数为0报错，数据数为0显示空表"""
        if(num == 0):
            data = [{'id':'', 'name':'', 'jobName':'', 'jobOfferid': ''}]
        datas = [num, data]
        self.all_job_datas = datas
        # 请求服务器访问数据库
        # jdata = [{'request': 'getJobDetail', 'begin': begin}]
        # client.send(json.dumps(jdata).encode())
        # j_res = json.loads(m_recv(client))
        # begin += j_res[0]['num']
        # self.all_job_datas = j_res[1:-1]
        # print(self.all_job_datas)

        self.column_name = ['账号', '名称', '应聘职位', '职位编号']
        self.model = QStandardItemModel(self.all_job_datas[0], len(self.all_job_datas[1][0]))
        self.model.setHorizontalHeaderLabels(self.column_name)
        self.table_view = self.ui.tableView
        self.table_view.setSelectionMode(QAbstractItemView.SingleSelection)  # 选中一个单元格
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectItems)  # 单元格选中模式
        self.table_view.doubleClicked.connect(self.get_table_item)
        self.table_view.clicked.connect(self.get_cell_tip)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 使表宽度自适应

        print(self.all_job_datas)
        for i in range(self.all_job_datas[0]):
            j = 0
            for key in self.all_job_datas[1][i] :
                job_info = QStandardItem(str(self.all_job_datas[1][i][key]))
                self.model.setItem(i, j, job_info)
                job_info.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                j += 1

        self.table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 表格不可编辑
        self.table_view.setModel(self.model)
        print('线程结束')
        return

    def get_cell_tip(self):
        """ 设置单元格提示信息 """
        contents = self.table_view.currentIndex().data()
        QToolTip.showText(QCursor.pos(), contents)

    def get_table_item(self):
        """获取表格中的数据"""
        # row = self.table_view.currentIndex().row() # 获取所在行数
        column = self.table_view.currentIndex().column()  # 获取所在列数
        contents = self.table_view.currentIndex().data()  # 获取数据
        # QToolTip.showText(QCursor.pos(), contents)
        clipboard = qApp.clipboard()  # 获取剪贴板
        clipboard.setText(contents)
        QToolTip.showText(QCursor.pos(), "已复制")

    #解决隐藏边框后界面无法拖拽问题(重写鼠标事件 ）
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

    def close_window_clicked(self):   #关闭窗口
        self.close()

    def min_window_clicked(self):     #最小化窗口
        self.showMinimized()

    def releaseJobInformation(self):
        jobName = self.ui.lineEdit.text()
        if(jobName == ""):
            QMessageBox.warning(self, "警告", "职位名称不能为空")
            return
        jobCompany = self.company
        jobSalary = self.ui.lineEdit_2.text()
        if(jobSalary == ""):
            QMessageBox.warning(self, "警告", "薪资不能为空")
            return
        jobPlace = self.ui.lineEdit_3.text()
        if (jobPlace == ""):
            QMessageBox.warning(self, "警告", "工作地点不能为空")
            return
        jobNumber = self.ui.lineEdit_4.text()
        if (jobNumber == ""):
            QMessageBox.warning(self, "警告", "招聘人数不能为空")
            return
        if (not jobNumber.isdigit()):
            QMessageBox.warning(self, "警告", "请输入正确的招聘人数")
            return
        jobEducation = self.ui.lineEdit_5.text()
        if (jobEducation == ""):
            QMessageBox.warning(self, "警告", "学历要求不能为空")
            return
        jobExperience = self.ui.lineEdit_6.text()
        if (jobExperience == ""):
            QMessageBox.warning(self, "警告", "经验要求不能为空")
            return
        jobDescribe = self.ui.textEdit.toPlainText()
        if (jobDescribe == ""):
            QMessageBox.warning(self, "警告", "职位描述不能为空")
            return

        # db = pymysql.connect(host="47.99.201.114", user="root", passwd="Aa123456", db="jobOfferinformation", port=3306,
        #                    charset="utf8")
        # cursor = db.cursor()
        sql = 'INSERT INTO jobOfferDetail(jobName,jobCompany,jobSalary,jobPlace,jobDescribe,jobNumber,jobEducation,jobExperience) VALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',{},\'{}\',\'{}\')'.format(jobName,jobCompany,jobSalary,jobPlace,jobDescribe,jobNumber,jobEducation,jobExperience)
        jdata = [{'request':'getJobDetailSQL', 'sql':sql}]
        self.client.send(json.dumps(jdata).encode())
        res = m_recv(self.client)

        # cursor.execute('INSERT INTO jobOfferDetail(jobName,jobCompany,jobSalary,jobPlace,jobDescribe,jobNumber,jobEducation,jobExperience) VALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'.format
        #               (jobName,jobCompany,jobSalary,jobPlace,jobDescribe,jobNumber,jobEducation,jobExperience))
        #print("OK")
        # db.commit()
        # db.close()
        if res[0]['request_return'] == 'getJobDetail':
            QMessageBox.about(self, "提示", "招聘发布成功")

        return


client = socket.socket()
host = '47.99.201.114'
port = 1010
client.connect((host, port))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = BoosWindow(client, '南宁市广迪自动化科技有限公司')
    sys.exit(app.exec_())



# boss = BoosWindow(client, '南宁市广迪自动化科技有限公司')