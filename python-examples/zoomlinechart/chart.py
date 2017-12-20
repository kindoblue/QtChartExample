from PyQt5.QtChart import QChart
from PyQt5.Qt import QEvent, QPinchGesture
from PyQt5.QtCore import Qt


class Chart(QChart):

    def __init__(self):
        super(QChart, self).__init__()
        self.grabGesture(Qt.PanGesture)
        self.grabGesture(Qt.PinchGesture)

    def scene_event(self, event):

        if event.type == QEvent.Gesture:
            return self.gesture_event(event)

        return QChart.event(event)

    def gesture_event(self, event):

        pan = event.getGesture(Qt.PanGesture)

        if pan:
            QChart.scroll(pan.delta().x(), pan.delta().y())

        pinch = event.getGesture(Qt.PinchGesture)

        if pinch:
            if pinch.changeFlags() & QPinchGesture.ScaleFactorChanged:
                QChart.zoom(pinch.scaleFactor())

        return True
