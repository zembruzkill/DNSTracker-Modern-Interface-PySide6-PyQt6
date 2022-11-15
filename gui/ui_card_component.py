# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'card_componentMuBXQu.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_CardComponent(object):
    def setupUi(self, CardComponent):
        if not CardComponent.objectName():
            CardComponent.setObjectName(u"CardComponent")
        CardComponent.resize(263, 104)
        CardComponent.setStyleSheet(u"QFrame#frame{\n"
"	background-color: #323258;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QFrame#card_frame_svg{\n"
"	background-color: #A16EFF;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLabel#card_title{\n"
"	font-size: 15pt;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#card_button{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 #B18AFF, stop:1 #A16FFF);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#card_button::hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 #D3BCFF, stop:1 #B18AFE);\n"
"}\n"
"\n"
"QFrame#circular_background{\n"
"	background-color: rgb(21, 26, 48);\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"QFrame#main_frame{\n"
"	background-color: rgb(50, 50, 88);\n"
"	border-radius: 23px;\n"
"}\n"
"\n"
"QLabel#card_value{\n"
"	color: white;\n"
"	font-weight: bold;\n"
"	font-size: 18px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(CardComponent)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(CardComponent)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame#frame{\n"
"	border-bottom: 6px solid rgb(66, 148, 245);\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.card_title = QLabel(self.frame)
        self.card_title.setObjectName(u"card_title")
        self.card_title.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.card_title)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.card_value = QLabel(self.frame_2)
        self.card_value.setObjectName(u"card_value")

        self.horizontalLayout_2.addWidget(self.card_value)

        self.circular_background = QFrame(self.frame_2)
        self.circular_background.setObjectName(u"circular_background")
        self.circular_background.setMinimumSize(QSize(60, 60))
        self.circular_background.setMaximumSize(QSize(60, 60))
        self.circular_background.setFrameShape(QFrame.NoFrame)
        self.circular_background.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.circular_background)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.circular_prog = QFrame(self.circular_background)
        self.circular_prog.setObjectName(u"circular_prog")
        self.circular_prog.setStyleSheet(u"QFrame#circular_prog{\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:271, stop:0.499 rgba(57, 127, 236, 0), stop:0.5 rgba(56, 127, 238, 255));\n"
"	border-radius: 30px;\n"
"}")
        self.circular_prog.setFrameShape(QFrame.NoFrame)
        self.circular_prog.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.circular_prog)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(7, 7, 7, 7)
        self.main_frame = QFrame(self.circular_prog)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.main_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.card_percentage = QLabel(self.main_frame)
        self.card_percentage.setObjectName(u"card_percentage")

        self.verticalLayout_4.addWidget(self.card_percentage)


        self.verticalLayout_3.addWidget(self.main_frame)


        self.verticalLayout_2.addWidget(self.circular_prog)


        self.horizontalLayout_2.addWidget(self.circular_background)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(CardComponent)

        QMetaObject.connectSlotsByName(CardComponent)
    # setupUi

    def retranslateUi(self, CardComponent):
        CardComponent.setWindowTitle(QCoreApplication.translate("CardComponent", u"Form", None))
        self.card_title.setText(QCoreApplication.translate("CardComponent", u"Card Title", None))
        self.card_value.setText(QCoreApplication.translate("CardComponent", u"1.000.000", None))
        self.card_percentage.setText(QCoreApplication.translate("CardComponent", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">50</span></p></body></html>", None))
    # retranslateUi

