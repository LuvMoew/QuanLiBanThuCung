import os
import shutil
import pandas as pd
from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QMainWindow, QMessageBox, QTableWidgetItem, QFileDialog,
    QWidget, QLabel, QVBoxLayout, QFrame
)
from mysql.connector import Error
from config.connectDB import connect_db
from ui.ui_product import Ui_ProductWindow  # File UI cho trang product

class ProductPage(QMainWindow):
    def __init__(self, user_id=None, user_role=None, parent=None):
        super().__init__(parent)
        self.user_role = user_role
        self.ui = Ui_ProductWindow()
        self.ui.setupUi(self)
        self.current_image_path = ""
        self.current_user_id = user_id 
        
        if self.user_role == "customer":
            # Nếu user là customer thì hiển thị trang danh sách sản phẩm
            self.ui.stackedWidget.setCurrentWidget(self.ui.productListPage)
            self.filter_products()
            self.ui.comboSort.currentIndexChanged.connect(self.filter_products)
            # Ẩn các nút quản lý dành cho admin
            self.ui.btnAdd.hide()
            self.ui.btnEdit.hide()
            self.ui.btnDelete.hide()
            self.ui.imgpathButton.hide()
            self.ui.excelButton.hide()
            self.load_products_grid()
        else:
            # Nếu không phải customer thì hiển thị trang quản lý sản phẩm
            self.ui.stackedWidget.setCurrentWidget(self.ui.productPage)
            self.ui.imgpathButton.clicked.connect(self.choose_image)
            self.ui.btnAdd.clicked.connect(self.add_product)
            self.ui.btnEdit.clicked.connect(self.update_product)
            self.ui.btnDelete.clicked.connect(self.delete_product)
            self.ui.tableProducts.itemClicked.connect(self.load_product_details)
            self.ui.excelButton.clicked.connect(self.import_from_excel)
            self.load_products_table()

    def load_products_grid(self):
        """
        Lấy danh sách sản phẩm từ bảng SanPham và hiển thị dưới dạng grid
        trên trang danh sách (dành cho customer).
        """
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor(dictionary=True)
                query = "SELECT MaSP, TenSP, Anh, Gia, SoLuongTon, MoTa, LoaiSP FROM SanPham Where SoLuongTon > 0"
                cursor.execute(query)
                records = cursor.fetchall()

                # Xóa hết các widget cũ trong layout productGrid
                layout = self.ui.productGrid
                layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                        widget.deleteLater()

                row = 0
                col = 0
                for rec in records:
                    try:
                        product_widget = self.create_product_widget(rec)
                        layout.addWidget(product_widget, row, col)
                        col += 1
                        if col >= 3:  # Ví dụ hiển thị 3 cột
                            col = 0
                            row += 1
                    except Exception as product_err:
                        print(f"Lỗi khi tạo widget cho sản phẩm {rec.get('MaSP', '')}: {product_err}")
                        # Tiếp tục với sản phẩm tiếp theo thay vì dừng toàn bộ quá trình

                cursor.close()
        except Exception as e:
            import traceback
            error_details = traceback.format_exc()
            QMessageBox.critical(self, "Error", f"Lỗi khi tải sản phẩm: {e}\n\nChi tiết: {error_details}")
        finally:
            if 'conn' in locals() and conn.is_connected():
                conn.close()
                
    def create_product_widget(self, record):
        """
        Tạo widget hiển thị thông tin sản phẩm với giao diện nâng cao,
        bao gồm hiển thị số lượng tồn và nút "Thêm vào giỏ hàng".
        Khi nhấn nút, sản phẩm sẽ được thêm vào giỏ hàng (cart).
        """
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

        layout = QVBoxLayout(widget)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(8)
        layout.setAlignment(Qt.AlignTop)

        # Container cho ảnh
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

        # Label mô tả (ẩn ban đầu)
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
        desc_label.hide()

        from PySide6.QtGui import QPixmap
        # Thiết lập ảnh
        image_path = record.get("Anh", "")
        if image_path and os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            scaled_pixmap = pixmap.scaled(180, 160, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            image_label.setPixmap(scaled_pixmap)
        else:
            image_label.setPixmap(QPixmap("user-placeholder.png").scaled(180, 160, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        image_layout.addWidget(image_label)
        image_layout.addWidget(desc_label)

        # Container cho thông tin
        info_container = QWidget()
        info_container.setFixedWidth(204)
        info_layout = QVBoxLayout(info_container)
        info_layout.setContentsMargins(0, 10, 0, 10)
        info_layout.setSpacing(10)
        info_layout.setAlignment(Qt.AlignLeft)
        info_container.setStyleSheet("background-color: #e2b4b7;")
        info_container.setCursor(Qt.PointingHandCursor)

        # Tên sản phẩm
        name_label = QLabel(record.get("TenSP", ""))
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
        name_label.setFixedWidth(196)
        metrics = name_label.fontMetrics()
        text = metrics.elidedText(record.get("TenSP", ""), Qt.ElideRight, 196)
        name_label.setText("Tên: " + text)

        # Giá sản phẩm
        price_value = float(record.get("Gia", 0))
        formatted_price = "{:,.2f}".format(price_value)
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
        price_label.setAlignment(Qt.AlignLeft)

        # Số lượng tồn
        quantity = record.get("SoLuongTon", 0)
        quantity_label = QLabel(f"Tồn: {quantity}")
        quantity_label.setStyleSheet("""
            QLabel {
                color: #333;
                font-size: 10pt;
                padding: 0px;
                margin: 0px;
                border: none;
            }
        """)
        quantity_label.setAlignment(Qt.AlignLeft)

        # Nút thêm vào giỏ hàng
        from PySide6.QtWidgets import QPushButton  # đảm bảo đã import
        add_to_cart_btn = QPushButton("Thêm vào giỏ hàng")
        add_to_cart_btn.setStyleSheet("""
            QPushButton {
                background-color: #6c7ee1;
                color: white;
                border: none;
                padding: 2px;
                border-radius: 4px;
                font-size: 10pt;
            }
            QPushButton:hover {
                background-color: #657d81;
            }
        """)
        add_to_cart_btn.setFixedHeight(30)

        # Kết nối sự kiện cho nút "Thêm vào giỏ hàng"
        add_to_cart_btn.clicked.connect(lambda: self.add_product_to_cart(record))

        # Thêm các widget vào layout thông tin
        info_layout.addWidget(name_label)
        info_layout.addWidget(price_label)
        info_layout.addWidget(quantity_label)
        info_layout.addWidget(add_to_cart_btn)

        layout.addWidget(image_frame)
        layout.addWidget(info_container)
        layout.addStretch()

        # Biến theo dõi trạng thái hiển thị
        info_container.is_showing_image = True
        desc_text = record.get("MoTa", "Không có mô tả")
        desc_label.setText(desc_text)

        # Khi nhấn vào container thì chuyển đổi hiển thị ảnh/mô tả
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
    
    def add_product_to_cart(self, record):
        """
        Thêm sản phẩm vào giỏ hàng và lưu vào database, bao gồm cả MaSP.
        """
        conn = None
        cursor = None
        try:
            # Lấy user_id từ session hoặc login info
            user_id = self.current_user_id  # Giả sử biến này đã được thiết lập từ quá trình đăng nhập

            # Khởi tạo kết nối database
            conn = connect_db()
            cursor = conn.cursor()

            # Chuẩn bị dữ liệu cho database
            ma_sp = record.get("MaSP")  # Lấy MaSP từ record
            if ma_sp is None:
                raise Exception("Mã sản phẩm không hợp lệ!")
            product_image = record.get("Anh", "")
            product_title = record.get("TenSP", "")
            price = float(record.get("Gia", 0))
            quantity = 1  # Số lượng mặc định
            total = price * quantity

            # Kiểm tra xem sản phẩm đã có trong giỏ hàng chưa (so sánh theo MaSP)
            check_query = """
                SELECT id, quantity, total FROM Cart 
                WHERE user_id = %s AND MaSP = %s
            """
            cursor.execute(check_query, (user_id, ma_sp))
            existing_item = cursor.fetchone()

            if existing_item:
                # Nếu sản phẩm đã tồn tại, cập nhật số lượng
                new_quantity = existing_item[1] + 1
                new_total = price * new_quantity
                update_query = """
                    UPDATE Cart 
                    SET quantity = %s, total = %s, updated_at = CURRENT_TIMESTAMP
                    WHERE id = %s
                """
                cursor.execute(update_query, (new_quantity, new_total, existing_item[0]))
            else:
                # Nếu là sản phẩm mới, thêm vào database (bao gồm MaSP)
                insert_query = """
                    INSERT INTO Cart (user_id, MaSP, product_image, product_title, price, quantity, total)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(insert_query, (user_id, ma_sp, product_image, product_title, price, quantity, total))

            conn.commit()

            # Cập nhật giao diện giỏ hàng nếu đang mở
            if hasattr(self, 'cartPage'):
                self.update_cart_display()

            QMessageBox.information(self, "Thành công", "Đã thêm sản phẩm vào giỏ hàng!")

        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Không thể thêm vào giỏ hàng: {str(e)}")
            if conn:
                conn.rollback()
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def update_cart_display(self):
        """
        Cập nhật hiển thị giỏ hàng từ database
        """
        conn = None
        cursor = None
        try:
            conn = connect_db()
            cursor = conn.cursor()

            # Lấy dữ liệu giỏ hàng từ database
            query = """
                SELECT id, product_image, product_title, price, quantity, total, order_details
                FROM Cart WHERE user_id = %s
                ORDER BY created_at DESC
            """
            cursor.execute(query, (self.current_user_id,))
            cart_items = cursor.fetchall()

            # Xóa dữ liệu cũ trong bảng
            self.cart_ui.cartTable.setRowCount(0)

            # Thêm dữ liệu mới vào bảng
            for item in cart_items:
                row = self.cart_ui.cartTable.rowCount()
                self.cart_ui.cartTable.insertRow(row)

                # Thêm từng cột
                self.cart_ui.cartTable.setItem(row, 0, QTableWidgetItem(str(item[0])))  # ID
                self.cart_ui.cartTable.setItem(row, 1, QTableWidgetItem(item[1]))       # Image
                self.cart_ui.cartTable.setItem(row, 2, QTableWidgetItem(item[2]))       # Title
                self.cart_ui.cartTable.setItem(row, 3, QTableWidgetItem(f"{item[3]:,.2f} VND"))  # Price
                self.cart_ui.cartTable.setItem(row, 4, QTableWidgetItem(str(item[4])))  # Quantity
                self.cart_ui.cartTable.setItem(row, 5, QTableWidgetItem(f"{item[5]:,.2f} VND"))  # Total
                self.cart_ui.cartTable.setItem(row, 6, QTableWidgetItem(item[6] or "")) # Details

            # Cập nhật tổng tiền
            if hasattr(self.cartPage, 'update_cart_totals'):
                self.cartPage.update_cart_totals()

        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Không thể cập nhật hiển thị giỏ hàng: {str(e)}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()                
                
    def filter_products(self):
        """
        Lọc sản phẩm theo giá trị chọn từ comboSort.
        Nếu giá trị khác "All" thì lọc theo LoaiSP.
        """
        selected_value = self.ui.comboSort.currentText()
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor(dictionary=True)
                base_query = "SELECT MaSP, TenSP, Anh, Gia, SoLuongTon, MoTa, LoaiSP FROM SanPham"
                if selected_value != "All":
                    query = base_query + " WHERE LoaiSP = %s"
                    cursor.execute(query, (selected_value,))
                else:
                    cursor.execute(base_query)
                records = cursor.fetchall()

                layout = self.ui.productGrid
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                        widget.deleteLater()

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
            self, "Chọn ảnh", "", "Image Files (*.png *.jpg *.jpeg *.bmp)"
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

    def add_product(self):
        """Lấy thông tin từ các ô nhập và chèn bản ghi mới vào bảng SanPham."""
        name = self.ui.lineEditTenSP.text().strip()
        category = self.ui.comboBoxLoaiSP.currentText()
        price = self.ui.lineEditGia.text().strip()
        quantity = self.ui.spinBoxSoLuongTon.value()
        description = self.ui.textEditMoTa.toPlainText().strip()
        image_path = self.current_image_path

        if not name or not category or not price:
            QMessageBox.warning(self, "Warning", "Vui lòng điền đầy đủ thông tin bắt buộc!")
            return
        
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                query = (
                    "INSERT INTO SanPham (TenSP, LoaiSP, Gia, SoLuongTon, MoTa, Anh) "
                    "VALUES (%s, %s, %s, %s, %s, %s)"
                )
                cursor.execute(query, (name, category, price, quantity, description, image_path))
                conn.commit()
                QMessageBox.information(self, "Success", "Sản phẩm đã được thêm thành công!")
                self.clear_fields()
                self.load_products_table()
            cursor.close()
        except Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")
        finally:
            if conn.is_connected():
                conn.close()

    def update_product(self):
        """Cập nhật thông tin sản phẩm dựa trên MaSP được chọn."""
        product_id = self.ui.lineEditMaSP.text().strip()
        if not product_id:
            QMessageBox.warning(self, "Warning", "Vui lòng chọn sản phẩm để cập nhật!")
            return
        
        name = self.ui.lineEditTenSP.text().strip()
        category = self.ui.comboBoxLoaiSP.currentText()
        price = self.ui.lineEditGia.text().strip()
        quantity = self.ui.spinBoxSoLuongTon.value()
        description = self.ui.textEditMoTa.toPlainText().strip()
        image_path = self.current_image_path
        
        if not name or not category or not price:
            QMessageBox.warning(self, "Warning", "Vui lòng điền đầy đủ thông tin bắt buộc!")
            return
        
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                query = (
                    "UPDATE SanPham SET TenSP = %s, LoaiSP = %s, Gia = %s, SoLuongTon = %s, MoTa = %s, Anh = %s "
                    "WHERE MaSP = %s"
                )
                cursor.execute(query, (name, category, price, quantity, description, image_path, product_id))
                conn.commit()
                QMessageBox.information(self, "Success", "Sản phẩm đã được cập nhật thành công!")
                self.clear_fields()
                self.load_products_table()
            cursor.close()
        except Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")
        finally:
            if conn.is_connected():
                conn.close()

    def delete_product(self):
        """Xóa sản phẩm dựa trên MaSP được chọn sau khi xác nhận."""
        product_id = self.ui.lineEditMaSP.text().strip()
        if not product_id:
            QMessageBox.warning(self, "Warning", "Vui lòng chọn sản phẩm để xóa!")
            return
        
        reply = QMessageBox.question(self, "Confirm Delete", "Bạn có chắc chắn muốn xóa sản phẩm này không?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                conn = connect_db()
                if conn.is_connected():
                    cursor = conn.cursor()
                    query = "DELETE FROM SanPham WHERE MaSP = %s"
                    cursor.execute(query, (product_id,))
                    conn.commit()
                    QMessageBox.information(self, "Success", "Sản phẩm đã được xóa thành công!")
                    self.clear_fields()
                    self.load_products_table()
                cursor.close()
            except Error as e:
                QMessageBox.critical(self, "Database Error", f"Error: {e}")
            finally:
                if conn.is_connected():
                    conn.close()

    def load_products_table(self):
        """
        Lấy danh sách sản phẩm từ bảng SanPham và hiển thị vào bảng quản lý (tableProducts).
        """
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute("SELECT MaSP, TenSP, LoaiSP, Gia, SoLuongTon, MoTa, Anh FROM SanPham")
                rows = cursor.fetchall()
                self.ui.tableProducts.setRowCount(0)
                for row_data in rows:
                    row_number = self.ui.tableProducts.rowCount()
                    self.ui.tableProducts.insertRow(row_number)
                    for column, data in enumerate(row_data):
                        item = QTableWidgetItem(str(data))
                        self.ui.tableProducts.setItem(row_number, column, item)
                cursor.close()
        except Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")
        finally:
            if conn.is_connected():
                conn.close()

    def load_product_details(self, item):
        """
        Khi click vào một dòng trong bảng, điền dữ liệu lên các ô nhập tương ứng.
        """
        row = item.row()
        self.ui.lineEditMaSP.setText(self.ui.tableProducts.item(row, 0).text())
        self.ui.lineEditTenSP.setText(self.ui.tableProducts.item(row, 1).text())
        category = self.ui.tableProducts.item(row, 2).text()
        index = self.ui.comboBoxLoaiSP.findText(category)
        if index != -1:
            self.ui.comboBoxLoaiSP.setCurrentIndex(index)
        self.ui.lineEditGia.setText(self.ui.tableProducts.item(row, 3).text())
        self.ui.spinBoxSoLuongTon.setValue(int(self.ui.tableProducts.item(row, 4).text()))
        self.ui.textEditMoTa.setPlainText(self.ui.tableProducts.item(row, 5).text())
        image_item = self.ui.tableProducts.item(row, 6)
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
        """Xóa các ô nhập sau khi thêm/sửa/xóa sản phẩm."""
        self.ui.lineEditMaSP.clear()
        self.ui.lineEditTenSP.clear()
        self.ui.comboBoxLoaiSP.setCurrentIndex(0)
        self.ui.lineEditGia.clear()
        self.ui.spinBoxSoLuongTon.setValue(0)
        self.ui.textEditMoTa.clear()
        self.current_image_path = ""
        self.ui.imagePreview.setPixmap(QPixmap("user-placeholder.png"))

    def import_from_excel(self):
        """
        Nhập dữ liệu sản phẩm từ file Excel và thêm vào bảng SanPham.
        File Excel cần có các cột: TenSP, LoaiSP, Gia, SoLuongTon, MoTa, Anh.
        """
        file_path, _ = QFileDialog.getOpenFileName(self, "Nhập dữ liệu từ Excel", "", "Excel Files (*.xlsx *.xls)")
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
                    name = str(row['TenSP']).strip() if 'TenSP' in row.index else ""
                    category = str(row['LoaiSP']).strip() if 'LoaiSP' in row.index else ""
                    price = str(row['Gia']).strip() if 'Gia' in row.index else ""
                    quantity = int(row['SoLuongTon']) if 'SoLuongTon' in row.index and not pd.isnull(row['SoLuongTon']) else 0
                    description = str(row['MoTa']).strip() if 'MoTa' in row.index else ""
                    image_path = str(row['Anh']).strip() if 'Anh' in row.index else ""
                    if not name or not category or not price:
                        continue
                    query = (
                        "INSERT INTO SanPham (TenSP, LoaiSP, Gia, SoLuongTon, MoTa, Anh) "
                        "VALUES (%s, %s, %s, %s, %s, %s)"
                    )
                    cursor.execute(query, (name, category, price, quantity, description, image_path))
                conn.commit()
                QMessageBox.information(self, "Success", "Dữ liệu đã được nhập từ Excel thành công!")
                self.load_products_table()
                cursor.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi nhập dữ liệu từ Excel: {e}")
        finally:
            if conn.is_connected():
                conn.close()
