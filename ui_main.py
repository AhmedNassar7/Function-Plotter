# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.functionInput = QLineEdit(self.centralwidget)
        self.functionInput.setObjectName(u"functionInput")

        self.verticalLayout.addWidget(self.functionInput)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.minInput = QLineEdit(self.centralwidget)
        self.minInput.setObjectName(u"minInput")

        self.horizontalLayout.addWidget(self.minInput)

        self.maxInput = QLineEdit(self.centralwidget)
        self.maxInput.setObjectName(u"maxInput")

        self.horizontalLayout.addWidget(self.maxInput)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.plotButton = QPushButton(self.centralwidget)
        self.plotButton.setObjectName(u"plotButton")

        self.verticalLayout.addWidget(self.plotButton)

        self.errorLabel = QLabel(self.centralwidget)
        self.errorLabel.setObjectName(u"errorLabel")

        self.verticalLayout.addWidget(self.errorLabel)

        self.plotWidget = QWidget(self.centralwidget)
        self.plotWidget.setObjectName(u"plotWidget")
        self.plotLayout = QVBoxLayout(self.plotWidget)
        self.plotLayout.setObjectName(u"plotLayout")
        self.plotLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.plotWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Function Plotter", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.functionInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter function of x (e.g., 5*x^3 + 2*x)", None))
        self.minInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Min value of x", None))
        self.maxInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Max value of x", None))
        self.plotButton.setText(QCoreApplication.translate("MainWindow", u"Plot Function", None))
        self.errorLabel.setText("")
    # retranslateUi

