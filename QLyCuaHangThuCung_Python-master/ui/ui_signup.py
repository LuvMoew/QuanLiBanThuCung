# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_SignupWindow(object):
    def setupUi(self, SignupWindow):
        if not SignupWindow.objectName():
            SignupWindow.setObjectName(u"SignupWindow")
        SignupWindow.resize(809, 395)
        SignupWindow.setStyleSheet(u"\n"
"    QMainWindow {\n"
"		background-color: #fef8ec;\n"
"    }\n"
"    QWidget#centralForm {\n"
"        background-color: rgb(250, 216, 217);\n"
"        border-radius: 20px;\n"
"    }\n"
"    QLabel#titleLabel {\n"
"        font-size: 24px;\n"
"        font-weight: bold;\n"
"        color: #333333;\n"
"    }\n"
"    QLabel#loginLabel {\n"
"        color: #666666;\n"
"    }\n"
"    QLabel#loginLink {\n"
"        color: #0046BE;\n"
"        text-decoration: underline;\n"
"    }\n"
"    QLineEdit {\n"
"        padding: 12px;\n"
"        border: 1px solid #E5E7EB;\n"
"        border-radius: 8px;\n"
"        background-color: #FFFFFF;\n"
"        font-size: 14px;\n"
"        min-height: 20px;\n"
"    }\n"
"    QPushButton#submitButton {\n"
"        background-color: #0046BE;\n"
"        color: white;\n"
"        border: none;\n"
"        border-radius: 8px;\n"
"        padding: 8px;\n"
"        font-size: 14px;\n"
"        font-weight: bold;\n"
"        min-height: 30px;\n"
"    }\n"
"    QCheckBox {\n"
"     "
                        "   color: #666666;\n"
"        font-size: 13px;\n"
"    }\n"
"   ")
        self.centralwidget = QWidget(SignupWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.centralForm = QWidget(self.centralwidget)
        self.centralForm.setObjectName(u"centralForm")
        self.horizontalLayout_2 = QHBoxLayout(self.centralForm)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout = QVBoxLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(40, -1, 40, -1)
        self.titleLabel = QLabel(self.centralForm)
        self.titleLabel.setObjectName(u"titleLabel")

        self.formLayout.addWidget(self.titleLabel)

        self.loginTextLayout = QHBoxLayout()
        self.loginTextLayout.setObjectName(u"loginTextLayout")
        self.loginLabel = QLabel(self.centralForm)
        self.loginLabel.setObjectName(u"loginLabel")

        self.loginTextLayout.addWidget(self.loginLabel)

        self.loginLink = QLabel(self.centralForm)
        self.loginLink.setObjectName(u"loginLink")
        self.loginLink.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.loginTextLayout.addWidget(self.loginLink)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.loginTextLayout.addItem(self.horizontalSpacer)


        self.formLayout.addLayout(self.loginTextLayout)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.formLayout.addItem(self.verticalSpacer)

        self.nameInput = QLineEdit(self.centralForm)
        self.nameInput.setObjectName(u"nameInput")

        self.formLayout.addWidget(self.nameInput)

        self.emailInput = QLineEdit(self.centralForm)
        self.emailInput.setObjectName(u"emailInput")

        self.formLayout.addWidget(self.emailInput)

        self.passwordInput = QLineEdit(self.centralForm)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setEchoMode(QLineEdit.Password)

        self.formLayout.addWidget(self.passwordInput)

        self.termsCheckbox = QCheckBox(self.centralForm)
        self.termsCheckbox.setObjectName(u"termsCheckbox")

        self.formLayout.addWidget(self.termsCheckbox)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.addItem(self.verticalSpacer_5)

        self.submitButton = QPushButton(self.centralForm)
        self.submitButton.setObjectName(u"submitButton")

        self.formLayout.addWidget(self.submitButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.formLayout)

        self.illustrationLabel = QLabel(self.centralForm)
        self.illustrationLabel.setObjectName(u"illustrationLabel")
        self.illustrationLabel.setMinimumSize(QSize(300, 300))
        self.illustrationLabel.setMaximumSize(QSize(600, 600))
        self.illustrationLabel.setPixmap(QPixmap(u":/Icons/petlogoshop.jpeg"))
        self.illustrationLabel.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.illustrationLabel)


        self.horizontalLayout.addWidget(self.centralForm)

        SignupWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SignupWindow)

        QMetaObject.connectSlotsByName(SignupWindow)
    # setupUi

    def retranslateUi(self, SignupWindow):
        SignupWindow.setWindowTitle(QCoreApplication.translate("SignupWindow", u"Sign Up", None))
        self.titleLabel.setText(QCoreApplication.translate("SignupWindow", u"Sign up", None))
        self.loginLabel.setText(QCoreApplication.translate("SignupWindow", u"Already have account?", None))
        self.loginLink.setText(QCoreApplication.translate("SignupWindow", u"Login here", None))
        self.nameInput.setPlaceholderText(QCoreApplication.translate("SignupWindow", u"Enter your name", None))
        self.emailInput.setPlaceholderText(QCoreApplication.translate("SignupWindow", u"Enter your email", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("SignupWindow", u"Enter your password", None))
        self.termsCheckbox.setText(QCoreApplication.translate("SignupWindow", u"By signing up you agree to receive updates and special offers", None))
        self.submitButton.setText(QCoreApplication.translate("SignupWindow", u"Submit", None))
        self.illustrationLabel.setText("")
    # retranslateUi

