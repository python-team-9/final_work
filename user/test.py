from PyQt5.QtChart import QPieSeries, QChart, QPieSlice

from TCPmodule import m_recv
from userUI import *
import pymysql
import sys
import json
import _thread

from PyQt5.QtWidgets import QWidget, QTableView, QAbstractItemView, QToolTip, qApp, QPushButton, QLabel, QVBoxLayout, \
    QHBoxLayout, QApplication, QMainWindow, QHeaderView

from PyQt5.QtCore import Qt, QStringListModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QCursor, QFont, QPainter


class UserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.messagelist = []  # *********************
        self.slm = QStringListModel()
        self.slm.setStringList(self.messagelist)
        self.ui.listView.setModel(self.slm)
        self.ui.pushButton_3.clicked.connect(self.sendresume)
        self.userid = '2020211754'

        # 隐藏窗口
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()





        # self.table_view.setColumnWidth(0, 100)
        # self.table_view.setColumnWidth(1, 130)
        # self.table_view.setColumnWidth(2, 150)
        # self.table_view.setColumnWidth(3, 150)
        # self.table_view.setColumnWidth(4, 160)
        # self.table_view.setColumnWidth(5, 165)
        # 调节列宽度


        try:
            self.getdata()
        except:
            print("启动线程1失败")
        try:
            self.getchartdetail()
        except:
            print("启动线程2失败")


    def getdata(self):
        # 直接访问数据库
        conn = pymysql.connect(host="47.99.201.114", port=3306, user ="root", password ="Aa123456",database ="jobOfferinformation",charset ="utf8")
        sql = """
        SELECT jobName,jobCompany,jobSalary,jobPlace,jobOfferid FROM jobOfferDetail;
        """
        sql2 = "SELECT jobName,jobCompany,jobSalary,jobPlace,jobOfferid FROM jobOfferDetail WHERE jobOfferid IN (SELECT jobOfferid FROM resume WHERE userid =\'{}\');".format(self.userid)
        # 得到一个可以执行SQL语句的光标对象
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
        # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 执行SQL语句
        num = cursor.execute(sql)
        data = cursor.fetchall()
        num2 = cursor.execute(sql2)
        data2 = cursor.fetchall()
        # 关闭光标对象
        cursor.close()
        # 关闭数据库连接
        conn.close()
        datas = [num, data]
        self.all_job_datas = datas
        datas = [num2, data2]
        self.all_job_datas2 = datas
        # 请求服务器访问数据库
        # jdata = [{'request': 'getJobDetail', 'begin': begin}]
        # client.send(json.dumps(jdata).encode())
        # j_res = json.loads(m_recv(client))
        # begin += j_res[0]['num']
        # self.all_job_datas = j_res[1:-1]
        # print(self.all_job_datas)

        self.column_name = ['工作名称', '公司', '薪酬', '工作地点']
        self.model = QStandardItemModel(self.all_job_datas[0], 4)
        self.model2 = QStandardItemModel(self.all_job_datas2[0], 4)
        self.model.setHorizontalHeaderLabels(self.column_name)
        self.model2.setHorizontalHeaderLabels(self.column_name)
        self.table_view = self.ui.tableView
        self.table_view_2 = self.ui.tableView_2
        self.table_view.setSelectionMode(QAbstractItemView.SingleSelection)  # 选中一个单元格
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectItems)  # 单元格选中模式
        self.table_view.doubleClicked.connect(self.get_table_item)
        self.table_view.clicked.connect(self.get_cell_tip)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 使表宽度自适应
        self.table_view_2.setSelectionMode(QAbstractItemView.SingleSelection)  # 选中一个单元格
        self.table_view_2.setSelectionBehavior(QAbstractItemView.SelectItems)  # 单元格选中模式
        self.table_view_2.doubleClicked.connect(self.get_table_item)
        self.table_view_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 使表宽度自适应

        for i in range(self.all_job_datas[0]):
            for j in range(4):
                job_info = QStandardItem(str(self.all_job_datas[1][i][j]))
                self.model.setItem(i, j, job_info)
                job_info.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        for i in range(self.all_job_datas2[0]):
            for j in range(4):
                job_info = QStandardItem(str(self.all_job_datas2[1][i][j]))
                self.model2.setItem(i, j, job_info)
                job_info.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 表格不可编辑
        self.table_view_2.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 表格不可编辑
        self.table_view.setModel(self.model)
        self.table_view_2.setModel(self.model2)
        return

    def get_cell_tip(self):
        """ 设置单元格提示信息 """
        contents = self.table_view.currentIndex().data()
        self.row = self.table_view.currentIndex().row()  # 获取所在行数
        print("选中行数为", self.row)
        self.jobOfferid = self.all_job_datas[1][self.row][4]
        print("选中工作id为", self.jobOfferid)
        QToolTip.showText(QCursor.pos(), contents)

    def get_table_item(self):
        """获取表格中的数据"""
        column = self.table_view.currentIndex().column()  # 获取所在列数
        contents = self.table_view.currentIndex().data()  # 获取数据
        # QToolTip.showText(QCursor.pos(), contents)
        clipboard = qApp.clipboard()  # 获取剪贴板
        clipboard.setText(contents)
        QToolTip.showText(QCursor.pos(), "已复制")

    def getchartdetail(self):
        conn = pymysql.connect(host="47.99.201.114", port=3306, user="root", password="Aa123456",
                               database="jobOfferinformation", charset="utf8")

        sql = """
                    SELECT jobEducation, COUNT(*) AS eduNum FROM jobOfferDetail GROUP BY jobEducation;
        """
        # 得到一个可以执行SQL语句的光标对象
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
        # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 执行SQL语句
        num = cursor.execute(sql)
        data = cursor.fetchall()

        sql2 = """
            SELECT jobPlace, COUNT(*) AS placeNum FROM jobOfferDetail GROUP BY jobPlace;
        """
        num2 = cursor.execute(sql2)
        data2 = cursor.fetchall()

        # 关闭光标对象
        cursor.close()
        # 关闭数据库连接
        conn.close()

        print('num', num)
        self.color = ["#ffc656", "#2fc7e8", "#3ed7b7", "#0099CC", "#99CC66", "#CCCCCC", "#FF6666"]
        self.pieseries1 = QPieSeries()
        self.pieseries1.hovered.connect(self.do_pieHover)
        for x in data:
            self.pieseries1.append(x[0], x[1])
            print(x[0], x[1])

        self.slice = QPieSlice()
        print(1)
        for i in range(0, num):
            self.slice = self.pieseries1.slices()[i]
            self.slice.setLabelVisible(False)
            # slice.setPen(QPen(Qt.white, 10))
            self.slice.setBrush(QtGui.QColor(self.color[i]))

        self.pieseries2 = QPieSeries()
        self.pieseries2.hovered.connect(self.do_pieHover)
        for x in data2:
            self.pieseries2.append(x[0], x[1])
            print(x[0], x[1])

        self.slice2 = QPieSlice()
        print(1)
        for i in range(0, num2):
            self.slice2 = self.pieseries2.slices()[i]
            self.slice2.setLabelVisible(False)
            # slice.setPen(QPen(Qt.white, 10))
            self.slice2.setBrush(QtGui.QColor(self.color[i]))

        self.chart1 = QChart()  # 定义QChart
        self.chart2 = QChart()

        self.chart1.legend().hide()
        self.chart2.legend().hide()

        self.chart1.createDefaultAxes()
        self.chart2.createDefaultAxes()

        self.chart1.addSeries(self.pieseries1)
        self.chart2.addSeries(self.pieseries2)

        self.chart1.setTitle("教育分布")
        self.chart2.setTitle("地区分布")

        self.chart1.legend().setVisible(True)
        self.chart2.legend().setVisible(True)

        self.chart1.legend().setAlignment(Qt.AlignBottom)
        self.chart2.legend().setAlignment(Qt.AlignBottom)

        self.chartview = self.ui.chartview
        self.chartview_2 = self.ui.chartview_2
        self.chart1.setAnimationOptions(QChart.SeriesAnimations)
        self.chart2.setAnimationOptions(QChart.SeriesAnimations)
        self.chartview.setRenderHint(QPainter.Antialiasing)
        self.chartview_2.setRenderHint(QPainter.Antialiasing)

        self.chartview.setChart(self.chart1)
        self.chartview.show()
        self.chartview_2.setChart(self.chart2)
        self.chartview_2.show()


    def do_pieHover(self, sli, states):
        if states:
            sli.setExploded(True)
            sli.setLabelVisible(True)
        else:
            sli.setExploded(False)
            sli.setLabelVisible(False)

    def sendresume(self):
        print("投递")
        # 直接访问数据库
        conn = pymysql.connect(host="47.99.201.114", port=3306, user="root", password="Aa123456",
                               database="jobOfferinformation", charset="utf8")
        sql1 = "SELECT * FROM resume WHERE userid='2020211754' AND jobOfferid={};".format(self.jobOfferid)
        # 得到一个可以执行SQL语句的光标对象
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
        # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 执行SQL语句
        num = cursor.execute(sql1)
        print("已存在", num)
        if num == 0:
            sql2 = "INSERT INTO resume VALUES ('2020211754',{});".format(self.jobOfferid)
            print(sql2)
            res = cursor.execute(sql2)
            print("res是", res)
            message = "投递简历至{}成功！".format(self.all_job_datas[1][self.row][0])
            self.messagelist.append(message)
            self.slm.setStringList(self.messagelist)

        # 关闭光标对象
        cursor.close()
        # 关闭数据库连接
        conn.close()
        
        try:
            _thread.start_new_thread(self.getdata, ())
            message = "刷新成功！"
            self.messagelist.append(message)
            self.slm.setStringList(self.messagelist)
        except:
            print("刷新失败")


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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = UserWindow()
    sys.exit(app.exec_())