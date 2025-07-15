# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customer.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_CustomerWindow(object):
    def setupUi(self, CustomerWindow):
        if not CustomerWindow.objectName():
            CustomerWindow.setObjectName(u"CustomerWindow")
        CustomerWindow.resize(1051, 699)
        CustomerWindow.setStyleSheet(u"\n"
"    QMainWindow {\n"
"        background-color: #f5f6fa;\n"
"    }\n"
"    QWidget#centralWidget {\n"
"        background-color: rgb(254, 248, 236);\n"
"    }\n"
"    QGroupBox {\n"
"        background-color: #ffffff;\n"
"        border-radius: 10px;\n"
"        border: none;\n"
"        margin-top: 15px;\n"
"    }\n"
"    QGroupBox::title {\n"
"        color: #2d3436;\n"
"        font-size: 14px;\n"
"        font-weight: bold;\n"
"        padding: 5px;\n"
"    }\n"
"    QLabel {\n"
"        color: #2d3436;\n"
"        font-size: 13px;\n"
"        font-weight: bold;\n"
"        background-color: white;\n"
"    }\n"
"    QLineEdit, QTextEdit {\n"
"        padding: 8px;\n"
"        border: 2px solid #dfe6e9;\n"
"        border-radius: 6px;\n"
"        background-color: #ffffff;\n"
"        font-size: 13px;\n"
"        min-height: 20px;\n"
"    }\n"
"    QLineEdit:focus, QTextEdit:focus {\n"
"        border: 2px solid #74b9ff;\n"
"    }\n"
"    QPushButton {\n"
"        padding: 8px 15px;\n"
"        border-"
                        "radius: 6px;\n"
"        font-size: 13px;\n"
"        font-weight: bold;\n"
"        min-width: 80px;\n"
"        color: #333;\n"
"    }\n"
"    QPushButton#addButton {\n"
"        background-color: #9ac1bb;\n"
"        color: #333;\n"
"        border: none;\n"
"    }\n"
"    QPushButton#addButton:hover {\n"
"        background-color: #84a6a0;\n"
"    }\n"
"    QPushButton#fixButton {\n"
"        background-color: #92b9e3;\n"
"        color: #333;\n"
"        border: none;\n"
"    }\n"
"    QPushButton#fixButton:hover {\n"
"        background-color: #7fa1c5;\n"
"    }\n"
"    QPushButton#deleteButton {\n"
"        background-color: #ef495a;\n"
"        color: #333;\n"
"        border: none;\n"
"    }\n"
"    QPushButton#deleteButton:hover {\n"
"        background-color: #dc4355;\n"
"    }\n"
"    QPushButton#imgpathButton {\n"
"        background-color: #d9adb0;\n"
"        color: #333;\n"
"        border: none;\n"
"    }\n"
"    QPushButton#imgpathButton:hover {\n"
"        background-color: #cc999e;\n"
"    "
                        "}\n"
"	QPushButton#excelButton {\n"
"        background-color: #00efaf;\n"
"        color: #333;\n"
"        border: none;\n"
"    }\n"
"    QPushButton#excelButton:hover {\n"
"        background-color: #00d095;\n"
"    }\n"
"    QTableWidget {\n"
"        background-color: #ffffff;\n"
"        border: none;\n"
"        border-radius: 10px;\n"
"        gridline-color: #dfe6e9;\n"
"    }\n"
"    QTableWidget::item {\n"
"        padding: 5px;\n"
"    }\n"
"    QHeaderView::section {\n"
"        background-color: #f5f6fa;\n"
"        padding: 5px;\n"
"        border: none;\n"
"        font-weight: bold;\n"
"    }\n"
"   ")
        self.centralWidget = QWidget(CustomerWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.customerInfoGroup = QGroupBox(self.centralWidget)
        self.customerInfoGroup.setObjectName(u"customerInfoGroup")
        self.horizontalLayout = QHBoxLayout(self.customerInfoGroup)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 9, -1, -1)
        self.formLayout = QGridLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.idLabel = QLabel(self.customerInfoGroup)
        self.idLabel.setObjectName(u"idLabel")

        self.formLayout.addWidget(self.idLabel, 0, 0, 1, 1)

        self.idInput = QLineEdit(self.customerInfoGroup)
        self.idInput.setObjectName(u"idInput")
        self.idInput.setEnabled(False)

        self.formLayout.addWidget(self.idInput, 0, 1, 1, 1)

        self.nameLabel = QLabel(self.customerInfoGroup)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.addWidget(self.nameLabel, 1, 0, 1, 1)

        self.nameInput = QLineEdit(self.customerInfoGroup)
        self.nameInput.setObjectName(u"nameInput")

        self.formLayout.addWidget(self.nameInput, 1, 1, 1, 1)

        self.phoneLabel = QLabel(self.customerInfoGroup)
        self.phoneLabel.setObjectName(u"phoneLabel")

        self.formLayout.addWidget(self.phoneLabel, 2, 0, 1, 1)

        self.phoneInput = QLineEdit(self.customerInfoGroup)
        self.phoneInput.setObjectName(u"phoneInput")

        self.formLayout.addWidget(self.phoneInput, 2, 1, 1, 1)

        self.emailLabel = QLabel(self.customerInfoGroup)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout.addWidget(self.emailLabel, 3, 0, 1, 1)

        self.emailInput = QLineEdit(self.customerInfoGroup)
        self.emailInput.setObjectName(u"emailInput")

        self.formLayout.addWidget(self.emailInput, 3, 1, 1, 1)

        self.addressLabel = QLabel(self.customerInfoGroup)
        self.addressLabel.setObjectName(u"addressLabel")

        self.formLayout.addWidget(self.addressLabel, 4, 0, 1, 1)

        self.addressInput = QTextEdit(self.customerInfoGroup)
        self.addressInput.setObjectName(u"addressInput")
        self.addressInput.setMaximumSize(QSize(16777215, 60))

        self.formLayout.addWidget(self.addressInput, 4, 1, 1, 1)

        self.startDateLabel = QLabel(self.customerInfoGroup)
        self.startDateLabel.setObjectName(u"startDateLabel")

        self.formLayout.addWidget(self.startDateLabel, 5, 0, 1, 1)

        self.registerDateEdit = QDateEdit(self.customerInfoGroup)
        self.registerDateEdit.setObjectName(u"registerDateEdit")
        self.registerDateEdit.setCalendarPopup(True)

        self.formLayout.addWidget(self.registerDateEdit, 5, 1, 1, 1)


        self.horizontalLayout.addLayout(self.formLayout)

        self.photoLabel = QLabel(self.customerInfoGroup)
        self.photoLabel.setObjectName(u"photoLabel")
        self.photoLabel.setMinimumSize(QSize(200, 200))
        self.photoLabel.setMaximumSize(QSize(200, 298))
        self.photoLabel.setStyleSheet(u"\n"
"           background-color: #dfe6e9;\n"
"           border-radius: 10px;\n"
"          ")
        self.photoLabel.setPixmap(QPixmap(u"user-placeholder.png"))
        self.photoLabel.setScaledContents(True)

        self.horizontalLayout.addWidget(self.photoLabel)


        self.verticalLayout.addWidget(self.customerInfoGroup)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer)

        self.imgpathButton = QPushButton(self.centralWidget)
        self.imgpathButton.setObjectName(u"imgpathButton")

        self.buttonLayout.addWidget(self.imgpathButton)

        self.excelButton = QPushButton(self.centralWidget)
        self.excelButton.setObjectName(u"excelButton")

        self.buttonLayout.addWidget(self.excelButton)

        self.addButton = QPushButton(self.centralWidget)
        self.addButton.setObjectName(u"addButton")

        self.buttonLayout.addWidget(self.addButton)

        self.fixButton = QPushButton(self.centralWidget)
        self.fixButton.setObjectName(u"fixButton")

        self.buttonLayout.addWidget(self.fixButton)

        self.deleteButton = QPushButton(self.centralWidget)
        self.deleteButton.setObjectName(u"deleteButton")

        self.buttonLayout.addWidget(self.deleteButton)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.customerTable = QTableWidget(self.centralWidget)
        if (self.customerTable.columnCount() < 7):
            self.customerTable.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.customerTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.customerTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.customerTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.customerTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.customerTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.customerTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.customerTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.customerTable.setObjectName(u"customerTable")
        self.customerTable.horizontalHeader().setDefaultSectionSize(110)
        self.customerTable.horizontalHeader().setStretchLastSection(True)
        self.customerTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.customerTable)

        CustomerWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(CustomerWindow)

        QMetaObject.connectSlotsByName(CustomerWindow)
    # setupUi

    def retranslateUi(self, CustomerWindow):
        CustomerWindow.setWindowTitle(QCoreApplication.translate("CustomerWindow", u"Qu\u1ea3n l\u00fd Kh\u00e1ch H\u00e0ng", None))
        self.customerInfoGroup.setTitle("")
        self.idLabel.setText(QCoreApplication.translate("CustomerWindow", u"M\u00e3 KH:", None))
        self.idInput.setPlaceholderText(QCoreApplication.translate("CustomerWindow", u"T\u1ef1 \u0111\u1ed9ng t\u1ea1o", None))
        self.nameLabel.setText(QCoreApplication.translate("CustomerWindow", u"H\u1ecd v\u00e0 t\u00ean:", None))
        self.nameInput.setPlaceholderText(QCoreApplication.translate("CustomerWindow", u"Nh\u1eadp h\u1ecd v\u00e0 t\u00ean \u0111\u1ea7y \u0111\u1ee7", None))
        self.phoneLabel.setText(QCoreApplication.translate("CustomerWindow", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i:", None))
        self.phoneInput.setPlaceholderText(QCoreApplication.translate("CustomerWindow", u"Nh\u1eadp s\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None))
        self.emailLabel.setText(QCoreApplication.translate("CustomerWindow", u"Email:", None))
        self.emailInput.setPlaceholderText(QCoreApplication.translate("CustomerWindow", u"Nh\u1eadp \u0111\u1ecba ch\u1ec9 email", None))
        self.addressLabel.setText(QCoreApplication.translate("CustomerWindow", u"\u0110\u1ecba ch\u1ec9:", None))
        self.addressInput.setPlaceholderText(QCoreApplication.translate("CustomerWindow", u"Nh\u1eadp \u0111\u1ecba ch\u1ec9 \u0111\u1ea7y \u0111\u1ee7", None))
        self.startDateLabel.setText(QCoreApplication.translate("CustomerWindow", u"Ng\u00e0y \u0111\u0103ng k\u00fd:", None))
        self.photoLabel.setText("")
        self.imgpathButton.setText(QCoreApplication.translate("CustomerWindow", u"Ch\u1ecdn \u1ea3nh", None))
        self.excelButton.setText(QCoreApplication.translate("CustomerWindow", u"Excel", None))
        self.addButton.setText(QCoreApplication.translate("CustomerWindow", u"Th\u00eam", None))
        self.fixButton.setText(QCoreApplication.translate("CustomerWindow", u"S\u1eeda", None))
        self.deleteButton.setText(QCoreApplication.translate("CustomerWindow", u"X\u00f3a", None))
        ___qtablewidgetitem = self.customerTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CustomerWindow", u"M\u00e3 KH", None));
        ___qtablewidgetitem1 = self.customerTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CustomerWindow", u"H\u1ecd v\u00e0 t\u00ean", None));
        ___qtablewidgetitem2 = self.customerTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("CustomerWindow", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None));
        ___qtablewidgetitem3 = self.customerTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("CustomerWindow", u"Email", None));
        ___qtablewidgetitem4 = self.customerTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("CustomerWindow", u"\u0110\u1ecba ch\u1ec9", None));
        ___qtablewidgetitem5 = self.customerTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("CustomerWindow", u"\u1ea2nh", None));
        ___qtablewidgetitem6 = self.customerTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("CustomerWindow", u"Ng\u00e0y \u0111\u0103ng k\u00fd", None));
    # retranslateUi

