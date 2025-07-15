# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(987, 600)
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(243, 250, 254);")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(226, 180, 183);\n"
"}\n"
"QPushButton{\n"
"	color: #333;\n"
"	text-align: center;\n"
"	height : 50px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #f5fafe;\n"
"	color: #e2b4b7;\n"
"	font-weight: bold;\n"
"}\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setStyleSheet(u"QLabel{\n"
"	border-radius: 50%;\n"
"}")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setPixmap(QPixmap(u":/Icons/logo2.jfif"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.home_icon = QPushButton(self.icon_only_widget)
        self.home_icon.setObjectName(u"home_icon")
        icon = QIcon()
        icon.addFile(u":/Icons/house-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/Icons/house-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.home_icon.setIcon(icon)
        self.home_icon.setCheckable(True)
        self.home_icon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_icon)

        self.customer_icon = QPushButton(self.icon_only_widget)
        self.customer_icon.setObjectName(u"customer_icon")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/users-rectangle-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/Icons/users-rectangle-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.customer_icon.setIcon(icon1)
        self.customer_icon.setCheckable(True)
        self.customer_icon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.customer_icon)

        self.employee_icon = QPushButton(self.icon_only_widget)
        self.employee_icon.setObjectName(u"employee_icon")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/user-tie-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/Icons/user-tie-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.employee_icon.setIcon(icon2)
        self.employee_icon.setCheckable(True)
        self.employee_icon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.employee_icon)

        self.pet_icon = QPushButton(self.icon_only_widget)
        self.pet_icon.setObjectName(u"pet_icon")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/dog-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/Icons/dog-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pet_icon.setIcon(icon3)
        self.pet_icon.setCheckable(True)
        self.pet_icon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pet_icon)

        self.accessories_food_icon = QPushButton(self.icon_only_widget)
        self.accessories_food_icon.setObjectName(u"accessories_food_icon")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/bone-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/Icons/bone-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.accessories_food_icon.setIcon(icon4)
        self.accessories_food_icon.setCheckable(True)
        self.accessories_food_icon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.accessories_food_icon)

        self.service_icon = QPushButton(self.icon_only_widget)
        self.service_icon.setObjectName(u"service_icon")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/edit_note_FILL1_wght700_GRAD0_opsz40.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.service_icon.setIcon(icon5)
        self.service_icon.setIconSize(QSize(20, 20))
        self.service_icon.setCheckable(True)
        self.service_icon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.service_icon)

        self.pay_icon = QPushButton(self.icon_only_widget)
        self.pay_icon.setObjectName(u"pay_icon")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/cash-payment.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pay_icon.setIcon(icon6)
        self.pay_icon.setCheckable(True)
        self.pay_icon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pay_icon)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 22, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton_6 = QPushButton(self.icon_only_widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/right-from-bracket-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon7)
        self.pushButton_6.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_6)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setEnabled(True)
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(226, 180, 183);\n"
"	color: #333;\n"
"}\n"
"QPushButton{\n"
"	color: #333;\n"
"	text-align: left;\n"
"	height : 50px;\n"
"    border: none; \n"
"	padding-left: 20px;\n"
"	border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"	border-top-right-radius: -20px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #f5fafe;\n"
"	color: #e2b4b7;\n"
"	font-weight: bold;\n"
"}\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/Icons/logo2.jfif"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"MV Boli"])
        font.setPointSize(12)
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(16)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(-1, 15, 0, -1)
        self.home_name = QPushButton(self.icon_name_widget)
        self.home_name.setObjectName(u"home_name")
        self.home_name.setIcon(icon)
        self.home_name.setCheckable(True)
        self.home_name.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_name)

        self.customer_name = QPushButton(self.icon_name_widget)
        self.customer_name.setObjectName(u"customer_name")
        self.customer_name.setIcon(icon1)
        self.customer_name.setCheckable(True)
        self.customer_name.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.customer_name)

        self.employee_name = QPushButton(self.icon_name_widget)
        self.employee_name.setObjectName(u"employee_name")
        self.employee_name.setIcon(icon2)
        self.employee_name.setCheckable(True)
        self.employee_name.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.employee_name)

        self.pet_name = QPushButton(self.icon_name_widget)
        self.pet_name.setObjectName(u"pet_name")
        self.pet_name.setIcon(icon3)
        self.pet_name.setCheckable(True)
        self.pet_name.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pet_name)

        self.accessories_food_name = QPushButton(self.icon_name_widget)
        self.accessories_food_name.setObjectName(u"accessories_food_name")
        self.accessories_food_name.setIcon(icon4)
        self.accessories_food_name.setCheckable(True)
        self.accessories_food_name.setAutoExclusive(True)
        self.accessories_food_name.setAutoDefault(False)

        self.verticalLayout_2.addWidget(self.accessories_food_name)

        self.service_name = QPushButton(self.icon_name_widget)
        self.service_name.setObjectName(u"service_name")
        self.service_name.setIcon(icon5)
        self.service_name.setIconSize(QSize(20, 20))
        self.service_name.setCheckable(True)
        self.service_name.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.service_name)

        self.pay_name = QPushButton(self.icon_name_widget)
        self.pay_name.setObjectName(u"pay_name")
        self.pay_name.setIcon(icon6)
        self.pay_name.setCheckable(True)
        self.pay_name.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pay_name)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 22, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButton_10 = QPushButton(self.icon_name_widget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setIcon(icon7)
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.pushButton_10)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.header_widget = QWidget(self.main_menu)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menu = QPushButton(self.header_widget)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"border: none;")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/bars-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu.setIcon(icon8)
        self.menu.setIconSize(QSize(20, 20))
        self.menu.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.menu)

        self.horizontalSpacer_2 = QSpacerItem(206, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #e2b4b7; /* Vi\u1ec1n m\u00e0u xanh */\n"
"    border-radius: 8px; /* Bo g\u00f3c */\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    background-color: #ecf0f1; /* M\u00e0u n\u1ec1n */\n"
"    color: #2c3e50; /* M\u00e0u ch\u1eef */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #e74c3c; /* Vi\u1ec1n \u0111\u1ed5i m\u00e0u khi focus */\n"
"    background-color: #ffffff;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_14 = QPushButton(self.header_widget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"border: none;")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/loupe (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_14.setIcon(icon9)

        self.horizontalLayout.addWidget(self.pushButton_14)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(206, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)
        
        self.cart_icon = QPushButton(self.header_widget)
        self.cart_icon.setObjectName(u"account_icon")
        self.cart_icon.setStyleSheet(u"border: none;")
        icon10 = QIcon()
        icon10.addFile(u":/Icons/shopping-cart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cart_icon.setIcon(icon10)
        self.cart_icon.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.cart_icon)

        self.account_icon = QPushButton(self.header_widget)
        self.account_icon.setObjectName(u"account_icon")
        self.account_icon.setStyleSheet(u"border: none;")
        icon10 = QIcon()
        icon10.addFile(u":/Icons/user-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.account_icon.setIcon(icon10)
        self.account_icon.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.account_icon)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(254, 248, 236);")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_14 = QVBoxLayout(self.home_page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.headerFrame = QFrame(self.home_page)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setMinimumSize(QSize(0, 100))
        self.headerFrame.setStyleSheet(u"background-color: #FCD9D9;\n"
"border-radius: 20px;")
        self.headerFrame.setFrameShape(QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.headerFrame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.storeNameLabel_2 = QLabel(self.headerFrame)
        self.storeNameLabel_2.setObjectName(u"storeNameLabel_2")
        self.storeNameLabel_2.setStyleSheet(u"font-size: 18px;\n"
"font-weight: bold;")

        self.verticalLayout_8.addWidget(self.storeNameLabel_2)

        self.sloganLabel1_2 = QLabel(self.headerFrame)
        self.sloganLabel1_2.setObjectName(u"sloganLabel1_2")
        font1 = QFont()
        font1.setPointSize(9)
        self.sloganLabel1_2.setFont(font1)

        self.verticalLayout_8.addWidget(self.sloganLabel1_2)

        self.sloganLabel2_2 = QLabel(self.headerFrame)
        self.sloganLabel2_2.setObjectName(u"sloganLabel2_2")
        self.sloganLabel2_2.setFont(font1)

        self.verticalLayout_8.addWidget(self.sloganLabel2_2)

        self.sloganLabel3_2 = QLabel(self.headerFrame)
        self.sloganLabel3_2.setObjectName(u"sloganLabel3_2")
        self.sloganLabel3_2.setFont(font1)

        self.verticalLayout_8.addWidget(self.sloganLabel3_2)

        self.sloganLabel4_2 = QLabel(self.headerFrame)
        self.sloganLabel4_2.setObjectName(u"sloganLabel4_2")
        self.sloganLabel4_2.setFont(font1)

        self.verticalLayout_8.addWidget(self.sloganLabel4_2)


        self.verticalLayout_14.addWidget(self.headerFrame)

        self.dashboardFrame = QFrame(self.home_page)
        self.dashboardFrame.setObjectName(u"dashboardFrame")
        self.dashboardFrame.setFrameShape(QFrame.StyledPanel)
        self.dashboardFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.dashboardFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.revenueFrame = QFrame(self.dashboardFrame)
        self.revenueFrame.setObjectName(u"revenueFrame")
        self.revenueFrame.setStyleSheet(u"background-color: #a0c9c3;\n"
"border-radius: 15px;")
        self.revenueFrame.setFrameShape(QFrame.StyledPanel)
        self.revenueFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.revenueFrame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.revenueLabel_2 = QLabel(self.revenueFrame)
        self.revenueLabel_2.setObjectName(u"revenueLabel_2")
        self.revenueLabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.revenueLabel_2)

        self.revenueProgress_2 = QProgressBar(self.revenueFrame)
        self.revenueProgress_2.setObjectName(u"revenueProgress_2")
        self.revenueProgress_2.setStyleSheet(u"QProgressBar {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"    background-color: #efffff;\n"
"	color: #fff;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #657d81;\n"
"    border-radius: 10px;\n"
"}")
        self.revenueProgress_2.setValue(65)

        self.verticalLayout_9.addWidget(self.revenueProgress_2)

        self.revenueAmount_2 = QLabel(self.revenueFrame)
        self.revenueAmount_2.setObjectName(u"revenueAmount_2")
        self.revenueAmount_2.setStyleSheet(u"font-size: 20px;\n"
"font-weight: bold;")
        self.revenueAmount_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.revenueAmount_2)


        self.horizontalLayout_5.addWidget(self.revenueFrame)


        self.verticalLayout_14.addWidget(self.dashboardFrame)

        self.dashboardFrame2 = QFrame(self.home_page)
        self.dashboardFrame2.setObjectName(u"dashboardFrame2")
        self.dashboardFrame2.setFrameShape(QFrame.StyledPanel)
        self.dashboardFrame2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.dashboardFrame2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.birdFrame = QFrame(self.dashboardFrame2)
        self.birdFrame.setObjectName(u"birdFrame")
        self.birdFrame.setStyleSheet(u"background-color: #e2b4b7;\n"
"border-radius: 15px;")
        self.birdFrame.setFrameShape(QFrame.StyledPanel)
        self.birdFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.birdFrame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.birdLabel = QLabel(self.birdFrame)
        self.birdLabel.setObjectName(u"birdLabel")
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.birdLabel.setFont(font2)
        self.birdLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.birdLabel)

        self.birdIcon = QLabel(self.birdFrame)
        self.birdIcon.setObjectName(u"birdIcon")
        self.birdIcon.setPixmap(QPixmap(u"icons/bird.png"))
        self.birdIcon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.birdIcon)

        self.birdCount = QLabel(self.birdFrame)
        self.birdCount.setObjectName(u"birdCount")
        self.birdCount.setStyleSheet(u"font-size: 24px;\n"
"font-weight: bold;")
        self.birdCount.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.birdCount)


        self.horizontalLayout_6.addWidget(self.birdFrame)

        self.dogFrame = QFrame(self.dashboardFrame2)
        self.dogFrame.setObjectName(u"dogFrame")
        self.dogFrame.setStyleSheet(u"background-color: #a0c9c3;\n"
"border-radius: 15px;")
        self.dogFrame.setFrameShape(QFrame.StyledPanel)
        self.dogFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.dogFrame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.dogLabel = QLabel(self.dogFrame)
        self.dogLabel.setObjectName(u"dogLabel")
        self.dogLabel.setFont(font2)
        self.dogLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.dogLabel)

        self.dogIcon = QLabel(self.dogFrame)
        self.dogIcon.setObjectName(u"dogIcon")
        self.dogIcon.setPixmap(QPixmap(u"icons/dog.png"))
        self.dogIcon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.dogIcon)

        self.dogCount = QLabel(self.dogFrame)
        self.dogCount.setObjectName(u"dogCount")
        self.dogCount.setStyleSheet(u"font-size: 24px;\n"
"font-weight: bold;")
        self.dogCount.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.dogCount)


        self.horizontalLayout_6.addWidget(self.dogFrame)

        self.catFrame = QFrame(self.dashboardFrame2)
        self.catFrame.setObjectName(u"catFrame")
        self.catFrame.setStyleSheet(u"background-color: #f3c2c5;\n"
"border-radius: 15px;")
        self.catFrame.setFrameShape(QFrame.StyledPanel)
        self.catFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.catFrame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.catLabel = QLabel(self.catFrame)
        self.catLabel.setObjectName(u"catLabel")
        font3 = QFont()
        font3.setPointSize(10)
        self.catLabel.setFont(font3)
        self.catLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.catLabel)

        self.catIcon = QLabel(self.catFrame)
        self.catIcon.setObjectName(u"catIcon")
        self.catIcon.setPixmap(QPixmap(u"icons/cat.png"))
        self.catIcon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.catIcon)

        self.catCount = QLabel(self.catFrame)
        self.catCount.setObjectName(u"catCount")
        self.catCount.setStyleSheet(u"font-size: 24px;\n"
"font-weight: bold;")
        self.catCount.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.catCount)


        self.horizontalLayout_6.addWidget(self.catFrame)

        self.fishFrame = QFrame(self.dashboardFrame2)
        self.fishFrame.setObjectName(u"fishFrame")
        self.fishFrame.setStyleSheet(u"background-color: #97b8ba;\n"
"border-radius: 15px;")
        self.fishFrame.setFrameShape(QFrame.StyledPanel)
        self.fishFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.fishFrame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.fishLabel = QLabel(self.fishFrame)
        self.fishLabel.setObjectName(u"fishLabel")
        self.fishLabel.setFont(font3)
        self.fishLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.fishLabel)

        self.fishIcon = QLabel(self.fishFrame)
        self.fishIcon.setObjectName(u"fishIcon")
        self.fishIcon.setPixmap(QPixmap(u"icons/fish.png"))
        self.fishIcon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.fishIcon)

        self.fishCount = QLabel(self.fishFrame)
        self.fishCount.setObjectName(u"fishCount")
        self.fishCount.setStyleSheet(u"font-size: 24px;\n"
"font-weight: bold;")
        self.fishCount.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.fishCount)


        self.horizontalLayout_6.addWidget(self.fishFrame)


        self.verticalLayout_14.addWidget(self.dashboardFrame2)

        self.stackedWidget.addWidget(self.home_page)
        self.service_page = QWidget()
        self.service_page.setObjectName(u"service_page")
        self.stackedWidget.addWidget(self.service_page)
        self.cart_page = QWidget()
        self.cart_page.setObjectName(u"cart_page")
        self.stackedWidget.addWidget(self.cart_page)
        self.pay_page = QWidget()
        self.pay_page.setObjectName(u"pay_page")
        self.stackedWidget.addWidget(self.pay_page)
        self.order_page = QWidget()
        self.order_page.setObjectName(u"order_page")
        self.stackedWidget.addWidget(self.order_page)
        self.customer_page = QWidget()
        self.customer_page.setObjectName(u"customer_page")
        self.label_5 = QLabel(self.customer_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 160, 181, 51))
        font4 = QFont()
        font4.setPointSize(20)
        self.label_5.setFont(font4)
        self.stackedWidget.addWidget(self.customer_page)
        self.employee_page = QWidget()
        self.employee_page.setObjectName(u"employee_page")
        self.label_6 = QLabel(self.employee_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(170, 160, 161, 51))
        self.label_6.setFont(font4)
        self.stackedWidget.addWidget(self.employee_page)
        self.pet_page = QWidget()
        self.pet_page.setObjectName(u"pet_page")
        self.label_7 = QLabel(self.pet_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(160, 180, 151, 51))
        self.label_7.setFont(font4)
        self.stackedWidget.addWidget(self.pet_page)
        self.account_page = QWidget()
        self.account_page.setObjectName(u"account_page")
        self.label_4 = QLabel(self.account_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 90, 141, 101))
        self.label_4.setFont(font4)
        self.stackedWidget.addWidget(self.account_page)
        self.accessories_food_page = QWidget()
        self.accessories_food_page.setObjectName(u"accessories_food_page")
        self.label_8 = QLabel(self.accessories_food_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(120, 160, 271, 71))
        self.label_8.setFont(font4)
        self.stackedWidget.addWidget(self.accessories_food_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 987, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.icon_only_widget.setHidden)
        self.menu.toggled.connect(self.icon_name_widget.setVisible)
        self.accessories_food_icon.toggled.connect(self.accessories_food_name.setChecked)
        self.pet_icon.toggled.connect(self.pet_name.setChecked)
        self.employee_icon.toggled.connect(self.employee_name.setChecked)
        self.customer_icon.toggled.connect(self.customer_name.setChecked)
        self.home_icon.toggled.connect(self.home_name.setChecked)
        self.home_name.toggled.connect(self.home_icon.setChecked)
        self.customer_name.toggled.connect(self.customer_icon.setChecked)
        self.employee_name.toggled.connect(self.employee_icon.setChecked)
        self.pet_name.toggled.connect(self.pet_icon.setChecked)
        self.accessories_food_name.toggled.connect(self.accessories_food_icon.setChecked)
        self.pushButton_6.toggled.connect(MainWindow.close)
        self.pushButton_10.toggled.connect(MainWindow.close)
        self.service_icon.toggled.connect(self.service_name.setChecked)
        self.service_name.toggled.connect(self.service_icon.setChecked)
        self.pay_icon.toggled.connect(self.pay_name.setChecked)
        self.pay_name.toggled.connect(self.pay_icon.setChecked)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.home_icon.setText("")
        self.customer_icon.setText("")
        self.employee_icon.setText("")
        self.pet_icon.setText("")
        self.accessories_food_icon.setText("")
        self.service_icon.setText("")
        self.pay_icon.setText("")
        self.pushButton_6.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pet Shop", None))
        self.home_name.setText(QCoreApplication.translate("MainWindow", u"Trang ch\u1ee7", None))
        self.customer_name.setText(QCoreApplication.translate("MainWindow", u"Kh\u00e1ch h\u00e0ng", None))
        self.employee_name.setText(QCoreApplication.translate("MainWindow", u"Nh\u00e2n vi\u00ean", None))
        self.pet_name.setText(QCoreApplication.translate("MainWindow", u"Th\u00fa c\u01b0ng", None))
        self.accessories_food_name.setText(QCoreApplication.translate("MainWindow", u"Ph\u1ee5 ki\u1ec7n - Th\u1ee9c \u0103n      ", None))
        self.service_name.setText(QCoreApplication.translate("MainWindow", u"D\u1ecbch v\u1ee5", None))
        self.pay_name.setText(QCoreApplication.translate("MainWindow", u"Thanh to\u00e1n", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u0110\u0103ng xu\u1ea5t", None))
        self.menu.setText("")
        self.pushButton_14.setText("")
        self.account_icon.setText("")
        self.storeNameLabel_2.setText(QCoreApplication.translate("MainWindow", u"String Pet Store", None))
        self.sloganLabel1_2.setText(QCoreApplication.translate("MainWindow", u"Th\u1ecbt ch\u00f3 th\u00ec ph\u1ea3i c\u00f3 ri\u1ec1ng ", None))
        self.sloganLabel2_2.setText(QCoreApplication.translate("MainWindow", u"Th\u1ecbt l\u1ee3n th\u00ec ph\u1ea3i c\u00f3 ri\u00eang m\u00f3n h\u00e0nh", None))
        self.sloganLabel3_2.setText(QCoreApplication.translate("MainWindow", u"Th\u1ecbt g\u00e0 c\u1ea7n ph\u1ea3i l\u00e1 chanh", None))
        self.sloganLabel4_2.setText(QCoreApplication.translate("MainWindow", u"T\u00eda t\u00f4 c\u00e0 chu\u1ed1i m\u1edbi th\u00e0nh ba ba.", None))
        self.revenueLabel_2.setText(QCoreApplication.translate("MainWindow", u"Doanh thu", None))
        self.revenueAmount_2.setText(QCoreApplication.translate("MainWindow", u"1905000", None))
        self.birdLabel.setText(QCoreApplication.translate("MainWindow", u"Chim:", None))
        self.birdIcon.setText("")
        self.birdCount.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.dogLabel.setText(QCoreApplication.translate("MainWindow", u"Ch\u00f3:", None))
        self.dogIcon.setText("")
        self.dogCount.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.catLabel.setText(QCoreApplication.translate("MainWindow", u"M\u00e8o:", None))
        self.catIcon.setText("")
        self.catCount.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.fishLabel.setText(QCoreApplication.translate("MainWindow", u"C\u00e1:", None))
        self.fishIcon.setText("")
        self.fishCount.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Khach hang ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Nhan vien ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Thu cung", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"account", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Phu kien - thuc an ", None))
    # retranslateUi

