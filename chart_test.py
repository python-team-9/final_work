import sys, math
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChartView,QChart,QLineSeries,QValueAxis
class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Demo12_1, QChart基本绘 图")
        self.resize(580,420)
        ##创建chart和chartView
        chart = QChart() #创建 chart
        chart.setTitle("简单函数曲线")
        chartView=QChartView(self) #创建 chartView
        chartView.setChart(chart) #chart添加到 chartView
        self.setCentralWidget(chartView) ##创建曲线序列
        series0 = QLineSeries()
        series1 = QLineSeries()
        series0.setName("Sin曲线")
        series1.setName("Cos曲线")
        chart.addSeries(series0) #序列添加到图表
        chart.addSeries(series1) ##序列添加数值
        t=0
        intv=0.1
        pointCount=100
        for i in range(pointCount):
            y1=math.cos(t)
            series0.append(t,y1)
            y2=1.5*math.sin(t+20)
            series1.append(t,y2)
            t=t+intv
##创建坐标轴
        axisX = QValueAxis() #x轴
        axisX.setRange(0, 10) #设置坐标轴范围
        axisX.setTitleText("time(secs)") #轴标题
        axisY = QValueAxis() #y轴
        axisY.setRange(-2, 2)
        axisY.setTitleText("value") ##为序列设置坐标轴
        chart.setAxisX(axisX, series0) #为序列 series0设置坐标轴
        chart.setAxisY(axisY, series0)
        chart.setAxisX(axisX, series1) #为序列 series1设置坐标轴
        chart.setAxisY(axisY, series1)
        ## ============窗体测试程序 ============================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form=QmyMainWindow()
    form.show()
    sys.exit(app.exec_())


