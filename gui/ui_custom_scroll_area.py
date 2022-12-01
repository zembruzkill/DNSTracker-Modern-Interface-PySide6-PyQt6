# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'custom_scroll_areajfZTAd.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_CustomScrollArea(object):
    def setupUi(self, CustomScrollArea):
        if not CustomScrollArea.objectName():
            CustomScrollArea.setObjectName(u"CustomScrollArea")
        CustomScrollArea.resize(544, 474)
        CustomScrollArea.setStyleSheet(u"QWidget#scrollArea_contents{\n"
"	background-color: rgb(21, 26, 48);\n"
"}")
        self.verticalLayout = QVBoxLayout(CustomScrollArea)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(CustomScrollArea)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea_contents = QWidget()
        self.scrollArea_contents.setObjectName(u"scrollArea_contents")
        self.scrollArea_contents.setGeometry(QRect(0, 0, 520, 450))
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea_contents.sizePolicy().hasHeightForWidth())
        self.scrollArea_contents.setSizePolicy(sizePolicy1)
        self.scrollArea.setWidget(self.scrollArea_contents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(CustomScrollArea)

        QMetaObject.connectSlotsByName(CustomScrollArea)
    # setupUi

    def retranslateUi(self, CustomScrollArea):
        CustomScrollArea.setWindowTitle(QCoreApplication.translate("CustomScrollArea", u"Form", None))
    # retranslateUi

