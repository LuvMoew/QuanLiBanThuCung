# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employee.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_EmployeeWindow(object):
    def setupUi(self, EmployeeWindow):
        if not EmployeeWindow.objectName():
            EmployeeWindow.setObjectName(u"EmployeeWindow")
        EmployeeWindow.resize(1000, 700)
        EmployeeWindow.setStyleSheet(u"\n"
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
"		background-color: white;\n"
"    }\n"
"    QLineEdit {\n"
"        padding: 8px;\n"
"        border: 2px solid #dfe6e9;\n"
"        border-radius: 6px;\n"
"        background-color: #ffffff;\n"
"        font-size: 13px;\n"
"        min-height: 20px;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        border: 2px solid #74b9ff;\n"
"    }\n"
"    QComboBox {\n"
"        padding: 8px;\n"
"        border: 2px solid #dfe6e9;\n"
"        border-ra"
                        "dius: 6px;\n"
"        background-color: #ffffff;\n"
"        min-height: 20px;\n"
"    }\n"
"    QComboBox:drop-down {\n"
"        border: none;\n"
"        padding: 0 5px;\n"
"    }\n"
"    QPushButton {\n"
"        padding: 8px 15px;\n"
"        border-radius: 6px;\n"
"        font-size: 13px;\n"
"        font-weight: bold;\n"
"        min-width: 80px;\n"
"		 color: #333;\n"
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
"        background-"
                        "color: #dc4355;\n"
"    }\n"
"	QPushButton#imgpathButton {\n"
"        background-color: #d9adb0;\n"
"        color: #333;\n"
"        border: none;\n"
"    }\n"
"    QPushButton#imgpathButton:hover {\n"
"        background-color: #cc999e;\n"
"    }\n"
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
        self.centralWidget = QWidget(EmployeeWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.employeeInfoGroup = QGroupBox(self.centralWidget)
        self.employeeInfoGroup.setObjectName(u"employeeInfoGroup")
        self.horizontalLayout = QHBoxLayout(self.employeeInfoGroup)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 9, -1, -1)
        self.formLayout = QGridLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.idLabel = QLabel(self.employeeInfoGroup)
        self.idLabel.setObjectName(u"idLabel")

        self.formLayout.addWidget(self.idLabel, 0, 0, 1, 1)

        self.idInput = QLineEdit(self.employeeInfoGroup)
        self.idInput.setObjectName(u"idInput")
        self.idInput.setEnabled(False)

        self.formLayout.addWidget(self.idInput, 0, 1, 1, 1)

        self.nameLabel = QLabel(self.employeeInfoGroup)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.addWidget(self.nameLabel, 1, 0, 1, 1)

        self.nameInput = QLineEdit(self.employeeInfoGroup)
        self.nameInput.setObjectName(u"nameInput")

        self.formLayout.addWidget(self.nameInput, 1, 1, 1, 1)

        self.phoneLabel = QLabel(self.employeeInfoGroup)
        self.phoneLabel.setObjectName(u"phoneLabel")

        self.formLayout.addWidget(self.phoneLabel, 2, 0, 1, 1)

        self.phoneInput = QLineEdit(self.employeeInfoGroup)
        self.phoneInput.setObjectName(u"phoneInput")

        self.formLayout.addWidget(self.phoneInput, 2, 1, 1, 1)

        self.emailLabel = QLabel(self.employeeInfoGroup)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout.addWidget(self.emailLabel, 3, 0, 1, 1)

        self.emailInput = QLineEdit(self.employeeInfoGroup)
        self.emailInput.setObjectName(u"emailInput")

        self.formLayout.addWidget(self.emailInput, 3, 1, 1, 1)

        self.positionLabel = QLabel(self.employeeInfoGroup)
        self.positionLabel.setObjectName(u"positionLabel")

        self.formLayout.addWidget(self.positionLabel, 4, 0, 1, 1)

        self.positionCombo = QComboBox(self.employeeInfoGroup)
        self.positionCombo.addItem("")
        self.positionCombo.addItem("")
        self.positionCombo.addItem("")
        self.positionCombo.setObjectName(u"positionCombo")

        self.formLayout.addWidget(self.positionCombo, 4, 1, 1, 1)

        self.salaryLabel = QLabel(self.employeeInfoGroup)
        self.salaryLabel.setObjectName(u"salaryLabel")

        self.formLayout.addWidget(self.salaryLabel, 5, 0, 1, 1)

        self.salaryInput = QLineEdit(self.employeeInfoGroup)
        self.salaryInput.setObjectName(u"salaryInput")

        self.formLayout.addWidget(self.salaryInput, 5, 1, 1, 1)

        self.startDateLabel = QLabel(self.employeeInfoGroup)
        self.startDateLabel.setObjectName(u"startDateLabel")

        self.formLayout.addWidget(self.startDateLabel, 6, 0, 1, 1)

        self.startDateEdit = QDateEdit(self.employeeInfoGroup)
        self.startDateEdit.setObjectName(u"startDateEdit")
        self.startDateEdit.setCalendarPopup(True)

        self.formLayout.addWidget(self.startDateEdit, 6, 1, 1, 1)


        self.horizontalLayout.addLayout(self.formLayout)

        self.photoLabel = QLabel(self.employeeInfoGroup)
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


        self.verticalLayout.addWidget(self.employeeInfoGroup)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer)

        self.imgpathButton = QPushButton(self.centralWidget)
        self.imgpathButton.setObjectName(u"imgpathButton")

        self.buttonLayout.addWidget(self.imgpathButton)

        self.addButton = QPushButton(self.centralWidget)
        self.addButton.setObjectName(u"addButton")

        self.buttonLayout.addWidget(self.addButton)
        
        self.excelButton = QPushButton(self.centralWidget)
        self.excelButton.setObjectName(u"excelButton")

        self.buttonLayout.addWidget(self.excelButton)

        self.fixButton = QPushButton(self.centralWidget)
        self.fixButton.setObjectName(u"fixButton")

        self.buttonLayout.addWidget(self.fixButton)

        self.deleteButton = QPushButton(self.centralWidget)
        self.deleteButton.setObjectName(u"deleteButton")

        self.buttonLayout.addWidget(self.deleteButton)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.employeeTable = QTableWidget(self.centralWidget)
        if (self.employeeTable.columnCount() < 8):
            self.employeeTable.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.employeeTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.employeeTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.employeeTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.employeeTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.employeeTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.employeeTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.employeeTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.employeeTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.employeeTable.setObjectName(u"employeeTable")
        self.employeeTable.horizontalHeader().setDefaultSectionSize(110)
        self.employeeTable.horizontalHeader().setStretchLastSection(True)
        self.employeeTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.employeeTable)

        EmployeeWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(EmployeeWindow)

        QMetaObject.connectSlotsByName(EmployeeWindow)
    # setupUi

    def retranslateUi(self, EmployeeWindow):
        EmployeeWindow.setWindowTitle(QCoreApplication.translate("EmployeeWindow", u"Employee Management System", None))
        self.employeeInfoGroup.setTitle("")
        self.idLabel.setText(QCoreApplication.translate("EmployeeWindow", u"Employee ID:", None))
        self.idInput.setPlaceholderText(QCoreApplication.translate("EmployeeWindow", u"T\u1ef1 \u0111\u1ed9ng t\u1ea1o", None))
        self.nameLabel.setText(QCoreApplication.translate("EmployeeWindow", u"H\u1ecd v\u00e0 t\u00ean:", None))
        self.nameInput.setPlaceholderText(QCoreApplication.translate("EmployeeWindow", u"Nh\u1eadp h\u1ecd v\u00e0 t\u00ean \u0111\u1ea7y \u0111\u1ee7", None))
        self.phoneLabel.setText(QCoreApplication.translate("EmployeeWindow", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i:", None))
        self.phoneInput.setPlaceholderText(QCoreApplication.translate("EmployeeWindow", u"Nh\u1eadp s\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None))
        self.emailLabel.setText(QCoreApplication.translate("EmployeeWindow", u"Email:", None))
        self.emailInput.setPlaceholderText(QCoreApplication.translate("EmployeeWindow", u"Nh\u1eadp \u0111\u1ecba ch\u1ec9 email", None))
        self.positionLabel.setText(QCoreApplication.translate("EmployeeWindow", u"Ch\u1ee9c v\u1ee5:", None))
        self.positionCombo.setItemText(0, QCoreApplication.translate("EmployeeWindow", u"Thu ng\u00e2n", None))
        self.positionCombo.setItemText(1, QCoreApplication.translate("EmployeeWindow", u"Nh\u00e2n vi\u00ean ch\u0103m s\u00f3c", None))
        self.positionCombo.setItemText(2, QCoreApplication.translate("EmployeeWindow", u"Qu\u1ea3n l\u00fd", None))

        self.salaryLabel.setText(QCoreApplication.translate("EmployeeWindow", u"L\u01b0\u01a1ng:", None))
        self.salaryInput.setPlaceholderText(QCoreApplication.translate("EmployeeWindow", u"Nh\u1eadp l\u01b0\u01a1ng", None))
        self.startDateLabel.setText(QCoreApplication.translate("EmployeeWindow", u"B\u1eaft \u0111\u1ea7u l\u00e0m:", None))
        self.photoLabel.setText("")
        self.imgpathButton.setText(QCoreApplication.translate("EmployeeWindow", u"Ch\u1ecdn \u1ea3nh", None))
        self.addButton.setText(QCoreApplication.translate("EmployeeWindow", u"Th\u00eam", None))
        self.excelButton.setText(QCoreApplication.translate("CustomerWindow", u"Excel", None))
        self.fixButton.setText(QCoreApplication.translate("EmployeeWindow", u"S\u1eeda", None))
        self.deleteButton.setText(QCoreApplication.translate("EmployeeWindow", u"X\u00f3a", None))
        ___qtablewidgetitem = self.employeeTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("EmployeeWindow", u"ID", None));
        ___qtablewidgetitem1 = self.employeeTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("EmployeeWindow", u"H\u1ecd v\u00e0 t\u00ean", None));
        ___qtablewidgetitem2 = self.employeeTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("EmployeeWindow", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None));
        ___qtablewidgetitem3 = self.employeeTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("EmployeeWindow", u"Email", None));
        ___qtablewidgetitem4 = self.employeeTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("EmployeeWindow", u"Ch\u1ee9c v\u1ee5", None));
        ___qtablewidgetitem5 = self.employeeTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("EmployeeWindow", u"L\u01b0\u01a1ng", None));
        ___qtablewidgetitem6 = self.employeeTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("EmployeeWindow", u"Img path", None));
        ___qtablewidgetitem7 = self.employeeTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("EmployeeWindow", u"Ng\u00e0y v\u00e0o l\u00e0m", None));
    # retranslateUi

