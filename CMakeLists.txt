cmake_minimum_required(VERSION 3.9)
project(QtChartExample)

set(CMAKE_CXX_STANDARD 11)

set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOMOC ON)

# brew install qt5
# brew link --force qt5 && ln -s /usr/local/Cellar/qt5/5.9.3/mkspecs /usr/local/mkspecs &&
# ln -s /usr/local/Cellar/qt5/5.9.3/plugins /usr/local/plugins

find_package(Qt5 COMPONENTS Core Gui Widgets Charts Qml Quick Multimedia REQUIRED)

add_executable(AreaChart qtcharts/examples/charts/areachart/main.cpp)

add_executable(Audio qtcharts/examples/charts/audio/main.cpp
        qtcharts/examples/charts/audio/widget.cpp
        qtcharts/examples/charts/audio/xyseriesiodevice.cpp)

add_executable(BarChart qtcharts/examples/charts/barchart/main.cpp)

add_executable(BarModelMapper qtcharts/examples/charts/barmodelmapper/main.cpp
        qtcharts/examples/charts/barmodelmapper/customtablemodel.cpp
        qtcharts/examples/charts/barmodelmapper/tablewidget.cpp)

add_executable(BoxPlotChart qtcharts/examples/charts/boxplotchart/main.cpp
        qtcharts/examples/charts/boxplotchart/boxdatareader.cpp
        qtcharts/examples/charts/boxplotchart/boxplotdata.qrc)

add_executable(Callout qtcharts/examples/charts/callout/main.cpp
        qtcharts/examples/charts/callout/callout.cpp
        qtcharts/examples/charts/callout/view.cpp)

add_executable(CandleStick qtcharts/examples/charts/candlestickchart/main.cpp
        qtcharts/examples/charts/candlestickchart/candlestickdatareader.cpp
        qtcharts/examples/charts/candlestickchart/candlestickdata.qrc)

add_executable(ChartInteractions qtcharts/examples/charts/chartinteractions/main.cpp
        qtcharts/examples/charts/chartinteractions/chart.cpp
        qtcharts/examples/charts/chartinteractions/chartview.cpp)

add_executable(ChartThemes qtcharts/examples/charts/chartthemes/main.cpp
        qtcharts/examples/charts/chartthemes/themewidget.cpp)

add_executable(CustomChart qtcharts/examples/charts/customchart/main.cpp)

add_executable(DateTimeAxis qtcharts/examples/charts/datetimeaxis/main.cpp
        qtcharts/examples/charts/datetimeaxis/sundata.qrc)

add_executable(DonutBreakdown qtcharts/examples/charts/donutbreakdown/main.cpp
        qtcharts/examples/charts/donutbreakdown/mainslice.cpp
        qtcharts/examples/charts/donutbreakdown/donutbreakdownchart.cpp)

add_executable(DonutChart qtcharts/examples/charts/donutchart/main.cpp)

add_executable(DynamicSpline qtcharts/examples/charts/dynamicspline/main.cpp
        qtcharts/examples/charts/dynamicspline/chart.cpp)

add_executable(HorizontalBarChart qtcharts/examples/charts/horizontalbarchart/main.cpp)

add_executable(HorizontalPercentBarChart qtcharts/examples/charts/horizontalpercentbarchart/main.cpp)

add_executable(HorizontalStackedBarChart qtcharts/examples/charts/horizontalstackedbarchart/main.cpp)

add_executable(Legend qtcharts/examples/charts/legend/main.cpp
        qtcharts/examples/charts/legend/mainwidget.cpp)

add_executable(LegendMarkers qtcharts/examples/charts/legendmarkers/main.cpp
        qtcharts/examples/charts/legendmarkers/mainwidget.cpp)

add_executable(LineAndBar qtcharts/examples/charts/lineandbar/main.cpp)

add_executable(LineChart qtcharts/examples/charts/linechart/main.cpp)

add_executable(LogValueAxis qtcharts/examples/charts/logvalueaxis/main.cpp)

add_executable(ModelData qtcharts/examples/charts/modeldata/main.cpp
        qtcharts/examples/charts/modeldata/tablewidget.cpp
        qtcharts/examples/charts/modeldata/customtablemodel.cpp)

add_executable(MultiAxis qtcharts/examples/charts/multiaxis/main.cpp)

add_executable(NestedDonut qtcharts/examples/charts/nesteddonuts/main.cpp
        qtcharts/examples/charts/nesteddonuts/widget.cpp)

add_executable(OpenGLSeries qtcharts/examples/charts/openglseries/main.cpp
        qtcharts/examples/charts/openglseries/datasource.cpp)

add_executable(PercentBarChart qtcharts/examples/charts/percentbarchart/main.cpp)

add_executable(PieChart qtcharts/examples/charts/piechart/main.cpp)

add_executable(PieChartCustomization qtcharts/examples/charts/piechartcustomization/main.cpp
        qtcharts/examples/charts/piechartcustomization/brushtool.cpp
        qtcharts/examples/charts/piechartcustomization/customslice.cpp
        qtcharts/examples/charts/piechartcustomization/mainwidget.cpp
        qtcharts/examples/charts/piechartcustomization/pentool.cpp)

add_executable(PieChartDrillDown qtcharts/examples/charts/piechartdrilldown/main.cpp
        qtcharts/examples/charts/piechartdrilldown/drilldownchart.cpp
        qtcharts/examples/charts/piechartdrilldown/drilldownslice.cpp)

add_executable(PolarChart qtcharts/examples/charts/polarchart/main.cpp
        qtcharts/examples/charts/polarchart/chartview.cpp)

add_executable(QMLAxes qtcharts/examples/charts/qmlaxes/main.cpp
        qtcharts/examples/charts/qmlaxes/resources.qrc)

add_executable(QMLBoxPlot qtcharts/examples/charts/qmlboxplot/main.cpp
        qtcharts/examples/charts/qmlboxplot/resources.qrc)

add_executable(QMLCandleStick qtcharts/examples/charts/qmlcandlestick/main.cpp
        qtcharts/examples/charts/qmlcandlestick/resources.qrc)

add_executable(QMLChart qtcharts/examples/charts/qmlchart/main.cpp
        qtcharts/examples/charts/qmlchart/resources.qrc)

target_link_libraries(AreaChart Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(Audio Qt5::Core Qt5::Widgets Qt5::Charts Qt5::Multimedia)
target_link_libraries(BarChart Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(BarModelMapper Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(BoxPlotChart Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(Callout Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(CandleStick Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(ChartInteractions Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(ChartThemes Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(CustomChart Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(DateTimeAxis Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(DonutBreakdown Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(DonutChart Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(DynamicSpline Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(HorizontalBarChart Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(HorizontalPercentBarChart Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(HorizontalStackedBarChart Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(Legend Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(LegendMarkers Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(LineAndBar Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(LineChart Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(LogValueAxis Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(ModelData Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(MultiAxis Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(NestedDonut Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(OpenGLSeries Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(PercentBarChart Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(PieChart Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(PieChartCustomization Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(PieChartDrillDown Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(PolarChart Qt5::Core Qt5::Widgets Qt5::Charts)
target_link_libraries(QMLAxes Qt5::Core Qt5::Widgets Qt5::Charts Qt5::Qml Qt5::Quick)
target_link_libraries(QMLBoxPlot Qt5::Core Qt5::Widgets Qt5::Charts Qt5::Qml Qt5::Quick)
target_link_libraries(QMLCandleStick Qt5::Core Qt5::Widgets Qt5::Charts Qt5::Qml Qt5::Quick)
target_link_libraries(QMLChart Qt5::Core Qt5::Widgets Qt5::Charts Qt5::Qml Qt5::Quick)
