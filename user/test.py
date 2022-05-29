from PyQt5.QtChart import QPieSeries, QChart, QPieSlice

from TCPmodule import m_recv
from userUI import *
import pymysql
import sys
import json
import _thread

from PyQt5.QtWidgets import QWidget, QTableView, QAbstractItemView, QToolTip, qApp, QPushButton, QLabel, QVBoxLayout, \
    QHBoxLayout, QApplication, QMainWindow, QHeaderView

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QCursor, QFont, QPainter


class UserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


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
        SELECT jobName,jobCompany,jobSalary,jobPlace FROM jobOfferDetail;
        """
        # 得到一个可以执行SQL语句的光标对象
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
        # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 执行SQL语句
        num = cursor.execute(sql)
        data = cursor.fetchall()
        # 关闭光标对象
        cursor.close()
        # 关闭数据库连接
        conn.close()
        print(num)
        print(data)
        datas = [num, data]
        self.all_job_datas = datas
        # 请求服务器访问数据库
        # jdata = [{'request': 'getJobDetail', 'begin': begin}]
        # client.send(json.dumps(jdata).encode())
        # j_res = json.loads(m_recv(client))
        # begin += j_res[0]['num']
        # self.all_job_datas = j_res[1:-1]
        # print(self.all_job_datas)

        self.column_name = ['工作名称', '公司', '薪酬', '工作地点']
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
        self.pieseries1 = QPieSeries()  # 定义PieSeries
        self.pieseries1.hovered.connect(self.do_pieHover)
        for x in data:
            self.pieseries1.append(x[0], x[1])  # 插入第一个元素
            print(x[0], x[1])

        self.slice = QPieSlice()
        print(1)
        for i in range(0, num):
            self.slice = self.pieseries1.slices()[i]
            self.slice.setLabelVisible(False)
            # slice.setPen(QPen(Qt.white, 10))
            self.slice.setBrush(QtGui.QColor(self.color[i]))

        self.pieseries2 = QPieSeries()  # 定义PieSeries
        self.pieseries2.hovered.connect(self.do_pieHover)
        for x in data2:
            self.pieseries2.append(x[0], x[1])  # 插入第一个元素
            print(x[0], x[1])

        self.slice2 = QPieSlice()
        print(1)
        for i in range(0, num2):
            self.slice2 = self.pieseries2.slices()[i]
            self.slice2.setLabelVisible(False)
            # slice.setPen(QPen(Qt.white, 10))
            self.slice2.setBrush(QtGui.QColor(self.color[i]))

        print(2)
        self.chart1 = QChart()  # 定义QChart
        self.chart2 = QChart()
        print(3)
        self.chart1.legend().hide()
        self.chart2.legend().hide()
        print(4)
        self.chart1.createDefaultAxes()
        self.chart2.createDefaultAxes()
        print(5)
        self.chart1.addSeries(self.pieseries1)  # 将 pieseries添加到chart里
        self.chart2.addSeries(self.pieseries2)
        print(6)
        self.chart1.setTitle("教育分布")  # 设置char的标题
        self.chart2.setTitle("地区分布")  # 设置char的标题
        print(7)
        self.chart1.legend().setVisible(True)
        self.chart2.legend().setVisible(True)
        print(8)
        self.chart1.legend().setAlignment(Qt.AlignBottom)# 对齐方式
        self.chart2.legend().setAlignment(Qt.AlignBottom)  # 对齐方式
        print(9)
        self.chartview = self.ui.chartview
        self.chartview_2 = self.ui.chartview_2
        self.chart1.setAnimationOptions(QChart.SeriesAnimations)
        self.chart2.setAnimationOptions(QChart.SeriesAnimations)
        self.chartview.setRenderHint(QPainter.Antialiasing)  # 设置抗锯齿
        self.chartview_2.setRenderHint(QPainter.Antialiasing)  # 设置抗锯齿
        print(10)
        self.chartview.setChart(self.chart1)
        self.chartview.show()
        self.chartview_2.setChart(self.chart2)
        self.chartview_2.show()
        print(11)

    def do_pieHover(self, sli, states):
        if states:
            sli.setExploded(True)
            sli.setLabelVisible(True)
        else:
            sli.setExploded(False)
            sli.setLabelVisible(False)

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