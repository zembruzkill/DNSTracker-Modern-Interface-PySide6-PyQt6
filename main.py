# PySide6 Imports
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QWidget, QFrame, QSpacerItem, QSizePolicy, QScrollArea, QMessageBox
from PySide6.QtGui import QColor, QPixmap, QIcon, QScreen
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QSize, QTimer, QUrl, QProcess
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWebEngineWidgets import QWebEngineView

# GUI Imports
from gui.ui_login import Ui_Login
from gui.ui_main import Ui_MainWindow
from gui.ui_card_component import Ui_CardComponent
from gui.ui_ui_chart_card import Ui_ChartCard
from gui.ui_custom_scroll_area import Ui_CustomScrollArea

# General imports
import time
import os
from settings import save_login, load_login,  BASE_URL, JSON_HEADERS
from apis.service import Service
# import requests
# import json
# import glob

# Scripts imports
# from scripts.crawler import CrawlerThread
from scripts.geolocation import GeoLocation

base_dir = os.path.dirname(os.path.abspath(__file__))

class CustomButton(QPushButton):
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.setCheckable(True)
        
        self.setStyleSheet("""
                        QPushButton{
                                min-height: 55px;
                                border: none;
                                border-bottom: 1px solid rgb(31, 31, 64);
                                text-align: left;
                                padding-left: 18px;
                                font-weight: 600;}
                        QPushButton::checked{
                               background-color: #151A30;}
                        """)
        
        self.setText(kwargs.get("text"))
        self.setIcon(QIcon(kwargs.get("icon")))
        self.setIconSize(QSize(20, 20))
        
class ChartCardComponent(QWidget, Ui_ChartCard):
    def __init__(self, **kwargs):
        super().__init__()
        self.setupUi(self)
        
        if 'title' in kwargs:
            self.card_title.setText(kwargs.get("title"))
        

class CardComponent(QWidget, Ui_CardComponent):
    def __init__(self, **kwargs):
        super().__init__()
        self.setupUi(self)
        
        self.updated_stylesheet_circular = ""
        
        self.stylesheet_base_border = """QFrame#frame{border-bottom: 6px solid {COLOR};}"""
        self.stylesheet_base_circular = """QFrame#circular_prog{\nbackground-color: qconicalgradient(cx:0.5, cy:0.5, angle:271, stop:{STOP_1} rgba(57, 127, 236, 0), stop:{STOP_2} {COLOR});\n	border-radius: 30px;\n}"""
            
        if 'title' in kwargs:
            self.card_title.setText(kwargs.get("title"))
            
        if 'value' in kwargs:
            self.card_value.setText(kwargs.get("value"))
            
        if 'color' in kwargs and 'percentage' in kwargs:
            self.updated_stylesheet_border = self.stylesheet_base_border.replace("{COLOR}", kwargs.get("color"))
            self.frame.setStyleSheet(self.updated_stylesheet_border)
            
            self.card_percentage.setText(kwargs.get("percentage"))
            self.stop_1 = (1 - ((int(kwargs.get("percentage")) / 100)) - 0.01)
            self.stop_2 = (1 - ((int(kwargs.get("percentage")) / 100)))
            self.updated_stylesheet_circular = self.stylesheet_base_circular.replace("{STOP_1}", str(self.stop_1)).replace("{STOP_2}", str(self.stop_2)).replace("{COLOR}", kwargs.get("color"))
            self.circular_prog.setStyleSheet(self.updated_stylesheet_circular)

class DashboardScrollArea(QWidget, Ui_CustomScrollArea):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.verticalLayout = QVBoxLayout()
        
        self.frame_cards = QFrame()
        self.frame_middle = QFrame()
        self.frame_bottom = QFrame()
        
        self.verticalLayout.addWidget(self.frame_cards)
        self.verticalLayout.addWidget(self.frame_middle)
        self.verticalLayout.addWidget(self.frame_bottom)
        
        self.scrollArea.setLayout(self.verticalLayout)
        self.scrollArea.layout().setContentsMargins(0, 0, 0, 0)
        self.scrollArea.layout().setSpacing(30)
        
        #Create cards
        self.cards_layout = QHBoxLayout()
        self.card_domains_analysed = CardComponent(color="#3399FF", title="Domains Analysed", value="200.400.458", percentage="95")
        self.card_nameservers_analysed = CardComponent(color="#FFB800", title="Nameservers Analysed", value="2.400.458", percentage="85")
        self.card_emails_analysed = CardComponent(color="#FF4D4F", title="Emails Analysed", value="1.400.458", percentage="65")
        self.card_vantage_poins = CardComponent(color="#FF0084", title="Vantage Points", value="29", percentage="99")
        
        
        self.cards_layout.addWidget(self.card_domains_analysed)
        self.cards_layout.addWidget(self.card_nameservers_analysed)
        self.cards_layout.addWidget(self.card_emails_analysed)
        self.cards_layout.addWidget(self.card_vantage_poins)
        
        self.frame_cards.setLayout(self.cards_layout)
        self.frame_cards.layout().setContentsMargins(0, 0, 0, 0)
        self.frame_cards.layout().setSpacing(30)
        
        self.middle_frame_layout = QHBoxLayout()
        self.bottom_frame_layout = QHBoxLayout()
        
        self.chart_1 = QWebEngineView()
        self.chart_1.setStyleSheet("border-radius: 5px;")
        self.chart_1.setUrl(QUrl().fromLocalFile(os.path.join(base_dir, 'charts/chart-stack.html')))
        
        self.chart_2 = QWebEngineView()
        self.chart_2.setStyleSheet("border-radius: 5px;")
        self.chart_2.setUrl(QUrl().fromLocalFile(os.path.join(base_dir, 'charts/graph-chart.html')))
        
        self.chart_3 = QWebEngineView()
        self.chart_3.setStyleSheet("border-radius: 5px;")
        self.chart_3.setUrl(QUrl().fromLocalFile(os.path.join(base_dir, 'charts/treemap.html')))
        
        self.chart_4 = QWebEngineView()
        self.chart_4.setStyleSheet("border-radius: 5px;")
        self.chart_4.setUrl(QUrl().fromLocalFile(os.path.join(base_dir, 'charts/geomap-animated.html')))
        
        self.middle_frame_layout.addWidget(self.chart_1)
        self.middle_frame_layout.addWidget(self.chart_2)
        self.frame_middle.setLayout(self.middle_frame_layout)
        self.frame_middle.layout().setContentsMargins(0, 0, 0, 0)
        self.frame_middle.layout().setSpacing(30)
        
        self.bottom_frame_layout.addWidget(self.chart_3)
        self.bottom_frame_layout.addWidget(self.chart_4)
        self.bottom_frame_layout.layout().setContentsMargins(0, 0, 0, 0)
        self.bottom_frame_layout.layout().setSpacing(30)
        self.frame_bottom.setLayout(self.bottom_frame_layout)
        
class Login(QMainWindow, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        login_saved = load_login()
        
        if login_saved.get('remember'):
            self.username_edit.setText(login_saved.get("username"))
            self.password_edit.setText(login_saved.get("password"))
            self.remember_checkbox.setChecked(True)
            
        
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        self.move(center.x() - self.width() / 2, center.y() - self.height() / 2)
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.close_button.clicked.connect(self.close)
        self.minimize_button.clicked.connect(self.showMinimized)
        
        self.username_edit.returnPressed.connect(self.login)
        self.password_edit.returnPressed.connect(self.login)
        
        self.login_button.clicked.connect(self.login)
        
    def login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()
        
        if self.remember_checkbox.isChecked():
            save_login({"username": username, "password": password, "remember": True})
        else:
            save_login({"username": "", "password": "", "remember": False})
        
        if username == "" or password == "":
            QMessageBox.warning(self, "Error", "Please fill in all the fields")
        else:
            self.service = Service()
            self.logged = self.service.login(username=username, password=password)
            print(self.logged.json())
            
            if self.logged.status_code == 200:
                self.main = MainWindow()
                self.main.show()
                self.close()
            
            
        
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()
        
    def mouseMoveEvent(self, event):
     self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos )
     self.dragPos = event.globalPosition().toPoint()
     event.accept()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.public_ipaddress.setText(geolocation_info['ip'])
        
        self.save_button.clicked.connect(self.save_settings)
        
        self.is_running = False
        self.changing_color = True
        self.process = QProcess()
        self.collection_in_progress()
          
        self.timer_collection = QTimer()
        self.timer_collection.timeout.connect(self.collection_in_progress)
        self.timer_collection.start(100000)
        

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        
        self.timer.start(300000)
        
        # self.showMaximized()
        
        # Add a shadow on frame color black
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(80)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(10)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        
        self.top_menu_frame.setGraphicsEffect(self.shadow)
        
        self.hamburger_menu.clicked.connect(self.toggle_menu)
        
        #Add custom buttons on menu
        self.buttons_layout = QVBoxLayout()
        
        self.spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        self.dashboard_page_button = CustomButton(
            icon="resources/icons/home-outline.svg",
            text="Home Dashboard"
        )
        
        self.hosting_page_button = CustomButton(
            icon="resources/icons/globe-outline.svg",
            text="Hosting Measurements"
        )
        
        self.dns_page_button = CustomButton(
            icon="resources/icons/globe-2-outline.svg",
            text="DNS Measurements"
        )
        
        self.email_page_button = CustomButton(
            icon="resources/icons/email-outline.svg",
            text="Email Measurements"
        )
        
        self.settings_page_button = CustomButton(
            icon="resources/icons/settings-2-outline.svg",
            text="Settings"
        )
        
        
        self.buttons_layout.addWidget(self.dashboard_page_button)
        self.buttons_layout.addWidget(self.hosting_page_button)
        self.buttons_layout.addWidget(self.dns_page_button)
        self.buttons_layout.addWidget(self.email_page_button)
        self.buttons_layout.addWidget(self.settings_page_button)
         
        
        self.buttons_layout.addItem(self.spacer)
        
        self.right_menu.setLayout(self.buttons_layout)
        self.right_menu.layout().setContentsMargins(0, 0, 0, 0)
        self.right_menu.layout().setSpacing(0)
        
        self.select_dashboard_page()
        
        self.dashboard_page_button.clicked.connect(self.select_dashboard_page)
        self.hosting_page_button.clicked.connect(self.select_hosting_page)
        self.dns_page_button.clicked.connect(self.select_dns_page)
        self.email_page_button.clicked.connect(self.select_email_page)
        self.settings_page_button.clicked.connect(self.select_settings_page)
        
        self.dashboard_page_layout = QHBoxLayout()
        
        self.dashboard_page_custom_scroll = DashboardScrollArea()
        self.dashboard_page_layout.addWidget(self.dashboard_page_custom_scroll)
        
        self.dashboard_page.setLayout(self.dashboard_page_layout)
    
    def closeEvent(self, event):
        self.process.kill()
        self.close()
        
        
    def update_data(self):
        geolocation = GeoLocation()
        geolocation_info = geolocation.get_location()
        
        service = Service()
        service.alive(worker_id=1, ip_address=geolocation_info['ip'], city=geolocation_info['city'], region=geolocation_info['region'], country=geolocation_info['country'])
        
        
    def process_finished(self):
        try:
            self.process.kill()
        except Exception as e:
            print(e)
        self.is_running = False
        
        self.collection_in_progress()
        
        
    def collection_in_progress(self):
        if not self.is_running:
            try:
                self.service = Service()
                self.service.alive(worker_id=1, ip_address=geolocation_info['ip'], city=geolocation_info['city'], region=geolocation_info['region'], country=geolocation_info['country'])
                self.version = self.service.version(worker_id=1)
                self.handle_version = self.service.handle_version(worker_id=1, version_id=self.version['data']['id'])
            except Exception as e:
                print(e)
                
            if self.version and self.handle_version:
                self.is_running = True
                self.process = QProcess()
                print('Running on range of domains: ' + 'from ' + str(self.handle_version['data']['rank_start'])+ ' to ' + str(self.handle_version['data']['rank_end']))
                self.process.start("python3", ["scripts/run.py",
                                                    str(self.handle_version['data']['id']),
                                                    str(self.version['data']['id']),
                                                    str(self.handle_version['data']['rank_start']),
                                                    str(self.handle_version['data']['rank_end'])])
                self.process.finished.connect(self.process_finished)
        else:
            print("Already running")
                
        
        if self.changing_color:
            self.is_collecting.setStyleSheet("""QPushButton#is_collecting{\n	background-color: rgb(255, 255, 51);\n	border-radius: 4px;\n}
                                            """)
            self.changing_color = False
        else:
            self.is_collecting.setStyleSheet("""QPushButton#is_collecting{\n	background-color: rgb(205, 78, 40);\n	border-radius: 4px;\n}
                                            """)
            self.changing_color = True
        
    def select_dashboard_page(self):
        self.stackedWidget.setCurrentIndex(0)
        self.dashboard_page_button.setChecked(True)
        self.hosting_page_button.setChecked(False)
        self.dns_page_button.setChecked(False)
        self.email_page_button.setChecked(False)
        self.settings_page_button.setChecked(False)
    
    def select_hosting_page(self):
        self.stackedWidget.setCurrentIndex(1)
        self.dashboard_page_button.setChecked(False)
        self.hosting_page_button.setChecked(True)
        self.dns_page_button.setChecked(False)
        self.email_page_button.setChecked(False)
        self.settings_page_button.setChecked(False)
        
    def select_dns_page(self):
        self.stackedWidget.setCurrentIndex(2)
        self.dashboard_page_button.setChecked(False)
        self.hosting_page_button.setChecked(False)
        self.dns_page_button.setChecked(True)
        self.email_page_button.setChecked(False)
        self.settings_page_button.setChecked(False)
        
    def select_email_page(self):
        self.stackedWidget.setCurrentIndex(3)
        self.dashboard_page_button.setChecked(False)
        self.hosting_page_button.setChecked(False)
        self.dns_page_button.setChecked(False)
        self.email_page_button.setChecked(True)
        self.settings_page_button.setChecked(False)
        
    def select_settings_page(self):
        self.stackedWidget.setCurrentIndex(4)
        self.dashboard_page_button.setChecked(False)
        self.hosting_page_button.setChecked(False)
        self.dns_page_button.setChecked(False)
        self.email_page_button.setChecked(False)
        self.settings_page_button.setChecked(True)
        
    def toggle_menu(self):
        if self.right_menu.width() == 251:
            new_width = 56
            self.dashboard_page_button.setText("")
            self.hosting_page_button.setText("")
            self.dns_page_button.setText("")
            self.email_page_button.setText("")
            self.settings_page_button.setText("")
            self.animation = QPropertyAnimation(self.right_menu, b"minimumWidth")
            self.animation.setDuration(500)
            self.animation.setEndValue(new_width)
            self.animation.setEasingCurve(QEasingCurve.OutBounce)
            self.animation.start()
        else:
            new_width = 251
            self.animation = QPropertyAnimation(self.right_menu, b"minimumWidth")
            self.animation.setDuration(500)
            self.animation.setEndValue(new_width)
            self.animation.setEasingCurve(QEasingCurve.OutBounce)
            self.animation.start()
            time.sleep(0.2)
            self.dashboard_page_button.setText("Home Dashboard")
            self.hosting_page_button.setText("Hosting Measurement")
            self.dns_page_button.setText("DNS Measurement")
            self.email_page_button.setText("Email Measurement")
            self.settings_page_button.setText("Settings")
            
    def save_settings(self):
        pass
            
        
if __name__ == "__main__":
    app = QApplication([])
    
    geolocation = GeoLocation()
    geolocation_info = geolocation.get_location()

    window = Login()
    window.show()

    app.exec()  
