/**
 * Example taken from https://evileg.com/en/post/275/
 */

#include "widget.h"
#include "ui_widget.h"

#include <QtCharts/QLogValueAxis>
#include <QtCharts/QLineSeries>
#include <QtCharts/QValueAxis>
#include <QtCharts/QChart>
#include <QtCharts/QChartView>

#include <math.h>

static int randomBetween(int low, int high, int seed)
{
    qsrand(seed); // Установка базового числа для отсчёта рандома в qrand
    return (qrand() % ((high + 1) - low) + low);
}

using namespace QtCharts;

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    // Инициализируещее число для установки базы рандома в qrand
    int seed = 0;

    for (int i = 0; i < 5; ++i)
    {
        // Создаём представление графика
        QChartView *chartView = new QChartView(this);
        chartView->setRenderHint(QPainter::Antialiasing);

        // Добавляем его в горизонтальный Layout
        ui->horizontalLayout->addWidget(chartView);

        // Создаём случайную синусоиду
        seed = randomBetween(0, 100, seed);
        QLineSeries *series = new QLineSeries();
        int k = 0;
        while (k <= 100)
        {
            *series << QPointF(sin((seed+ k)*0.1), k);
            ++k;
        }

        // Создаём график и добаляем в него синусоиду
        QChart *chart = new QChart();
        chart->addSeries(series);
        chart->legend()->hide();
        chart->setTitle("Graphic");

        // Добавим всплывающую подсказку для графика
        chart->setToolTip(QString("График №%1\n"
                                  "Количество отсчётов %2").arg(i + 1).arg(k));

        // Настройка осей графика
        QValueAxis *axisX = new QValueAxis();
        axisX->setTitleText("x, м");
        axisX->setLabelFormat("%i");
        axisX->setTickCount(1);
        chart->addAxis(axisX, Qt::AlignBottom);
        series->attachAxis(axisX);

        QValueAxis *axisY = new QValueAxis();
        axisY->setTitleText("t, мс");
        axisY->setLabelFormat("%g");
        axisY->setTickCount(5);
        chart->addAxis(axisY, Qt::AlignLeft);
        series->attachAxis(axisY);

        // Устанавливаем график в представление
        chartView->setChart(chart);
    }
}

Widget::~Widget()
{
    delete ui;
}
