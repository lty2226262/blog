# hello world

新建console

main.cpp

```cpp
#include <QCoreApplication>
#include <QDebug>

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QString mStr = "hello world";

    qDebug() << "hello world";
    qDebug() << mStr;

    return a.exec();
}
```

qt-002.pro

```
#-------------------------------------------------
#
# Project created by QtCreator 2014-06-17T13:39:21
# Lost tutorial re-created by Ian Co (ian@tower.com.ph)
#
#-------------------------------------------------

QT       += core # adding the core framework

QT       -= gui #removing the gui portion

TARGET = Qt-002 
CONFIG   += console # add console config
CONFIG   -= app_bundle # remove app_bundle config

TEMPLATE = app


SOURCES += main.cpp
```

