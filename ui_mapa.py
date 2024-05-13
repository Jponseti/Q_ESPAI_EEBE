# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'probaDRFCvI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1338, 743)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1321, 711))
        self.label.setPixmap(QPixmap(u"EEBE_Mapa_Temperatures/dibuix.png"))
        self.label.setScaledContents(True)
        self.aula1 = QLabel(self.centralwidget)
        self.aula1.setObjectName(u"aula1")
        self.aula1.setGeometry(QRect(50, 340, 191, 91))
        self.aula1.setPixmap(QPixmap(u"cuadrado blanco.png"))
        self.aula1.setScaledContents(True)
        self.T_aula1 = QLineEdit(self.centralwidget)
        self.T_aula1.setObjectName(u"T_aula1")
        self.T_aula1.setGeometry(QRect(100, 180, 113, 20))
        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(250, 0, 341, 201))
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(10, 530, 781, 20))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1338, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.T_aula1.textChanged.connect(MainWindow.update_color)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.aula1.setText("")
    # retranslateUi

