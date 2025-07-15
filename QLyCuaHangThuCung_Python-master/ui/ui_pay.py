# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pay.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_PaymentPage(object):
    def setupUi(self, PaymentPage):
        if not PaymentPage.objectName():
            PaymentPage.setObjectName(u"PaymentPage")
        PaymentPage.resize(1155, 547)
        PaymentPage.setStyleSheet(u"\n"
"    QWidget {\n"
"      background-color: #fef8ec;\n"
"      font-family: Arial;\n"
"    }\n"
"    QLabel {\n"
"      color: #333333;\n"
"    }\n"
"   ")
        self.mainLayout = QHBoxLayout(PaymentPage)
        self.mainLayout.setSpacing(30)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(20, 20, 20, 20)
        self.leftLayout = QVBoxLayout()
        self.leftLayout.setObjectName(u"leftLayout")
        self.storeLabel = QLabel(PaymentPage)
        self.storeLabel.setObjectName(u"storeLabel")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        font.setBold(True)
        self.storeLabel.setFont(font)

        self.leftLayout.addWidget(self.storeLabel)

        self.cartFrame = QFrame(PaymentPage)
        self.cartFrame.setObjectName(u"cartFrame")
        self.cartFrame.setFrameShape(QFrame.NoFrame)
        self.cartLayout = QVBoxLayout(self.cartFrame)
        self.cartLayout.setObjectName(u"cartLayout")
        self.itemLabel = QLabel(self.cartFrame)
        self.itemLabel.setObjectName(u"itemLabel")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.itemLabel.setFont(font1)

        self.cartLayout.addWidget(self.itemLabel)

        self.itemTable = QTableWidget(self.cartFrame)
        if (self.itemTable.columnCount() < 7):
            self.itemTable.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.itemTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.itemTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.itemTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.itemTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.itemTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.itemTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.itemTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.itemTable.setObjectName(u"itemTable")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itemTable.sizePolicy().hasHeightForWidth())
        self.itemTable.setSizePolicy(sizePolicy)
        self.itemTable.setStyleSheet(u"\n"
"       QTableWidget {\n"
"         gridline-color: #e0e0e0;\n"
"       }\n"
"      ")
        self.itemTable.horizontalHeader().setStretchLastSection(True)
        self.itemTable.verticalHeader().setStretchLastSection(False)

        self.cartLayout.addWidget(self.itemTable)


        self.leftLayout.addWidget(self.cartFrame)


        self.mainLayout.addLayout(self.leftLayout)

        self.rightLayout = QVBoxLayout()
        self.rightLayout.setObjectName(u"rightLayout")
        self.billDetailLabel = QLabel(PaymentPage)
        self.billDetailLabel.setObjectName(u"billDetailLabel")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.billDetailLabel.setFont(font2)

        self.rightLayout.addWidget(self.billDetailLabel)

        self.billFrame = QFrame(PaymentPage)
        self.billFrame.setObjectName(u"billFrame")
        self.billLayout = QVBoxLayout(self.billFrame)
        self.billLayout.setObjectName(u"billLayout")
        self.billDetails = QFormLayout()
        self.billDetails.setObjectName(u"billDetails")
        self.cartTotalLabel = QLabel(self.billFrame)
        self.cartTotalLabel.setObjectName(u"cartTotalLabel")

        self.billDetails.setWidget(0, QFormLayout.LabelRole, self.cartTotalLabel)

        self.cartTotalValue = QLabel(self.billFrame)
        self.cartTotalValue.setObjectName(u"cartTotalValue")
        self.cartTotalValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.billDetails.setWidget(0, QFormLayout.FieldRole, self.cartTotalValue)

        self.shippingLabel = QLabel(self.billFrame)
        self.shippingLabel.setObjectName(u"shippingLabel")

        self.billDetails.setWidget(1, QFormLayout.LabelRole, self.shippingLabel)

        self.shippingValue = QLabel(self.billFrame)
        self.shippingValue.setObjectName(u"shippingValue")
        self.shippingValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.billDetails.setWidget(1, QFormLayout.FieldRole, self.shippingValue)


        self.billLayout.addLayout(self.billDetails)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.billLayout.addItem(self.verticalSpacer)

        self.totalLayout = QHBoxLayout()
        self.totalLayout.setObjectName(u"totalLayout")
        self.totalLabel = QLabel(self.billFrame)
        self.totalLabel.setObjectName(u"totalLabel")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.totalLabel.setFont(font3)

        self.totalLayout.addWidget(self.totalLabel)

        self.totalValue = QLabel(self.billFrame)
        self.totalValue.setObjectName(u"totalValue")
        self.totalValue.setFont(font3)
        self.totalValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.totalLayout.addWidget(self.totalValue)


        self.billLayout.addLayout(self.totalLayout)

        self.placeOrderButton = QPushButton(self.billFrame)
        self.placeOrderButton.setObjectName(u"placeOrderButton")
        self.placeOrderButton.setMinimumSize(QSize(0, 40))
        self.placeOrderButton.setStyleSheet(u"\n"
"            QPushButton {\n"
"              background-color: #a0c9c3;\n"
"              color: #333;\n"
"              border-radius: 4px;\n"
"              font-weight: bold;\n"
"              font-size: 14px;\n"
"            }\n"
"            QPushButton:hover {\n"
"              background-color: #657d81;\n"
"		 	  color: white;\n"
"            }\n"
"           ")

        self.billLayout.addWidget(self.placeOrderButton)

        self.exportButton = QPushButton(self.billFrame)
        self.exportButton.setObjectName(u"exportButton")
        self.exportButton.setMinimumSize(QSize(0, 40))
        self.exportButton.setStyleSheet(u"\n"
"            QPushButton {\n"
"              background-color: #e2b4b7;\n"
"              color: #333;\n"
"              border-radius: 4px;\n"
"              font-weight: bold;\n"
"              font-size: 14px;\n"
"            }\n"
"            QPushButton:hover {\n"
"              background-color: #bd637e;\n"
"		 	  color: white;\n"
"            }\n"
"           ")

        self.billLayout.addWidget(self.exportButton)


        self.rightLayout.addWidget(self.billFrame)


        self.mainLayout.addLayout(self.rightLayout)


        self.retranslateUi(PaymentPage)

        QMetaObject.connectSlotsByName(PaymentPage)
    # setupUi

    def retranslateUi(self, PaymentPage):
        PaymentPage.setWindowTitle(QCoreApplication.translate("PaymentPage", u"The Store - Payment", None))
        self.storeLabel.setText(QCoreApplication.translate("PaymentPage", u"Thanh to\u00e1n ", None))
        self.itemLabel.setText(QCoreApplication.translate("PaymentPage", u"Gi\u1ecf h\u00e0ng (1 m\u1eb7t h\u00e0ng)", None))
        ___qtablewidgetitem = self.itemTable.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PaymentPage", u"Product Image", None));
        ___qtablewidgetitem1 = self.itemTable.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PaymentPage", u"Product Title", None));
        ___qtablewidgetitem2 = self.itemTable.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PaymentPage", u"Price", None));
        ___qtablewidgetitem3 = self.itemTable.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PaymentPage", u"Quantity", None));
        ___qtablewidgetitem4 = self.itemTable.horizontalHeaderItem(5)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PaymentPage", u"Total", None));
        ___qtablewidgetitem5 = self.itemTable.horizontalHeaderItem(6)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PaymentPage", u"Order Details", None));
        self.billDetailLabel.setText(QCoreApplication.translate("PaymentPage", u"Chi ti\u1ebft h\u00f3a \u0111\u01a1n", None))
        self.billFrame.setStyleSheet(QCoreApplication.translate("PaymentPage", u"\n"
"         QFrame {\n"
"           border: 1px solid #e0e0e0;\n"
"           border-radius: 8px;\n"
"           padding: 20px;\n"
"         }\n"
"        ", None))
        self.cartTotalLabel.setText(QCoreApplication.translate("PaymentPage", u"T\u1ed5ng gi\u1ecf h\u00e0ng", None))
        self.cartTotalValue.setText(QCoreApplication.translate("PaymentPage", u"1029.80", None))
        self.shippingLabel.setText(QCoreApplication.translate("PaymentPage", u"V\u1eadn chuy\u1ec3n", None))
        self.shippingValue.setStyleSheet(QCoreApplication.translate("PaymentPage", u"color: #44cc44;", None))
        self.shippingValue.setText(QCoreApplication.translate("PaymentPage", u"Free", None))
        self.totalLabel.setText(QCoreApplication.translate("PaymentPage", u"T\u1ed5ng", None))
        self.totalValue.setText(QCoreApplication.translate("PaymentPage", u"1,683.80", None))
        self.placeOrderButton.setText(QCoreApplication.translate("PaymentPage", u"Thanh to\u00e1n ", None))
        self.exportButton.setText(QCoreApplication.translate("PaymentPage", u"Xu\u1ea5t h\u00f3a \u0111\u01a1n", None))
    # retranslateUi

