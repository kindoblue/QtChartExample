/**
 * Example taken from https://evileg.com/en/post/275/
 */
#include "widget.h"

#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    QMainWindow window;
    window.setCentralWidget(new Widget());
    window.resize(800, 600);
    window.show();

    return a.exec();
}
