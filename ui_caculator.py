# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'caculator.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(361, 588)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.outputLabel = QLabel(self.centralwidget)
        self.outputLabel.setObjectName(u"outputLabel")
        self.outputLabel.setGeometry(QRect(10, 10, 341, 91))
        font = QFont()
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.outputLabel.setFrameShape(QFrame.Box)
        self.outputLabel.setFrameShadow(QFrame.Plain)
        self.outputLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.outputLabel.setMargin(10)
        self.percentButton = QPushButton(self.centralwidget)
        self.percentButton.setObjectName(u"percentButton")
        self.percentButton.setGeometry(QRect(10, 110, 80, 80))
        font1 = QFont()
        font1.setPointSize(26)
        self.percentButton.setFont(font1)
        self.percentButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:40px;\n"
"	background-color:rgb(160,160,160);\n"
"	color:rgb(255,255,255);\n"
"	min-width:80px;\n"
"	min-height:80px;\n"
"	max-width:80px;\n"
"	max-height:80px;\n"
"	padding:0;\n"
"\n"
"}")
        self.percentButton.setCheckable(False)
        self.arrowButton = QPushButton(self.centralwidget)
        self.arrowButton.setObjectName(u"arrowButton")
        self.arrowButton.setGeometry(QRect(185, 110, 80, 80))
        self.arrowButton.setFont(font1)
        self.arrowButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:40px;\n"
"	background-color:rgb(160,160,160);\n"
"	color:rgb(255,255,255);\n"
"	min-width:80px;\n"
"	min-height:80px;\n"
"	max-width:80px;\n"
"	max-height:80px;\n"
"	padding:0;\n"
"\n"
"}")
        self.divineButton = QPushButton(self.centralwidget)
        self.divineButton.setObjectName(u"divineButton")
        self.divineButton.setGeometry(QRect(275, 110, 80, 80))
        self.divineButton.setFont(font1)
        self.divineButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:40px;\n"
"	background-color:rgb(246,154,6);\n"
"	color:rgb(255,255,255);\n"
"	min-width:80px;\n"
"	min-height:80px;\n"
"	max-width:80px;\n"
"	max-height:80px;\n"
"	padding:0;\n"
"\n"
"}")
        self.cButton = QPushButton(self.centralwidget)
        self.cButton.setObjectName(u"cButton")
        self.cButton.setGeometry(QRect(100, 110, 80, 80))
        self.cButton.setFont(font1)
        self.cButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:40px;\n"
"	background-color:rgb(160,160,160);\n"
"	color:rgb(255,255,255);\n"
"	min-width:80px;\n"
"	min-height:80px;\n"
"	max-width:80px;\n"
"	max-height:80px;\n"
"	padding:0;\n"
"\n"
"}")
        self.nineButton = QPushButton(self.centralwidget)
        self.nineButton.setObjectName(u"nineButton")
        self.nineButton.setGeometry(QRect(185, 197, 80, 80))
        self.nineButton.setFont(font1)
        self.nineButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:40px;\n"
"	background-color:rgb(49,49,49);\n"
"	color:rgb(255,255,255);\n"
"	min-width:80px;\n"
"	min-height:80px;\n"
"	max-width:80px;\n"
"	max-height:80px;\n"
"	padding:0;\n"
"\n"
"}")
        self.multiplyButton = QPushButton(self.centralwidget)
        self.multiplyButton.setObjectName(u"multiplyButton")
        self.multiplyButton.setGeometry(QRect(275, 197, 80, 80))
        self.multiplyButton.setFont(font1)
        self.multiplyButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:40px;\n"
"	background-color:rgb(246,154,6);\n"
"	color:rgb(255,255,255);\n"
"	min-width:80px;\n"
"	min-height:80px;\n"
"	max-width:80px;\n"
"	max-height:80px;\n"
"	padding:0;\n"
"\n"
"}")
        self.eightButton = QPushButton(self.centralwidget)
        self.eightButton.setObjectName(u"eightButton")
        self.eightButton.setGeometry(QRect(100, 197, 80, 80))
        self.eightButton.setFont(font1)
        self.eightButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:40px;\n"
"	background-color:rgb(49,49,49);\n"
"	color:rgb(255,255,255);\n"
"	min-width:80px;\n"
"	min-height:80px;\n"
"	max-width:80px;\n"
"	max-height:80px;\n"
"	padding:0;\n"
"\n"
"}")
        self.sevenButton = QPushButton(self.centralwidget)
        self.sevenButton.setObjectName(u"sevenButton")
        self.sevenButton.setGeometry(QRect(10, 197, 80, 80))
        self.sevenButton.setFont(font1)
        self.sevenButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:40px;\n"
"	background-color:rgb(49,49,49);\n"
"	color:rgb(255,255,255);\n"
"	min-width:80px;\n"
"	min-height:80px;\n"
"	max-width:80px;\n"
"	max-height:80px;\n"
"	padding:0;\n"
"\n"
"}")
        self.sixButton = QPushButton(self.centralwidget)
        self.sixButton.setObjectName(u"sixButton")
        self.sixButton.setGeometry(QRect(185, 284, 80, 80))
        self.sixButton.setFont(font1)
        self.sixButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:40px;\n"
"	background-color:rgb(49,49,49);\n"
"	color:rgb(255,255,255);\n"
"	min-width:80px;\n"
"	min-height:80px;\n"
"	max-width:80px;\n"
"	max-height:80px;\n"
"	padding:0;\n"
"\n"
"}")
        self.minusButton = QPushButton(self.centralwidget)
        self.minusButton.setObjectName(u"minusButton")
        self.minusButton.setGeometry(QRect(275, 284, 80, 80))
        self.minusButton.setFont(font1)
        self.minusButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:40px;\n"
"	background-color:rgb(246,154,6);\n"
"	color:rgb(255,255,255);\n"
"	min-width:80px;\n"
"	min-height:80px;\n"
"	max-width:80px;\n"
"	max-height:80px;\n"
"	padding:0;\n"
"\n"
"}")
        self.fiveButton = QPushButton(self.centralwidget)
        self.fiveButton.setObjectName(u"fiveButton")
        self.fiveButton.setGeometry(QRect(100, 284, 80, 80))
        self.fiveButton.setFont(font1)
        self.fiveButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:40px;\n"
"	background-color:rgb(49,49,49);\n"
"	color:rgb(255,255,255);\n"
"	min-width:80px;\n"
"	min-height:80px;\n"
"	max-width:80px;\n"
"	max-height:80px;\n"
"	padding:0;\n"
"\n"
"}")
        self.fourButton = QPushButton(self.centralwidget)
        self.fourButton.setObjectName(u"fourButton")
        self.fourButton.setGeometry(QRect(10, 284, 80, 80))
        self.fourButton.setFont(font1)
        self.fourButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:40px;\n"
"	background-color:rgb(49,49,49);\n"
"	color:rgb(255,255,255);\n"
"	min-width:80px;\n"
"	min-height:80px;\n"
"	max-width:80px;\n"
"	max-height:80px;\n"
"	padding:0;\n"
"\n"
"}")
        self.threeButton = QPushButton(self.centralwidget)
        self.threeButton.setObjectName(u"threeButton")
        self.threeButton.setGeometry(QRect(185, 371, 80, 80))
        self.threeButton.setFont(font1)
        self.threeButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:40px;\n"
"	background-color:rgb(49,49,49);\n"
"	color:rgb(255,255,255);\n"
"	min-width:80px;\n"
"	min-height:80px;\n"
"	max-width:80px;\n"
"	max-height:80px;\n"
"	padding:0;\n"
"\n"
"}")
        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(275, 371, 80, 80))
        self.addButton.setFont(font1)
        self.addButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:40px;\n"
"	background-color:rgb(246,154,6);\n"
"	color:rgb(255,255,255);\n"
"	min-width:80px;\n"
"	min-height:80px;\n"
"	max-width:80px;\n"
"	max-height:80px;\n"
"	padding:0;\n"
"\n"
"}")
        self.twoButton = QPushButton(self.centralwidget)
        self.twoButton.setObjectName(u"twoButton")
        self.twoButton.setGeometry(QRect(100, 371, 80, 80))
        self.twoButton.setFont(font1)
        self.twoButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:40px;\n"
"	background-color:rgb(49,49,49);\n"
"	color:rgb(255,255,255);\n"
"	min-width:80px;\n"
"	min-height:80px;\n"
"	max-width:80px;\n"
"	max-height:80px;\n"
"	padding:0;\n"
"\n"
"}")
        self.oneButton = QPushButton(self.centralwidget)
        self.oneButton.setObjectName(u"oneButton")
        self.oneButton.setGeometry(QRect(10, 371, 80, 80))
        self.oneButton.setFont(font1)
        self.oneButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:40px;\n"
"	background-color:rgb(49,49,49);\n"
"	color:rgb(255,255,255);\n"
"	min-width:80px;\n"
"	min-height:80px;\n"
"	max-width:80px;\n"
"	max-height:80px;\n"
"	padding:0;\n"
"\n"
"}")
        self.decimalButton = QPushButton(self.centralwidget)
        self.decimalButton.setObjectName(u"decimalButton")
        self.decimalButton.setGeometry(QRect(185, 458, 80, 80))
        self.decimalButton.setFont(font1)
        self.decimalButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:40px;\n"
"	background-color:rgb(49,49,49);\n"
"	color:rgb(255,255,255);\n"
"	min-width:80px;\n"
"	min-height:80px;\n"
"	max-width:80px;\n"
"	max-height:80px;\n"
"	padding:0;\n"
"\n"
"}")
        self.equalButton = QPushButton(self.centralwidget)
        self.equalButton.setObjectName(u"equalButton")
        self.equalButton.setGeometry(QRect(275, 458, 80, 80))
        self.equalButton.setFont(font1)
        self.equalButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:40px;\n"
"	background-color:rgb(246,154,6);\n"
"	color:rgb(255,255,255);\n"
"	min-width:80px;\n"
"	min-height:80px;\n"
"	max-width:80px;\n"
"	max-height:80px;\n"
"	padding:0;\n"
"\n"
"}")
        self.zeroButton = QPushButton(self.centralwidget)
        self.zeroButton.setObjectName(u"zeroButton")
        self.zeroButton.setGeometry(QRect(100, 458, 80, 80))
        self.zeroButton.setFont(font1)
        self.zeroButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:40px;\n"
"	background-color:rgb(49,49,49);\n"
"	color:rgb(255,255,255);\n"
"	min-width:80px;\n"
"	min-height:80px;\n"
"	max-width:80px;\n"
"	max-height:80px;\n"
"	padding:0;\n"
"\n"
"}")
        self.ansButton = QPushButton(self.centralwidget)
        self.ansButton.setObjectName(u"ansButton")
        self.ansButton.setGeometry(QRect(10, 458, 80, 80))
        self.ansButton.setFont(font1)
        self.ansButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:40px;\n"
"	background-color:rgb(49,49,49);\n"
"	color:rgb(255,255,255);\n"
"	min-width:80px;\n"
"	min-height:80px;\n"
"	max-width:80px;\n"
"	max-height:80px;\n"
"	padding:0;\n"
"\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 361, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Caculator", None))
        self.outputLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.percentButton.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.arrowButton.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.divineButton.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.cButton.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.nineButton.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.multiplyButton.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.eightButton.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.sevenButton.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.sixButton.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.minusButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.fiveButton.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.fourButton.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.threeButton.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.twoButton.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.oneButton.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.decimalButton.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.equalButton.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.zeroButton.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ansButton.setText(QCoreApplication.translate("MainWindow", u"Ans", None))
    # retranslateUi

