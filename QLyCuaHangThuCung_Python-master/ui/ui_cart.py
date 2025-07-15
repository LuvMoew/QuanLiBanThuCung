# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cart.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_ShoppingCart(object):
    def setupUi(self, ShoppingCart):
        if not ShoppingCart.objectName():
            ShoppingCart.setObjectName(u"ShoppingCart")
        ShoppingCart.resize(841, 600)
        ShoppingCart.setStyleSheet(u"\n"
"    QWidget {\n"
"      background-color: #fef8ec;\n"
"      font-family: Arial;\n"
"    }\n"
"    QLabel {\n"
"      color: #333333;\n"
"    }\n"
"    QGroupBox {\n"
"      background-color: white;\n"
"      border: 1px solid #e0e0e0;\n"
"      border-radius: 8px;\n"
"      padding: 15px;\n"
"    }\n"
"    QTableWidget {\n"
"      background-color: white;\n"
"      border: 1px solid #e0e0e0;\n"
"      border-radius: 8px;\n"
"      padding: 10px;\n"
"    }\n"
"    QTableWidget::item {\n"
"      padding: 8px;\n"
"    }\n"
"    QHeaderView::section {\n"
"      background-color: #f8f8f8;\n"
"      padding: 8px;\n"
"      border: none;\n"
"      font-weight: bold;\n"
"    }\n"
"   ")
        self.verticalLayout = QVBoxLayout(ShoppingCart)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.titleLabel = QLabel(ShoppingCart)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(24)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet(u"\n"
"       color: #2c3e50;\n"
"       margin-bottom: 20px;\n"
"      ")
        self.titleLabel.setAlignment(Qt.AlignLeading)

        self.verticalLayout.addWidget(self.titleLabel)

        self.cartTable = QTableWidget(ShoppingCart)
        if (self.cartTable.columnCount() < 7):
            self.cartTable.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.cartTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.cartTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.cartTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.cartTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.cartTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.cartTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.cartTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.cartTable.setObjectName(u"cartTable")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cartTable.sizePolicy().hasHeightForWidth())
        self.cartTable.setSizePolicy(sizePolicy)
        self.cartTable.setStyleSheet(u"\n"
"       QTableWidget {\n"
"         gridline-color: #e0e0e0;\n"
"       }\n"
"      ")

        self.verticalLayout.addWidget(self.cartTable)

        self.couponLayout = QHBoxLayout()
        self.couponLayout.setSpacing(10)
        self.couponLayout.setObjectName(u"couponLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.couponLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(ShoppingCart)
        self.label.setObjectName(u"label")

        self.couponLayout.addWidget(self.label)

        self.editSL = QLineEdit(ShoppingCart)
        self.editSL.setObjectName(u"editSL")
        self.editSL.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;        /* M\u00e0u n\u1ec1n */\n"
"    border: 2px solid #e0e0e0;       /* \u0110\u01b0\u1eddng vi\u1ec1n */\n"
"    border-radius: 6px;              /* Bo g\u00f3c */\n"
"    padding: 6px;                    /* Kho\u1ea3ng c\u00e1ch b\u00ean trong */\n"
"    font-size: 14px;                 /* C\u1ee1 ch\u1eef */\n"
"    color: #333333;                  /* M\u00e0u ch\u1eef */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4a90e2;       /* \u0110\u1ed5i m\u00e0u vi\u1ec1n khi focus */\n"
"    outline: none;                   /* X\u00f3a outline m\u1eb7c \u0111\u1ecbnh */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #bdbdbd;       /* \u0110\u1ed5i m\u00e0u vi\u1ec1n khi di chu\u1ed9t */\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #f0f0f0;       /* M\u00e0u n\u1ec1n khi b\u1ecb v\u00f4 hi\u1ec7u */\n"
"    color: #aaaaaa;                  /* M\u00e0u ch\u1eef khi b\u1ecb v\u00f4 hi\u1ec7u */\n"
"}\n"
"\n"
"/* T\u00f9y ch"
                        "\u1ec9nh placeholder (c\u1ea7n Qt 5.2 tr\u1edf l\u00ean) */\n"
"QLineEdit[placeholderText]:empty:focus:before {\n"
"    color: #999999;                  /* M\u00e0u placeholder */\n"
"    content: attr(placeholderText);  /* Hi\u1ec3n th\u1ecb placeholder */\n"
"}\n"
"")

        self.couponLayout.addWidget(self.editSL)

        self.updateCartButton = QPushButton(ShoppingCart)
        self.updateCartButton.setObjectName(u"updateCartButton")
        self.updateCartButton.setMinimumSize(QSize(120, 40))
        self.updateCartButton.setStyleSheet(u"\n"
"         QPushButton {\n"
"           background-color: #40cc92;\n"
"           color: white;\n"
"           border-radius: 6px;\n"
"           font-weight: bold;\n"
"         }\n"
"         QPushButton:hover {\n"
"           background-color: #38b481;\n"
"         }\n"
"         QPushButton:pressed {\n"
"           background-color: #219a52;\n"
"         }\n"
"        ")

        self.couponLayout.addWidget(self.updateCartButton)


        self.verticalLayout.addLayout(self.couponLayout)

        self.totalLayout = QHBoxLayout()
        self.totalLayout.setObjectName(u"totalLayout")
        self.returnButton = QPushButton(ShoppingCart)
        self.returnButton.setObjectName(u"returnButton")
        self.returnButton.setMinimumSize(QSize(120, 40))
        self.returnButton.setStyleSheet(u"\n"
"         QPushButton {\n"
"           background-color: transparent;\n"
"           color: #3498db;\n"
"           border: none;\n"
"           font-weight: bold;\n"
"         }\n"
"         QPushButton:hover {\n"
"           color: #2980b9;\n"
"         }\n"
"        ")
        icon = QIcon()
        icon.addFile(u":/Icons/left-arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.returnButton.setIcon(icon)

        self.totalLayout.addWidget(self.returnButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.totalLayout.addItem(self.horizontalSpacer_2)

        self.cartTotalsBox = QGroupBox(ShoppingCart)
        self.cartTotalsBox.setObjectName(u"cartTotalsBox")
        self.cartTotalsBox.setMinimumSize(QSize(300, 0))
        self.cartTotalsBox.setStyleSheet(u"\n"
"         QGroupBox {\n"
"           font-weight: bold;\n"
"           font-size: 16px;\n"
"         }\n"
"        ")
        self.verticalLayout_2 = QVBoxLayout(self.cartTotalsBox)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.subtotalLayout = QHBoxLayout()
        self.subtotalLayout.setObjectName(u"subtotalLayout")
        self.subtotalLabel = QLabel(self.cartTotalsBox)
        self.subtotalLabel.setObjectName(u"subtotalLabel")
        self.subtotalLabel.setStyleSheet(u"font-size: 14px;")

        self.subtotalLayout.addWidget(self.subtotalLabel)

        self.subtotalValue = QLabel(self.cartTotalsBox)
        self.subtotalValue.setObjectName(u"subtotalValue")
        self.subtotalValue.setStyleSheet(u"\n"
"              font-size: 14px;\n"
"              font-weight: bold;\n"
"             ")
        self.subtotalValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.subtotalLayout.addWidget(self.subtotalValue)


        self.verticalLayout_2.addLayout(self.subtotalLayout)

        self.line = QFrame(self.cartTotalsBox)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: #e0e0e0;")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.totalPriceLayout = QHBoxLayout()
        self.totalPriceLayout.setObjectName(u"totalPriceLayout")
        self.totalLabel = QLabel(self.cartTotalsBox)
        self.totalLabel.setObjectName(u"totalLabel")
        self.totalLabel.setStyleSheet(u"\n"
"              font-size: 16px;\n"
"              font-weight: bold;\n"
"             ")

        self.totalPriceLayout.addWidget(self.totalLabel)

        self.totalValue = QLabel(self.cartTotalsBox)
        self.totalValue.setObjectName(u"totalValue")
        self.totalValue.setStyleSheet(u"\n"
"              font-size: 16px;\n"
"              font-weight: bold;\n"
"              color: #2ecc71;\n"
"             ")
        self.totalValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.totalPriceLayout.addWidget(self.totalValue)


        self.verticalLayout_2.addLayout(self.totalPriceLayout)

        self.checkoutButton = QPushButton(self.cartTotalsBox)
        self.checkoutButton.setObjectName(u"checkoutButton")
        self.checkoutButton.setMinimumSize(QSize(0, 45))
        self.checkoutButton.setStyleSheet(u"\n"
"            QPushButton {\n"
"              background-color: #e74f44;\n"
"              color: white;\n"
"              border-radius: 6px;\n"
"              font-size: 14px;\n"
"              font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"              background-color: #c0392b;\n"
"            }\n"
"            QPushButton:pressed {\n"
"              background-color: #a93226;\n"
"            }\n"
"           ")

        self.verticalLayout_2.addWidget(self.checkoutButton)


        self.totalLayout.addWidget(self.cartTotalsBox)


        self.verticalLayout.addLayout(self.totalLayout)


        self.retranslateUi(ShoppingCart)

        QMetaObject.connectSlotsByName(ShoppingCart)
    # setupUi

    def retranslateUi(self, ShoppingCart):
        ShoppingCart.setWindowTitle(QCoreApplication.translate("ShoppingCart", u"Shopping Cart", None))
        self.titleLabel.setText(QCoreApplication.translate("ShoppingCart", u"Shopping Cart", None))
        ___qtablewidgetitem = self.cartTable.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ShoppingCart", u"Product Image", None));
        ___qtablewidgetitem1 = self.cartTable.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ShoppingCart", u"Product Title", None));
        ___qtablewidgetitem2 = self.cartTable.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ShoppingCart", u"Price", None));
        ___qtablewidgetitem3 = self.cartTable.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ShoppingCart", u"Quantity", None));
        ___qtablewidgetitem4 = self.cartTable.horizontalHeaderItem(5)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ShoppingCart", u"Total", None));
        ___qtablewidgetitem5 = self.cartTable.horizontalHeaderItem(6)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ShoppingCart", u"Order Details", None));
        self.label.setText(QCoreApplication.translate("ShoppingCart", u"S\u1ed1 l\u01b0\u1ee3ng:", None))
        self.editSL.setPlaceholderText(QCoreApplication.translate("ShoppingCart", u"Nh\u1eadp s\u1ed1 l\u01b0\u1ee3ng..", None))
        self.updateCartButton.setText(QCoreApplication.translate("ShoppingCart", u"  C\u1eadp nh\u1eadt gi\u1ecf h\u00e0ng  ", None))
        self.returnButton.setText(QCoreApplication.translate("ShoppingCart", u"Quay l\u1ea1i", None))
        self.cartTotalsBox.setTitle(QCoreApplication.translate("ShoppingCart", u"Cart Totals", None))
        self.subtotalLabel.setText(QCoreApplication.translate("ShoppingCart", u"Subtotal", None))
        self.subtotalValue.setText(QCoreApplication.translate("ShoppingCart", u"$50.00", None))
        self.totalLabel.setText(QCoreApplication.translate("ShoppingCart", u"Total", None))
        self.totalValue.setText(QCoreApplication.translate("ShoppingCart", u"$50.00", None))
        self.checkoutButton.setText(QCoreApplication.translate("ShoppingCart", u"Thanh to\u00e1n", None))
    # retranslateUi

