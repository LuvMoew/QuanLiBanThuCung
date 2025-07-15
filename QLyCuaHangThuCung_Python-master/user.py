import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QLineEdit
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
import mysql.connector
from datetime import datetime
from ui.ui_user2 import Ui_UserManagement
from config.connectDB import connect_db

class UserManagement(QMainWindow):
    def __init__(self):
        super(UserManagement, self).__init__()
        self.ui = Ui_UserManagement()
        self.ui.setupUi(self)
        self.password_visible = False
        self.toggle_action = self.ui.lineEditPassword.addAction(
            QIcon(":/Icons/hide.png"), QLineEdit.TrailingPosition
        )
        self.toggle_action.triggered.connect(self.toggle_password_visibility)

        self.ui.pushButtonAdd.clicked.connect(self.add_user)
        self.ui.pushButtonEdit.clicked.connect(self.edit_user)
        self.ui.pushButtonDelete.clicked.connect(self.delete_user)
        self.ui.tableWidget.cellClicked.connect(self.populate_form)

        self.ui.tableWidget.setColumnWidth(0, 50)   # user_id
        self.ui.tableWidget.setColumnWidth(1, 150)  # name
        self.ui.tableWidget.setColumnWidth(2, 180)  # email
        self.ui.tableWidget.setColumnWidth(3, 100)  # pass
        self.ui.tableWidget.setColumnWidth(4, 80)   # role
        self.ui.tableWidget.setColumnWidth(5, 120)  # created_at
        self.ui.tableWidget.setColumnWidth(6, 120)  # updated_at

        self.load_users()

    def toggle_password_visibility(self):
        if self.password_visible:
            self.ui.lineEditPassword.setEchoMode(QLineEdit.Password)
            self.toggle_action.setIcon(QIcon(":/Icons/hide.png"))
            self.password_visible = False
        else:
            self.ui.lineEditPassword.setEchoMode(QLineEdit.Normal)
            self.toggle_action.setIcon(QIcon(":/Icons/view.png"))
            self.password_visible = True

    def load_users(self):
        connection = connect_db()
        if not connection:
            return

        cursor = connection.cursor()
        try:
            cursor.execute("SELECT user_id, name, email, pass, role, created_at, updated_at FROM users")
            users = cursor.fetchall()

            self.ui.tableWidget.setRowCount(0)
            for row_index, user in enumerate(users):
                self.ui.tableWidget.insertRow(row_index)
                for col_index, value in enumerate(user):
                    if isinstance(value, datetime):
                        value = value.strftime('%Y-%m-%d %H:%M:%S')
                    if col_index == 3:
                        value = '••••••••'
                    item = QTableWidgetItem(str(value))
                    if col_index == 0:
                        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                    self.ui.tableWidget.setItem(row_index, col_index, item)

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error loading users: {err}")
        finally:
            cursor.close()
            connection.close()

    def populate_form(self, row, column):
        user_id = self.ui.tableWidget.item(row, 0).text()
        connection = connect_db()
        if not connection:
            return

        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT user_id, name, email, pass, role FROM users WHERE user_id = %s", (user_id,))
            user = cursor.fetchone()
            if user:
                self.ui.lineEditId.setText(str(user['user_id']))
                self.ui.lineEditName.setText(user['name'])
                self.ui.lineEditEmail.setText(user['email'])
                self.ui.lineEditPassword.setText(user['pass'])
                role_index = 0 if user['role'] == 'admin' else 1
                self.ui.comboBoxRole.setCurrentIndex(role_index)
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error retrieving user data: {err}")
        finally:
            cursor.close()
            connection.close()

    def validate_form(self):
        if not self.ui.lineEditName.text().strip():
            QMessageBox.warning(self, "Validation Error", "Tên người dùng không được để trống.")
            return False
        if not self.ui.lineEditEmail.text().strip():
            QMessageBox.warning(self, "Validation Error", "Email không được để trống.")
            return False
        if not self.ui.lineEditId.text() and not self.ui.lineEditPassword.text():
            QMessageBox.warning(self, "Validation Error", "Mật khẩu là bắt buộc cho người dùng mới.")
            return False
        return True

    def add_user(self):
        if not self.validate_form():
            return
        name = self.ui.lineEditName.text()
        email = self.ui.lineEditEmail.text()
        password = self.ui.lineEditPassword.text()
        role = self.ui.comboBoxRole.currentText()

        connection = connect_db()
        if not connection:
            return

        cursor = connection.cursor()
        try:
            cursor.execute("SELECT user_id FROM users WHERE email = %s", (email,))
            if cursor.fetchone():
                QMessageBox.warning(self, "Duplicate Email", "Email đã tồn tại")
                return

            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(
                "INSERT INTO users (name, email, pass, role, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)",
                (name, email, password, role, now, now)
            )
            connection.commit()
            QMessageBox.information(self, "Success", "Thêm người dùng thành công")
            self.clear_form()
            self.load_users()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error adding user: {err}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()

    def edit_user(self):
        if not self.ui.lineEditId.text():
            QMessageBox.warning(self, "Selection Required", "Vui lòng chọn một người dùng để chỉnh sửa.")
            return
        if not self.validate_form():
            return

        user_id = self.ui.lineEditId.text()
        name = self.ui.lineEditName.text()
        email = self.ui.lineEditEmail.text()
        password = self.ui.lineEditPassword.text()
        role = self.ui.comboBoxRole.currentText()

        connection = connect_db()
        if not connection:
            return

        cursor = connection.cursor()
        try:
            cursor.execute("SELECT user_id FROM users WHERE email = %s AND user_id != %s", (email, user_id))
            if cursor.fetchone():
                QMessageBox.warning(self, "Duplicate Email", "Email đã được dùng bởi người khác.")
                return

            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if password:
                cursor.execute(
                    "UPDATE users SET name = %s, email = %s, pass = %s, role = %s, updated_at = %s WHERE user_id = %s",
                    (name, email, password, role, now, user_id)
                )
            else:
                cursor.execute(
                    "UPDATE users SET name = %s, email = %s, role = %s, updated_at = %s WHERE user_id = %s",
                    (name, email, role, now, user_id)
                )
            connection.commit()
            QMessageBox.information(self, "Success", "Người dùng đã được cập nhật.")
            self.clear_form()
            self.load_users()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error updating user: {err}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()

    def delete_user(self):
        if not self.ui.lineEditId.text():
            QMessageBox.warning(self, "Selection Required", "Vui lòng chọn người dùng để xóa.")
            return

        user_id = self.ui.lineEditId.text()
        reply = QMessageBox.question(self, "Xác nhận xóa", "Bạn có chắc chắn muốn xóa người dùng này?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return

        connection = connect_db()
        if not connection:
            return

        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
            connection.commit()
            QMessageBox.information(self, "Success", "Người dùng đã bị xóa.")
            self.clear_form()
            self.load_users()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error deleting user: {err}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()

    def clear_form(self):
        self.ui.lineEditId.clear()
        self.ui.lineEditName.clear()
        self.ui.lineEditEmail.clear()
        self.ui.lineEditPassword.clear()
        self.ui.comboBoxRole.setCurrentIndex(0)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = UserManagement()
#     window.show()
#     sys.exit(app.exec())
