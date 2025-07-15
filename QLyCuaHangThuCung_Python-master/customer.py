import os
import shutil
import pandas as pd
from PySide6.QtCore import QDate
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QFileDialog
)
from mysql.connector import Error
from config.connectDB import connect_db
from ui.ui_customer import Ui_CustomerWindow  # đảm bảo file này tồn tại và đã thiết kế UI

class CustomerPage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CustomerWindow()
        self.ui.setupUi(self)
        
        # Biến lưu đường dẫn ảnh được chọn
        self.current_image_path = ""
        
        # Kết nối các nút chức năng với hàm xử lý
        self.ui.imgpathButton.clicked.connect(self.choose_image)
        self.ui.addButton.clicked.connect(self.add_customer)
        self.ui.fixButton.clicked.connect(self.update_customer)
        self.ui.deleteButton.clicked.connect(self.delete_customer)
        self.ui.customerTable.itemClicked.connect(self.load_customer_details)
        self.ui.excelButton.clicked.connect(self.import_from_excel)
        
        # Load dữ liệu khách hàng vào bảng
        self.load_customers()

    def choose_image(self):
        """Mở hộp thoại chọn ảnh, copy ảnh vào folder 'img' và cập nhật ảnh lên label."""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Choose Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)"
        )
        if file_path:
            dest_folder = os.path.join(os.getcwd(), "img")
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            filename = os.path.basename(file_path)
            dest_path = os.path.join(dest_folder, filename)
            try:
                shutil.copy(file_path, dest_path)
                # Lưu đường dẫn tương đối để lưu vào DB
                relative_path = os.path.join(".", "img", filename)
                self.current_image_path = relative_path
                self.ui.photoLabel.setPixmap(QPixmap(dest_path))
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Không thể sao chép hình ảnh: {e}")

    def add_customer(self):
        """Lấy thông tin từ các ô nhập, lưu ảnh (nếu có) và chèn bản ghi mới vào bảng KhachHang."""
        name = self.ui.nameInput.text().strip()
        phone = self.ui.phoneInput.text().strip()
        email = self.ui.emailInput.text().strip()
        address = self.ui.addressInput.toPlainText().strip()
        registration_date = self.ui.registerDateEdit.date().toString("yyyy-MM-dd")
        image_path = self.current_image_path

        if not name or not phone:
            QMessageBox.warning(self, "Warning", "Vui lòng điền vào các trường bắt buộc (Họ tên và SĐT)!")
            return

        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                query = ("INSERT INTO KhachHang (HoTen, SDT, Email, DiaChi, Anh, NgayDangKy) "
                         "VALUES (%s, %s, %s, %s, %s, %s)")
                cursor.execute(query, (name, phone, email, address, image_path, registration_date))
                conn.commit()
                QMessageBox.information(self, "Success", "Khách hàng đã được thêm thành công!")
                self.clear_fields()
                self.load_customers()
        except Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def update_customer(self):
        """Cập nhật thông tin khách hàng dựa trên MaKH được chọn."""
        cust_id = self.ui.idInput.text().strip()
        if not cust_id:
            QMessageBox.warning(self, "Warning", "Vui lòng chọn khách hàng để cập nhật!")
            return

        name = self.ui.nameInput.text().strip()
        phone = self.ui.phoneInput.text().strip()
        email = self.ui.emailInput.text().strip()
        address = self.ui.addressInput.toPlainText().strip()
        registration_date = self.ui.registerDateEdit.date().toString("yyyy-MM-dd")
        image_path = self.current_image_path

        if not name or not phone:
            QMessageBox.warning(self, "Warning", "Vui lòng điền vào các trường bắt buộc (Họ tên và SĐT)!")
            return

        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                query = ("UPDATE KhachHang SET HoTen = %s, SDT = %s, Email = %s, DiaChi = %s, Anh = %s, NgayDangKy = %s "
                         "WHERE MaKH = %s")
                cursor.execute(query, (name, phone, email, address, image_path, registration_date, cust_id))
                conn.commit()
                QMessageBox.information(self, "Success", "Khách hàng đã được cập nhật thành công!")
                self.clear_fields()
                self.load_customers()
        except Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def delete_customer(self):
        """Xóa khách hàng dựa trên MaKH được chọn sau khi xác nhận và xóa luôn người dùng tương ứng trong bảng users."""
        cust_id = self.ui.idInput.text().strip()
        if not cust_id:
            QMessageBox.warning(self, "Warning", "Vui lòng chọn khách hàng để xóa!")
            return

        reply = QMessageBox.question(
            self, "Confirm Delete", "Bạn có chắc chắn muốn xóa khách hàng này không?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            try:
                conn = connect_db()
                if conn.is_connected():
                    # Sử dụng cursor với dictionary=True để lấy user_id
                    cursor = conn.cursor(dictionary=True)
                    # Lấy user_id từ KhachHang dựa trên MaKH
                    select_query = "SELECT user_id FROM KhachHang WHERE MaKH = %s"
                    cursor.execute(select_query, (cust_id,))
                    result = cursor.fetchone()
                    user_id = result.get("user_id") if result else None

                    # Xóa khách hàng từ bảng KhachHang
                    delete_query = "DELETE FROM KhachHang WHERE MaKH = %s"
                    cursor.execute(delete_query, (cust_id,))
                    conn.commit()

                    # Nếu có user_id, xóa người dùng tương ứng từ bảng users
                    if user_id:
                        delete_user_query = "DELETE FROM users WHERE id = %s"
                        cursor.execute(delete_user_query, (user_id,))
                        conn.commit()

                    QMessageBox.information(self, "Success", "Khách hàng và người dùng liên quan đã được xóa thành công!")
                    self.clear_fields()
                    self.load_customers()
                    cursor.close()
            except Error as e:
                QMessageBox.critical(self, "Database Error", f"Error: {e}")
            finally:
                if conn.is_connected():
                    conn.close()

    def load_customers(self):
        """Lấy danh sách khách hàng từ bảng KhachHang và hiển thị vào bảng."""
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute("SELECT MaKH, HoTen, SDT, Email, DiaChi, Anh, NgayDangKy FROM KhachHang")
                rows = cursor.fetchall()
                self.ui.customerTable.setRowCount(0)
                for row_data in rows:
                    row_number = self.ui.customerTable.rowCount()
                    self.ui.customerTable.insertRow(row_number)
                    for column, data in enumerate(row_data):
                        item = QTableWidgetItem(str(data))
                        self.ui.customerTable.setItem(row_number, column, item)
        except Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def load_customer_details(self, item):
        """Khi click vào 1 dòng trong bảng, điền dữ liệu lên các ô nhập tương ứng."""
        row = item.row()
        self.ui.idInput.setText(self.ui.customerTable.item(row, 0).text())
        self.ui.nameInput.setText(self.ui.customerTable.item(row, 1).text())
        self.ui.phoneInput.setText(self.ui.customerTable.item(row, 2).text())
        self.ui.emailInput.setText(self.ui.customerTable.item(row, 3).text())
        self.ui.addressInput.setText(self.ui.customerTable.item(row, 4).text())
        
        image_path = self.ui.customerTable.item(row, 5).text()
        self.current_image_path = image_path
        if image_path and os.path.exists(image_path):
            self.ui.photoLabel.setPixmap(QPixmap(image_path))
        else:
            self.ui.photoLabel.setPixmap(QPixmap("user-placeholder.png"))
        
        date_str = self.ui.customerTable.item(row, 6).text()
        if date_str:
            date = QDate.fromString(date_str, "yyyy-MM-dd")
            self.ui.registerDateEdit.setDate(date)

    def clear_fields(self):
        """Xóa các ô nhập sau khi thêm/sửa/xóa khách hàng."""
        self.ui.idInput.clear()
        self.ui.nameInput.clear()
        self.ui.phoneInput.clear()
        self.ui.emailInput.clear()
        self.ui.addressInput.clear()
        self.ui.registerDateEdit.date().toString("yyyy-MM-dd")
        self.current_image_path = ""
        self.ui.photoLabel.setPixmap(QPixmap("user-placeholder.png"))

    def import_from_excel(self):
        """
        Nhập dữ liệu khách hàng từ file Excel và thêm vào database.
        File Excel cần có các cột: HoTen, SDT, Email, DiaChi, Anh, NgayDangKy.
        Nếu cột NgayDangKy bị thiếu hoặc rỗng thì sẽ lấy ngày hiện tại.
        """
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Import Excel File", "", "Excel Files (*.xlsx *.xls)"
        )
        if not file_path:
            return

        try:
            df = pd.read_excel(file_path)
            if df.empty:
                QMessageBox.warning(self, "Warning", "File Excel trống!")
                return

            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                for index, row in df.iterrows():
                    # Lấy dữ liệu từ các cột trong file Excel
                    name = str(row['HoTen']).strip() if 'HoTen' in row.index else ""
                    phone = str(row['SDT']).strip() if 'SDT' in row.index else ""
                    email = str(row['Email']).strip() if 'Email' in row.index else ""
                    address = str(row['DiaChi']).strip() if 'DiaChi' in row.index else ""
                    image_path = str(row['Anh']).strip() if 'Anh' in row.index else ""
                    reg_date = row['NgayDangKy'] if 'NgayDangKy' in row.index else None

                    if pd.isnull(reg_date) or reg_date is None:
                        reg_date = QDate.currentDate().toString("yyyy-MM-dd")
                    else:
                        reg_date = pd.to_datetime(reg_date).strftime("%Y-%m-%d")

                    # Bỏ qua các bản ghi thiếu các trường bắt buộc
                    if not name or not phone:
                        continue

                    query = ("INSERT INTO KhachHang (HoTen, SDT, Email, DiaChi, Anh, NgayDangKy) "
                             "VALUES (%s, %s, %s, %s, %s, %s)")
                    cursor.execute(query, (name, phone, email, address, image_path, reg_date))
                conn.commit()
                QMessageBox.information(self, "Success", "Dữ liệu đã được nhập từ Excel thành công!")
                self.load_customers()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi nhập dữ liệu từ Excel: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()


# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     window = CustomerPage()
#     window.show()
#     sys.exit(app.exec())
