/**
 * Example taken from https://xtuer.github.io/qtbook-paint-realtime-curve-qchart/
 */
#include "RealTimeCurveQChartWidget.h"
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);

    auto widget = new RealTimeCurveQChartWidget();

    QMainWindow window;
    window.setCentralWidget(widget);
    window.resize(400, 300);
    window.show();

    return a.exec();
}