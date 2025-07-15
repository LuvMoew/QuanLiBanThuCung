import os
import shutil
import pandas as pd
from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QFileDialog,
    QWidget, QLabel, QVBoxLayout, QFrame
)
from mysql.connector import Error
from config.connectDB import connect_db
from ui.ui_pet import Ui_PetWindow  # File UI cho trang Pet, có QStackedWidget chứa 2 trang: petManagementPage và productPage

class PetPage(QMainWindow):
    def __init__(self, user_role=None, parent=None):
        super().__init__(parent)
        self.user_role = user_role
        self.ui = Ui_PetWindow()
        self.ui.setupUi(self)
        self.current_image_path = ""
        
        # Kiểm tra role của user: nếu "customer" thì hiển thị widget productPage
        if self.user_role == "customer":
            # Giả sử trong QStackedWidget có widget productPage
            self.ui.stackedWidget.setCurrentWidget(self.ui.productPage)
            self.filter_products()
            self.ui.comboSort.currentIndexChanged.connect(self.filter_products)
            # Ẩn các nút chức năng quản lý (không cần thiết cho khách hàng)
            self.ui.btnAdd.hide()
            self.ui.btnEdit.hide()
            self.ui.btnDelete.hide()
            self.ui.imgpathButton.hide()
            self.ui.btnExcel.hide()
            # Nếu cần, ẩn cả table hiển thị thú cưng quản lý
            # self.ui.tablePets.hide()
            self.load_products()
        else:
            # Nếu không phải customer thì hiển thị trang quản lý thú cưng (petPage)
            self.ui.stackedWidget.setCurrentWidget(self.ui.petPage)
            self.ui.imgpathButton.clicked.connect(self.choose_image)
            self.ui.btnAdd.clicked.connect(self.add_pet)
            self.ui.btnEdit.clicked.connect(self.update_pet)
            self.ui.btnDelete.clicked.connect(self.delete_pet)
            self.ui.tablePets.itemClicked.connect(self.load_pet_details)
            self.ui.btnExcel.clicked.connect(self.import_from_excel)
            self.load_pets()

    def load_products(self):
        """
        Lấy danh sách thú cưng từ database và hiển thị trong productGrid của productPage.
        Chỉ được gọi khi user có role là "customer".
        """
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor(dictionary=True)
                # Lấy các trường cần thiết: MaThuCung, TenThuCung, Anh, GiaBan, TinhTrang
                query = "SELECT MaThuCung, TenThuCung, Anh, GiaBan, TinhTrang, MoTa FROM ThuCung"
                cursor.execute(query)
                records = cursor.fetchall()

                # Xóa hết các widget cũ trong productGrid
                layout = self.ui.productGrid
                # Căn chỉnh layout từ góc trên bên trái
                layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                        widget.deleteLater()

                # Thêm các sản phẩm vào grid (ví dụ 3 cột)
                row = 0
                col = 0
                for rec in records:
                    product_widget = self.create_product_widget(rec)
                    layout.addWidget(product_widget, row, col)
                    col += 1
                    if col >= 3:
                        col = 0
                        row += 1

                cursor.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi tải sản phẩm: {e}")
        finally:
            if conn.is_connected():
                conn.close()

    def create_product_widget(self, record):
        """
        Tạo widget hiển thị thông tin sản phẩm với giao diện nâng cao
        """
        # Widget chính 
        widget = QFrame()
        widget.setFixedSize(220, 280)
        widget.setStyleSheet("""
            QFrame {
                background-color: #e2b4b7;
                border-radius: 12px;
                border: 1px solid #e0e0e0;
            }
            QFrame:hover {
                border: 1px solid #bdbdbd;
            }
        """)
        
        # layout chính 
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(8)
        layout.setAlignment(Qt.AlignTop)
        
        # container chứa ảnh 
        image_frame = QFrame()
        image_frame.setStyleSheet("""
            QFrame {
                background-color: #f5f5f5;
                border-radius: 8px;
                border: 1px solid #eeeeee;
            }
        """)
        image_frame.setFixedSize(204, 180)
        
        image_layout = QVBoxLayout(image_frame)
        image_layout.setContentsMargins(0, 0, 0, 0)
        
        image_label = QLabel()
        image_label.setAlignment(Qt.AlignCenter)
        
        # Thêm description label
        desc_label = QLabel()
        desc_label.setAlignment(Qt.AlignCenter)
        desc_label.setWordWrap(True)
        desc_label.setStyleSheet("""
            QLabel {
                color: #212121;
                font-size: 10pt;
                padding: 10px;
                background-color: white;
                border-radius: 8px;
            }
        """)
        desc_label.hide()  # Ẩn mô tả ban đầu
        
        # Tải và thiết lập hình ảnh với tỷ lệ phù hợp
        image_path = record.get("Anh", "")
        if image_path and os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            scaled_pixmap = pixmap.scaled(180, 160, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            image_label.setPixmap(scaled_pixmap)
        else:
            image_label.setPixmap(QPixmap("user-placeholder.png").scaled(180, 160, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        
        # Thêm cả image_label và desc_label vào image_layout
        image_layout.addWidget(image_label)
        image_layout.addWidget(desc_label)
        
        status_text = record.get("TinhTrang", "")
        status_label = QLabel(status_text)
        status_color = "#a0c9c3" if status_text.lower() == "good" else "#efd174"
        status_label.setStyleSheet(f"""
            QLabel {{
                background-color: {status_color};
                color: white;
                padding: 4px 10px;
                border-radius: 5px;
                font-size: 10pt;
                font-weight: bold;
            }}
        """)
        status_label.setFixedHeight(22)
        
        # Đặt nhãn trạng thái vị trí ở góc trên bên phải của hình ảnh.
        status_label.setParent(image_frame)
        status_label.adjustSize()
        status_label.move(image_frame.width() - status_label.width() - 8, 8)
        
        info_container = QWidget()
        info_container.setFixedWidth(204)  # Khớp chiều rộng với parent 
        info_layout = QVBoxLayout(info_container)
        info_layout.setContentsMargins(0, 10, 0, 10) 
        info_layout.setSpacing(10)
        info_layout.setAlignment(Qt.AlignLeft) 
        info_container.setStyleSheet("""
            QWidget {
                background-color: #e2b4b7;
            }
        """)
        info_container.setCursor(Qt.PointingHandCursor)
        
        name_label = QLabel(record.get("TenThuCung", ""))
        name_label.setStyleSheet("""
            QLabel {
                font-weight: bold;
                font-size: 12pt;
                color: #212121;
                padding: 0px;
                margin: 0px;
                border: none;
            }
        """)
        name_label.setAlignment(Qt.AlignLeft) 
        name_label.setWordWrap(False)
        name_label.setFixedWidth(196)  # Account for parent padding
        metrics = name_label.fontMetrics()
        text = metrics.elidedText(record.get("TenThuCung", ""), Qt.ElideRight, 196)
        name_label.setText("Tên: " + text)
        
        price_value = float(record.get("GiaBan", 0))
        formatted_price = "{:,.0f}".format(price_value)
        price_label = QLabel(f"{formatted_price} VND")
        price_label.setStyleSheet("""
            QLabel {
                color: #657d81;
                font-size: 11pt;
                font-weight: bold;
                padding: 0px;
                margin: 0px;
                border: none;
            }
        """)
        price_label.setAlignment(Qt.AlignLeft)  # căn trái chữ 
        
        info_layout.addWidget(name_label)
        info_layout.addWidget(price_label)
        
        #Thêm các thành phần vào layout chính 
        layout.addWidget(image_frame)
        layout.addWidget(info_container)
        layout.addStretch()
        
        # Tạo biến để theo dõi trạng thái hiển thị
        info_container.is_showing_image = True
        
        # Set mô tả cho desc_label
        desc_text = record.get("MoTa", "Không có mô tả") 
        desc_label.setText(desc_text)
        
        # Xử lý sự kiện click
        def toggle_display():
            if info_container.is_showing_image:
                image_label.hide()
                desc_label.show()
            else:
                desc_label.hide()
                image_label.show()
            info_container.is_showing_image = not info_container.is_showing_image
        
        info_container.mousePressEvent = lambda event: toggle_display()
        
        return widget    
    def filter_products(self):
        """
        Lấy giá trị từ comboSort, nếu != "All" thì lọc theo Loai,
        ngược lại lấy tất cả. Sau đó hiển thị các sản phẩm lên productGrid.
        """
        selected_value = self.ui.comboSort.currentText()

        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor(dictionary=True)
                # Query cơ bản
                base_query = "SELECT MaThuCung, TenThuCung, Anh, GiaBan, TinhTrang, Loai FROM ThuCung"
                
                if selected_value != "All":
                    # Lọc theo cột Loai
                    query = base_query + " WHERE Loai = %s"
                    cursor.execute(query, (selected_value,))
                else:
                    # Lấy tất cả
                    cursor.execute(base_query)
                
                records = cursor.fetchall()

                # Xóa các widget cũ trong productGrid
                layout = self.ui.productGrid
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                        widget.deleteLater()

                # Thêm các sản phẩm vào grid (3 cột, ví dụ)
                row = 0
                col = 0
                for rec in records:
                    product_widget = self.create_product_widget(rec)
                    layout.addWidget(product_widget, row, col)
                    col += 1
                    if col >= 3:
                        col = 0
                        row += 1

                cursor.close()
        except Exception as e:
            print(e)
        finally:
            if conn.is_connected():
                conn.close()

    def choose_image(self):
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
                self.ui.imagePreview.setPixmap(QPixmap(dest_path))
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Không thể sao chép hình ảnh: {e}")

    def add_pet(self):
        """Lấy thông tin từ các ô nhập và chèn bản ghi mới vào bảng ThuCung."""
        name = self.ui.lineEditTenThuCung.text().strip()
        pet_type = self.ui.comboBoxLoai.currentText()    # Ví dụ: Chó, Mèo, Hamster,...
        gender = self.ui.comboBoxGioiTinh.currentText()     # 'Đực' hoặc 'Cái'
        birth_date = self.ui.dateEditNgaySinh.date().toString("yyyy-MM-dd")
        price = self.ui.lineEditGiaBan.text().strip()
        status = self.ui.lineEditTinhTrang.text().strip()
        description = self.ui.textEditMoTa.toPlainText().strip()
        image_path = self.current_image_path
        
        if not name or not pet_type or not gender:
            QMessageBox.warning(self, "Warning", "Vui lòng điền vào các trường bắt buộc!")
            return
        
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                query = (
                    "INSERT INTO ThuCung (TenThuCung, Loai, GioiTinh, NgaySinh, GiaBan, TinhTrang, MoTa, Anh) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                )
                cursor.execute(query, (name, pet_type, gender, birth_date, price, status, description, image_path))
                conn.commit()
                QMessageBox.information(self, "Success", "Thú cưng đã được thêm thành công!")
                self.clear_fields()
                self.load_pets()
        except Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def update_pet(self):
        """Cập nhật thông tin thú cưng dựa trên MaThuCung được chọn."""
        pet_id = self.ui.lineEditMaThuCung.text().strip()
        if not pet_id:
            QMessageBox.warning(self, "Warning", "Vui lòng chọn một thú cưng để cập nhật!")
            return
        
        name = self.ui.lineEditTenThuCung.text().strip()
        pet_type = self.ui.comboBoxLoai.currentText()
        gender = self.ui.comboBoxGioiTinh.currentText()
        birth_date = self.ui.dateEditNgaySinh.date().toString("yyyy-MM-dd")
        price = self.ui.lineEditGiaBan.text().strip()
        status = self.ui.lineEditTinhTrang.text().strip()
        description = self.ui.textEditMoTa.toPlainText().strip()
        image_path = self.current_image_path
        
        if not name or not pet_type or not gender:
            QMessageBox.warning(self, "Warning", "Vui lòng điền vào các trường bắt buộc!")
            return
        
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                query = (
                    "UPDATE ThuCung SET TenThuCung = %s, Loai = %s, GioiTinh = %s, NgaySinh = %s, GiaBan = %s, TinhTrang = %s, MoTa = %s, Anh = %s "
                    "WHERE MaThuCung = %s"
                )
                cursor.execute(query, (name, pet_type, gender, birth_date, price, status, description, image_path, pet_id))
                conn.commit()
                QMessageBox.information(self, "Success", "Thú cưng đã được cập nhật thành công!")
                self.clear_fields()
                self.load_pets()
        except Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def delete_pet(self):
        """Xóa thú cưng dựa trên MaThuCung được chọn sau khi xác nhận."""
        pet_id = self.ui.lineEditMaThuCung.text().strip()
        if not pet_id:
            QMessageBox.warning(self, "Warning", "Vui lòng chọn một thú cưng để xóa!")
            return
        
        reply = QMessageBox.question(self, "Confirm Delete", "Bạn có chắc chắn muốn xóa thú cưng này không?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                conn = connect_db()
                if conn.is_connected():
                    cursor = conn.cursor()
                    query = "DELETE FROM ThuCung WHERE MaThuCung = %s"
                    cursor.execute(query, (pet_id,))
                    conn.commit()
                    QMessageBox.information(self, "Success", "Thú cưng đã được xóa thành công!")
                    self.clear_fields()
                    self.load_pets()
            except Error as e:
                QMessageBox.critical(self, "Database Error", f"Error: {e}")
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()

    def load_pets(self):
        """Lấy danh sách thú cưng từ bảng ThuCung và hiển thị vào bảng."""
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute("SELECT MaThuCung, TenThuCung, Loai, GioiTinh, NgaySinh, GiaBan, TinhTrang, MoTa, Anh FROM ThuCung")
                rows = cursor.fetchall()
                self.ui.tablePets.setRowCount(0)
                for row_data in rows:
                    row_number = self.ui.tablePets.rowCount()
                    self.ui.tablePets.insertRow(row_number)
                    for column, data in enumerate(row_data):
                        item = QTableWidgetItem(str(data))
                        self.ui.tablePets.setItem(row_number, column, item)
        except Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def load_pet_details(self, item):
        """Khi click vào 1 dòng trong bảng, điền dữ liệu lên các ô nhập tương ứng."""
        row = item.row()
        self.ui.lineEditMaThuCung.setText(self.ui.tablePets.item(row, 0).text())
        self.ui.lineEditTenThuCung.setText(self.ui.tablePets.item(row, 1).text())
        pet_type = self.ui.tablePets.item(row, 2).text()
        index2 = self.ui.comboBoxLoai.findText(pet_type)
        if index2 != -1:
            self.ui.comboBoxLoai.setCurrentIndex(index2)
        gender = self.ui.tablePets.item(row, 3).text()
        index = self.ui.comboBoxGioiTinh.findText(gender)
        if index != -1:
            self.ui.comboBoxGioiTinh.setCurrentIndex(index)
        birth_date_str = self.ui.tablePets.item(row, 4).text()
        if birth_date_str:
            date = QDate.fromString(birth_date_str, "yyyy-MM-dd")
            self.ui.dateEditNgaySinh.setDate(date)
        self.ui.lineEditGiaBan.setText(self.ui.tablePets.item(row, 5).text())
        self.ui.lineEditTinhTrang.setText(self.ui.tablePets.item(row, 6).text())
        self.ui.textEditMoTa.setPlainText(self.ui.tablePets.item(row, 7).text())
        image_item = self.ui.tablePets.item(row, 8)
        if image_item is not None:
            image_path = image_item.text()
        else:
            image_path = ""
        self.current_image_path = image_path
        if image_path and os.path.exists(image_path):
            self.ui.imagePreview.setPixmap(QPixmap(image_path))
        else:
            self.ui.imagePreview.setPixmap(QPixmap("user-placeholder.png"))

    def clear_fields(self):
        """Xóa các ô nhập sau khi thêm/sửa/xóa thú cưng."""
        self.ui.lineEditMaThuCung.clear()
        self.ui.lineEditTenThuCung.clear()
        self.ui.comboBoxLoai.setCurrentIndex(0)
        self.ui.comboBoxGioiTinh.setCurrentIndex(0)
        self.ui.dateEditNgaySinh.setDate(QDate.currentDate())
        self.ui.lineEditGiaBan.clear()
        self.ui.lineEditTinhTrang.clear()
        self.ui.textEditMoTa.clear()
        self.current_image_path = ""
        self.ui.imagePreview.setPixmap(QPixmap("user-placeholder.png"))

    def import_from_excel(self):
        """
        Nhập dữ liệu thú cưng từ file Excel và thêm vào database.
        File Excel cần có các cột: TenThuCung, Loai, GioiTinh, NgaySinh, GiaBan, TinhTrang, MoTa, Anh.
        Nếu cột NgaySinh bị thiếu hoặc rỗng thì sẽ lấy ngày hiện tại.
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
                    name = str(row['TenThuCung']).strip() if 'TenThuCung' in row.index else ""
                    pet_type = str(row['Loai']).strip() if 'Loai' in row.index else ""
                    gender = str(row['GioiTinh']).strip() if 'GioiTinh' in row.index else ""
                    birth_date = row['NgaySinh'] if 'NgaySinh' in row.index else None
                    if pd.isnull(birth_date) or birth_date is None:
                        birth_date = QDate.currentDate().toString("yyyy-MM-dd")
                    else:
                        birth_date = pd.to_datetime(birth_date).strftime("%Y-%m-%d")
                    price = str(row['GiaBan']).strip() if 'GiaBan' in row.index else ""
                    status = str(row['TinhTrang']).strip() if 'TinhTrang' in row.index else ""
                    description = str(row['MoTa']).strip() if 'MoTa' in row.index else ""
                    image_path = str(row['Anh']).strip() if 'Anh' in row.index else ""
                    if not name or not pet_type or not gender:
                        continue
                    query = (
                        "INSERT INTO ThuCung (TenThuCung, Loai, GioiTinh, NgaySinh, GiaBan, TinhTrang, MoTa, Anh) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    )
                    cursor.execute(query, (name, pet_type, gender, birth_date, price, status, description, image_path))
                conn.commit()
                QMessageBox.information(self, "Success", "Dữ liệu đã được nhập từ Excel thành công!")
                self.load_pets()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi nhập dữ liệu từ Excel: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     window = PetPage(user_role="customer")
#     window.show()
#     sys.exit(app.exec())
