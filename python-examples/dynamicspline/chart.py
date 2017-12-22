from PyQt5.QtChart import QChart, QValueAxis, QSplineSeries
from PyQt5.Qt import QPen

from PyQt5.QtCore import Qt, QTime, QTimer, pyqtSlot

import random


class Chart(QChart):

    def __init__(self):
        super(QChart, self).__init__()

        self.m_timer = QTimer()
        self.m_series = None
        self.m_titles = []
        self.m_axis = QValueAxis()
        self.m_step = None
        self.m_x = 5
        self.m_y = 1

        random.seed(QTime.currentTime().msec())

        self.m_timer.timeout.connect(self.handleTimeout)
        self.m_timer.setInterval(1000)

        self.m_series = QSplineSeries(self)
        green = QPen(Qt.green)
        green.setWidth(3)
        self.m_series.setPen(green)
        self.m_series.append(self.m_x, self.m_y)

        self.addSeries(self.m_series)
        self.createDefaultAxes()
        self.setAxisX(self.m_axis, self.m_series)
        self.m_axis.setTickCount(5)
        self.axisX().setRange(0, 10)
        self.axisY().setRange(-5, 10)

        self.m_timer.start()


    @pyqtSlot()
    def handleTimeout(self):
        x = self.plotArea().width() / self.m_axis.tickCount()
        y = (self.m_axis.max() - self.m_axis.min()) / self.m_axis.tickCount()
        self.m_x += y
        self.m_y = random.randint(0, 5) - 2.5
        self.m_series.append(self.m_x, self.m_y)
        self.scroll(x, 0)
        if self.m_x is 100:
            self.m_timer.stop()



