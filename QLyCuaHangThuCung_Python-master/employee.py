import os
import shutil
from PySide6.QtCore import QCoreApplication, QMetaObject, Qt, QDate
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGroupBox, QHBoxLayout, QLabel,
                               QLineEdit, QMainWindow, QMessageBox, QPushButton, QSpacerItem,
                               QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QFileDialog)
from mysql.connector import Error
from config.connectDB import connect_db
from ui.ui_employee import Ui_EmployeeWindow
import pandas as pd


class EmployeePage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_EmployeeWindow()
        self.ui.setupUi(self)
        
        # Biến lưu đường dẫn ảnh được chọn
        self.current_image_path = ""
        
        # Kết nối các nút chức năng với hàm xử lý
        self.ui.imgpathButton.clicked.connect(self.choose_image)
        self.ui.addButton.clicked.connect(self.add_employee)
        self.ui.fixButton.clicked.connect(self.update_employee)
        self.ui.deleteButton.clicked.connect(self.delete_employee)
        self.ui.employeeTable.itemClicked.connect(self.load_employee_details)
        self.ui.excelButton.clicked.connect(self.import_from_excel)
        
        # Load dữ liệu nhân viên vào bảng
        self.load_employees()

    def choose_image(self):
        """Mở hộp thoại chọn ảnh, copy ảnh vào folder 'img' và cập nhật ảnh lên label."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Choose Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            dest_folder = os.path.join(os.getcwd(), "img")
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            filename = os.path.basename(file_path)
            dest_path = os.path.join(dest_folder, filename)
            try:
                shutil.copy(file_path, dest_path)
                # Lưu đường dẫn tương đối để hiển thị trong DB
                relative_path = os.path.join(".", "img", filename)
                self.current_image_path = relative_path
                self.ui.photoLabel.setPixmap(QPixmap(dest_path))
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Không thể sao chép hình ảnh: {e}")

    def add_employee(self):
        """Lấy thông tin từ các ô nhập, lưu ảnh (nếu có) và chèn bản ghi mới vào bảng NhanVien."""
        name = self.ui.nameInput.text().strip()
        phone = self.ui.phoneInput.text().strip()
        email = self.ui.emailInput.text().strip()
        position = self.ui.positionCombo.currentText()
        salary = self.ui.salaryInput.text().strip()
        start_date = self.ui.startDateEdit.date().toString("yyyy-MM-dd")
        image_path = self.current_image_path
        
        if not name or not phone or not salary:
            QMessageBox.warning(self, "Warning", "Vui lòng điền vào tất cả các trường bắt buộc!")
            return
        
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                query = ("INSERT INTO NhanVien (HoTen, SDT, Email, ChucVu, Luong, Anh, NgayVaoLam) "
                         "VALUES (%s, %s, %s, %s, %s, %s, %s)")
                cursor.execute(query, (name, phone, email, position, salary, image_path, start_date))
                conn.commit()
                QMessageBox.information(self, "Success", "Nhân viên đã được thêm thành công!")
                self.clear_fields()
                self.load_employees()
        except Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def update_employee(self):
        """Cập nhật thông tin nhân viên dựa trên MaNV được chọn."""
        emp_id = self.ui.idInput.text().strip()
        if not emp_id:
            QMessageBox.warning(self, "Warning", "Vui lòng chọn một nhân viên để cập nhật.!")
            return
        
        name = self.ui.nameInput.text().strip()
        phone = self.ui.phoneInput.text().strip()
        email = self.ui.emailInput.text().strip()
        position = self.ui.positionCombo.currentText()
        salary = self.ui.salaryInput.text().strip()
        start_date = self.ui.startDateEdit.date().toString("yyyy-MM-dd")
        image_path = self.current_image_path
        
        if not name or not phone or not salary:
            QMessageBox.warning(self, "Warning", "Vui lòng điền vào tất cả các trường bắt buộc!")
            return
        
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                query = ("UPDATE NhanVien SET HoTen = %s, SDT = %s, Email = %s, ChucVu = %s, Luong = %s, Anh = %s, NgayVaoLam = %s "
                         "WHERE MaNV = %s")
                cursor.execute(query, (name, phone, email, position, salary, image_path, start_date, emp_id))
                conn.commit()
                QMessageBox.information(self, "Success", "Nhân viên đã cập nhật thành công!")
                self.clear_fields()
                self.load_employees()
        except Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def delete_employee(self):
        """Xóa nhân viên dựa trên MaNV được chọn sau khi xác nhận."""
        emp_id = self.ui.idInput.text().strip()
        if not emp_id:
            QMessageBox.warning(self, "Warning", "Vui lòng chọn một nhân viên để xóa!")
            return
        
        reply = QMessageBox.question(self, "Confirm Delete", "Bạn có chắc chắn muốn xóa nhân viên này không?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                conn = connect_db()
                if conn.is_connected():
                    cursor = conn.cursor()
                    query = "DELETE FROM NhanVien WHERE MaNV = %s"
                    cursor.execute(query, (emp_id,))
                    conn.commit()
                    QMessageBox.information(self, "Success", "Nhân viên đã xóa thành công!")
                    self.clear_fields()
                    self.load_employees()
            except Error as e:
                QMessageBox.critical(self, "Database Error", f"Error: {e}")
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()

    def load_employees(self):
        """Lấy danh sách nhân viên từ bảng NhanVien và hiển thị vào bảng."""
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute("SELECT MaNV, HoTen, SDT, Email, ChucVu, Luong, Anh, NgayVaoLam FROM NhanVien")
                rows = cursor.fetchall()
                self.ui.employeeTable.setRowCount(0)
                for row_data in rows:
                    row_number = self.ui.employeeTable.rowCount()
                    self.ui.employeeTable.insertRow(row_number)
                    for column, data in enumerate(row_data):
                        item = QTableWidgetItem(str(data))
                        self.ui.employeeTable.setItem(row_number, column, item)
        except Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def load_employee_details(self, item):
        """Khi click vào 1 dòng trong bảng, điền dữ liệu lên các ô nhập tương ứng."""
        row = item.row()
        self.ui.idInput.setText(self.ui.employeeTable.item(row, 0).text())
        self.ui.nameInput.setText(self.ui.employeeTable.item(row, 1).text())
        self.ui.phoneInput.setText(self.ui.employeeTable.item(row, 2).text())
        self.ui.emailInput.setText(self.ui.employeeTable.item(row, 3).text())
        position = self.ui.employeeTable.item(row, 4).text()
        index = self.ui.positionCombo.findText(position)
        if index != -1:
            self.ui.positionCombo.setCurrentIndex(index)
        self.ui.salaryInput.setText(self.ui.employeeTable.item(row, 5).text())
        image_path = self.ui.employeeTable.item(row, 6).text()
        self.current_image_path = image_path
        if image_path and os.path.exists(image_path):
            self.ui.photoLabel.setPixmap(QPixmap(image_path))
        else:
            self.ui.photoLabel.setPixmap(QPixmap("user-placeholder.png"))
        date_str = self.ui.employeeTable.item(row, 7).text()
        if date_str:
            date = QDate.fromString(date_str, "yyyy-MM-dd")
            self.ui.startDateEdit.setDate(date)

    def clear_fields(self):
        """Xóa các ô nhập sau khi thêm/sửa/xóa nhân viên."""
        self.ui.idInput.clear()
        self.ui.nameInput.clear()
        self.ui.phoneInput.clear()
        self.ui.emailInput.clear()
        self.ui.salaryInput.clear()
        self.ui.startDateEdit.setDate(QDate.currentDate())
        self.current_image_path = ""
        self.ui.photoLabel.setPixmap(QPixmap("user-placeholder.png"))
        self.ui.positionCombo.setCurrentIndex(0)

    def import_from_excel(self):
        """
        Nhập dữ liệu nhân viên từ file Excel và thêm vào database.
        File Excel cần có các cột: HoTen, SDT, Email, ChucVu, Luong, Anh, NgayVaoLam.
        Nếu cột NgayVaoLam bị thiếu hoặc rỗng thì sẽ lấy ngày hiện tại.
        """
        file_path, _ = QFileDialog.getOpenFileName(self, "Import Excel File", "", "Excel Files (*.xlsx *.xls)")
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
                    position = str(row['ChucVu']).strip() if 'ChucVu' in row.index else ""
                    salary = str(row['Luong']).strip() if 'Luong' in row.index else ""
                    image_path = str(row['Anh']).strip() if 'Anh' in row.index else ""
                    start_date = row['NgayVaoLam'] if 'NgayVaoLam' in row.index else None

                    if pd.isnull(start_date) or start_date is None:
                        start_date = QDate.currentDate().toString("yyyy-MM-dd")
                    else:
                        start_date = pd.to_datetime(start_date).strftime("%Y-%m-%d")

                    # Bỏ qua các bản ghi thiếu các trường bắt buộc
                    if not name or not phone or not salary:
                        continue

                    query = ("INSERT INTO NhanVien (HoTen, SDT, Email, ChucVu, Luong, Anh, NgayVaoLam) "
                             "VALUES (%s, %s, %s, %s, %s, %s, %s)")
                    cursor.execute(query, (name, phone, email, position, salary, image_path, start_date))
                conn.commit()
                QMessageBox.information(self, "Success", "Dữ liệu đã được nhập từ Excel thành công!")
                self.load_employees()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi nhập dữ liệu từ Excel: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     window = EmployeePage()
#     window.show()
#     sys.exit(app.exec())