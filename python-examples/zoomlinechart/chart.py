from PyQt5.QtChart import QChart
from PyQt5.Qt import QEvent, QPinchGesture
from PyQt5.QtCore import Qt


class Chart(QChart):

    def __init__(self):
        super(QChart, self).__init__()

        # Seems that QGraphicsView (QChartView) does not grab gestures.
        # They can only be grabbed here in the QGraphicsWidget (QChart).
        self.grabGesture(Qt.PanGesture)
        self.grabGesture(Qt.PinchGesture)

    def sceneEvent(self, event):

        if event.type() in (QEvent.Gesture,):
            return self.gestureEvent(event)

        return super(QChart, self).event(event)

    def gestureEvent(self, event):

        pan = event.gesture(Qt.PanGesture)

        if pan:
            QChart.scroll(pan.delta().x(), pan.delta().y())

        pinch = event.gesture(Qt.PinchGesture)

        if pinch:
            if pinch.changeFlags() & QPinchGesture.ScaleFactorChanged:
                self.zoom(pinch.scaleFactor())

        return True
