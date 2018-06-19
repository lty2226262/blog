# 4. Signals and Slots

用horizontal slidebar去控制progress bar。

可以拖动，也可以写connet。

```cpp

// QT Tutorial
// http://www.voidrealms.com
// https://www.youtube.com/watch?v=6KtOzh0StTc&list=PL7C604D492F9E0E0B

#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    connect(ui->horizontalSlider,SIGNAL(valueChanged(int)),
            ui->progressBar,SLOT(setValue(int)));

    connect(ui->horizontalSlider,SIGNAL(valueChanged(int)),
            ui->progressBar_2,SLOT(setValue(int)));

    disconnect(ui->horizontalSlider,SIGNAL(valueChanged(int)),
            ui->progressBar,SLOT(setValue(int)));
}

MainWindow::~MainWindow()
{
    delete ui;
}
```

