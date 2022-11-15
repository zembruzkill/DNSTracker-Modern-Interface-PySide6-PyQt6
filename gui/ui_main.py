# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainDmomdm.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1363, 659)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(1710, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QLabel, QPushButton{\n"
"	color: white;\n"
"}\n"
"\n"
"QWidget#top_menu_frame{\n"
"	background-color: #222B45;\n"
"}\n"
"\n"
"QWidget#dashboard_scrollArea_contents{\n"
"	background-color: rgb(21, 26, 48);\n"
"}\n"
"\n"
"Line{\n"
"	background-color: #1B1B38;\n"
"	max-height: 20px;\n"
"}\n"
"\n"
"QLabel#user_name{\n"
"	font-size: 15px;\n"
"	font-weight: bold;\n"
"	color: #FFFFFF;\n"
"}\n"
"\n"
"QLabel#system_name{\n"
"	color: #FFFFFF;\n"
"	font: \"Noto Sans\";\n"
"	font-size: 28px;\n"
"}\n"
"\n"
"QFrame#right_menu{\n"
"	background-color: #222B45;\n"
"}\n"
"\n"
"QFrame#left_main{\n"
"	background-color: #151A30;\n"
"}\n"
"\n"
"QPushButton#hamburger_menu{\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton#search_button,#email_button, #notification_button{\n"
"	border: none;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_menu_frame = QFrame(self.centralwidget)
        self.top_menu_frame.setObjectName(u"top_menu_frame")
        self.top_menu_frame.setMinimumSize(QSize(0, 76))
        self.top_menu_frame.setMaximumSize(QSize(16777215, 76))
        self.top_menu_frame.setFrameShape(QFrame.NoFrame)
        self.top_menu_frame.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout = QHBoxLayout(self.top_menu_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.top_menu_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(70, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.hamburger_menu = QPushButton(self.frame)
        self.hamburger_menu.setObjectName(u"hamburger_menu")
        self.hamburger_menu.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/icons/resources/icons/menu-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.hamburger_menu.setIcon(icon)
        self.hamburger_menu.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.hamburger_menu)


        self.horizontalLayout.addWidget(self.frame)

        self.line = QFrame(self.top_menu_frame)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(1, 22))
        self.line.setStyleSheet(u"background-color: #1B1B38;\n"
"max-height: 20px;")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.frame_2 = QFrame(self.top_menu_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.system_name = QLabel(self.frame_2)
        self.system_name.setObjectName(u"system_name")

        self.horizontalLayout_7.addWidget(self.system_name)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.top_menu_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(62, 16777215))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.search_button = QPushButton(self.frame_5)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/icons/search-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search_button.setIcon(icon1)
        self.search_button.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.search_button)


        self.horizontalLayout.addWidget(self.frame_5)

        self.line_2 = QFrame(self.top_menu_frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMaximumSize(QSize(1, 22))
        self.line_2.setStyleSheet(u"background-color: #1B1B38;\n"
"max-height: 20px;")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.frame_6 = QFrame(self.top_menu_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(62, 16777215))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.email_button = QPushButton(self.frame_6)
        self.email_button.setObjectName(u"email_button")
        self.email_button.setMinimumSize(QSize(30, 30))
        self.email_button.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icons/resources/icons/email-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.email_button.setIcon(icon2)
        self.email_button.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.email_button)


        self.horizontalLayout.addWidget(self.frame_6)

        self.line_3 = QFrame(self.top_menu_frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMaximumSize(QSize(1, 22))
        self.line_3.setStyleSheet(u"background-color: #1B1B38;\n"
"max-height: 20px;")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.frame_7 = QFrame(self.top_menu_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(62, 16777215))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.notification_button = QPushButton(self.frame_7)
        self.notification_button.setObjectName(u"notification_button")
        self.notification_button.setMinimumSize(QSize(30, 30))
        self.notification_button.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u":/icons/resources/icons/bell-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notification_button.setIcon(icon3)
        self.notification_button.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.notification_button)


        self.horizontalLayout.addWidget(self.frame_7)

        self.line_4 = QFrame(self.top_menu_frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMaximumSize(QSize(1, 22))
        self.line_4.setStyleSheet(u"background-color: #1B1B38;\n"
"max-height: 20px;")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_4)

        self.frame_8 = QFrame(self.top_menu_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(170, 16777215))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.user_pic = QLabel(self.frame_8)
        self.user_pic.setObjectName(u"user_pic")
        self.user_pic.setMaximumSize(QSize(50, 50))
        self.user_pic.setPixmap(QPixmap(u":/images/resources/images/86445195.png"))
        self.user_pic.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.user_pic)

        self.user_name = QLabel(self.frame_8)
        self.user_name.setObjectName(u"user_name")

        self.horizontalLayout_6.addWidget(self.user_name)


        self.horizontalLayout.addWidget(self.frame_8)


        self.verticalLayout.addWidget(self.top_menu_frame)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.main_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.right_menu = QFrame(self.main_frame)
        self.right_menu.setObjectName(u"right_menu")
        self.right_menu.setMinimumSize(QSize(251, 0))
        self.right_menu.setMaximumSize(QSize(251, 16777215))
        self.right_menu.setStyleSheet(u"")
        self.right_menu.setFrameShape(QFrame.NoFrame)
        self.right_menu.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.right_menu)

        self.left_main = QFrame(self.main_frame)
        self.left_main.setObjectName(u"left_main")
        self.left_main.setFrameShape(QFrame.NoFrame)
        self.left_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.left_main)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.left_main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.horizontalLayout_3 = QHBoxLayout(self.dashboard_page)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.dashboard_scrollArea = QScrollArea(self.dashboard_page)
        self.dashboard_scrollArea.setObjectName(u"dashboard_scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.dashboard_scrollArea.sizePolicy().hasHeightForWidth())
        self.dashboard_scrollArea.setSizePolicy(sizePolicy)
        self.dashboard_scrollArea.setFrameShape(QFrame.NoFrame)
        self.dashboard_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.dashboard_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.dashboard_scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.dashboard_scrollArea.setWidgetResizable(True)
        self.dashboard_scrollArea_contents = QWidget()
        self.dashboard_scrollArea_contents.setObjectName(u"dashboard_scrollArea_contents")
        self.dashboard_scrollArea_contents.setGeometry(QRect(0, 0, 1088, 559))
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dashboard_scrollArea_contents.sizePolicy().hasHeightForWidth())
        self.dashboard_scrollArea_contents.setSizePolicy(sizePolicy1)
        self.verticalLayout_10 = QVBoxLayout(self.dashboard_scrollArea_contents)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_cards = QFrame(self.dashboard_scrollArea_contents)
        self.frame_cards.setObjectName(u"frame_cards")
        self.frame_cards.setFrameShape(QFrame.NoFrame)
        self.frame_cards.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_cards)

        self.frame_middle = QFrame(self.dashboard_scrollArea_contents)
        self.frame_middle.setObjectName(u"frame_middle")
        self.frame_middle.setFrameShape(QFrame.NoFrame)
        self.frame_middle.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_middle)

        self.frame_bottom = QFrame(self.dashboard_scrollArea_contents)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_bottom)

        self.verticalSpacer = QSpacerItem(20, 454, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.dashboard_scrollArea.setWidget(self.dashboard_scrollArea_contents)

        self.horizontalLayout_3.addWidget(self.dashboard_scrollArea)

        self.stackedWidget.addWidget(self.dashboard_page)
        self.hosting_page = QWidget()
        self.hosting_page.setObjectName(u"hosting_page")
        self.verticalLayout_6 = QVBoxLayout(self.hosting_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.hosting_page)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.hosting_page)
        self.dns_page = QWidget()
        self.dns_page.setObjectName(u"dns_page")
        self.verticalLayout_7 = QVBoxLayout(self.dns_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.dns_page)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_7.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.dns_page)
        self.email_page = QWidget()
        self.email_page.setObjectName(u"email_page")
        self.verticalLayout_8 = QVBoxLayout(self.email_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.email_page)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_8.addWidget(self.label_4)

        self.stackedWidget.addWidget(self.email_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.verticalLayout_9 = QVBoxLayout(self.settings_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.settings_page)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_9.addWidget(self.label_5)

        self.stackedWidget.addWidget(self.settings_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.left_main)


        self.verticalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.main_frame.raise_()
        self.top_menu_frame.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Internet Centralization Observatory", None))
        self.hamburger_menu.setText("")
        self.system_name.setText(QCoreApplication.translate("MainWindow", u"Internet Centralization Observatory", None))
        self.search_button.setText("")
        self.email_button.setText("")
        self.notification_button.setText("")
        self.user_pic.setText("")
        self.user_name.setText(QCoreApplication.translate("MainWindow", u"Luciano", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:30pt; font-weight:700; color:#ffffff;\">Hosting Page</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:30pt; font-weight:700; color:#ffffff;\">DNS Page</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:30pt; font-weight:700; color:#ffffff;\">Email Page</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:30pt; font-weight:700; color:#ffffff;\">Settings Page</span></p></body></html>", None))
    # retranslateUi

