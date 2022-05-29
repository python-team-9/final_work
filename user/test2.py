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


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5饼图")

        # 显示位置
        self.setGeometry(100, 100, 800, 600)
        self.create_piechart()
        self.show()

    def create_piechart(self):
        # 创建QPieSeries对象，它用来存放饼图的数据
        series = QPieSeries()

        module_name = ["trojan_trigger.v", "TSC.v", "aes_128.v"]
        signal_num = [128, 12, 8]
        color = [ "#ffc656", "#2fc7e8", "#3ed7b7"]
        for i in range(0, 3):
            # print(module_name[i], signal_num[i])
            series.append(module_name[i], signal_num[i])

        # 单独处理某个扇区
        slice = QPieSlice()
        for i in range(0, 3):
            slice = series.slices()[i]
            slice.setLabelVisible(True)
            # slice.setPen(QPen(Qt.white, 10))
            slice.setBrush(QtGui.QColor(color[i]))

        # 创建QChart实例，它是PyQt5中的类
        chart = QChart()
        # QLegend类是显示图表的图例，先隐藏掉
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()

        # 设置动画效果
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # 设置标题
        chart.setTitle("统计结果")

        chart.legend().setVisible(True)

        # 对齐方式
        chart.legend().setAlignment(Qt.AlignBottom)

        # 创建ChartView，它是显示图表的控件
        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartview)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
