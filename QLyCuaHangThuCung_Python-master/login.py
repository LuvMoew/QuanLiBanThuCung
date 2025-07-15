from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from PySide6.QtGui import QIcon
from config.connectDB import connect_db
import sys
from ui.ui_login import Ui_LoginWindow 

class LoginWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        # Tạo đối tượng UI và thiết lập cho cửa sổ hiện tại

        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.googleButton.setHidden(True)
        self.ui.orLabel.setText("With")
        self.ui.signInLabel.setText("Sign in to Pet Shop")
        # Thêm icon "eye" để ẩn/hiện mật khẩu
        self.password_visible = False
        self.toggle_action = self.ui.passwordInput.addAction(
            QIcon(":/Icons/hide.png"), QLineEdit.TrailingPosition
        )
        self.toggle_action.triggered.connect(self.toggle_password_visibility)
        
        self.ui.signInButton.clicked.connect(self.handle_login)
        
        self.ui.signUpLabel.mousePressEvent = self.go_to_logup
        
        self.ui.forgotPasswordButton.clicked.connect(self.go_to_forgotpass)

        self.ui.usernameInput.setStyleSheet("""
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

        self.ui.passwordInput.setStyleSheet("""
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
            # Ẩn mật khẩu
            self.ui.passwordInput.setEchoMode(QLineEdit.Password)
            self.toggle_action.setIcon(QIcon(":/Icons/hide.png"))
            self.password_visible = False
        else:
            # Hiển thị mật khẩu
            self.ui.passwordInput.setEchoMode(QLineEdit.Normal)
            self.toggle_action.setIcon(QIcon(":/Icons/view.png"))
            self.password_visible = True

            
            
    def handle_login(self):
        # Lấy dữ liệu từ các ô nhập liệu và loại bỏ khoảng trắng thừa
        username = self.ui.usernameInput.text().strip()
        password = self.ui.passwordInput.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Input Error", "Vui lòng điền đầy đủ thông tin!")
            return

        try:
            connection = connect_db()
            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)
                # Tìm người dùng dựa trên email (trường username)
                query = "SELECT * FROM users WHERE email = %s"
                cursor.execute(query, (username,))
                user = cursor.fetchone()
                if user is None:
                    QMessageBox.warning(self, "Login Failed", "Tài khoản không tồn tại!")
                else:
                    # So sánh mật khẩu (plain text) trong DB với mật khẩu nhập vào
                    if user["password"] == password:
                        QMessageBox.information(self, "Login Success", "Đăng nhập thành công!")
                        # Lấy role và id của user
                        user_role = user.get("role", "").lower()
                        user_id = user.get("id")
                        
                        from main2 import MainWindow 
                        self.main_window = MainWindow(user_role=user_role, user_id=user_id)
                        self.main_window.show()
                        self.close()
                    else:
                        QMessageBox.warning(self, "Login Failed", "Mật khẩu không đúng!")
                cursor.close()
            connection.close()
        except Exception as err:
            print(err)

    def go_to_logup(self, event):
        from signup import SignupWindow  
        self.logup_window = SignupWindow() 
        self.logup_window.show()            
        self.close()                     

    def go_to_forgotpass(self, event):
        from forgotpass import ForgotPassWindow  
        self.logup_window = ForgotPassWindow()
        self.logup_window.show()           
        self.close()                     

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
