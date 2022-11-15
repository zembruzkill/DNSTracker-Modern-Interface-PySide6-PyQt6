# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_chart_cardPBwwxR.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_ChartCard(object):
    def setupUi(self, ChartCard):
        if not ChartCard.objectName():
            ChartCard.setObjectName(u"ChartCard")
        ChartCard.resize(576, 406)
        ChartCard.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(ChartCard)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(ChartCard)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame#frame{\n"
"	background-color: rgb(50, 50, 88);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QLabel#card_title{\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"\n"
"QFrame#frame_main{\n"
"	border-top: 2px solid rgb(21, 26, 48);\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.card_title = QLabel(self.frame)
        self.card_title.setObjectName(u"card_title")
        self.card_title.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.card_title)

        self.frame_main = QFrame(self.frame)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_main)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(ChartCard)

        QMetaObject.connectSlotsByName(ChartCard)
    # setupUi

    def retranslateUi(self, ChartCard):
        ChartCard.setWindowTitle(QCoreApplication.translate("ChartCard", u"Form", None))
        self.card_title.setText(QCoreApplication.translate("ChartCard", u"Top DNS Providers Concentration per Year", None))
    # retranslateUi

