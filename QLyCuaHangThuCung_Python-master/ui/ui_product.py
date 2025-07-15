# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'product.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpinBox, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_ProductWindow(object):
    def setupUi(self, ProductWindow):
        if not ProductWindow.objectName():
            ProductWindow.setObjectName(u"ProductWindow")
        ProductWindow.resize(988, 800)
        ProductWindow.setStyleSheet(u"\n"
"    QMainWindow {\n"
"        background-color: #fef8ec;\n"
"    }\n"
"    \n"
"    QWidget {\n"
"        background-color: #fef8ec;\n"
"        font-family: Arial;\n"
"    }\n"
"    \n"
"    QLabel {\n"
"        color: #333333;\n"
"        font-size: 14px;\n"
"        padding: 5px 0;\n"
"    }\n"
"    \n"
"    QLineEdit, QComboBox, QDateEdit, QTextEdit {\n"
"        padding: 8px;\n"
"        border: 1px solid #e0e0e0;\n"
"        border-radius: 6px;\n"
"        background-color: #ffffff;\n"
"        min-height: 20px;\n"
"        margin: 5px 0;\n"
"    }\n"
"    \n"
"    QLineEdit:focus, QComboBox:focus, QDateEdit:focus, QTextEdit:focus {\n"
"        border: 2px solid #4a90e2;\n"
"    }\n"
"    \n"
"    QPushButton {\n"
"        padding: 10px 20px;\n"
"        border-radius: 6px;\n"
"        font-weight: bold;\n"
"        color: #333;\n"
"        min-width: 100px;\n"
"        margin: 5px;\n"
"    }\n"
"  \n"
"    QPushButton#btnAdd {\n"
"        background-color: #a0c9c3;\n"
"    }\n"
"	 QPushButton#btnAd"
                        "d:hover {\n"
"        background-color: #657d81;\n"
"    }\n"
"    \n"
"	QPushButton#excelButton {\n"
"        background-color: #8ec9b6;\n"
"    }\n"
"	 QPushButton#excelButton:hover {\n"
"        background-color: #657d81;\n"
"    }\n"
"\n"
"    QPushButton#btnEdit {\n"
"        background-color: #92b9e3;\n"
"    }\n"
"	QPushButton#btnEdit:hover {\n"
"        background-color: #6c7ee1;\n"
"    }\n"
"    \n"
"    QPushButton#btnDelete {\n"
"        background-color: #dc4048;\n"
"    }\n"
"    QPushButton#btnDelete:hover {\n"
"        background-color: #c73943;\n"
"    }\n"
"    \n"
"    QPushButton#imgpathButton {\n"
"        background-color: #6c757d;\n"
"    }\n"
"    \n"
"    QPushButton:hover {\n"
"        opacity: 0.9;\n"
"    }\n"
"    \n"
"    QTableWidget {\n"
"        border: 1px solid #e0e0e0;\n"
"        border-radius: 6px;\n"
"        gridline-color: #f0f0f0;\n"
"    }\n"
"    \n"
"    QTableWidget::item {\n"
"        padding: 8px;\n"
"    }\n"
"    \n"
"    QHeaderView::section {\n"
"        back"
                        "ground-color: #f8f9fa;\n"
"        padding: 8px;\n"
"        border: none;\n"
"        font-weight: bold;\n"
"    }\n"
"    \n"
"    #imagePreview {\n"
"        background-color: white;\n"
"        border: 2px dashed #cccccc;\n"
"        border-radius: 8px;\n"
"        padding: 10px;\n"
"    }\n"
"    \n"
"    .ProductCard {\n"
"        background: #f8f9fa;\n"
"        border-radius: 8px;\n"
"        padding: 15px;\n"
"        margin: 10px;\n"
"    }\n"
"   ")
        self.centralwidget = QWidget(ProductWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.productPage = QWidget()
        self.productPage.setObjectName(u"productPage")
        self.productPageMainLayout = QVBoxLayout(self.productPage)
        self.productPageMainLayout.setObjectName(u"productPageMainLayout")
        self.productContentLayout = QHBoxLayout()
        self.productContentLayout.setObjectName(u"productContentLayout")
        self.productFormContainer = QVBoxLayout()
        self.productFormContainer.setObjectName(u"productFormContainer")
        self.productFormLayout = QFormLayout()
        self.productFormLayout.setObjectName(u"productFormLayout")
        self.labelMaSP = QLabel(self.productPage)
        self.labelMaSP.setObjectName(u"labelMaSP")

        self.productFormLayout.setWidget(0, QFormLayout.LabelRole, self.labelMaSP)

        self.lineEditMaSP = QLineEdit(self.productPage)
        self.lineEditMaSP.setObjectName(u"lineEditMaSP")
        self.lineEditMaSP.setEnabled(False)

        self.productFormLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditMaSP)

        self.labelTenSP = QLabel(self.productPage)
        self.labelTenSP.setObjectName(u"labelTenSP")

        self.productFormLayout.setWidget(1, QFormLayout.LabelRole, self.labelTenSP)

        self.lineEditTenSP = QLineEdit(self.productPage)
        self.lineEditTenSP.setObjectName(u"lineEditTenSP")

        self.productFormLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditTenSP)

        self.labelLoaiSP = QLabel(self.productPage)
        self.labelLoaiSP.setObjectName(u"labelLoaiSP")

        self.productFormLayout.setWidget(2, QFormLayout.LabelRole, self.labelLoaiSP)

        self.comboBoxLoaiSP = QComboBox(self.productPage)
        self.comboBoxLoaiSP.addItem("")
        self.comboBoxLoaiSP.addItem("")
        self.comboBoxLoaiSP.addItem("")
        self.comboBoxLoaiSP.setObjectName(u"comboBoxLoaiSP")

        self.productFormLayout.setWidget(2, QFormLayout.FieldRole, self.comboBoxLoaiSP)

        self.labelGia = QLabel(self.productPage)
        self.labelGia.setObjectName(u"labelGia")

        self.productFormLayout.setWidget(3, QFormLayout.LabelRole, self.labelGia)

        self.lineEditGia = QLineEdit(self.productPage)
        self.lineEditGia.setObjectName(u"lineEditGia")

        self.productFormLayout.setWidget(3, QFormLayout.FieldRole, self.lineEditGia)

        self.labelSoLuongTon = QLabel(self.productPage)
        self.labelSoLuongTon.setObjectName(u"labelSoLuongTon")

        self.productFormLayout.setWidget(4, QFormLayout.LabelRole, self.labelSoLuongTon)

        self.spinBoxSoLuongTon = QSpinBox(self.productPage)
        self.spinBoxSoLuongTon.setObjectName(u"spinBoxSoLuongTon")
        self.spinBoxSoLuongTon.setMinimum(0)
        self.spinBoxSoLuongTon.setMaximum(9999)

        self.productFormLayout.setWidget(4, QFormLayout.FieldRole, self.spinBoxSoLuongTon)

        self.labelMoTa = QLabel(self.productPage)
        self.labelMoTa.setObjectName(u"labelMoTa")

        self.productFormLayout.setWidget(5, QFormLayout.LabelRole, self.labelMoTa)

        self.textEditMoTa = QTextEdit(self.productPage)
        self.textEditMoTa.setObjectName(u"textEditMoTa")

        self.productFormLayout.setWidget(5, QFormLayout.FieldRole, self.textEditMoTa)


        self.productFormContainer.addLayout(self.productFormLayout)


        self.productContentLayout.addLayout(self.productFormContainer)

        self.imageContainer = QVBoxLayout()
        self.imageContainer.setObjectName(u"imageContainer")
        self.imagePreview = QLabel(self.productPage)
        self.imagePreview.setObjectName(u"imagePreview")
        self.imagePreview.setMinimumSize(QSize(200, 200))
        self.imagePreview.setMaximumSize(QSize(200, 200))
        self.imagePreview.setFrameShape(QFrame.Box)
        self.imagePreview.setScaledContents(True)
        self.imagePreview.setAlignment(Qt.AlignCenter)

        self.imageContainer.addWidget(self.imagePreview)

        self.imgpathButton = QPushButton(self.productPage)
        self.imgpathButton.setObjectName(u"imgpathButton")

        self.imageContainer.addWidget(self.imgpathButton)


        self.productContentLayout.addLayout(self.imageContainer)


        self.productPageMainLayout.addLayout(self.productContentLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnAdd = QPushButton(self.productPage)
        self.btnAdd.setObjectName(u"btnAdd")

        self.buttonLayout.addWidget(self.btnAdd)

        self.excelButton = QPushButton(self.productPage)
        self.excelButton.setObjectName(u"excelButton")

        self.buttonLayout.addWidget(self.excelButton)

        self.btnEdit = QPushButton(self.productPage)
        self.btnEdit.setObjectName(u"btnEdit")

        self.buttonLayout.addWidget(self.btnEdit)

        self.btnDelete = QPushButton(self.productPage)
        self.btnDelete.setObjectName(u"btnDelete")

        self.buttonLayout.addWidget(self.btnDelete)


        self.productPageMainLayout.addLayout(self.buttonLayout)

        self.tableProducts = QTableWidget(self.productPage)
        if (self.tableProducts.columnCount() < 7):
            self.tableProducts.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableProducts.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableProducts.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableProducts.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableProducts.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableProducts.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableProducts.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableProducts.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableProducts.setObjectName(u"tableProducts")
        self.tableProducts.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableProducts.horizontalHeader().setStretchLastSection(True)

        self.productPageMainLayout.addWidget(self.tableProducts)

        self.stackedWidget.addWidget(self.productPage)
        self.productListPage = QWidget()
        self.productListPage.setObjectName(u"productListPage")
        self.productLayout = QVBoxLayout(self.productListPage)
        self.productLayout.setObjectName(u"productLayout")
        self.filterLayout = QHBoxLayout()
        self.filterLayout.setObjectName(u"filterLayout")
        self.labelSort = QLabel(self.productListPage)
        self.labelSort.setObjectName(u"labelSort")

        self.filterLayout.addWidget(self.labelSort)

        self.comboSort = QComboBox(self.productListPage)
        self.comboSort.addItem("")
        self.comboSort.addItem("")
        self.comboSort.addItem("")
        self.comboSort.addItem("")
        self.comboSort.setObjectName(u"comboSort")

        self.filterLayout.addWidget(self.comboSort)

        self.productLayout.addLayout(self.filterLayout)

        self.scrollArea = QScrollArea(self.productListPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 950, 706))
        self.productGrid = QGridLayout(self.scrollAreaWidgetContents)
        self.productGrid.setSpacing(20)
        self.productGrid.setObjectName(u"productGrid")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.productLayout.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.productListPage)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        ProductWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProductWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ProductWindow)
    # setupUi

    def retranslateUi(self, ProductWindow):
        ProductWindow.setWindowTitle(QCoreApplication.translate("ProductWindow", u"Product Management", None))
        self.labelMaSP.setText(QCoreApplication.translate("ProductWindow", u"M\u00e3 s\u1ea3n ph\u1ea9m:", None))
        self.lineEditMaSP.setPlaceholderText(QCoreApplication.translate("ProductWindow", u"T\u1ef1 \u0111\u1ed9ng t\u1ea1o", None))
        self.labelTenSP.setText(QCoreApplication.translate("ProductWindow", u"T\u00ean s\u1ea3n ph\u1ea9m:", None))
        self.lineEditTenSP.setPlaceholderText(QCoreApplication.translate("ProductWindow", u"Nh\u1eadp t\u00ean s\u1ea3n ph\u1ea9m", None))
        self.labelLoaiSP.setText(QCoreApplication.translate("ProductWindow", u"Lo\u1ea1i:", None))
        self.comboBoxLoaiSP.setItemText(0, QCoreApplication.translate("ProductWindow", u"Th\u1ee9c \u0103n", None))
        self.comboBoxLoaiSP.setItemText(1, QCoreApplication.translate("ProductWindow", u"Ph\u1ee5 ki\u1ec7n", None))
        self.comboBoxLoaiSP.setItemText(2, QCoreApplication.translate("ProductWindow", u"\u0110\u1ed3 ch\u01a1i", None))

        self.labelGia.setText(QCoreApplication.translate("ProductWindow", u"Gi\u00e1:", None))
        self.lineEditGia.setPlaceholderText(QCoreApplication.translate("ProductWindow", u"Nh\u1eadp gi\u00e1 s\u1ea3n ph\u1ea9m", None))
        self.labelSoLuongTon.setText(QCoreApplication.translate("ProductWindow", u"S\u1ed1 l\u01b0\u1ee3ng t\u1ed3n:", None))
        self.labelMoTa.setText(QCoreApplication.translate("ProductWindow", u"M\u00f4 t\u1ea3:", None))
        self.textEditMoTa.setPlaceholderText(QCoreApplication.translate("ProductWindow", u"Nh\u1eadp m\u00f4 t\u1ea3 chi ti\u1ebft", None))
        self.imagePreview.setText(QCoreApplication.translate("ProductWindow", u"H\u00ecnh \u1ea3nh", None))
        self.imgpathButton.setText(QCoreApplication.translate("ProductWindow", u"Ch\u1ecdn \u1ea3nh", None))
        self.btnAdd.setText(QCoreApplication.translate("ProductWindow", u"Th\u00eam", None))
        self.excelButton.setText(QCoreApplication.translate("ProductWindow", u"Excel", None))
        self.btnEdit.setText(QCoreApplication.translate("ProductWindow", u"S\u1eeda", None))
        self.btnDelete.setText(QCoreApplication.translate("ProductWindow", u"X\u00f3a", None))
        ___qtablewidgetitem = self.tableProducts.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ProductWindow", u"M\u00e3 SP", None));
        ___qtablewidgetitem1 = self.tableProducts.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ProductWindow", u"T\u00ean s\u1ea3n ph\u1ea9m", None));
        ___qtablewidgetitem2 = self.tableProducts.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ProductWindow", u"Lo\u1ea1i", None));
        ___qtablewidgetitem3 = self.tableProducts.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ProductWindow", u"Gi\u00e1", None));
        ___qtablewidgetitem4 = self.tableProducts.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ProductWindow", u"S\u1ed1 l\u01b0\u1ee3ng t\u1ed3n", None));
        ___qtablewidgetitem5 = self.tableProducts.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ProductWindow", u"M\u00f4 t\u1ea3", None));
        ___qtablewidgetitem6 = self.tableProducts.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ProductWindow", u"\u1ea2nh", None));
        self.labelSort.setText(QCoreApplication.translate("ProductWindow", u"Sort by:", None))
        self.comboSort.setItemText(0, QCoreApplication.translate("ProductWindow", u"All", None))
        self.comboSort.setItemText(1, QCoreApplication.translate("ProductWindow", u"Phụ kiện", None))
        self.comboSort.setItemText(2, QCoreApplication.translate("ProductWindow", u"Thức ăn", None))
        self.comboSort.setItemText(3, QCoreApplication.translate("ProductWindow", u"Đồ chơi", None))

    # retranslateUi

