from PyQt5.Qt import QTextStream
from PyQt5.QtChart import QCandlestickSet


class CandlestickDataReader(QTextStream):

    def __init__(self, device):
        super(CandlestickDataReader, self).__init__(device)

    def read_file(self, device):
        QTextStream.setDevice(device)

    def read_candlestick_set(self):

        line = self.readLine()

        if line.startswith("#") or line is None:
            return None

        (timestamp, open_, high, low, close) = line.split(" ")  # SkipEmptyParts\

        candlestickset = QCandlestickSet(float(timestamp))
        candlestickset.setOpen(float(open_))
        candlestickset.setHigh(float(high))
        candlestickset.setLow(float(low))
        candlestickset.setClose(float(close))

        return candlestickset


