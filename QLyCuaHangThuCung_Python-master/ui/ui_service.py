# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'service.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextEdit, QTimeEdit, QVBoxLayout,
    QWidget)

class Ui_ServiceWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #fef8ec;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 8pt;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QLineEdit, QTextEdit, QComboBox, QDateEdit, QTimeEdit, QSpinBox {\n"
"    padding: 8px;\n"
"    border: 2px solid #dfe6e9;\n"
"    border-radius: 6px;\n"
"    background-color: #ffffff;\n"
"    font-size: 13px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus, QComboBox:focus, QDateEdit:focus, QTimeEdit:focus {\n"
"    border: 2px solid #74b9ff;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 4px;\n"
"    padding: 8px 16px;\n"
"    font-weight: bold;\n"
"    color: #333;\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"QPushButton#btnThem, QPushButton#btnThemLichHen {\n"
"    background-color: #a0c9c3;\n"
"}\n"
"\n"
"QPushButton#btnThem:hover, QPushButton#btnThemLichHen:hover {\n"
"    background-color: #657d81;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#btnSua {\n"
"    background-color: #92b9e3;\n"
"}\n"
"\n"
"QPushButton#btnSua:hover {\n"
"    backgr"
                        "ound-color: #6c7ee1;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#btnXoa {\n"
"    background-color: #e7473c;\n"
"}\n"
"\n"
"QPushButton#btnXoa:hover {\n"
"    background-color: #ce3d35;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#btnExcel {\n"
"    background-color: #7fba92;\n"
"}\n"
"\n"
"QPushButton#btnExcel:hover {\n"
"    background-color: #689877;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#btnXoaLichHen {\n"
"    background-color: #e7473c;\n"
"}\n"
"\n"
"QPushButton#btnXoaLichHen:hover {\n"
"    background-color: #ce3d35;\n"
"	color: white;\n"
"}\n"
"QPushButton#btnQLyLichHen {\n"
"    background-color: #e2b4b7;\n"
"}\n"
"\n"
"QPushButton#btnQLyLichHen:hover {\n"
"    background-color: #bd637e;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#btnBack {\n"
"    background-color: #92b9e3;\n"
"}\n"
"\n"
"QPushButton#btnBack:hover {\n"
"    background-color: #6c7ee1;\n"
"	color: white;\n"
"}\n"
"\n"
"\n"
"QPushButton#btnDanhSachDV, QPushButton#btnQuanLyDV, QPushButton#btnDatLichHen {\n"
"    background-co"
                        "lor: #673AB7;\n"
"}\n"
"\n"
"QPushButton#btnDanhSachDV:hover, QPushButton#btnQuanLyDV:hover, QPushButton#btnDatLichHen:hover {\n"
"    background-color: #5e35b1;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    border: 1px solid #c0c0c0;\n"
"    border-radius: 4px;\n"
"    alternate-background-color: #f9f9f9;\n"
"    gridline-color: #dcdcdc;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #4c9ed9;\n"
"    color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #e0e0e0;\n"
"    padding: 4px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-right: 1px solid #c0c0c0;\n"
"    border-bottom: 1px solid #c0c0c0;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 1px solid #c0c0c0;\n"
"    border-radius: 4px;\n"
"    margin-top: 20px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 5px;\n"
"    color: #333333;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pageQuanLyDV = QWidget()
        self.pageQuanLyDV.setObjectName(u"pageQuanLyDV")
        self.verticalLayout_2 = QVBoxLayout(self.pageQuanLyDV)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBoxThongTinDV = QGroupBox(self.pageQuanLyDV)
        self.groupBoxThongTinDV.setObjectName(u"groupBoxThongTinDV")
        self.gridLayout = QGridLayout(self.groupBoxThongTinDV)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txtTenDV = QLineEdit(self.groupBoxThongTinDV)
        self.txtTenDV.setObjectName(u"txtTenDV")

        self.gridLayout.addWidget(self.txtTenDV, 1, 1, 1, 1)

        self.txtMoTa = QTextEdit(self.groupBoxThongTinDV)
        self.txtMoTa.setObjectName(u"txtMoTa")

        self.gridLayout.addWidget(self.txtMoTa, 3, 1, 1, 1)

        self.lblMaDV = QLabel(self.groupBoxThongTinDV)
        self.lblMaDV.setObjectName(u"lblMaDV")
        self.lblMaDV.setEnabled(True)
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        self.lblMaDV.setFont(font)

        self.gridLayout.addWidget(self.lblMaDV, 0, 0, 1, 1)

        self.txtMaDV = QLineEdit(self.groupBoxThongTinDV)
        self.txtMaDV.setObjectName(u"txtMaDV")
        self.txtMaDV.setReadOnly(True)

        self.gridLayout.addWidget(self.txtMaDV, 0, 1, 1, 1)

        self.lblMoTa = QLabel(self.groupBoxThongTinDV)
        self.lblMoTa.setObjectName(u"lblMoTa")
        self.lblMoTa.setFont(font)

        self.gridLayout.addWidget(self.lblMoTa, 3, 0, 1, 1)

        self.lblGia = QLabel(self.groupBoxThongTinDV)
        self.lblGia.setObjectName(u"lblGia")
        self.lblGia.setFont(font)

        self.gridLayout.addWidget(self.lblGia, 2, 0, 1, 1)

        self.lblTenDV = QLabel(self.groupBoxThongTinDV)
        self.lblTenDV.setObjectName(u"lblTenDV")
        self.lblTenDV.setFont(font)

        self.gridLayout.addWidget(self.lblTenDV, 1, 0, 1, 1)

        self.txtGia = QLineEdit(self.groupBoxThongTinDV)
        self.txtGia.setObjectName(u"txtGia")

        self.gridLayout.addWidget(self.txtGia, 2, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBoxThongTinDV)

        self.widgetButtons = QWidget(self.pageQuanLyDV)
        self.widgetButtons.setObjectName(u"widgetButtons")
        self.horizontalLayout_2 = QHBoxLayout(self.widgetButtons)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnThem = QPushButton(self.widgetButtons)
        self.btnThem.setObjectName(u"btnThem")

        self.horizontalLayout_2.addWidget(self.btnThem)

        self.btnExcel = QPushButton(self.widgetButtons)
        self.btnExcel.setObjectName(u"btnExcel")

        self.horizontalLayout_2.addWidget(self.btnExcel)

        self.btnSua = QPushButton(self.widgetButtons)
        self.btnSua.setObjectName(u"btnSua")

        self.horizontalLayout_2.addWidget(self.btnSua)

        self.btnXoa = QPushButton(self.widgetButtons)
        self.btnXoa.setObjectName(u"btnXoa")

        self.horizontalLayout_2.addWidget(self.btnXoa)

        self.btnQLyLichHen = QPushButton(self.widgetButtons)
        self.btnQLyLichHen.setObjectName(u"btnQLyLichHen")

        self.horizontalLayout_2.addWidget(self.btnQLyLichHen)


        self.verticalLayout_2.addWidget(self.widgetButtons)

        self.tblDichVuPage1 = QTableWidget(self.pageQuanLyDV)
        if (self.tblDichVuPage1.columnCount() < 4):
            self.tblDichVuPage1.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblDichVuPage1.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblDichVuPage1.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblDichVuPage1.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblDichVuPage1.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tblDichVuPage1.setObjectName(u"tblDichVuPage1")
        font1 = QFont()
        font1.setPointSize(8)
        self.tblDichVuPage1.setFont(font1)
        self.tblDichVuPage1.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tblDichVuPage1)

        self.stackedWidget.addWidget(self.pageQuanLyDV)
        self.pageDanhSachDV = QWidget()
        self.pageDanhSachDV.setObjectName(u"pageDanhSachDV")
        self.verticalLayout_3 = QVBoxLayout(self.pageDanhSachDV)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widgetTimKiem = QWidget(self.pageDanhSachDV)
        self.widgetTimKiem.setObjectName(u"widgetTimKiem")
        self.horizontalLayout_3 = QHBoxLayout(self.widgetTimKiem)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lblTimKiem = QLabel(self.widgetTimKiem)
        self.lblTimKiem.setObjectName(u"lblTimKiem")

        self.horizontalLayout_3.addWidget(self.lblTimKiem)

        self.txtTimKiem = QLineEdit(self.widgetTimKiem)
        self.txtTimKiem.setObjectName(u"txtTimKiem")

        self.horizontalLayout_3.addWidget(self.txtTimKiem)

        self.lblLocLoai = QLabel(self.widgetTimKiem)
        self.lblLocLoai.setObjectName(u"lblLocLoai")

        self.horizontalLayout_3.addWidget(self.lblLocLoai)

        self.cboLocLoai = QComboBox(self.widgetTimKiem)
        self.cboLocLoai.addItem("")
        self.cboLocLoai.addItem("")
        self.cboLocLoai.addItem("")
        self.cboLocLoai.addItem("")
        self.cboLocLoai.addItem("")
        self.cboLocLoai.setObjectName(u"cboLocLoai")

        self.horizontalLayout_3.addWidget(self.cboLocLoai)


        self.verticalLayout_3.addWidget(self.widgetTimKiem)

        self.tblDanhSachDV = QTableWidget(self.pageDanhSachDV)
        if (self.tblDanhSachDV.columnCount() < 6):
            self.tblDanhSachDV.setColumnCount(6)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblDanhSachDV.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblDanhSachDV.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblDanhSachDV.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblDanhSachDV.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tblDanhSachDV.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tblDanhSachDV.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        self.tblDanhSachDV.setObjectName(u"tblDanhSachDV")
        self.tblDanhSachDV.setAlternatingRowColors(True)
        self.tblDanhSachDV.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tblDanhSachDV.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.tblDanhSachDV)

        self.stackedWidget.addWidget(self.pageDanhSachDV)
        self.pageDatLichHen = QWidget()
        self.pageDatLichHen.setObjectName(u"pageDatLichHen")
        self.verticalLayout_5 = QVBoxLayout(self.pageDatLichHen)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBoxLichHen = QGroupBox(self.pageDatLichHen)
        self.groupBoxLichHen.setObjectName(u"groupBoxLichHen")
        self.gridLayout_2 = QGridLayout(self.groupBoxLichHen)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lblMaLichHen = QLabel(self.groupBoxLichHen)
        self.lblMaLichHen.setObjectName(u"lblMaLichHen")

        self.gridLayout_2.addWidget(self.lblMaLichHen, 0, 0, 1, 1)

        self.txtMaLichHen = QLineEdit(self.groupBoxLichHen)
        self.txtMaLichHen.setObjectName(u"txtMaLichHen")
        self.txtMaLichHen.setReadOnly(True)

        self.gridLayout_2.addWidget(self.txtMaLichHen, 0, 1, 1, 1)

        self.lblNgayHen = QLabel(self.groupBoxLichHen)
        self.lblNgayHen.setObjectName(u"lblNgayHen")

        self.gridLayout_2.addWidget(self.lblNgayHen, 0, 2, 1, 1)

        self.dateNgayHen = QDateEdit(self.groupBoxLichHen)
        self.dateNgayHen.setObjectName(u"dateNgayHen")
        self.dateNgayHen.setCalendarPopup(True)

        self.gridLayout_2.addWidget(self.dateNgayHen, 0, 3, 1, 1)

        self.lblMaKH = QLabel(self.groupBoxLichHen)
        self.lblMaKH.setObjectName(u"lblMaKH")

        self.gridLayout_2.addWidget(self.lblMaKH, 1, 0, 1, 1)

        self.cboKhachHang = QComboBox(self.groupBoxLichHen)
        self.cboKhachHang.setObjectName(u"cboKhachHang")

        self.gridLayout_2.addWidget(self.cboKhachHang, 1, 1, 1, 1)

        self.lblGioHen = QLabel(self.groupBoxLichHen)
        self.lblGioHen.setObjectName(u"lblGioHen")

        self.gridLayout_2.addWidget(self.lblGioHen, 1, 2, 1, 1)

        self.timeGioHen = QTimeEdit(self.groupBoxLichHen)
        self.timeGioHen.setObjectName(u"timeGioHen")

        self.gridLayout_2.addWidget(self.timeGioHen, 1, 3, 1, 1)

        self.lblMaNV = QLabel(self.groupBoxLichHen)
        self.lblMaNV.setObjectName(u"lblMaNV")

        self.gridLayout_2.addWidget(self.lblMaNV, 2, 0, 1, 1)

        self.cboNhanVien = QComboBox(self.groupBoxLichHen)
        self.cboNhanVien.setObjectName(u"cboNhanVien")

        self.gridLayout_2.addWidget(self.cboNhanVien, 2, 1, 1, 1)

        self.lblTrangThai = QLabel(self.groupBoxLichHen)
        self.lblTrangThai.setObjectName(u"lblTrangThai")

        self.gridLayout_2.addWidget(self.lblTrangThai, 2, 2, 1, 1)

        self.cboTrangThai = QComboBox(self.groupBoxLichHen)
        self.cboTrangThai.addItem("")
        self.cboTrangThai.addItem("")
        self.cboTrangThai.addItem("")
        self.cboTrangThai.setObjectName(u"cboTrangThai")

        self.gridLayout_2.addWidget(self.cboTrangThai, 2, 3, 1, 1)

        self.lblMaDV_LichHen = QLabel(self.groupBoxLichHen)
        self.lblMaDV_LichHen.setObjectName(u"lblMaDV_LichHen")

        self.gridLayout_2.addWidget(self.lblMaDV_LichHen, 3, 0, 1, 1)

        self.cboDichVu = QComboBox(self.groupBoxLichHen)
        self.cboDichVu.setObjectName(u"cboDichVu")

        self.gridLayout_2.addWidget(self.cboDichVu, 3, 1, 1, 1)

        self.lblGiaDV = QLabel(self.groupBoxLichHen)
        self.lblGiaDV.setObjectName(u"lblGiaDV")

        self.gridLayout_2.addWidget(self.lblGiaDV, 3, 2, 1, 1)

        self.txtGiaDV = QLineEdit(self.groupBoxLichHen)
        self.txtGiaDV.setObjectName(u"txtGiaDV")
        self.txtGiaDV.setReadOnly(True)

        self.gridLayout_2.addWidget(self.txtGiaDV, 3, 3, 1, 1)

        self.lblGhiChu = QLabel(self.groupBoxLichHen)
        self.lblGhiChu.setObjectName(u"lblGhiChu")

        self.gridLayout_2.addWidget(self.lblGhiChu, 4, 0, 1, 1)

        self.txtGhiChu = QTextEdit(self.groupBoxLichHen)
        self.txtGhiChu.setObjectName(u"txtGhiChu")

        self.gridLayout_2.addWidget(self.txtGhiChu, 4, 1, 1, 3)


        self.verticalLayout_5.addWidget(self.groupBoxLichHen)

        self.widgetButtonsLichHen = QWidget(self.pageDatLichHen)
        self.widgetButtonsLichHen.setObjectName(u"widgetButtonsLichHen")
        self.horizontalLayout_4 = QHBoxLayout(self.widgetButtonsLichHen)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnThemLichHen = QPushButton(self.widgetButtonsLichHen)
        self.btnThemLichHen.setObjectName(u"btnThemLichHen")

        self.horizontalLayout_4.addWidget(self.btnThemLichHen)

        self.btnXoaLichHen = QPushButton(self.widgetButtonsLichHen)
        self.btnXoaLichHen.setObjectName(u"btnXoaLichHen")

        self.horizontalLayout_4.addWidget(self.btnXoaLichHen)

        self.btnBack = QPushButton(self.widgetButtonsLichHen)
        self.btnBack.setObjectName(u"btnBack")

        self.horizontalLayout_4.addWidget(self.btnBack)


        self.verticalLayout_5.addWidget(self.widgetButtonsLichHen)

        self.tblLichHen = QTableWidget(self.pageDatLichHen)
        if (self.tblLichHen.columnCount() < 8):
            self.tblLichHen.setColumnCount(8)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tblLichHen.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tblLichHen.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tblLichHen.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tblLichHen.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tblLichHen.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tblLichHen.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tblLichHen.setHorizontalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tblLichHen.setHorizontalHeaderItem(7, __qtablewidgetitem17)
        self.tblLichHen.setObjectName(u"tblLichHen")
        self.tblLichHen.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_5.addWidget(self.tblLichHen)

        self.stackedWidget.addWidget(self.pageDatLichHen)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Qu\u1ea3n l\u00fd D\u1ecbch v\u1ee5", None))
        self.groupBoxThongTinDV.setTitle(QCoreApplication.translate("MainWindow", u"Qu\u1ea3n l\u00fd d\u1ecbch v\u1ee5", None))
        self.txtTenDV.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp t\u00ean d\u1ecbch v\u1ee5", None))
        self.txtMoTa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp m\u00f4 t\u1ea3 chi ti\u1ebft", None))
        self.lblMaDV.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 d\u1ecbch v\u1ee5:", None))
        self.txtMaDV.setPlaceholderText(QCoreApplication.translate("MainWindow", u"T\u1ef1 \u0111\u1ed9ng t\u1ea1o", None))
        self.lblMoTa.setText(QCoreApplication.translate("MainWindow", u"M\u00f4 t\u1ea3:", None))
        self.lblGia.setText(QCoreApplication.translate("MainWindow", u"Gi\u00e1:", None))
        self.lblTenDV.setText(QCoreApplication.translate("MainWindow", u"T\u00ean d\u1ecbch v\u1ee5:", None))
        self.txtGia.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp gi\u00e1 d\u1ecbch v\u1ee5", None))
        self.btnThem.setText(QCoreApplication.translate("MainWindow", u"Th\u00eam", None))
        self.btnExcel.setText(QCoreApplication.translate("MainWindow", u"Excel", None))
        self.btnSua.setText(QCoreApplication.translate("MainWindow", u"S\u1eeda", None))
        self.btnXoa.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a", None))
        self.btnQLyLichHen.setText(QCoreApplication.translate("MainWindow", u"L\u1ecbch h\u1eb9n d\u1ecbch v\u1ee5", None))
        ___qtablewidgetitem = self.tblDichVuPage1.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 DV", None));
        ___qtablewidgetitem1 = self.tblDichVuPage1.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"T\u00ean d\u1ecbch v\u1ee5", None));
        ___qtablewidgetitem2 = self.tblDichVuPage1.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Gi\u00e1", None));
        ___qtablewidgetitem3 = self.tblDichVuPage1.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"M\u00f4 t\u1ea3", None));
        self.lblTimKiem.setText(QCoreApplication.translate("MainWindow", u"T\u00ecm ki\u1ebfm:", None))
        self.txtTimKiem.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp t\u1eeb kh\u00f3a t\u00ecm ki\u1ebfm", None))
        self.lblLocLoai.setText(QCoreApplication.translate("MainWindow", u"L\u1ecdc theo gi\u00e1:", None))
        self.cboLocLoai.setItemText(0, QCoreApplication.translate("MainWindow", u"T\u1ea5t c\u1ea3", None))
        self.cboLocLoai.setItemText(1, QCoreApplication.translate("MainWindow", u"D\u01b0\u1edbi 100k", None))
        self.cboLocLoai.setItemText(2, QCoreApplication.translate("MainWindow", u"T\u1eeb 100k - 300k", None))
        self.cboLocLoai.setItemText(3, QCoreApplication.translate("MainWindow", u"T\u1eeb 300k - 500k", None))
        self.cboLocLoai.setItemText(4, QCoreApplication.translate("MainWindow", u"Tr\u00ean 500k", None))

        ___qtablewidgetitem4 = self.tblDanhSachDV.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 DV", None));
        ___qtablewidgetitem5 = self.tblDanhSachDV.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"T\u00ean d\u1ecbch v\u1ee5", None));
        ___qtablewidgetitem6 = self.tblDanhSachDV.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Lo\u1ea1i", None));
        ___qtablewidgetitem7 = self.tblDanhSachDV.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Gi\u00e1", None));
        ___qtablewidgetitem8 = self.tblDanhSachDV.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"M\u00f4 t\u1ea3", None));
        ___qtablewidgetitem9 = self.tblDanhSachDV.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Thao t\u00e1c", None));
        self.groupBoxLichHen.setTitle(QCoreApplication.translate("MainWindow", u"Th\u00f4ng tin l\u1ecbch h\u1eb9n d\u1ecbch v\u1ee5", None))
        self.lblMaLichHen.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 l\u1ecbch h\u1eb9n:", None))
        self.txtMaLichHen.setPlaceholderText(QCoreApplication.translate("MainWindow", u"T\u1ef1 \u0111\u1ed9ng t\u1ea1o", None))
        self.lblNgayHen.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y h\u1eb9n:", None))
        self.lblMaKH.setText(QCoreApplication.translate("MainWindow", u"Kh\u00e1ch h\u00e0ng:", None))
        self.lblGioHen.setText(QCoreApplication.translate("MainWindow", u"Gi\u1edd h\u1eb9n:", None))
        self.timeGioHen.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm", None))
        self.lblMaNV.setText(QCoreApplication.translate("MainWindow", u"Nh\u00e2n vi\u00ean:", None))
        self.lblTrangThai.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ea1ng th\u00e1i:", None))
        self.cboTrangThai.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0110\u00e3 \u0111\u1eb7t", None))
        self.cboTrangThai.setItemText(1, QCoreApplication.translate("MainWindow", u"Ho\u00e0n th\u00e0nh", None))
        self.cboTrangThai.setItemText(2, QCoreApplication.translate("MainWindow", u"H\u1ee7y", None))

        self.lblMaDV_LichHen.setText(QCoreApplication.translate("MainWindow", u"D\u1ecbch v\u1ee5:", None))
        self.lblGiaDV.setText(QCoreApplication.translate("MainWindow", u"Gi\u00e1 d\u1ecbch v\u1ee5:", None))
        self.lblGhiChu.setText(QCoreApplication.translate("MainWindow", u"Ghi ch\u00fa:", None))
        self.txtGhiChu.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp ghi ch\u00fa n\u1ebfu c\u00f3", None))
        self.btnThemLichHen.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1eb7t l\u1ecbch h\u1eb9n", None))
        self.btnXoaLichHen.setText(QCoreApplication.translate("MainWindow", u"H\u1ee7y l\u1ecbch h\u1eb9n", None))
        self.btnBack.setText(QCoreApplication.translate("MainWindow", u"Quay l\u1ea1i", None))
        ___qtablewidgetitem10 = self.tblLichHen.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 l\u1ecbch h\u1eb9n", None));
        ___qtablewidgetitem11 = self.tblLichHen.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Kh\u00e1ch h\u00e0ng", None));
        ___qtablewidgetitem12 = self.tblLichHen.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Nh\u00e2n vi\u00ean", None));
        ___qtablewidgetitem13 = self.tblLichHen.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"D\u1ecbch v\u1ee5", None));
        ___qtablewidgetitem14 = self.tblLichHen.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y h\u1eb9n", None));
        ___qtablewidgetitem15 = self.tblLichHen.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Gi\u1edd h\u1eb9n", None));
        ___qtablewidgetitem16 = self.tblLichHen.horizontalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ea1ng th\u00e1i", None));
        ___qtablewidgetitem17 = self.tblLichHen.horizontalHeaderItem(7)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Ghi ch\u00fa", None));
    # retranslateUi

