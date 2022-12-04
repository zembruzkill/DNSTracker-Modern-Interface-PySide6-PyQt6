# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainmdynzQ.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1363, 659)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
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
"QPushButton#is_collecting{\n"
"	background-color: rgb(239, 135, 51);\n"
"	border-radius: 4px;\n"
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
"QFrame#worker_frame{\n"
"	background-color: rgb(34, 43, 6"
                        "9);\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#settings_page\n"
"\n"
"QFrame#frame_name{\n"
"	background-color: rgb(34, 43, 69);\n"
"	border-bottom: 2px solid rgb(21, 26, 48);\n"
"}\n"
"\n"
"QLabel#card_name{\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: #252547;\n"
"	min-height: 41px;\n"
"	border-radius: 5px;\n"
"	border: 1px solid black;\n"
"	padding-left: 17px;\n"
"	color: white;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"	border: 1px solid #A16EFF;\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"	background-color: #1B1B38;\n"
"	border: 1px solid #A16EFF;\n"
"}\n"
"\n"
"QPushButton#save_button{\n"
"	font-weight: bold;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(176, 137, 254, 255), stop:0.98 rgba(160, 110, 254, 255));\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#save_button::hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #D3BEFE, stop:0.98 #B18AFE);\n"
"}\n"
""
                        "\n"
"QLabel#worker_name_required{\n"
"	font-size: 10px;\n"
"	color: #FF3D71;\n"
"}\n"
"\n"
"\n"
"\n"
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

        self.line_2 = QFrame(self.top_menu_frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMaximumSize(QSize(1, 22))
        self.line_2.setStyleSheet(u"background-color: #1B1B38;\n"
"max-height: 20px;")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

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
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.is_collecting = QPushButton(self.frame_7)
        self.is_collecting.setObjectName(u"is_collecting")
        self.is_collecting.setMinimumSize(QSize(8, 8))
        self.is_collecting.setMaximumSize(QSize(8, 8))
        self.is_collecting.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.is_collecting)


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
        self.horizontalLayout_4 = QHBoxLayout(self.settings_page)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_3 = QFrame(self.settings_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.worker_frame = QFrame(self.frame_3)
        self.worker_frame.setObjectName(u"worker_frame")
        self.worker_frame.setMinimumSize(QSize(0, 400))
        self.worker_frame.setMaximumSize(QSize(500, 16777215))
        self.worker_frame.setFrameShape(QFrame.NoFrame)
        self.worker_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.worker_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_name = QFrame(self.worker_frame)
        self.frame_name.setObjectName(u"frame_name")
        self.frame_name.setMaximumSize(QSize(16777215, 40))
        self.frame_name.setFrameShape(QFrame.NoFrame)
        self.frame_name.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_name)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(25, -1, 25, -1)
        self.card_name = QLabel(self.frame_name)
        self.card_name.setObjectName(u"card_name")

        self.horizontalLayout_3.addWidget(self.card_name)


        self.verticalLayout_2.addWidget(self.frame_name)

        self.frame_form = QFrame(self.worker_frame)
        self.frame_form.setObjectName(u"frame_form")
        self.frame_form.setFrameShape(QFrame.NoFrame)
        self.frame_form.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.worker_name = QLineEdit(self.frame_form)
        self.worker_name.setObjectName(u"worker_name")

        self.verticalLayout_3.addWidget(self.worker_name)

        self.public_ip_address = QLineEdit(self.frame_form)
        self.public_ip_address.setObjectName(u"public_ip_address")
        self.public_ip_address.setEnabled(False)

        self.verticalLayout_3.addWidget(self.public_ip_address)

        self.save_button = QPushButton(self.frame_form)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setMinimumSize(QSize(100, 40))
        self.save_button.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_3.addWidget(self.save_button, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_form, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.worker_frame)

        self.verticalSpacer_2 = QSpacerItem(20, 92, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.settings_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.settings_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.left_main)


        self.verticalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.main_frame.raise_()
        self.top_menu_frame.raise_()

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Internet Centralization Observatory", None))
        self.hamburger_menu.setText("")
        self.system_name.setText(QCoreApplication.translate("MainWindow", u"Internet Centralization Toolkit", None))
#if QT_CONFIG(tooltip)
        self.is_collecting.setToolTip(QCoreApplication.translate("MainWindow", u"Collection in progress", None))
#endif // QT_CONFIG(tooltip)
        self.is_collecting.setText("")
        self.user_pic.setText("")
        self.user_name.setText(QCoreApplication.translate("MainWindow", u"Luciano", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:30pt; font-weight:700; color:#ffffff;\">Hosting Page</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:30pt; font-weight:700; color:#ffffff;\">DNS Page</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:30pt; font-weight:700; color:#ffffff;\">Email Page</span></p></body></html>", None))
        self.card_name.setText(QCoreApplication.translate("MainWindow", u"Worker Configuration", None))
        self.worker_name.setText("")
        self.worker_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Worker Name", None))
        self.public_ip_address.setText("")
        self.public_ip_address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Public IP Address", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

