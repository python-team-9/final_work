#ifndef COMMONUSERWINDOW_H
#define COMMONUSERWINDOW_H

#include <QMainWindow>

namespace Ui {
class CommonUserWindow;
}

class CommonUserWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit CommonUserWindow(QWidget *parent = 0);
    ~CommonUserWindow();

private:
    Ui::CommonUserWindow *ui;
};

#endif // COMMONUSERWINDOW_H
