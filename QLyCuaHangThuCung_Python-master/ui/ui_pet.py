# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pet.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_PetWindow(object):
    def setupUi(self, PetWindow):
        if not PetWindow.objectName():
            PetWindow.setObjectName(u"PetWindow")
        PetWindow.resize(1000, 800)
        PetWindow.setStyleSheet(u"\n"
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
"    \n"
"    QPushButton#btnNavPets {\n"
"        background-color: #4a90e2;\n"
"    }\n"
"    \n"
"    "
                        "QPushButton#btnNavProducts {\n"
"        background-color: #17a2b8;\n"
"    }\n"
"    \n"
"    QPushButton#btnAdd {\n"
"        background-color: #a0c9c3;\n"
"    }\n"
"	 QPushButton#btnAdd:hover {\n"
"        background-color: #657d81;\n"
"    }\n"
"\n"
"    QPushButton#btnExcel {\n"
"        background-color: #8ec9b6;\n"
"    }\n"
"	 QPushButton#btnExcel:hover {\n"
"        background-color: #657d81;\n"
"    }\n"
"    \n"
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
"        border-radiu"
                        "s: 6px;\n"
"        gridline-color: #f0f0f0;\n"
"    }\n"
"    \n"
"    QTableWidget::item {\n"
"        padding: 8px;\n"
"    }\n"
"    \n"
"    QHeaderView::section {\n"
"        background-color: #f8f9fa;\n"
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
        self.centralwidget = QWidget(PetWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.petPage = QWidget()
        self.petPage.setObjectName(u"petPage")
        self.petPageMainLayout = QVBoxLayout(self.petPage)
        self.petPageMainLayout.setObjectName(u"petPageMainLayout")
        self.petContentLayout = QHBoxLayout()
        self.petContentLayout.setObjectName(u"petContentLayout")
        self.petFormContainer = QVBoxLayout()
        self.petFormContainer.setObjectName(u"petFormContainer")
        self.petFormLayout = QFormLayout()
        self.petFormLayout.setObjectName(u"petFormLayout")
        self.labelMaThuCung = QLabel(self.petPage)
        self.labelMaThuCung.setObjectName(u"labelMaThuCung")

        self.petFormLayout.setWidget(0, QFormLayout.LabelRole, self.labelMaThuCung)

        self.lineEditMaThuCung = QLineEdit(self.petPage)
        self.lineEditMaThuCung.setObjectName(u"lineEditMaThuCung")
        self.lineEditMaThuCung.setEnabled(False)

        self.petFormLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditMaThuCung)

        self.labelTenThuCung = QLabel(self.petPage)
        self.labelTenThuCung.setObjectName(u"labelTenThuCung")

        self.petFormLayout.setWidget(1, QFormLayout.LabelRole, self.labelTenThuCung)

        self.lineEditTenThuCung = QLineEdit(self.petPage)
        self.lineEditTenThuCung.setObjectName(u"lineEditTenThuCung")

        self.petFormLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditTenThuCung)

        self.labelLoai = QLabel(self.petPage)
        self.labelLoai.setObjectName(u"labelLoai")

        self.petFormLayout.setWidget(2, QFormLayout.LabelRole, self.labelLoai)

        self.comboBoxLoai = QComboBox(self.petPage)
        self.comboBoxLoai.addItem("")
        self.comboBoxLoai.addItem("")
        self.comboBoxLoai.addItem("")
        self.comboBoxLoai.setObjectName(u"comboBoxLoai")

        self.petFormLayout.setWidget(2, QFormLayout.FieldRole, self.comboBoxLoai)

        self.labelGioiTinh = QLabel(self.petPage)
        self.labelGioiTinh.setObjectName(u"labelGioiTinh")

        self.petFormLayout.setWidget(3, QFormLayout.LabelRole, self.labelGioiTinh)

        self.comboBoxGioiTinh = QComboBox(self.petPage)
        self.comboBoxGioiTinh.addItem("")
        self.comboBoxGioiTinh.addItem("")
        self.comboBoxGioiTinh.setObjectName(u"comboBoxGioiTinh")

        self.petFormLayout.setWidget(3, QFormLayout.FieldRole, self.comboBoxGioiTinh)

        self.labelNgaySinh = QLabel(self.petPage)
        self.labelNgaySinh.setObjectName(u"labelNgaySinh")

        self.petFormLayout.setWidget(4, QFormLayout.LabelRole, self.labelNgaySinh)

        self.dateEditNgaySinh = QDateEdit(self.petPage)
        self.dateEditNgaySinh.setObjectName(u"dateEditNgaySinh")
        self.dateEditNgaySinh.setCalendarPopup(True)

        self.petFormLayout.setWidget(4, QFormLayout.FieldRole, self.dateEditNgaySinh)

        self.labelGiaBan = QLabel(self.petPage)
        self.labelGiaBan.setObjectName(u"labelGiaBan")

        self.petFormLayout.setWidget(5, QFormLayout.LabelRole, self.labelGiaBan)

        self.lineEditGiaBan = QLineEdit(self.petPage)
        self.lineEditGiaBan.setObjectName(u"lineEditGiaBan")

        self.petFormLayout.setWidget(5, QFormLayout.FieldRole, self.lineEditGiaBan)

        self.labelTinhTrang = QLabel(self.petPage)
        self.labelTinhTrang.setObjectName(u"labelTinhTrang")

        self.petFormLayout.setWidget(6, QFormLayout.LabelRole, self.labelTinhTrang)

        self.lineEditTinhTrang = QLineEdit(self.petPage)
        self.lineEditTinhTrang.setObjectName(u"lineEditTinhTrang")

        self.petFormLayout.setWidget(6, QFormLayout.FieldRole, self.lineEditTinhTrang)

        self.labelMoTa = QLabel(self.petPage)
        self.labelMoTa.setObjectName(u"labelMoTa")

        self.petFormLayout.setWidget(7, QFormLayout.LabelRole, self.labelMoTa)

        self.textEditMoTa = QTextEdit(self.petPage)
        self.textEditMoTa.setObjectName(u"textEditMoTa")

        self.petFormLayout.setWidget(7, QFormLayout.FieldRole, self.textEditMoTa)


        self.petFormContainer.addLayout(self.petFormLayout)


        self.petContentLayout.addLayout(self.petFormContainer)

        self.imageContainer = QVBoxLayout()
        self.imageContainer.setObjectName(u"imageContainer")
        self.imagePreview = QLabel(self.petPage)
        self.imagePreview.setObjectName(u"imagePreview")
        self.imagePreview.setMinimumSize(QSize(200, 200))
        self.imagePreview.setMaximumSize(QSize(200, 200))
        self.imagePreview.setFrameShape(QFrame.Box)
        self.imagePreview.setScaledContents(True)
        self.imagePreview.setAlignment(Qt.AlignCenter)

        self.imageContainer.addWidget(self.imagePreview)

        self.imgpathButton = QPushButton(self.petPage)
        self.imgpathButton.setObjectName(u"imgpathButton")

        self.imageContainer.addWidget(self.imgpathButton)


        self.petContentLayout.addLayout(self.imageContainer)


        self.petPageMainLayout.addLayout(self.petContentLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnAdd = QPushButton(self.petPage)
        self.btnAdd.setObjectName(u"btnAdd")

        self.buttonLayout.addWidget(self.btnAdd)

        self.btnExcel = QPushButton(self.petPage)
        self.btnExcel.setObjectName(u"btnExcel")

        self.buttonLayout.addWidget(self.btnExcel)

        self.btnEdit = QPushButton(self.petPage)
        self.btnEdit.setObjectName(u"btnEdit")

        self.buttonLayout.addWidget(self.btnEdit)

        self.btnDelete = QPushButton(self.petPage)
        self.btnDelete.setObjectName(u"btnDelete")

        self.buttonLayout.addWidget(self.btnDelete)


        self.petPageMainLayout.addLayout(self.buttonLayout)

        self.tablePets = QTableWidget(self.petPage)
        if (self.tablePets.columnCount() < 9):
            self.tablePets.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablePets.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablePets.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablePets.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablePets.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablePets.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablePets.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablePets.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablePets.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tablePets.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tablePets.setObjectName(u"tablePets")
        self.tablePets.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tablePets.horizontalHeader().setStretchLastSection(True)

        self.petPageMainLayout.addWidget(self.tablePets)

        self.stackedWidget.addWidget(self.petPage)
        self.productPage = QWidget()
        self.productPage.setObjectName(u"productPage")
        self.productLayout = QVBoxLayout(self.productPage)
        self.productLayout.setObjectName(u"productLayout")
        self.filterLayout = QHBoxLayout()
        self.filterLayout.setObjectName(u"filterLayout")
        self.labelSort = QLabel(self.productPage)
        self.labelSort.setObjectName(u"labelSort")

        self.filterLayout.addWidget(self.labelSort)

        self.comboSort = QComboBox(self.productPage)
        self.comboSort.addItem("")
        self.comboSort.addItem("")
        self.comboSort.addItem("")
        self.comboSort.addItem("")
        self.comboSort.setObjectName(u"comboSort")

        self.filterLayout.addWidget(self.comboSort)


        self.productLayout.addLayout(self.filterLayout)

        self.scrollArea = QScrollArea(self.productPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 962, 706))
        self.productGrid = QGridLayout(self.scrollAreaWidgetContents)
        self.productGrid.setSpacing(20)
        self.productGrid.setObjectName(u"productGrid")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.productLayout.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.productPage)

        self.verticalLayout.addWidget(self.stackedWidget)

        PetWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PetWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(PetWindow)
    # setupUi

    def retranslateUi(self, PetWindow):
        PetWindow.setWindowTitle(QCoreApplication.translate("PetWindow", u"Pet Shop Management", None))
        self.labelMaThuCung.setText(QCoreApplication.translate("PetWindow", u"M\u00e3 th\u00fa c\u01b0ng:", None))
        self.lineEditMaThuCung.setPlaceholderText(QCoreApplication.translate("PetWindow", u"T\u1ef1 \u0111\u1ed9ng t\u1ea1o", None))
        self.labelTenThuCung.setText(QCoreApplication.translate("PetWindow", u"T\u00ean th\u00fa c\u01b0ng:", None))
        self.lineEditTenThuCung.setPlaceholderText(QCoreApplication.translate("PetWindow", u"Nh\u1eadp t\u00ean th\u00fa c\u01b0ng", None))
        self.labelLoai.setText(QCoreApplication.translate("PetWindow", u"Lo\u1ea1i:", None))
        self.comboBoxLoai.setItemText(0, QCoreApplication.translate("PetWindow", u"Ch\u00f3", None))
        self.comboBoxLoai.setItemText(1, QCoreApplication.translate("PetWindow", u"M\u00e8o", None))
        self.comboBoxLoai.setItemText(2, QCoreApplication.translate("PetWindow", u"Hamster", None))

        self.labelGioiTinh.setText(QCoreApplication.translate("PetWindow", u"Gi\u1edbi t\u00ednh:", None))
        self.comboBoxGioiTinh.setItemText(0, QCoreApplication.translate("PetWindow", u"\u0110\u1ef1c", None))
        self.comboBoxGioiTinh.setItemText(1, QCoreApplication.translate("PetWindow", u"C\u00e1i", None))

        self.labelNgaySinh.setText(QCoreApplication.translate("PetWindow", u"Ng\u00e0y sinh:", None))
        self.labelGiaBan.setText(QCoreApplication.translate("PetWindow", u"Gi\u00e1 b\u00e1n:", None))
        self.lineEditGiaBan.setPlaceholderText(QCoreApplication.translate("PetWindow", u"Nh\u1eadp gi\u00e1 b\u00e1n", None))
        self.labelTinhTrang.setText(QCoreApplication.translate("PetWindow", u"T\u00ecnh tr\u1ea1ng:", None))
        self.lineEditTinhTrang.setPlaceholderText(QCoreApplication.translate("PetWindow", u"Nh\u1eadp t\u00ecnh tr\u1ea1ng s\u1ee9c kh\u1ecfe", None))
        self.labelMoTa.setText(QCoreApplication.translate("PetWindow", u"M\u00f4 t\u1ea3:", None))
        self.textEditMoTa.setPlaceholderText(QCoreApplication.translate("PetWindow", u"Nh\u1eadp m\u00f4 t\u1ea3 chi ti\u1ebft", None))
        self.imagePreview.setText(QCoreApplication.translate("PetWindow", u"H\u00ecnh \u1ea3nh", None))
        self.imgpathButton.setText(QCoreApplication.translate("PetWindow", u"Ch\u1ecdn \u1ea3nh", None))
        self.btnAdd.setText(QCoreApplication.translate("PetWindow", u"Th\u00eam", None))
        self.btnExcel.setText(QCoreApplication.translate("PetWindow", u"Excel", None))
        self.btnEdit.setText(QCoreApplication.translate("PetWindow", u"S\u1eeda", None))
        self.btnDelete.setText(QCoreApplication.translate("PetWindow", u"X\u00f3a", None))
        ___qtablewidgetitem = self.tablePets.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PetWindow", u"M\u00e3 th\u00fa c\u01b0ng", None));
        ___qtablewidgetitem1 = self.tablePets.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PetWindow", u"T\u00ean th\u00fa c\u01b0ng", None));
        ___qtablewidgetitem2 = self.tablePets.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PetWindow", u"Lo\u1ea1i", None));
        ___qtablewidgetitem3 = self.tablePets.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PetWindow", u"Gi\u1edbi t\u00ednh", None));
        ___qtablewidgetitem4 = self.tablePets.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PetWindow", u"Ng\u00e0y sinh", None));
        ___qtablewidgetitem5 = self.tablePets.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PetWindow", u"Gi\u00e1 b\u00e1n", None));
        ___qtablewidgetitem6 = self.tablePets.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("PetWindow", u"T\u00ecnh tr\u1ea1ng", None));
        ___qtablewidgetitem7 = self.tablePets.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("PetWindow", u"M\u00f4 t\u1ea3", None));
        ___qtablewidgetitem8 = self.tablePets.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("PetWindow", u"\u1ea2nh", None));
        self.labelSort.setText(QCoreApplication.translate("PetWindow", u"Sort by:", None))
        self.comboSort.setItemText(0, QCoreApplication.translate("PetWindow", u"All", None))
        self.comboSort.setItemText(1, QCoreApplication.translate("PetWindow", u"Ch\u00f3", None))
        self.comboSort.setItemText(2, QCoreApplication.translate("PetWindow", u"M\u00e8o", None))
        self.comboSort.setItemText(3, QCoreApplication.translate("PetWindow", u"Hamster", None))

    # retranslateUi

