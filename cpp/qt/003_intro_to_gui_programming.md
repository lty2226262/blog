# 3. Intro to GUI programming

按钮，连接到关闭主窗口。



拖出来一个按钮，然后点上面的`Edit Signals`，选中一下`show signals and slots inherited from QWidget `。

然后选clicked（），close（）

Qt-003.pro

```cpp
#-------------------------------------------------
#
# Project created by QtCreator 2014-06-17T13:45:36
# Lost tutorial re-created by Ian Co (ian@tower.com.ph)
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = Qt-003
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp

HEADERS  += mainwindow.h

FORMS    += mainwindow.ui
```

main.cpp

```cpp
// QT Tutorial
// http://www.voidrealms.com
// https://www.youtube.com/watch?v=6KtOzh0StTc&list=PL7C604D492F9E0E0B

// for Qt5: instead of choosing "Qt Gui Application"
//    select "Qt Widgets Application" instead

#include "mainwindow.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();

    return a.exec();
}
```

mainwindow.cpp

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
    ui->pushButton->setText("Close");
}

MainWindow::~MainWindow()
{
    delete ui;
}
```

mainwindow.h

```cpp
#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
```

mainwindow.ui

```cpp
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralWidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>20</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>PushButton</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menuBar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>400</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QToolBar" name="mainToolBar">
   <attribute name="toolBarArea">
    <enum>TopToolBarArea</enum>
   </attribute>
   <attribute name="toolBarBreak">
    <bool>false</bool>
   </attribute>
  </widget>
  <widget class="QStatusBar" name="statusBar"/>
 </widget>
 <layoutdefault spacing="6" margin="11"/>
 <resources/>
 <connections>
  <connection>
   <sender>pushButton</sender>
   <signal>clicked()</signal>
   <receiver>MainWindow</receiver>
   <slot>close()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>59</x>
     <y>75</y>
    </hint>
    <hint type="destinationlabel">
     <x>121</x>
     <y>119</y>
    </hint>
   </hints>
  </connection>
 </connections>
</ui>
```

