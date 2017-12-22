from PyQt5.QtCore import Qt, QPointF
from PyQt5.Qt import QMainWindow, QApplication, QPainter
from PyQt5.QtChart import QChart, QChartView, QLineSeries

from chart import Chart
from chartview import ChartView

import math
import random

# example qtcharts/examples/zoomlinechart tranlated in python
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    # [1]
    series = QLineSeries()
    for i in range(500):
        p = QPointF(i, 100 * math.sin(math.pi/50 * i) + random.randint(0, 20))
        series.append(p)
    # [1]

    chart = Chart()
    chart.addSeries(series)
    chart.setTitle("Zoom in/out example")
    chart.setAnimationOptions(QChart.SeriesAnimations)
    chart.legend().hide()
    chart.createDefaultAxes()

    chartView = ChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)

    window = QMainWindow()

    window.setCentralWidget(chartView)
    window.resize(400, 300)
    window.grabGesture(Qt.PanGesture)
    window.grabGesture(Qt.PinchGesture)
    window.show()

    sys.exit(app.exec_())
