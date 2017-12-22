from PyQt5.Qt import QMainWindow, QApplication, QPainter
from PyQt5.QtChart import QChart, QChartView

from chart import Chart

# example qtcharts/examples/dynamicspline tranlated in python
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    chart = Chart()
    chart.setTitle("Zoom in/out example")
    chart.setAnimationOptions(QChart.AllAnimations)
    chart.legend().hide()

    chartView = QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)

    window = QMainWindow()

    window.setCentralWidget(chartView)
    window.resize(400, 300)
    window.show()

    sys.exit(app.exec_())