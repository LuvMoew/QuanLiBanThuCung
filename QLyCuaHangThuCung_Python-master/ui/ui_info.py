# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 641)
        MainWindow.setStyleSheet(u"\n"
"    QMainWindow {\n"
"        background-color: #fef8ec;\n"
"    }\n"
"    \n"
"    QWidget#centralwidget {\n"
"        background-color: #fef8ec;\n"
"        border-radius: 8px;\n"
"        margin: 20px;\n"
"        padding: 20px;\n"
"    }\n"
"    \n"
"    QLabel#label_overview {\n"
"        font-family: Arial;\n"
"        font-size: 24px;\n"
"        font-weight: bold;\n"
"        color: #333333;\n"
"        padding: 10px 0;\n"
"        border-bottom: 2px solid #e0e0e0;\n"
"        margin-bottom: 20px;\n"
"    }\n"
"    \n"
"    QLabel#label_photo {\n"
"        background-color: #f8f9fa;\n"
"        border: 2px solid #e0e0e0;\n"
"        border-radius: 75px;\n"
"        padding: 5px;\n"
"    }\n"
"    \n"
"    QLineEdit {\n"
"        padding: 8px;\n"
"        border: 1px solid #e0e0e0;\n"
"        border-radius: 4px;\n"
"        background-color: #ffffff;\n"
"        font-size: 14px;\n"
"        min-height: 25px;\n"
"    }\n"
"    \n"
"    QLineEdit:focus {\n"
"        border: 2px solid #4a90e2;\n"
"  "
                        "      outline: none;\n"
"    }\n"
"    \n"
"    QLineEdit:hover {\n"
"        border: 1px solid #4a90e2;\n"
"    }\n"
"    \n"
"    QTextEdit {\n"
"        padding: 8px;\n"
"        border: 1px solid #e0e0e0;\n"
"        border-radius: 4px;\n"
"        background-color: #ffffff;\n"
"        font-size: 14px;\n"
"    }\n"
"    \n"
"    QTextEdit:focus {\n"
"        border: 2px solid #4a90e2;\n"
"        outline: none;\n"
"    }\n"
"    \n"
"    QDateEdit {\n"
"        padding: 8px;\n"
"        border: 1px solid #e0e0e0;\n"
"        border-radius: 4px;\n"
"        background-color: #ffffff;\n"
"        min-height: 25px;\n"
"    }\n"
"    \n"
"    QLabel {\n"
"        color: #333333;\n"
"        font-size: 14px;\n"
"        font-weight: 500;\n"
"    }\n"
"    \n"
"    QPushButton {\n"
"        background-color: #92b9e3;\n"
"        color: white;\n"
"        border: none;\n"
"        border-radius: 4px;\n"
"        padding: 8px 16px;\n"
"        font-size: 14px;\n"
"    }\n"
"    \n"
"    QPushButton:hover {\n"
"  "
                        "      background-color: #6c7ee1;\n"
"    }\n"
"   ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_overview = QLabel(self.centralwidget)
        self.label_overview.setObjectName(u"label_overview")

        self.verticalLayout.addWidget(self.label_overview)

        self.horizontalLayout_photo = QHBoxLayout()
        self.horizontalLayout_photo.setObjectName(u"horizontalLayout_photo")
        self.label_photo = QLabel(self.centralwidget)
        self.label_photo.setObjectName(u"label_photo")
        self.label_photo.setMinimumSize(QSize(150, 150))
        self.label_photo.setMaximumSize(QSize(150, 150))
        self.label_photo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_photo.addWidget(self.label_photo)

        self.pushButton_choosePhoto = QPushButton(self.centralwidget)
        self.pushButton_choosePhoto.setObjectName(u"pushButton_choosePhoto")
        self.pushButton_choosePhoto.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_photo.addWidget(self.pushButton_choosePhoto)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_photo.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_photo)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_hoTen = QLabel(self.centralwidget)
        self.label_hoTen.setObjectName(u"label_hoTen")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_hoTen)

        self.lineEdit_hoTen = QLineEdit(self.centralwidget)
        self.lineEdit_hoTen.setObjectName(u"lineEdit_hoTen")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_hoTen)

        self.label_sdt = QLabel(self.centralwidget)
        self.label_sdt.setObjectName(u"label_sdt")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_sdt)

        self.lineEdit_sdt = QLineEdit(self.centralwidget)
        self.lineEdit_sdt.setObjectName(u"lineEdit_sdt")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_sdt)

        self.label_email = QLabel(self.centralwidget)
        self.label_email.setObjectName(u"label_email")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_email)

        self.lineEdit_email = QLineEdit(self.centralwidget)
        self.lineEdit_email.setObjectName(u"lineEdit_email")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_email)

        self.label_diaChi = QLabel(self.centralwidget)
        self.label_diaChi.setObjectName(u"label_diaChi")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_diaChi)

        self.textEdit_diaChi = QTextEdit(self.centralwidget)
        self.textEdit_diaChi.setObjectName(u"textEdit_diaChi")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.textEdit_diaChi)

        self.label_ngayDangKy = QLabel(self.centralwidget)
        self.label_ngayDangKy.setObjectName(u"label_ngayDangKy")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_ngayDangKy)

        self.dateEdit_ngayDangKy = QDateEdit(self.centralwidget)
        self.dateEdit_ngayDangKy.setObjectName(u"dateEdit_ngayDangKy")
        self.dateEdit_ngayDangKy.setCalendarPopup(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.dateEdit_ngayDangKy)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_buttons = QHBoxLayout()
        self.horizontalLayout_buttons.setObjectName(u"horizontalLayout_buttons")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_buttons.addItem(self.horizontalSpacer)

        self.pushButton_save = QPushButton(self.centralwidget)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.horizontalLayout_buttons.addWidget(self.pushButton_save)

        self.pushButton_cancel = QPushButton(self.centralwidget)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_buttons.addWidget(self.pushButton_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_buttons)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Th\u00f4ng tin kh\u00e1ch h\u00e0ng", None))
        self.label_overview.setText(QCoreApplication.translate("MainWindow", u"Th\u00f4ng tin kh\u00e1ch h\u00e0ng", None))
        self.label_photo.setText(QCoreApplication.translate("MainWindow", u"\u1ea2nh", None))
        self.pushButton_choosePhoto.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn \u1ea3nh", None))
        self.label_hoTen.setText(QCoreApplication.translate("MainWindow", u"H\u1ecd t\u00ean: *", None))
        self.label_sdt.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i: *", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_diaChi.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ecba ch\u1ec9:", None))
        self.label_ngayDangKy.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y \u0111\u0103ng k\u00fd:", None))
        self.dateEdit_ngayDangKy.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"L\u01b0u", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("MainWindow", u"H\u1ee7y", None))
    # retranslateUi

