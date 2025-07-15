# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'order.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpinBox,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1232, 651)
        MainWindow.setStyleSheet(u"\n"
"    QMainWindow {\n"
"        background-color: #fef8ec;\n"
"    }\n"
"    QPushButton {\n"
"        background-color: #a0c9c3;\n"
"        color: #333;\n"
"        border: none;\n"
"        padding: 8px 16px;\n"
"        border-radius: 4px;\n"
"        font-size: 14px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #657d81;\n"
"		color: white;\n"
"    }\n"
"    QTableWidget {\n"
"        background-color: white;\n"
"        border: 1px solid #ddd;\n"
"        border-radius: 4px;\n"
"    }\n"
"    QTableWidget::item {\n"
"        padding: 4px;\n"
"    }\n"
"    QLabel {\n"
"        font-size: 14px;\n"
"        color: #333;\n"
"    }\n"
"    QDateEdit, QSpinBox {\n"
"        padding: 4px;\n"
"        border: 1px solid #ddd;\n"
"        border-radius: 4px;\n"
"    }\n"
"   ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_order_list = QWidget()
        self.page_order_list.setObjectName(u"page_order_list")
        self.verticalLayout_2 = QVBoxLayout(self.page_order_list)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_filters = QGroupBox(self.page_order_list)
        self.groupBox_filters.setObjectName(u"groupBox_filters")
        self.gridLayout = QGridLayout(self.groupBox_filters)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_date_from = QLabel(self.groupBox_filters)
        self.label_date_from.setObjectName(u"label_date_from")

        self.gridLayout.addWidget(self.label_date_from, 0, 0, 1, 1)

        self.dateEdit_from = QDateEdit(self.groupBox_filters)
        self.dateEdit_from.setObjectName(u"dateEdit_from")

        self.gridLayout.addWidget(self.dateEdit_from, 0, 1, 1, 1)

        self.label_date_to = QLabel(self.groupBox_filters)
        self.label_date_to.setObjectName(u"label_date_to")

        self.gridLayout.addWidget(self.label_date_to, 0, 2, 1, 1)

        self.dateEdit_to = QDateEdit(self.groupBox_filters)
        self.dateEdit_to.setObjectName(u"dateEdit_to")

        self.gridLayout.addWidget(self.dateEdit_to, 0, 3, 1, 1)

        self.label_price_from = QLabel(self.groupBox_filters)
        self.label_price_from.setObjectName(u"label_price_from")

        self.gridLayout.addWidget(self.label_price_from, 1, 0, 1, 1)

        self.spinBox_price_from = QSpinBox(self.groupBox_filters)
        self.spinBox_price_from.setObjectName(u"spinBox_price_from")
        self.spinBox_price_from.setMaximum(999999999)

        self.gridLayout.addWidget(self.spinBox_price_from, 1, 1, 1, 1)

        self.label_price_to = QLabel(self.groupBox_filters)
        self.label_price_to.setObjectName(u"label_price_to")

        self.gridLayout.addWidget(self.label_price_to, 1, 2, 1, 1)

        self.spinBox_price_to = QSpinBox(self.groupBox_filters)
        self.spinBox_price_to.setObjectName(u"spinBox_price_to")
        self.spinBox_price_to.setMaximum(999999999)

        self.gridLayout.addWidget(self.spinBox_price_to, 1, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_filters)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_create_order = QPushButton(self.page_order_list)
        self.pushButton_create_order.setObjectName(u"pushButton_create_order")

        self.horizontalLayout.addWidget(self.pushButton_create_order)

        self.pushButton_view_details = QPushButton(self.page_order_list)
        self.pushButton_view_details.setObjectName(u"pushButton_view_details")

        self.horizontalLayout.addWidget(self.pushButton_view_details)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tableWidget_orders = QTableWidget(self.page_order_list)
        if (self.tableWidget_orders.columnCount() < 6):
            self.tableWidget_orders.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_orders.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_orders.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_orders.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_orders.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_orders.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_orders.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget_orders.setObjectName(u"tableWidget_orders")
        self.tableWidget_orders.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tableWidget_orders)

        self.stackedWidget.addWidget(self.page_order_list)
        self.page_create_order = QWidget()
        self.page_create_order.setObjectName(u"page_create_order")
        self.horizontalLayout_6 = QHBoxLayout(self.page_create_order)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tableWidget_product = QTableWidget(self.page_create_order)
        if (self.tableWidget_product.columnCount() < 6):
            self.tableWidget_product.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_product.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_product.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_product.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_product.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_product.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_product.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.tableWidget_product.setObjectName(u"tableWidget_product")
        self.tableWidget_product.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_4.addWidget(self.tableWidget_product)

        self.tableWidget_menu = QTableWidget(self.page_create_order)
        if (self.tableWidget_menu.columnCount() < 6):
            self.tableWidget_menu.setColumnCount(6)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_menu.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_menu.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_menu.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_menu.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_menu.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_menu.setHorizontalHeaderItem(5, __qtablewidgetitem17)
        self.tableWidget_menu.setObjectName(u"tableWidget_menu")

        self.horizontalLayout_4.addWidget(self.tableWidget_menu)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label_quantity = QLabel(self.page_create_order)
        self.label_quantity.setObjectName(u"label_quantity")

        self.verticalLayout.addWidget(self.label_quantity)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit_quantity = QLineEdit(self.page_create_order)
        self.lineEdit_quantity.setObjectName(u"lineEdit_quantity")

        self.horizontalLayout_5.addWidget(self.lineEdit_quantity)

        self.updateSLButton = QPushButton(self.page_create_order)
        self.updateSLButton.setObjectName(u"updateSLButton")

        self.horizontalLayout_5.addWidget(self.updateSLButton)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_add_to_order = QPushButton(self.page_create_order)
        self.pushButton_add_to_order.setObjectName(u"pushButton_add_to_order")

        self.horizontalLayout_2.addWidget(self.pushButton_add_to_order)

        self.pushButton_payment = QPushButton(self.page_create_order)
        self.pushButton_payment.setObjectName(u"pushButton_payment")

        self.horizontalLayout_2.addWidget(self.pushButton_payment)

        self.pushButton_print = QPushButton(self.page_create_order)
        self.pushButton_print.setObjectName(u"pushButton_print")

        self.horizontalLayout_2.addWidget(self.pushButton_print)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_total = QLabel(self.page_create_order)
        self.label_total.setObjectName(u"label_total")

        self.verticalLayout.addWidget(self.label_total)


        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.stackedWidget.addWidget(self.page_create_order)
        self.page_order_details = QWidget()
        self.page_order_details.setObjectName(u"page_order_details")
        self.verticalLayout_4 = QVBoxLayout(self.page_order_details)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_order_details = QLabel(self.page_order_details)
        self.label_order_details.setObjectName(u"label_order_details")
        self.label_order_details.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_order_details)

        self.tableWidget_order_details = QTableWidget(self.page_order_details)
        if (self.tableWidget_order_details.columnCount() < 5):
            self.tableWidget_order_details.setColumnCount(5)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_order_details.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_order_details.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_order_details.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_order_details.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_order_details.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        self.tableWidget_order_details.setObjectName(u"tableWidget_order_details")
        self.tableWidget_order_details.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_4.addWidget(self.tableWidget_order_details)

        self.backButton = QPushButton(self.page_order_details)
        self.backButton.setObjectName(u"backButton")
        icon = QIcon()
        icon.addFile(u":/Icons/left-arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.backButton)

        self.stackedWidget.addWidget(self.page_order_details)

        self.horizontalLayout_3.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Order Management System", None))
        self.groupBox_filters.setTitle(QCoreApplication.translate("MainWindow", u"T\u00ecm ki\u1ebfm", None))
        self.label_date_from.setText(QCoreApplication.translate("MainWindow", u"From Date:", None))
        self.label_date_to.setText(QCoreApplication.translate("MainWindow", u"To Date:", None))
        self.label_price_from.setText(QCoreApplication.translate("MainWindow", u"Price From:", None))
        self.label_price_to.setText(QCoreApplication.translate("MainWindow", u"Price To:", None))
        self.pushButton_create_order.setText(QCoreApplication.translate("MainWindow", u"T\u1ea1o \u0111\u01a1n h\u00e0ng", None))
        self.pushButton_view_details.setText(QCoreApplication.translate("MainWindow", u"Xem chi ti\u1ebft \u0111\u01a1n h\u00e0ng", None))
        ___qtablewidgetitem = self.tableWidget_orders.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 DH", None));
        ___qtablewidgetitem1 = self.tableWidget_orders.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 KH", None));
        ___qtablewidgetitem2 = self.tableWidget_orders.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 NV", None));
        ___qtablewidgetitem3 = self.tableWidget_orders.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y \u0111\u1eb7t ", None));
        ___qtablewidgetitem4 = self.tableWidget_orders.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"T\u1ed5ng ti\u1ec1n", None));
        ___qtablewidgetitem5 = self.tableWidget_orders.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ea1ng th\u00e1i", None));
        ___qtablewidgetitem6 = self.tableWidget_product.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 SP", None));
        ___qtablewidgetitem7 = self.tableWidget_product.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ea3n ph\u1ea9m", None));
        ___qtablewidgetitem8 = self.tableWidget_product.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u1ea2nh", None));
        ___qtablewidgetitem9 = self.tableWidget_product.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"M\u00f4 t\u1ea3", None));
        ___qtablewidgetitem10 = self.tableWidget_product.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Gi\u00e1", None));
        ___qtablewidgetitem11 = self.tableWidget_product.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Lo\u1ea1i", None));
        ___qtablewidgetitem12 = self.tableWidget_menu.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 SP", None));
        ___qtablewidgetitem13 = self.tableWidget_menu.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"T\u00ean s\u1ea3n ph\u1ea9m", None));
        ___qtablewidgetitem14 = self.tableWidget_menu.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u1ea2nh", None));
        ___qtablewidgetitem15 = self.tableWidget_menu.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 L\u01b0\u1ee3ng", None));
        ___qtablewidgetitem16 = self.tableWidget_menu.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"M\u00f4 t\u1ea3", None));
        ___qtablewidgetitem17 = self.tableWidget_menu.horizontalHeaderItem(5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Giá", None));
        self.label_quantity.setText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp s\u1ed1 l\u01b0\u1ee3ng:", None))
        self.updateSLButton.setText(QCoreApplication.translate("MainWindow", u"C\u1eadp nh\u1eadt s\u1ed1 l\u01b0\u1ee3ng", None))
        self.pushButton_add_to_order.setText(QCoreApplication.translate("MainWindow", u"Th\u00eam v\u00e0o h\u00f3a \u0111\u01a1n", None))
        self.pushButton_payment.setText(QCoreApplication.translate("MainWindow", u"Thanh to\u00e1n", None))
        self.pushButton_print.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t h\u00f3a \u0111\u01a1n", None))
        self.label_total.setText(QCoreApplication.translate("MainWindow", u"T\u1ed5ng ti\u1ec1n: 0", None))
        self.label_order_details.setStyleSheet(QCoreApplication.translate("MainWindow", u"font-size: 18px; font-weight: bold; margin: 10px;", None))
        self.label_order_details.setText(QCoreApplication.translate("MainWindow", u"Chi ti\u1ebft \u0111\u01a1n h\u00e0ng", None))
        ___qtablewidgetitem18 = self.tableWidget_order_details.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 DH", None));
        ___qtablewidgetitem19 = self.tableWidget_order_details.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 SP", None));
        ___qtablewidgetitem20 = self.tableWidget_order_details.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 L\u01b0\u1ee3ng", None));
        ___qtablewidgetitem21 = self.tableWidget_order_details.horizontalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u0110\u01a1n Gi\u00e1", None));
        ___qtablewidgetitem22 = self.tableWidget_order_details.horizontalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Th\u00e0nh Ti\u1ec1n", None));
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Quay l\u1ea1i ", None))
    # retranslateUi

