from TCPmodule import m_recv
from AdministratorUI1 import *
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




class AdministratorWindow(QMainWindow):
    def __init__(self, client, userid, password, username, identity):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 隐藏窗口
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()

        self.userid = userid
        self.password = password
        self.username = username
        self.identity = identity
        self.client = client

        #self.client = socket.socket()
        #host = '47.99.201.114'
        #port = 1010
        #self.client.connect((host, port))



        # self.table_view.setColumnWidth(0, 100)
        # self.table_view.setColumnWidth(1, 130)
        # self.table_view.setColumnWidth(2, 150)
        # self.table_view.setColumnWidth(3, 150)
        # self.table_view.setColumnWidth(4, 160)
        # self.table_view.setColumnWidth(5, 165)
        # 调节列宽度

        self.ui.pushButton_8.clicked.connect(self.zhuxiao)
        self.ui.pushButton_7.clicked.connect(self.deleteJob)
        self.ui.pushButton_6.clicked.connect(self.search)
        self.ui.pushButton_5.clicked.connect(self.close_window_clicked)
        self.ui.pushButton_4.clicked.connect(self.min_window_clicked)
        self.ui.lineEdit_4.returnPressed.connect(self.search)
        self.ui.lineEdit_5.returnPressed.connect(self.deleteJob)
        sql = """
                SELECT jobName,jobCompany,jobSalary,jobPlace,jobOfferid FROM jobOfferDetail;"""
        """try:
            _thread.start_new_thread(self.getdata, (self.client,sql))
        except:
            print("启动线程失败")"""
        self.getdata(self.client,sql)


    def getdata(self, client,sql):
        # 直接访问数据库
        #conn = pymysql.connect(host="47.99.201.114", port=3306, user ="root", password ="Aa123456",database ="jobOfferinformation",charset ="utf8")
        # 得到一个可以执行SQL语句的光标对象
        #cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
        # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 执行SQL语句
        #num = cursor.execute(sql)
        #data = cursor.fetchall()
        # 关闭光标对象
        #cursor.close()
        # 关闭数据库连接
        #conn.close()

        sql = "SELECT jobName,jobCompany,jobSalary,jobPlace,jobOfferid FROM jobOfferDetail;"
        jdata = [{'request': 'getJobDetailSQL', 'sql': sql}]
        self.client.send(json.dumps(jdata).encode())
        jres = json.loads(m_recv(client))
        print("jres是", jres)
        print("jres[0]['num']", jres[0]['num'])
        self.all_job_datas = []
        self.all_job_datas.append(jres[0]['num'])
        self.all_job_datas.append([])
        for i in range(0, jres[0]['num']):
            job = []
            job.append(jres[i + 1]['jobName'])
            job.append(jres[i + 1]['jobCompany'])
            job.append(jres[i + 1]['jobSalary'])
            job.append(jres[i + 1]['jobPlace'])
            job.append(jres[i + 1]['jobOfferid'])
            self.all_job_datas[1].append(job)
        print(self.all_job_datas)

        print(num)
        print(data)
        """防止最后数据数为0报错，数据数为0显示空表"""
        if(num == 0):
            data = (('','','','',''))
        self.ui.label_3.setText("招聘信息总数:"+str(num))
        datas = [num, data]
        self.all_job_datas = datas
        # 请求服务器访问数据库
        # jdata = [{'request': 'getJobDetail', 'begin': begin}]
        # client.send(json.dumps(jdata).encode())
        # j_res = json.loads(m_recv(client))
        # begin += j_res[0]['num']
        # self.all_job_datas = j_res[1:-1]
        # print(self.all_job_datas)

        self.column_name = ['工作名称', '公司', '薪酬', '工作地点','jobOfferid']
        self.model = QStandardItemModel(self.all_job_datas[0], len(self.all_job_datas[1][0]))
        self.model.setHorizontalHeaderLabels(self.column_name)
        self.table_view = self.ui.tableView
        self.table_view.setSelectionMode(QAbstractItemView.SingleSelection)  # 选中一个单元格
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectItems)  # 单元格选中模式
        self.table_view.doubleClicked.connect(self.get_table_item)
        self.table_view.clicked.connect(self.get_cell_tip)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 使表宽度自适应

        for i in range(self.all_job_datas[0]):
            for j in range(len(self.all_job_datas[1][0])):
                job_info = QStandardItem(str(self.all_job_datas[1][i][j]))
                self.model.setItem(i, j, job_info)
                job_info.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

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

    def search(self):
        text = self.ui.lineEdit_4.text()
        searsql = """SELECT jobName,jobCompany,jobSalary,jobPlace,jobOfferid FROM jobOfferinformation.jobOfferDetail where jobName like \"%"""+text+"""%\""""
        print(searsql)
        try:
            _thread.start_new_thread(self.getdata, (self.client,searsql))
        except:
            print("启动线程失败")
    def deleteJob(self):
        text = self.ui.lineEdit_5.text()
        sql = """SELECT * FROM jobOfferinformation.jobOfferDetail where jobOfferid = """+text
        # 直接访问数据库
        conn = pymysql.connect(host="47.99.201.114", port=3306, user="root", password="Aa123456",
                               database="jobOfferinformation", charset="utf8")
        # 得到一个可以执行SQL语句的光标对象
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
        # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 执行SQL语句
        num = cursor.execute(sql)
        if num == 0:
            QMessageBox.warning(self, "警告", "jobOfferid不存在")
            return
        sql = """delete FROM jobOfferinformation.jobOfferDetail where jobOfferid = """+text
        cursor.execute(sql)
        conn.commit()#不提交不会显示
        sql = """
                SELECT jobName,jobCompany,jobSalary,jobPlace,jobOfferid FROM jobOfferDetail;
                """
        num = cursor.execute(sql)
        data = cursor.fetchall()
        # 关闭光标对象
        cursor.close()
        # 关闭数据库连接
        conn.close()
        print(num)
        print(data)
        """防止最后数据数为0报错，数据数为0显示空表"""
        if(num == 0):
            data = (('','','','',''))
        self.ui.label_3.setText("招聘信息总数:" + str(num))
        datas = [num, data]
        self.all_job_datas = datas
        # 请求服务器访问数据库
        # jdata = [{'request': 'getJobDetail', 'begin': begin}]
        # client.send(json.dumps(jdata).encode())
        # j_res = json.loads(m_recv(client))
        # begin += j_res[0]['num']
        # self.all_job_datas = j_res[1:-1]
        # print(self.all_job_datas)

        self.column_name = ['工作名称', '公司', '薪酬', '工作地点', 'jobOfferid']
        self.model = QStandardItemModel(self.all_job_datas[0], len(self.all_job_datas[1][0]))
        self.model.setHorizontalHeaderLabels(self.column_name)
        self.table_view = self.ui.tableView
        self.table_view.setSelectionMode(QAbstractItemView.SingleSelection)  # 选中一个单元格
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectItems)  # 单元格选中模式
        self.table_view.doubleClicked.connect(self.get_table_item)
        self.table_view.clicked.connect(self.get_cell_tip)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 使表宽度自适应

        for i in range(self.all_job_datas[0]):
            for j in range(len(self.all_job_datas[1][0])):
                job_info = QStandardItem(str(self.all_job_datas[1][i][j]))
                self.model.setItem(i, j, job_info)
                job_info.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 表格不可编辑
        self.table_view.setModel(self.model)
        print('线程结束')
        return

    def zhuxiao(self):
        res = QMessageBox.question(self, "确认注销账号", "账号注销数据无法恢复！", QMessageBox.Yes|QMessageBox.Cancel)
        if res==QMessageBox.Yes:
            sql = "DELETE FROM {} WHERE id=\'{}\';".format(self.identity, self.userid)
            print("删除账号", sql)
            jdata = [{'request': 'getAccDetailSQL', 'sql': sql}]
            self.client.send(json.dumps(jdata).encode())
            jres = json.loads(m_recv(self.client))
            if jres[0]['num'] == 1:
                QMessageBox.about(self, '注销账号', '成功！')
                self.close()
            else:
                QMessageBox.critical(self, '注销账号失败', '可能存在网络问题')
        else:
            return

client = socket.socket()
host = '47.99.201.114'
port = 1010
client.connect((host, port))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = AdministratorWindow(client,"1","1", '南宁市广迪自动化科技有限公司','manager')
    sys.exit(app.exec_())