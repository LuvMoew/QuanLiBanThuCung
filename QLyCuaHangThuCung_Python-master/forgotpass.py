import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QLabel, QLineEdit
from PySide6.QtGui import QIcon, QPixmap, QCursor
from PySide6.QtCore import Qt
from mysql.connector import Error
from config.connectDB import connect_db

# Import UI đã biên dịch
from ui.ui_forgotpass import Ui_PasswordResetWindow


# ... [import giữ nguyên như bạn gửi] ...

class ForgotPassWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PasswordResetWindow()
        self.ui.setupUi(self)

        # Giao diện quay lại
        self.backLabel = QLabel(self.ui.forgotPasswordForm)
        self.backLabel.setObjectName("backLabel")
        self.backLabel.setPixmap(QIcon(":/Icons/left-arrow.png").pixmap(24, 24))
        self.backLabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.ui.formLayout.insertWidget(0, self.backLabel)
        self.backLabel.mousePressEvent = self.go_to_login

        # Sự kiện các nút
        self.ui.continueButton.clicked.connect(self.handle_continue)
        self.ui.changeButton.clicked.connect(self.handle_change)

        # Mật khẩu ẩn/hiện
        self.password_visible_new = False
        self.toggle_action_new = self.ui.newPasswordInput.addAction(QIcon(":/Icons/hide.png"), QLineEdit.TrailingPosition)
        self.toggle_action_new.triggered.connect(self.toggle_password_visibility_new)

        self.password_visible_confirm = False
        self.toggle_action_confirm = self.ui.confirmPasswordInput.addAction(QIcon(":/Icons/hide.png"), QLineEdit.TrailingPosition)
        self.toggle_action_confirm.triggered.connect(self.toggle_password_visibility_confirm)

        # Biến email được xác thực
        self.user_email = None

    def toggle_password_visibility_new(self):
        if self.password_visible_new:
            self.ui.newPasswordInput.setEchoMode(QLineEdit.Password)
            self.toggle_action_new.setIcon(QIcon(":/Icons/hide.png"))
        else:
            self.ui.newPasswordInput.setEchoMode(QLineEdit.Normal)
            self.toggle_action_new.setIcon(QIcon(":/Icons/view.png"))
        self.password_visible_new = not self.password_visible_new

    def toggle_password_visibility_confirm(self):
        if self.password_visible_confirm:
            self.ui.confirmPasswordInput.setEchoMode(QLineEdit.Password)
            self.toggle_action_confirm.setIcon(QIcon(":/Icons/hide.png"))
        else:
            self.ui.confirmPasswordInput.setEchoMode(QLineEdit.Normal)
            self.toggle_action_confirm.setIcon(QIcon(":/Icons/view.png"))
        self.password_visible_confirm = not self.password_visible_confirm

    def handle_continue(self):
        """Xác thực email tồn tại trong bảng users"""
        email = self.ui.emailInput.text().strip()
        if not email:
            QMessageBox.warning(self, "Warning", "Vui lòng nhập địa chỉ email!")
            return

        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                query = "SELECT user_id FROM users WHERE email = %s"
                cursor.execute(query, (email,))
                user = cursor.fetchone()
                if not user:
                    QMessageBox.warning(self, "Warning", "Email không tồn tại!")
                    return
                else:
                    self.user_email = email
        except Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")
            return
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

        self.ui.stackedWidget.setCurrentIndex(1)

    def handle_change(self):
        """Đổi mật khẩu nếu hợp lệ"""
        new_pass = self.ui.newPasswordInput.text().strip()
        confirm_pass = self.ui.confirmPasswordInput.text().strip()

        if not new_pass or not confirm_pass:
            QMessageBox.warning(self, "Warning", "Vui lòng nhập đầy đủ mật khẩu!")
            return

        if new_pass != confirm_pass:
            QMessageBox.warning(self, "Warning", "Mật khẩu xác nhận không khớp!")
            return

        if not self.user_email:
            QMessageBox.critical(self, "Error", "Không xác định được email. Vui lòng thử lại!")
            return

        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                update_query = "UPDATE users SET password = %s WHERE email = %s"
                cursor.execute(update_query, (new_pass, self.user_email))
                conn.commit()
        except Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")
            return
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

        QMessageBox.information(self, "Success", "Mật khẩu đã được thay đổi thành công!")
        self.go_to_login()

    def go_to_login(self, event=None):
        from login import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()
