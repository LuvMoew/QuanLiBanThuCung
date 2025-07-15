# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(809, 420)
        LoginWindow.setStyleSheet(u" QMainWindow {\n"
"        background-color: #fef8ec;\n"
"    }\n"
"    QLabel#titleLabel {\n"
"        font-size: 24px;\n"
"        font-weight: bold;\n"
"        color: #333333;\n"
"    }\n"
"    QLabel#subtitleLabel {\n"
"        font-size: 16px;\n"
"        color: #666666;\n"
"    }\n"
"    QLineEdit {\n"
"        padding: 12px;\n"
"        border: 1px solid #e5e5e5;\n"
"        border-radius: 4px;\n"
"        background-color: #ffffff;\n"
"        font-size: 14px;\n"
"    }\n"
"    QPushButton#googleButton {\n"
"        padding: 12px;\n"
"        background-color: #4285f4;\n"
"        color: white;\n"
"        border: none;\n"
"        border-radius: 4px;\n"
"        font-size: 14px;\n"
"    }\n"
"    QPushButton#signInButton {\n"
"        padding: 12px;\n"
"        background-color: #ea4c89;\n"
"        color: white;\n"
"        border: none;\n"
"        border-radius: 4px;\n"
"        font-size: 14px;\n"
"    }\n"
"    QPushButton#forgotPasswordButton {\n"
"        color: #4285f4;\n"
"        border: no"
                        "ne;\n"
"        background: none;\n"
"        text-decoration: underline;\n"
"    }\n"
"   ")
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftPanel = QWidget(self.centralwidget)
        self.leftPanel.setObjectName(u"leftPanel")
        self.leftPanel.setStyleSheet(u"background-color: #fac7cb;")
        self.verticalLayout_2 = QVBoxLayout(self.leftPanel)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.leftPanel)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Papyrus"])
        font.setPointSize(18)
        font.setItalic(False)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.titleLabel = QLabel(self.leftPanel)
        self.titleLabel.setObjectName(u"titleLabel")
        font1 = QFont()
        font1.setFamilies([u"Arial Rounded MT Bold"])
        font1.setBold(True)
        font1.setItalic(False)
        self.titleLabel.setFont(font1)
        self.titleLabel.setStyleSheet(u"color: #333;")

        self.verticalLayout_2.addWidget(self.titleLabel)

        self.illustrationLabel = QLabel(self.leftPanel)
        self.illustrationLabel.setObjectName(u"illustrationLabel")
        self.illustrationLabel.setMinimumSize(QSize(300, 300))
        self.illustrationLabel.setMaximumSize(QSize(300, 300))
        self.illustrationLabel.setPixmap(QPixmap(u":/Icons/petlogoshop.jpeg"))
        self.illustrationLabel.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.illustrationLabel)


        self.horizontalLayout.addWidget(self.leftPanel)

        self.rightPanel = QWidget(self.centralwidget)
        self.rightPanel.setObjectName(u"rightPanel")
        self.verticalLayout = QVBoxLayout(self.rightPanel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.signInLabel = QLabel(self.rightPanel)
        self.signInLabel.setObjectName(u"signInLabel")
        font2 = QFont()
        font2.setFamilies([u"MS Sans Serif"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.signInLabel.setFont(font2)
        self.signInLabel.setLayoutDirection(Qt.LeftToRight)
        self.signInLabel.setStyleSheet(u"text-align: left;\n"
"color: #333;")

        self.verticalLayout.addWidget(self.signInLabel)

        self.googleButton = QPushButton(self.rightPanel)
        self.googleButton.setObjectName(u"googleButton")
        self.googleButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.googleButton)

        self.orLabel = QLabel(self.rightPanel)
        self.orLabel.setObjectName(u"orLabel")
        font3 = QFont()
        font3.setFamilies([u"MS UI Gothic"])
        font3.setPointSize(9)
        self.orLabel.setFont(font3)
        self.orLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.orLabel)

        self.usernameInput = QLineEdit(self.rightPanel)
        self.usernameInput.setObjectName(u"usernameInput")

        self.verticalLayout.addWidget(self.usernameInput)

        self.passwordInput = QLineEdit(self.rightPanel)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.passwordInput)

        self.forgotPasswordButton = QPushButton(self.rightPanel)
        self.forgotPasswordButton.setObjectName(u"forgotPasswordButton")
        self.forgotPasswordButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.forgotPasswordButton)

        self.signInButton = QPushButton(self.rightPanel)
        self.signInButton.setObjectName(u"signInButton")
        self.signInButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.signInButton)

        self.signUpLabel = QLabel(self.rightPanel)
        self.signUpLabel.setObjectName(u"signUpLabel")
        self.signUpLabel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        font4 = QFont()
        font4.setPointSize(8)
        font4.setUnderline(True)
        self.signUpLabel.setFont(font4)
        self.signUpLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.signUpLabel)


        self.horizontalLayout.addWidget(self.rightPanel)

        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Sign in to Dribbble", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"Pet Shop", None))
        self.titleLabel.setText(QCoreApplication.translate("LoginWindow", u"WELCOME \n"
"Thi\u00ean \u0111\u01b0\u1eddng th\u00fa c\u01b0ng!", None))
        self.illustrationLabel.setText("")
        self.signInLabel.setText(QCoreApplication.translate("LoginWindow", u"Sign in to Dribbble", None))
        self.googleButton.setText(QCoreApplication.translate("LoginWindow", u"Sign in with Google", None))
        self.orLabel.setText(QCoreApplication.translate("LoginWindow", u"Or", None))
        self.usernameInput.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Username or Email Address", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.forgotPasswordButton.setText(QCoreApplication.translate("LoginWindow", u"Forgot password?", None))
        self.signInButton.setText(QCoreApplication.translate("LoginWindow", u"Sign In", None))
        self.signUpLabel.setText(QCoreApplication.translate("LoginWindow", u"Not a member? Sign up now", None))
    # retranslateUi

