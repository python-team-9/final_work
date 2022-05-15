#include "commonuserwindow.h"
#include "ui_commonuserwindow.h"

CommonUserWindow::CommonUserWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::CommonUserWindow)
{
    ui->setupUi(this);
}

CommonUserWindow::~CommonUserWindow()
{
    delete ui;
}
