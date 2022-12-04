# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginULtuKs.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(550, 500)
        Login.setMinimumSize(QSize(550, 500))
        Login.setMaximumSize(QSize(550, 500))
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"	background-color: rgb(34, 43, 69);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLabel#login_label{\n"
"	color: white;\n"
"	font-size: 30px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QLabel#login_msg{\n"
"	color: white;\n"
"}\n"
"\n"
"QLabel#username_label, #password_label{\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	color: #B4B4DB;\n"
"}\n"
"\n"
"QLabel#username_required, #password_required{\n"
"	font-size: 10px;\n"
"	color: #FF3D71;\n"
"}\n"
"\n"
"QFrame#frame_content{\n"
"	background-color: rgb(21, 26, 48);\n"
"	border-radius: 10px;\n"
"	margin-left: 75px;\n"
"	margin-right: 75px;\n"
"	margin-bottom: 40px;\n"
"}\n"
"\n"
"QPushButton#minimize_button{\n"
"	border-radius: 8px;\n"
"	background-color: rgb(255, 255, 116);\n"
"}\n"
"\n"
"QPushButton#close_button{\n"
"	border-radius: 8px;\n"
"	background-color: rgb(252, 101, 95);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: #252547;\n"
"	min-height: 41px;\n"
"	border-radius: 5px;\n"
"	border: 1px solid black;\n"
"	padding-left: 17px;"
                        "\n"
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
"QPushButton#login_button{\n"
"	min-height: 38px;\n"
"	font-weight: bold;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(176, 137, 254, 255), stop:0.98 rgba(160, 110, 254, 255));\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#login_button::hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #D3BEFE, stop:0.98 #B18AFE);\n"
"}\n"
"\n"
"QPushButton#forgot_button{\n"
"	border: none;\n"
"	color: white;\n"
"	text-align: right;\n"
"	padding-right: 5px;\n"
"	font-style: italic;\n"
"	font-size: 10px;\n"
"}\n"
"\n"
"QCheckBox#remember_checkbox{\n"
"	color: white;\n"
"	font-size: 10px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalSpacer = QSpacerItem(451, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.minimize_button = QPushButton(self.frame_2)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setMinimumSize(QSize(16, 16))
        self.minimize_button.setMaximumSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.minimize_button)

        self.close_button = QPushButton(self.frame_2)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMinimumSize(QSize(16, 16))
        self.close_button.setMaximumSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.close_button)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.login_label = QLabel(self.centralwidget)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.login_label)

        self.login_msg = QLabel(self.centralwidget)
        self.login_msg.setObjectName(u"login_msg")
        self.login_msg.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.login_msg)

        self.frame_content = QFrame(self.centralwidget)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_content)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.username_label = QLabel(self.frame_content)
        self.username_label.setObjectName(u"username_label")

        self.verticalLayout.addWidget(self.username_label)

        self.username_edit = QLineEdit(self.frame_content)
        self.username_edit.setObjectName(u"username_edit")
        self.username_edit.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid #2CE69B;\n"
"}")

        self.verticalLayout.addWidget(self.username_edit)

        self.username_required = QLabel(self.frame_content)
        self.username_required.setObjectName(u"username_required")

        self.verticalLayout.addWidget(self.username_required)

        self.password_label = QLabel(self.frame_content)
        self.password_label.setObjectName(u"password_label")

        self.verticalLayout.addWidget(self.password_label)

        self.password_edit = QLineEdit(self.frame_content)
        self.password_edit.setObjectName(u"password_edit")
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.password_edit)

        self.password_required = QLabel(self.frame_content)
        self.password_required.setObjectName(u"password_required")

        self.verticalLayout.addWidget(self.password_required)

        self.frame = QFrame(self.frame_content)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 30))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.remember_checkbox = QCheckBox(self.frame)
        self.remember_checkbox.setObjectName(u"remember_checkbox")

        self.horizontalLayout_2.addWidget(self.remember_checkbox)

        self.forgot_button = QPushButton(self.frame)
        self.forgot_button.setObjectName(u"forgot_button")

        self.horizontalLayout_2.addWidget(self.forgot_button)


        self.verticalLayout.addWidget(self.frame)

        self.login_button = QPushButton(self.frame_content)
        self.login_button.setObjectName(u"login_button")

        self.verticalLayout.addWidget(self.login_button)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_content)

        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.minimize_button.setToolTip(QCoreApplication.translate("Login", u"Minimize Button", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_button.setText("")
#if QT_CONFIG(tooltip)
        self.close_button.setToolTip(QCoreApplication.translate("Login", u"Close Button", None))
#endif // QT_CONFIG(tooltip)
        self.close_button.setText("")
        self.login_label.setText(QCoreApplication.translate("Login", u"Login", None))
        self.login_msg.setText(QCoreApplication.translate("Login", u"Hello! Login with your username!", None))
        self.username_label.setText(QCoreApplication.translate("Login", u"Username", None))
        self.username_edit.setText("")
        self.username_edit.setPlaceholderText(QCoreApplication.translate("Login", u"Username", None))
        self.username_required.setText(QCoreApplication.translate("Login", u"Email is required!", None))
        self.password_label.setText(QCoreApplication.translate("Login", u"Password", None))
        self.password_edit.setPlaceholderText(QCoreApplication.translate("Login", u"Password", None))
        self.password_required.setText(QCoreApplication.translate("Login", u"Password is required!", None))
        self.remember_checkbox.setText(QCoreApplication.translate("Login", u"Remember me", None))
        self.forgot_button.setText(QCoreApplication.translate("Login", u"Forgot Password?", None))
        self.login_button.setText(QCoreApplication.translate("Login", u"Login", None))
    # retranslateUi

