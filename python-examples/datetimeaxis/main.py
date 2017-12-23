from PyQt5.Qt import QMainWindow, QApplication, QPainter, QFile, QIODevice, QTextStream
from PyQt5.QtChart import QChart, QValueAxis, QLineSeries, QChartView, QDateTimeAxis
from PyQt5.QtCore import Qt, QDateTime, QDate

# example qtcharts/examples/datetimeaxis tranlated in python
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    # [1]
    series = QLineSeries()
    # [1]

    # [2]
    # data from http://www.swpc.noaa.gov/ftpdir/weekly/RecentIndices.txt
    # http://www.swpc.noaa.gov/ftpdir/weekly/README
    # http://www.weather.gov/disclaimer
    sunSpots = QFile("sun_spots.txt")
    if not sunSpots.open(QIODevice.ReadOnly | QIODevice.Text):
        sys.exit(1)

    stream = QTextStream(sunSpots)

    while not stream.atEnd():
        line = stream.readLine()

        if line.startswith("#") or line.startswith(":") or line is None:
            continue

        values = line.split()

        day = QDate(int(values[0]), int(values[1]), 15)

        momentInTime = QDateTime(day)

        series.append(momentInTime.toMSecsSinceEpoch(), float(values[3]))

    sunSpots.close()
    # [2]

    # [3] create the chart
    chart = QChart()
    chart.addSeries(series)
    chart.setTitle("Sunspots count (by Space Weather Prediction Center)")
    # [3]

    # [4]
    axisX = QDateTimeAxis()
    axisX.setTickCount(10)
    axisX.setFormat("MMM yyyy")
    axisX.setTitleText("Date")
    chart.addAxis(axisX, Qt.AlignBottom)
    series.attachAxis(axisX)

    axisY = QValueAxis()
    axisY.setLabelFormat("%i")
    axisY.setTitleText("Sunspots count")
    chart.addAxis(axisY, Qt.AlignLeft)
    series.attachAxis(axisY)
    # [4]

    # [5] prepare the chart view
    chartView = QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)
    # [5]

    # [6] show the main window
    window = QMainWindow()
    window.setCentralWidget(chartView)
    window.resize(800, 600)
    window.show()
    # [6]

    sys.exit(app.exec_())