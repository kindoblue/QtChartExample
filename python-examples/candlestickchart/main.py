from PyQt5.QtCore import Qt
from PyQt5.Qt import QMainWindow, QApplication, QColor, QDateTime, QIODevice, QFile, QPainter
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QCandlestickSeries, QCandlestickSet
from candlestickdatareader import CandlestickDataReader


# example qtcharts/examples/candlestickchart tranlated in python
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    # [1]
    acmeSeries = QCandlestickSeries()
    acmeSeries.setName("Acme Ltd");
    acmeSeries.setIncreasingColor(QColor("light green"))
    acmeSeries.setDecreasingColor(QColor("red"))
    # [1]

    # [2]  load the data
    acmeData = QFile("acme_data.txt")
    if not acmeData.open(QIODevice.ReadOnly | QIODevice.Text):
        sys.exit(1)

    categories = []
    dataReader = CandlestickDataReader(acmeData)

    while not dataReader.atEnd():
        line = dataReader.read_candlestick_set()
        if line is not None:
            acmeSeries.append(line)
            categories.append(QDateTime.fromMSecsSinceEpoch(line.timestamp()).toString("dd"))

    # [2]

    # [3] create the chart
    chart = QChart()
    chart.addSeries(acmeSeries)
    chart.setTitle("Acme Ltd Historical Data (July 2015)")
    chart.setAnimationOptions(QChart.SeriesAnimations)
    # [3]

    # [4] set the axes properties
    chart.createDefaultAxes()
    axisX = chart.axes(Qt.Horizontal)[0]
    axisX.setCategories(categories)

    axisY = chart.axes(Qt.Vertical)[0]
    axisY.setMax(axisY.max() * 1.01)
    axisY.setMin(axisY.min() * 0.99)
    # [4]

    # [5]
    chart.legend().setVisible(True)
    chart.legend().setAlignment(Qt.AlignBottom)
    # [5]

    # [6] prepare the chart view
    chartView = QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)
    # [6]

    # [7] show the main window
    window = QMainWindow()
    window.setCentralWidget(chartView)
    window.resize(800, 600)
    window.show()
    # [7]

    sys.exit(app.exec_())