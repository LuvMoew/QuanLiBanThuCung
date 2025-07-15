import os
import shutil
import sys
import datetime
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
from PySide6.QtGui import QPixmap, QPainter, QPainterPath
from PySide6.QtCore import QDate, Qt
from config.connectDB import connect_db
from ui.ui_info import Ui_MainWindow  # File UI chuyển từ info.ui


class InfoWindow(QMainWindow):
    def __init__(self, user_id, parent=None):
        """
        :param user_id: user_id trong bảng users
        """
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Thông tin khách hàng")
        self.user_id = user_id
        self.photo_path = None  # Lưu đường dẫn ảnh hiện hành

        # Nạp thông tin khách hàng từ database
        self.load_customer_info()

        # Kết nối sự kiện
        self.ui.pushButton_cancel.setHidden(True)
        self.ui.pushButton_choosePhoto.clicked.connect(self.choose_photo)
        self.ui.pushButton_save.clicked.connect(self.save_info)
        self.ui.pushButton_cancel.clicked.connect(self.go_home)

    def go_home(self):
        parent = self.parent()
        if parent is not None and hasattr(parent, "home_page"):
            parent.setCurrentWidget(parent.home_page)
        else:
            self.close()

    def setCircularPixmap(self, pixmap):
        """
        Cắt ảnh thành hình tròn dựa theo kích thước của label_photo
        và đặt ảnh đã cắt lên label.
        """
        size = self.ui.label_photo.size()
        circular = QPixmap(size)
        circular.fill(Qt.transparent)

        painter = QPainter(circular)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        path.addEllipse(0, 0, size.width(), size.height())
        painter.setClipPath(path)

        scaled = pixmap.scaled(size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        painter.drawPixmap(0, 0, scaled)
        painter.end()

        self.ui.label_photo.setPixmap(circular)

    def load_customer_info(self):
        """Lấy thông tin khách hàng từ bảng KhachHang dựa theo user_id và điền lên các widget."""
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor(dictionary=True)
                query = "SELECT * FROM KhachHang WHERE user_id = %s"
                cursor.execute(query, (self.user_id,))
                record = cursor.fetchone()
                if record:
                    self.ui.lineEdit_hoTen.setText(record.get("HoTen", ""))
                    self.ui.lineEdit_sdt.setText(record.get("SDT", ""))
                    self.ui.lineEdit_email.setText(record.get("Email", ""))
                    self.ui.textEdit_diaChi.setPlainText(record.get("DiaChi", ""))

                    # Ngày đăng ký
                    ngayDangKy = record.get("NgayDangKy")
                    if ngayDangKy:
                        if isinstance(ngayDangKy, (datetime.date, datetime.datetime)):
                            qdate = QDate(ngayDangKy.year, ngayDangKy.month, ngayDangKy.day)
                        else:
                            qdate = QDate.fromString(ngayDangKy, "yyyy-MM-dd")
                        self.ui.dateEdit_ngayDangKy.setDate(qdate)

                    # Ảnh đại diện
                    anh = record.get("Anh")
                    if anh and os.path.exists(anh):
                        pixmap = QPixmap(anh)
                        self.setCircularPixmap(pixmap)
                        self.photo_path = anh
                    else:
                        self.ui.label_photo.setText("No Image")
                else:
                    QMessageBox.warning(self, "Warning", "Không tìm thấy thông tin khách hàng.")
                cursor.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi tải thông tin: {e}")
        finally:
            if conn.is_connected():
                conn.close()

    def choose_photo(self):
        """Mở hộp thoại chọn ảnh và cập nhật ảnh khách hàng theo hình tròn."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Chọn ảnh", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            dest_folder = os.path.join(os.getcwd(), "img")
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            filename = os.path.basename(file_path)
            dest_path = os.path.join(dest_folder, filename)
            try:
                shutil.copy(file_path, dest_path)
                relative_path = os.path.join(".", "img", filename)
                self.photo_path = relative_path
                pixmap = QPixmap(dest_path)
                self.setCircularPixmap(pixmap)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Lỗi sao chép ảnh: {e}")

    def save_info(self):
        """Lưu lại các thay đổi thông tin khách hàng vào database."""
        hoTen = self.ui.lineEdit_hoTen.text().strip()
        sdt = self.ui.lineEdit_sdt.text().strip()
        email = self.ui.lineEdit_email.text().strip()
        diaChi = self.ui.textEdit_diaChi.toPlainText().strip()
        ngayDangKy = self.ui.dateEdit_ngayDangKy.date().toString("yyyy-MM-dd")
        photo = self.photo_path  # có thể None nếu chưa chọn ảnh

        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()

                # Cập nhật bảng KhachHang
                query_customer = """
                    UPDATE KhachHang 
                    SET HoTen = %s, SDT = %s, Email = %s, DiaChi = %s, NgayDangKy = %s, Anh = %s 
                    WHERE user_id = %s
                """
                cursor.execute(query_customer, (hoTen, sdt, email, diaChi, ngayDangKy, photo, self.user_id))

                # Đồng bộ email và cập nhật updated_at trong bảng users
                query_user = """
                    UPDATE users 
                    SET email = %s, updated_at = NOW() 
                    WHERE user_id = %s
                """
                cursor.execute(query_user, (email, self.user_id))

                conn.commit()
                QMessageBox.information(self, "Success", "Thông tin đã được cập nhật thành công!")
                cursor.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi cập nhật: {e}")
        finally:
            if conn.is_connected():
                conn.close()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = InfoWindow(user_id=1)
#     window.show()
#     sys.exit(app.exec())
