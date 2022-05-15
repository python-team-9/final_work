#include "commonuserwindow.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    CommonUserWindow w;
    w.show();

    return a.exec();
}
