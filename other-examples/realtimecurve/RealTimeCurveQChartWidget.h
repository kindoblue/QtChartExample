/**
 * Example taken from https://xtuer.github.io/qtbook-paint-realtime-curve-qchart/
 */

#ifndef QTCHARTEXAMPLE_REALTIMECURVEQCHARTWIDGET_H
#define QTCHARTEXAMPLE_REALTIMECURVEQCHARTWIDGET_H

#include <QtWidgets/QWidget>
#include <QtCore/QList>
#include <QtCharts/QSplineSeries>
#include <QtCharts/QScatterSeries>
#include <QtCharts/QChart>
#include <QtCharts/QChartView>

using namespace QtCharts;
class RealTimeCurveQChartWidget : public QWidget {
Q_OBJECT
public:
    explicit RealTimeCurveQChartWidget(QWidget *parent = 0);
    ~RealTimeCurveQChartWidget() = default;
protected:
    void timerEvent(QTimerEvent *event) Q_DECL_OVERRIDE;
private:
    /**
     * 接收到数据源发送来的数据，数据源可以下位机，采集卡，传感器等。
     */
    void dataReceived(int value);
    int timerId;
    int maxSize;  // data 最多存储 maxSize 个元素
    int maxValue; // 业务数据的最大值
    QList<double> data; // 存储业务数据的 list
    QChart *chart;
    QChartView *chartView;
    QSplineSeries *splineSeries;
    QScatterSeries *scatterSeries;
};

#endif //QTCHARTEXAMPLE_REALTIMECURVEQCHARTWIDGET_H
