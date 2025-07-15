# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_UserManagement(object):
    def setupUi(self, UserManagement):
        if not UserManagement.objectName():
            UserManagement.setObjectName(u"UserManagement")
        UserManagement.resize(1002, 667)
        UserManagement.setStyleSheet(u"QMainWindow {\n"
"	background-color: #fef8ec;\n"
"}\n"
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
"QPushButton#pushButtonAdd{\n"
"   background-color: #a0c9c3;\n"
"}\n"
"\n"
"QPushButton#pushButtonAdd:hover {\n"
"    background-color: #657d81;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#pushButtonEdit {\n"
"    background-color: #92b9e3;\n"
"}\n"
"\n"
"QPushButton#pushButtonEdit:hover {\n"
"    background-color: #6c7ee1;\n"
"	color: white;\n"
"}\n"
"QPushButton#pushButtonDelete {\n"
"    background-color: #e7473c;\n"
""
                        "}\n"
"\n"
"QPushButton#pushButtonDelete:hover {\n"
"    background-color: #ce3d35;\n"
"	color: white;\n"
"}")
        self.centralwidget = QWidget(UserManagement)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelEmail = QLabel(self.groupBox)
        self.labelEmail.setObjectName(u"labelEmail")

        self.gridLayout.addWidget(self.labelEmail, 2, 0, 1, 1)

        self.labelRole = QLabel(self.groupBox)
        self.labelRole.setObjectName(u"labelRole")

        self.gridLayout.addWidget(self.labelRole, 4, 0, 1, 1)

        self.lineEditPassword = QLineEdit(self.groupBox)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lineEditPassword, 3, 1, 1, 1)

        self.labelId = QLabel(self.groupBox)
        self.labelId.setObjectName(u"labelId")

        self.gridLayout.addWidget(self.labelId, 0, 0, 1, 1)

        self.labelName = QLabel(self.groupBox)
        self.labelName.setObjectName(u"labelName")

        self.gridLayout.addWidget(self.labelName, 1, 0, 1, 1)

        self.comboBoxRole = QComboBox(self.groupBox)
        self.comboBoxRole.addItem("")
        self.comboBoxRole.addItem("")
        self.comboBoxRole.setObjectName(u"comboBoxRole")

        self.gridLayout.addWidget(self.comboBoxRole, 4, 1, 1, 1)

        self.lineEditId = QLineEdit(self.groupBox)
        self.lineEditId.setObjectName(u"lineEditId")
        self.lineEditId.setEnabled(False)

        self.gridLayout.addWidget(self.lineEditId, 0, 1, 1, 1)

        self.lineEditEmail = QLineEdit(self.groupBox)
        self.lineEditEmail.setObjectName(u"lineEditEmail")

        self.gridLayout.addWidget(self.lineEditEmail, 2, 1, 1, 1)

        self.labelPassword = QLabel(self.groupBox)
        self.labelPassword.setObjectName(u"labelPassword")

        self.gridLayout.addWidget(self.labelPassword, 3, 0, 1, 1)

        self.lineEditName = QLineEdit(self.groupBox)
        self.lineEditName.setObjectName(u"lineEditName")

        self.gridLayout.addWidget(self.lineEditName, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonAdd = QPushButton(self.centralwidget)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")
        self.pushButtonAdd.setMinimumSize(QSize(0, 46))
        self.pushButtonAdd.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.pushButtonAdd)

        self.pushButtonEdit = QPushButton(self.centralwidget)
        self.pushButtonEdit.setObjectName(u"pushButtonEdit")
        self.pushButtonEdit.setMinimumSize(QSize(0, 46))
        self.pushButtonEdit.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.pushButtonEdit)

        self.pushButtonDelete = QPushButton(self.centralwidget)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")
        self.pushButtonDelete.setMinimumSize(QSize(0, 46))
        self.pushButtonDelete.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.pushButtonDelete)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tableWidget)

        UserManagement.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(UserManagement)
        self.statusbar.setObjectName(u"statusbar")
        UserManagement.setStatusBar(self.statusbar)

        self.retranslateUi(UserManagement)

        QMetaObject.connectSlotsByName(UserManagement)
    # setupUi

    def retranslateUi(self, UserManagement):
        UserManagement.setWindowTitle(QCoreApplication.translate("UserManagement", u"User Management", None))
        self.groupBox.setTitle(QCoreApplication.translate("UserManagement", u"User Information", None))
        self.labelEmail.setText(QCoreApplication.translate("UserManagement", u"Email:", None))
        self.labelRole.setText(QCoreApplication.translate("UserManagement", u"Role:", None))
        self.lineEditPassword.setPlaceholderText(QCoreApplication.translate("UserManagement", u"Nh\u1eadp m\u1eadt kh\u1ea9u", None))
        self.labelId.setText(QCoreApplication.translate("UserManagement", u"ID:", None))
        self.labelName.setText(QCoreApplication.translate("UserManagement", u"Name:", None))
        self.comboBoxRole.setItemText(0, QCoreApplication.translate("UserManagement", u"admin", None))
        self.comboBoxRole.setItemText(1, QCoreApplication.translate("UserManagement", u"customer", None))

        self.lineEditId.setPlaceholderText(QCoreApplication.translate("UserManagement", u"T\u1ef1 \u0111\u1ed9ng t\u1ea1o", None))
        self.lineEditEmail.setPlaceholderText(QCoreApplication.translate("UserManagement", u"Nh\u1eadp \u0111\u1ecba ch\u1ec9 email", None))
        self.labelPassword.setText(QCoreApplication.translate("UserManagement", u"Password:", None))
        self.lineEditName.setPlaceholderText(QCoreApplication.translate("UserManagement", u"Nh\u1eadp t\u00ean ng\u01b0\u1eddi d\u00f9ng", None))
        self.pushButtonAdd.setText(QCoreApplication.translate("UserManagement", u"Th\u00eam", None))
        self.pushButtonEdit.setText(QCoreApplication.translate("UserManagement", u"S\u1eeda", None))
        self.pushButtonDelete.setText(QCoreApplication.translate("UserManagement", u"X\u00f3a", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("UserManagement", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("UserManagement", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("UserManagement", u"Email", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("UserManagement", u"Pass", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("UserManagement", u"Role", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("UserManagement", u"Created At", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("UserManagement", u"Updated At", None));
    # retranslateUi

