# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'forgotpass.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_PasswordResetWindow(object):
    def setupUi(self, PasswordResetWindow):
        if not PasswordResetWindow.objectName():
            PasswordResetWindow.setObjectName(u"PasswordResetWindow")
        PasswordResetWindow.resize(595, 353)
        PasswordResetWindow.setStyleSheet(u"\n"
"    QMainWindow {\n"
"        background-color: #fef8ec;\n"
"    }\n"
"    QWidget#forgotPasswordForm, QWidget#newPasswordForm {\n"
"        background-color: white;\n"
"        border-radius: 12px;\n"
"    }\n"
"    QLabel#titleLabel {\n"
"        font-size: 20px;\n"
"        font-weight: bold;\n"
"        color: #333333;\n"
"        margin-bottom: 10px;\n"
"    }\n"
"    QLabel#subtitleLabel {\n"
"        font-size: 14px;\n"
"        color: #666666;\n"
"    }\n"
"    QLabel#messageLabel {\n"
"        background-color: #E8F5E9;\n"
"        padding: 10px;\n"
"        border-radius: 6px;\n"
"        color: #2E7D32;\n"
"        font-size: 13px;\n"
"    }\n"
"    QLineEdit {\n"
"        padding: 12px;\n"
"        border: 1px solid #E0E0E0;\n"
"        border-radius: 6px;\n"
"        font-size: 14px;\n"
"        min-height: 20px;\n"
"    }\n"
"    QPushButton {\n"
"        background-color: #d8939d;\n"
"        color: white;\n"
"        border: none;\n"
"        border-radius: 6px;\n"
"        padding: 10px;\n"
"        font-size: 14px;\n"
"        min-height: 25px;\n"
"        min-width: 40px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #bd637e;\n"
"    }\n"
"   ")
        self.centralwidget = QWidget(PasswordResetWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.forgotPasswordPage = QWidget()
        self.forgotPasswordPage.setObjectName(u"forgotPasswordPage")
        self.verticalLayout = QVBoxLayout(self.forgotPasswordPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.forgotPasswordForm = QWidget(self.forgotPasswordPage)
        self.forgotPasswordForm.setObjectName(u"forgotPasswordForm")
        self.formLayout = QVBoxLayout(self.forgotPasswordForm)
        self.formLayout.setSpacing(20)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(30, -1, 30, -1)

        self.titleLabel = QLabel(self.forgotPasswordForm)
        self.titleLabel.setObjectName(u"titleLabel")

        self.formLayout.addWidget(self.titleLabel)

        self.subtitleLabel = QLabel(self.forgotPasswordForm)
        self.subtitleLabel.setObjectName(u"subtitleLabel")

        self.formLayout.addWidget(self.subtitleLabel)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.addItem(self.verticalSpacer_2)

        self.emailInput = QLineEdit(self.forgotPasswordForm)
        self.emailInput.setObjectName(u"emailInput")

        self.formLayout.addWidget(self.emailInput)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.addItem(self.verticalSpacer_3)

        self.continueButton = QPushButton(self.forgotPasswordForm)
        self.continueButton.setObjectName(u"continueButton")

        self.formLayout.addWidget(self.continueButton)


        self.verticalLayout.addWidget(self.forgotPasswordForm)

        self.stackedWidget.addWidget(self.forgotPasswordPage)
        self.newPasswordPage = QWidget()
        self.newPasswordPage.setObjectName(u"newPasswordPage")
        self.verticalLayout_2 = QVBoxLayout(self.newPasswordPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.newPasswordForm = QWidget(self.newPasswordPage)
        self.newPasswordForm.setObjectName(u"newPasswordForm")
        self.formLayout_2 = QVBoxLayout(self.newPasswordForm)
        self.formLayout_2.setSpacing(20)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(30, -1, 30, -1)
        self.titleLabel_2 = QLabel(self.newPasswordForm)
        self.titleLabel_2.setObjectName(u"titleLabel_2")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.titleLabel_2.setFont(font)

        self.formLayout_2.addWidget(self.titleLabel_2)

        self.messageLabel = QLabel(self.newPasswordForm)
        self.messageLabel.setObjectName(u"messageLabel")
        self.messageLabel.setWordWrap(True)

        self.formLayout_2.addWidget(self.messageLabel)

        self.newPasswordInput = QLineEdit(self.newPasswordForm)
        self.newPasswordInput.setObjectName(u"newPasswordInput")
        self.newPasswordInput.setEchoMode(QLineEdit.Password)

        self.formLayout_2.addWidget(self.newPasswordInput)

        self.confirmPasswordInput = QLineEdit(self.newPasswordForm)
        self.confirmPasswordInput.setObjectName(u"confirmPasswordInput")
        self.confirmPasswordInput.setEchoMode(QLineEdit.Password)

        self.formLayout_2.addWidget(self.confirmPasswordInput)

        self.changeButton = QPushButton(self.newPasswordForm)
        self.changeButton.setObjectName(u"changeButton")

        self.formLayout_2.addWidget(self.changeButton)


        self.verticalLayout_2.addWidget(self.newPasswordForm)

        self.stackedWidget.addWidget(self.newPasswordPage)

        self.horizontalLayout.addWidget(self.stackedWidget)

        PasswordResetWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PasswordResetWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PasswordResetWindow)
    # setupUi

    def retranslateUi(self, PasswordResetWindow):
        PasswordResetWindow.setWindowTitle(QCoreApplication.translate("PasswordResetWindow", u"Password Reset", None))
        self.titleLabel.setText(QCoreApplication.translate("PasswordResetWindow", u"Forgot Password", None))
        self.subtitleLabel.setText(QCoreApplication.translate("PasswordResetWindow", u"Nh\u1eadp \u0111\u1ecba ch\u1ec9 email c\u1ee7a b\u1ea1n.", None))
        self.emailInput.setPlaceholderText(QCoreApplication.translate("PasswordResetWindow", u"Nh\u1eadp \u0111\u1ecba ch\u1ec9 email", None))
        self.continueButton.setText(QCoreApplication.translate("PasswordResetWindow", u"Continue", None))
        self.titleLabel_2.setText(QCoreApplication.translate("PasswordResetWindow", u"New Password", None))
        self.messageLabel.setText(QCoreApplication.translate("PasswordResetWindow", u"Vui l\u00f2ng t\u1ea1o m\u1ed9t m\u1eadt kh\u1ea9u m\u1edbi \n"
"kh\u1ecfe v\u00e0 an to\u00e0n h\u01a1n.", None))
        self.newPasswordInput.setPlaceholderText(QCoreApplication.translate("PasswordResetWindow", u"T\u1ea1o m\u1eadt kh\u1ea9u m\u1edbi", None))
        self.confirmPasswordInput.setPlaceholderText(QCoreApplication.translate("PasswordResetWindow", u"X\u00e1c nh\u1eadn m\u1eadt kh\u1ea9u c\u1ee7a b\u1ea1n", None))
        self.changeButton.setText(QCoreApplication.translate("PasswordResetWindow", u"Change", None))
    # retranslateUi

