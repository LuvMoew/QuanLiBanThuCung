from PySide6.QtWidgets import QApplication, QMainWindow
import sys
from pet_sidebar import MySidebar

class MainWindow(QMainWindow):
    def __init__(self, user_role=None, user_id=None):
        super().__init__()
        # Khởi tạo và thêm sidebar với user_role
        self.sidebar = MySidebar(user_role=user_role, user_id=user_id)
        self.setCentralWidget(self.sidebar)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow(user_role="customer")  # ví dụ: role customer
#     window.show()
#     sys.exit(app.exec())
