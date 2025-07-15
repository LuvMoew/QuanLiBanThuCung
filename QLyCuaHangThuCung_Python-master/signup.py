import sys
import mysql.connector
from mysql.connector import Error
from config.connectDB import connect_db
from login import LoginWindow

from PySide6.QtWidgets import QMainWindow, QMessageBox, QLineEdit
from PySide6.QtGui import QIcon
from ui.ui_signup import Ui_SignupWindow


class SignupWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SignupWindow()
        self.ui.setupUi(self)

        # Toggle password visibility
        self.password_visible = False
        self.toggle_action = self.ui.passwordInput.addAction(
            QIcon(":/Icons/hide.png"), QLineEdit.TrailingPosition
        )
        self.toggle_action.triggered.connect(self.toggle_password_visibility)

        self.ui.submitButton.clicked.connect(self.register_account)
        self.ui.loginLink.mousePressEvent = self.go_to_login

        # Set styles
        for field in [self.ui.nameInput, self.ui.emailInput, self.ui.passwordInput]:
            field.setStyleSheet("""
                QLineEdit {
                    color: black;
                    background-color: white;
                    selection-color: white;
                    selection-background-color: #2F4F4F;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                    padding: 5px;
                }
            """)

    def toggle_password_visibility(self):
        if self.password_visible:
            self.ui.passwordInput.setEchoMode(QLineEdit.Password)
            self.toggle_action.setIcon(QIcon(":/Icons/hide.png"))
            self.password_visible = False
        else:
            self.ui.passwordInput.setEchoMode(QLineEdit.Normal)
            self.toggle_action.setIcon(QIcon(":/Icons/view.png"))
            self.password_visible = True

    def register_account(self):
        full_name = self.ui.nameInput.text().strip()
        email = self.ui.emailInput.text().strip()
        password = self.ui.passwordInput.text().strip()

        if not full_name or not email or not password:
            QMessageBox.warning(self, "Input Error", "Vui lòng điền đầy đủ thông tin")
            return

        if not self.ui.termsCheckbox.isChecked():
            QMessageBox.warning(self, "Terms", "Bạn phải đồng ý với các điều khoản và điều kiện!")
            return

        try:
            connection = connect_db()
            if connection.is_connected():
                cursor = connection.cursor()

                # Kiểm tra email đã tồn tại chưa
                cursor.execute("SELECT user_id FROM users WHERE email = %s", (email,))
                if cursor.fetchone():
                    QMessageBox.warning(self, "Registration Error", "Email đã tồn tại!")
                    return

                # Tạo username tạm từ email nếu không có input riêng
                username = email.split('@')[0]

                # Thêm user mới
                insert_user = """
                    INSERT INTO users (username, password, email, role)
                    VALUES (%s, %s, %s, 'customer')
                """
                cursor.execute(insert_user, (username, password, email))
                connection.commit()
                new_user_id = cursor.lastrowid

                # Tạo số điện thoại giả
                dummy_phone = f"000000{new_user_id}"

                # Thêm vào bảng customers
                insert_customer = """
                    INSERT INTO customers (full_name, phone, email, address, user_id)
                    VALUES (%s, %s, %s, '', %s)
                """
                cursor.execute(insert_customer, (full_name, dummy_phone, email, new_user_id))
                connection.commit()

                QMessageBox.information(self, "Success", "Tài khoản đã đăng ký thành công!")
                self.go_to_login(None)

        except Error as err:
            QMessageBox.critical(self, "Database Error", f"Error: {err}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def go_to_login(self, event):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()
