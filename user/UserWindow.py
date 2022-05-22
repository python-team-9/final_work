from userUI import *
import pymysql
import sys
from PyQt5.QtWidgets import QWidget, QTableView, QAbstractItemView, QToolTip, qApp, QPushButton, QLabel, QVBoxLayout, \
    QHBoxLayout, QApplication, QMainWindow, QHeaderView

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QCursor, QFont


def getdata():
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
    return datas

class UserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 隐藏窗口
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()

        self.all_job_datas = getdata()
        self.column_name = ['工作名称', '公司', '薪酬', '工作地点']
        self.model = QStandardItemModel(self.all_job_datas[0], len(self.all_job_datas[1][0]))
        self.model.setHorizontalHeaderLabels(self.column_name)
        self.table_view = self.ui.tableView
        self.table_view.setSelectionMode(QAbstractItemView.SingleSelection)  # 选中一个单元格
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectItems)  # 单元格选中模式
        self.table_view.doubleClicked.connect(self.get_table_item)
        self.table_view.clicked.connect(self.get_cell_tip)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 使表宽度自适应
        # self.table_view.setColumnWidth(0, 100)
        # self.table_view.setColumnWidth(1, 130)
        # self.table_view.setColumnWidth(2, 150)
        # self.table_view.setColumnWidth(3, 150)
        # self.table_view.setColumnWidth(4, 160)
        # self.table_view.setColumnWidth(5, 165)
        # 调节列宽度
        self.table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 表格不可编辑
        self.table_view.setModel(self.model)
        for i in range(self.all_job_datas[0]):
            for j in range(4):
                job_info = QStandardItem(str(self.all_job_datas[1][i][j]))
                self.model.setItem(i, j, job_info)
                job_info.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

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