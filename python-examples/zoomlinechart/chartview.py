
from PyQt5.QtChart import QChart, QChartView
from PyQt5.QtCore import Qt
from PyQt5.Qt import QEvent, QGraphicsView


class ChartView(QChartView):

    def __init__(self, chart):
        super(QChartView, self).__init__(chart)
        self.is_touching = False
        self.setRubberBand(QChartView.RectangleRubberBand)


    def viewportEvent(self, event):

        if event.type() == QEvent.TouchBegin:
            self.is_touching = True
            self.chart().setAnimationOptions(QChart.NoAnimation)

        return super(QChartView, self).viewportEvent(event)

    def mousePressEvent(self, event):
        if self.is_touching:
            return
        return super(QChartView, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.is_touching:
            return
        return super(QChartView, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.is_touching:
            self.is_touching = False
        self.chart().setAnimationOptions(QChart.SeriesAnimations)

        return super(QChartView, self).mouseReleaseEvent(event)

    def keyPressEvent(self, event):
        switcher = {
            Qt.Key_Plus: lambda chart: chart.zoomIn(),
            Qt.Key_Minus: lambda chart: chart.zoomOut(),
            Qt.Key_Left: lambda chart: chart.scroll(-10, 0),
            Qt.Key_Right: lambda chart: chart.scroll(10, 0),
            Qt.Key_Up: lambda chart: chart.scroll(0, 10),
            Qt.Key_Down: lambda chart: chart.scroll(0, -10)
        }

        func = switcher.get(event.key(), lambda chart: super(QGraphicsView, self).keyPressEvent(event))

        return func(self.chart())

