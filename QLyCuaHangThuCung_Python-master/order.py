import os
import sys
from datetime import datetime
import qrcode
from PySide6.QtCore import Qt, QMarginsF, QSizeF, QDate
from PySide6.QtGui import QPixmap, QTextDocument, QPageLayout, QPageSize
from PySide6.QtPrintSupport import QPrinter
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QDialog,
    QVBoxLayout, QPlainTextEdit, QWidget
)
from config.connectDB import connect_db
from ui.ui_order import Ui_MainWindow


class OrderPage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Quản lý đơn hàng")
        self.ui.tableWidget_menu.verticalHeader().setDefaultSectionSize(80)
        self.ui.tableWidget_product.verticalHeader().setDefaultSectionSize(80)

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_order_list)

        self.ui.pushButton_create_order.clicked.connect(
            self.switch_to_create_order)
        self.ui.pushButton_view_details.clicked.connect(
            self.switch_to_order_details)

        # Kết nối các nút trên trang page_create_order
        self.ui.updateSLButton.setHidden(True)
        self.ui.pushButton_add_to_order.clicked.connect(self.add_to_menu)
        self.ui.pushButton_payment.clicked.connect(self.payment)
        self.ui.pushButton_print.clicked.connect(self.export_receipt_pdf)
        
        self.ui.dateEdit_to.editingFinished.connect(self.search_orders)
        self.ui.label_date_from.mousePressEvent = lambda event: self.reset_filters_and_reload()
        self.ui.spinBox_price_to.setHidden(True)
        self.ui.label_price_to.setHidden(True)
        self.ui.spinBox_price_from.setHidden(True)
        self.ui.label_price_from.setHidden(True)

        # Nút Back trên trang order_details
        self.ui.backButton.clicked.connect(self.switch_to_order_list)

        # Load dữ liệu ban đầu
        self.load_order_list()
        self.load_product_list()  # load danh sách sản phẩm từ SanPham

    def search_orders(self):
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor(dictionary=True)

                # Lấy giá trị từ giao diện
                date_from = self.ui.dateEdit_from.date().toString("yyyy-MM-dd")
                date_to = self.ui.dateEdit_to.date().toString("yyyy-MM-dd")
                price_from = self.ui.spinBox_price_from.value()
                price_to = self.ui.spinBox_price_to.value()

                # Tạo truy vấn SQL động
                query = """
                    SELECT *, 
                        CAST(REPLACE(REPLACE(TongTien, ',', ''), ' VND', '') AS DECIMAL(18,2)) AS TongTienSo 
                    FROM DonHang 
                    WHERE TrangThai = 'Đã thanh toán'
                """
                params = []

                # Kiểm tra điều kiện ngày
                if date_from and date_to:
                    query += " AND NgayDat BETWEEN %s AND %s"
                    params.extend([date_from, date_to])

                # Kiểm tra điều kiện giá
                if price_from > 0 or price_to > 0:
                    query += " AND TongTienSo BETWEEN %s AND %s"
                    params.extend([price_from, price_to])

                query += " ORDER BY NgayDat DESC"

                cursor.execute(query, params)
                results = cursor.fetchall()

                # Hiển thị kết quả
                self.ui.tableWidget_orders.setRowCount(0)  
                for row_num, row in enumerate(results):
                    self.ui.tableWidget_orders.insertRow(row_num)
                    for col_num, (col_name, col_value) in enumerate(row.items()):
                        # Định dạng cột 'TongTien' thành 50,000.00 VND khi hiển thị
                        if col_name == "TongTien":
                            try:
                                formatted_price = f"{float(col_value):,.2f} VND"
                            except ValueError:
                                formatted_price = str(col_value)  # Giữ nguyên nếu lỗi
                            self.ui.tableWidget_orders.setItem(row_num, col_num, QTableWidgetItem(formatted_price))
                        else:
                            self.ui.tableWidget_orders.setItem(row_num, col_num, QTableWidgetItem(str(col_value)))

                if not results:
                    QMessageBox.information(self, "Thông báo", "Không tìm thấy đơn hàng phù hợp.")

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi tìm kiếm đơn hàng: {e}")
        finally:
            if conn and conn.is_connected():
                conn.close()

    def reset_filters_and_reload(self):
        """ Xóa dữ liệu nhập và tải lại bảng khi nhấn vào label """
        self.ui.dateEdit_from.setDate(QDate(2000, 1, 1))
        self.ui.dateEdit_to.setDate(QDate(2000, 1, 1))
        self.ui.spinBox_price_from.setValue(0)  
        self.ui.spinBox_price_to.setValue(0)  
        self.load_order_list()
    
    def load_order_list(self):
        """
        Load danh sách đơn hàng từ bảng DonHang 
        và hiển thị vào tableWidget_orders.
        """
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor(dictionary=True)
                query = """
                    SELECT MaDH, MaKH, MaNV, NgayDat, TongTien, TrangThai 
                    FROM DonHang
                """
                cursor.execute(query,)
                records = cursor.fetchall()
                self.ui.tableWidget_orders.setRowCount(0)
                for record in records:
                    row = self.ui.tableWidget_orders.rowCount()
                    self.ui.tableWidget_orders.insertRow(row)
                    self.ui.tableWidget_orders.setItem(
                        row, 0, QTableWidgetItem(str(record.get("MaDH", ""))))
                    self.ui.tableWidget_orders.setItem(
                        row, 1, QTableWidgetItem(str(record.get("MaKH", ""))))
                    self.ui.tableWidget_orders.setItem(
                        row, 2, QTableWidgetItem(str(record.get("MaNV", ""))))
                    self.ui.tableWidget_orders.setItem(
                        row, 3, QTableWidgetItem(str(record.get("NgayDat", ""))))
                    self.ui.tableWidget_orders.setItem(row, 4, QTableWidgetItem(
                        "{:,.2f} VND".format(record.get("TongTien", 0))))
                    self.ui.tableWidget_orders.setItem(
                        row, 5, QTableWidgetItem(record.get("TrangThai", "")))
                cursor.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi tải đơn hàng: {e}")
        finally:
            if conn and conn.is_connected():
                conn.close()

    def switch_to_order_list(self):
        """Chuyển về trang order_list."""
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_order_list)
        self.load_order_list()

    def switch_to_order_details(self):
        """
        Chuyển sang trang order_details và load chi tiết đơn hàng dựa trên đơn hàng được chọn.
        """
        selected_items = self.ui.tableWidget_orders.selectedItems()
        if not selected_items:
            QMessageBox.warning(
                self, "Warning", "Vui lòng chọn đơn hàng để xem chi tiết!")
            return
        row = selected_items[0].row()
        order_id_item = self.ui.tableWidget_orders.item(row, 0)
        if not order_id_item:
            QMessageBox.warning(
                self, "Warning", "Không xác định được đơn hàng!")
            return
        order_id = order_id_item.text().strip()
        # Load chi tiết đơn hàng từ bảng ChiTietDonHang
        self.load_order_details(order_id)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_order_details)

    def load_order_details(self, order_id):
        """
        Load chi tiết đơn hàng từ bảng ChiTietDonHang theo MaDH và hiển thị vào tableWidget_order_details.
        """
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor(dictionary=True)
                query = """
                        SELECT ctdh.MaSP, sp.TenSP, ctdh.SoLuong, ctdh.DonGia, ctdh.ThanhTien
                        FROM ChiTietDonHang ctdh
                        JOIN SanPham sp ON ctdh.MaSP = sp.MaSP
                        WHERE ctdh.MaDH = %s
                    """
                cursor.execute(query, (order_id,))
                records = cursor.fetchall()
                self.ui.tableWidget_order_details.setRowCount(0)
                for record in records:
                    row = self.ui.tableWidget_order_details.rowCount()
                    self.ui.tableWidget_order_details.insertRow(row)
                    self.ui.tableWidget_order_details.setItem(
                        row, 0, QTableWidgetItem(str(record.get("MaSP", ""))))
                    self.ui.tableWidget_order_details.setItem(
                        row, 1, QTableWidgetItem(str(record.get("TenSP", ""))))
                    self.ui.tableWidget_order_details.setItem(
                        row, 2, QTableWidgetItem(str(record.get("SoLuong", ""))))
                    self.ui.tableWidget_order_details.setItem(
                        row, 3, QTableWidgetItem("{:,.2f} VND".format(record.get("DonGia", 0))))
                    self.ui.tableWidget_order_details.setItem(row, 4, QTableWidgetItem(
                        "{:,.2f} VND".format(record.get("ThanhTien", 0))))
                cursor.close()
        except Exception as e:
            QMessageBox.critical(
                self, "Error", f"Lỗi khi tải chi tiết đơn hàng: {e}")
        finally:
            if conn and conn.is_connected():
                conn.close()

    def load_product_list(self):
        """
        Load danh sách sản phẩm từ bảng SanPham và hiển thị vào tableWidget_product.
        Cột ảnh sẽ được hiển thị bằng cách sử dụng setCellWidget với QLabel.
        """
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor(dictionary=True)
                query = """
                    SELECT MaSP, TenSP, LoaiSP, Gia, SoLuongTon, MoTa, Anh
                    FROM SanPham Where SoLuongTon > 0
                """
                cursor.execute(query)
                records = cursor.fetchall()
                self.ui.tableWidget_product.setRowCount(0)
                for record in records:
                    row = self.ui.tableWidget_product.rowCount()
                    self.ui.tableWidget_product.insertRow(row)
                    self.ui.tableWidget_product.setItem(
                        row, 0, QTableWidgetItem(str(record.get("MaSP", ""))))
                    self.ui.tableWidget_product.setItem(
                        row, 1, QTableWidgetItem(record.get("TenSP", "")))
                    self.ui.tableWidget_product.setItem(row, 2, QTableWidgetItem(
                        # Tạm, sẽ hiển thị ảnh bên dưới
                        record.get("Anh", "")))
                    self.ui.tableWidget_product.setItem(
                        row, 3, QTableWidgetItem(record.get("MoTa", "")))
                    self.ui.tableWidget_product.setItem(row, 4, QTableWidgetItem(
                        "{:,.2f} VND".format(record.get("Gia", 0))))
                    self.ui.tableWidget_product.setItem(
                        row, 5, QTableWidgetItem(record.get("LoaiSP", "")))

                    # Hiển thị ảnh ở cột 2 bằng setCellWidget với QLabel
                    image_path = record.get("Anh", "")
                    from PySide6.QtWidgets import QLabel
                    image_label = QLabel()
                    if image_path and os.path.exists(image_path):
                        pixmap = QPixmap(image_path)
                        scaled_pix = pixmap.scaled(
                            80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                        image_label.setPixmap(scaled_pix)
                    else:
                        image_label.setText("No Image")
                    image_label.setAlignment(Qt.AlignCenter)
                    self.ui.tableWidget_product.setCellWidget(
                        row, 2, image_label)
                cursor.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi tải sản phẩm: {e}")
        finally:
            if conn and conn.is_connected():
                conn.close()

    def add_to_menu(self):
        """
        Thêm sản phẩm vào hóa đơn (menu) dựa trên lựa chọn từ bảng sản phẩm (tableWidget_product).
        Lấy số lượng từ QLineEdit, sau đó chèn dữ liệu vào bảng hóa đơn (tableWidget_menu)
        với các cột: MaSP, Ảnh, Tên sản phẩm, Số lượng, Mô tả, Giá.
        """
        selected_items = self.ui.tableWidget_product.selectedItems()
        if not selected_items:
            QMessageBox.warning(
                self, "Lỗi", "Vui lòng chọn sản phẩm để thêm vào hóa đơn!")
            return

        # Lấy số lượng từ QLineEdit
        quantity_text = self.ui.lineEdit_quantity.text().strip()
        if not quantity_text.isdigit() or int(quantity_text) <= 0:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập số lượng hợp lệ!")
            return

        quantity = int(quantity_text)

        # Xác định các hàng được chọn (dùng set để tránh trùng lặp)
        selected_rows = {item.row() for item in selected_items}

        for row in selected_rows:
            # Lấy dữ liệu sản phẩm từ tableWidget_product
            product_id_item = self.ui.tableWidget_product.item(row, 0)   # MaSP
            product_name_item = self.ui.tableWidget_product.item(
                row, 1)   # Tên sản phẩm
            image_item = self.ui.tableWidget_product.item(
                row, 2)          # Đường dẫn ảnh
            description_item = self.ui.tableWidget_product.item(
                row, 3)      # Mô tả
            price_item = self.ui.tableWidget_product.item(
                row, 4)            # Giá

            if not product_id_item or not product_name_item or not price_item:
                QMessageBox.warning(
                    self, "Lỗi", "Dữ liệu sản phẩm không đầy đủ!")
                continue

            product_id = product_id_item.text().strip()
            product_name = product_name_item.text().strip()
            product_description = description_item.text().strip() if description_item else ""

            try:
                price = float(price_item.text().replace(
                    "VND", "").replace(",", "").strip())
            except ValueError:
                QMessageBox.warning(
                    self, "Lỗi", f"Giá không hợp lệ cho sản phẩm {product_name}!")
                continue
            
            # Tạo QTableWidgetItem cho MaSP, lưu dữ liệu vào UserRole
            item_ma_sp = QTableWidgetItem(product_id)
            try:
                # Cố gắng lưu dưới dạng số nguyên
                item_ma_sp.setData(Qt.UserRole, int(product_id))
            except ValueError:
                # Nếu không thể chuyển thành int, lưu dưới dạng chuỗi
                item_ma_sp.setData(Qt.UserRole, product_id)

            # Thêm dữ liệu vào bảng hóa đơn (tableWidget_menu)
            menu_row = self.ui.tableWidget_menu.rowCount()
            self.ui.tableWidget_menu.insertRow(menu_row)

            # Cột 0: MaSP
            self.ui.tableWidget_menu.setItem(
                menu_row, 0, QTableWidgetItem(product_id))

            # Cột 1: Ảnh sản phẩm
            from PySide6.QtWidgets import QLabel
            img_label = QLabel()
            product_image = image_item.text().strip() if image_item else ""
            if product_image and os.path.exists(product_image):
                pixmap = QPixmap(product_image)
                scaled_pix = pixmap.scaled(
                    80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                img_label.setPixmap(scaled_pix)
            else:
                img_label.setText("No Image")
            img_label.setAlignment(Qt.AlignCenter)
            self.ui.tableWidget_menu.setCellWidget(menu_row, 1, img_label)

            # Cột 2: Tên sản phẩm
            self.ui.tableWidget_menu.setItem(
                menu_row, 2, QTableWidgetItem(product_name))

            # Cột 3: Số lượng
            self.ui.tableWidget_menu.setItem(
                menu_row, 3, QTableWidgetItem(str(quantity)))

            # Cột 4: Mô tả
            self.ui.tableWidget_menu.setItem(
                menu_row, 4, QTableWidgetItem(product_description))

            # Cột 5: Giá
            self.ui.tableWidget_menu.setItem(
                menu_row, 5, QTableWidgetItem(f"{price:.2f} VND"))

        # Cập nhật tổng tiền của hóa đơn (hàm này cần được định nghĩa riêng)
        self.update_total_bill()
        # Xóa nội dung trong QLineEdit sau khi thêm sản phẩm
        self.ui.lineEdit_quantity.clear()

    def update_total_bill(self):
        """Tính tổng tiền của toàn bộ hóa đơn và hiển thị lên QLabel `label_total`."""
        total = 0.0
        row_count = self.ui.tableWidget_menu.rowCount()
        for row in range(row_count):
            price_item = self.ui.tableWidget_menu.item(row, 5)
            quantity_item = self.ui.tableWidget_menu.item(row, 3)
            if price_item is None or quantity_item is None:
                continue
            try:
                # Lấy text, loại bỏ "VND" và dấu phẩy, sau đó chuyển sang số thực
                price_text = price_item.text().replace("VND", "").replace(",", "").strip()
                price = float(price_text)
                quantity = float(quantity_item.text().strip())
                total += price * quantity
            except ValueError:
                continue
        self.ui.label_total.setText(f"Tổng tiền: {total:.2f} VND")

    def export_receipt_pdf(self):
        """
        Xuất hóa đơn sang file PDF với định dạng giống biên lai thực tế.
        """
        now = datetime.now()
        current_date = now.strftime("%d/%m/%Y")
        current_time = now.strftime("%H:%M:%S")
        
        # Thông tin cửa hàng
        store_name = "HÓA ĐƠN THANH TOÁN"
        invoice_code = "0006"
        
        # Lấy tổng tiền
        total_amount = self.ui.label_total.text()
        
        # Xây dựng HTML
        html_content = f"""
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; font-size: 10pt; text-align: center; }}
                .header {{ font-weight: bold; margin-bottom: 5px; }}
                .title {{ font-size: 14pt; font-weight: bold; margin: 10px 0; }}
                .divider {{ border-top: 1px dotted #000; margin: 5px 0; }}
                .info-row {{ display: flex; justify-content: space-between; margin: 2px 0; }}
                .product-table {{ width: 100%; margin: 10px 0; }}
                .product-table td {{ padding: 2px 4px; }}
                .product-row {{ display: flex; }}
                .product-name {{ text-align: left; width: 50%; }}
                .product-qty {{ text-align: center; width: 10%; }}
                .product-price {{ text-align: right; width: 20%; }}
                .product-total {{ text-align: right; width: 20%; }}
                .total-row {{ display: flex; justify-content: space-between; margin: 5px 0; font-weight: bold; }}
                .final-total {{ font-size: 14pt; font-weight: bold; margin: 5px 0; }}
                .footer {{ margin-top: 10px; font-style: italic; }}
            </style>
        </head>
        <body>
            <h1>Cửa hàng thú cưng</h1>
            <div class="header">{store_name}</div>
            <div class="info-row">
                <div style="text-align: left;"><b>HĐ</b>: {invoice_code}</div>
                <div style="text-align: right;">Giờ: {current_time}</div>
            </div>
            <div class="info-row">
                <div style="text-align: left;"><b>Ngày</b>: {current_date}</div>
                <div style="text-align: right;"><b>A 1</b></div>
            </div>
            <div class="info-row" style="font-weight: bold;">
                <div style="text-align: left;">BÁN:</div>
            </div>
            
            <div class="divider"></div>
            
            <table class="product-table" cellspacing="0" cellpadding="0">
                <tr style="font-weight: bold;">
                    <td style="text-align: left;">TÊN HÀNG</td>
                    <td style="text-align: center;">SL</td>
                    <td style="text-align: right;">Đ.GIÁ</td>
                    <td style="text-align: right;">T.TIỀN</td>
                </tr>
        """
        
        # Thêm các sản phẩm vào HTML
        row_count = self.ui.tableWidget_menu.rowCount()
        total_quantity = 0
        
        for row in range(row_count):
            product_title_item = self.ui.tableWidget_menu.item(row, 2)
            price_item = self.ui.tableWidget_menu.item(row, 3)
            quantity_item = self.ui.tableWidget_menu.item(row, 4)
            total_item = self.ui.tableWidget_menu.item(row, 5)
            
            product_title = product_title_item.text() if product_title_item else ""
            price_str = price_item.text() if price_item else ""
            quantity_str = quantity_item.text() if quantity_item else ""
            total_str = total_item.text() if total_item else ""
            
            # Thêm dòng sản phẩm vào bảng
            html_content += f"""
                <tr>
                    <td style="text-align: left; border-bottom: 1px dotted #aaa;">{product_title}</td>
                    <td style="text-align: center; border-bottom: 1px dotted #aaa;">{quantity_str}</td>
                    <td style="text-align: right; border-bottom: 1px dotted #aaa;">{price_str}</td>
                    <td style="text-align: right; border-bottom: 1px dotted #aaa;">{total_str}</td>
                </tr>
            """
            total_quantity += int(quantity_str) if quantity_str.isdigit() else 0
        
        # Hoàn thành HTML
        html_content += f"""
            </table>
            
            <div class="divider"></div>
            
            <div class="total-row">
                <div>T.CỘNG</div>
                <div>{total_quantity}</div>
                <div></div>
                <div>{total_amount}</div>
            </div>
            
            <div class="final-total">
                <div style="display: flex; justify-content: space-between;">
                    <div><b>TIỀN MẶT</b></div>
                    <div><b>{total_amount}</b></div>
                </div>
            </div>
            <div class="footer">
                Cảm ơn quý khách và hẹn gặp lại!
            </div>
        </body>
        </html>
        """
        
        # Tạo QTextDocument với nội dung HTML
        doc = QTextDocument()
        doc.setHtml(html_content)
        
        # Thiết lập kích thước giấy cho hóa đơn nhỏ (80mm x độ dài tùy chỉnh)
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName("receipt.pdf")
        
        # Thiết lập kích thước trang cho hóa đơn loại nhỏ
        printer.setPageSize(QPageSize(QSizeF(80, 200), QPageSize.Millimeter))
        printer.setPageMargins(QMarginsF(5, 5, 5, 5), QPageLayout.Millimeter)
        
        # In từ QTextDocument sang PDF
        doc.print_(printer)
        QMessageBox.information(self, "Xuất PDF", "Hóa đơn đã được xuất ra!")

    def switch_to_create_order(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_create_order)
        self.load_product_list()

    def switch_to_order_list(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_order_list)
        self.load_order_list()

    def payment(self):
        """
        Khi ấn nút "Thanh toán" trong trang page_create_order:
          - Hiển thị dialog hỏi thanh toán bằng tiền mặt hay QR code.
          - Nếu chọn tiền mặt: lưu đơn hàng vào bảng DonHang và ChiTietDonHang.
          - Nếu chọn QR code: hiển thị QR code thanh toán.
        """
        if self.ui.tableWidget_menu.rowCount() == 0:
            QMessageBox.warning(self, "Checkout", "Hóa đơn trống!")
            return

        # Hiển thị dialog lựa chọn phương thức thanh toán
        from PySide6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel
        dialog = QDialog(self)
        dialog.setWindowTitle("Chọn phương thức thanh toán")
        layout = QVBoxLayout(dialog)
        label = QLabel("Chọn phương thức thanh toán:")
        layout.addWidget(label)

        btn_cash = QPushButton("Thanh toán bằng tiền mặt")
        btn_qr = QPushButton("Thanh toán bằng QR code")
        layout.addWidget(btn_cash)
        layout.addWidget(btn_qr)

        # Kết quả thanh toán (dùng biến để lưu kết quả)
        payment_method = {"method": None}

        def select_cash():
            payment_method["method"] = "cash"
            dialog.accept()

        def select_qr():
            payment_method["method"] = "qr"
            dialog.accept()

        btn_cash.clicked.connect(select_cash)
        btn_qr.clicked.connect(select_qr)

        result = dialog.exec()

        if result == QDialog.Accepted:
            if payment_method["method"] == "cash":
                self.create_order_in_db(payment_method="cash")
            elif payment_method["method"] == "qr":
                # Hiển thị QR code thanh toán
                self.show_qr_dialog()

    def create_order_in_db(self, payment_method="cash"):
        """
        Tạo đơn hàng trong bảng DonHang và ChiTietDonHang từ dữ liệu trong tableWidget_menu.
        Cập nhật số lượng tồn của sản phẩm trong bảng SanPham.
        """
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                # Giả sử: MaKH = self.user_id, MaNV = 2 (nhân viên quản lý)
                insert_order = """
                    INSERT INTO DonHang (MaKH, MaNV, TongTien, TrangThai)
                    VALUES (%s, %s, %s, %s)
                """
                # Tính tổng tiền: tính bằng cách lấy số lượng từ cột 3 và giá từ cột 5 của tableWidget_menu
                total = 0.0
                row_count = self.ui.tableWidget_menu.rowCount()
                for row in range(row_count):
                    quantity_item = self.ui.tableWidget_menu.item(row, 3)
                    price_item = self.ui.tableWidget_menu.item(row, 5)
                    if quantity_item is None or price_item is None:
                        continue
                    try:
                        quantity = float(quantity_item.text().strip())
                        price_str = price_item.text().replace("VND", "").replace(",", "").strip()
                        price = float(price_str)
                        total += price * quantity
                    except ValueError:
                        continue
                cursor.execute(insert_order, (0, 2, total, "Đã thanh toán"))
                conn.commit()
                order_id = cursor.lastrowid  # Lấy MaDH vừa insert

                # Insert ChiTietDonHang cho từng sản phẩm trong tableWidget_menu
                for row in range(row_count):
                    ma_sp_item = self.ui.tableWidget_menu.item(row, 0)
                    if not ma_sp_item:
                        continue
                    try:
                        # Lấy MaSP từ dữ liệu lưu trong UserRole nếu có, hoặc từ text
                        ma_sp = int(ma_sp_item.data(Qt.UserRole)) if ma_sp_item.data(Qt.UserRole) is not None else int(ma_sp_item.text())
                    except (ValueError, TypeError):
                        print(f"Warning: invalid product id in row {row}. Skipping this row.")
                        continue

                    quantity_item = self.ui.tableWidget_menu.item(row, 3)
                    so_luong = int(quantity_item.text()) if quantity_item and quantity_item.text().isdigit() else 1

                    price_item = self.ui.tableWidget_menu.item(row, 5)
                    if price_item:
                        price_str = price_item.text().replace("VND", "").replace(",", "").strip()
                        don_gia = float(price_str) if price_str else 0.0
                    else:
                        don_gia = 0.0

                    insert_detail = """
                        INSERT INTO ChiTietDonHang (MaDH, MaSP, SoLuong, DonGia)
                        VALUES (%s, %s, %s, %s)
                    """
                    cursor.execute(insert_detail, (order_id, ma_sp, so_luong, don_gia))
                    
                    update_product = """
                        UPDATE SanPham 
                        SET SoLuongTon = SoLuongTon - %s 
                        WHERE MaSP = %s AND SoLuongTon >= %s
                    """
                    cursor.execute(update_product, (so_luong, ma_sp, so_luong))
                conn.commit()
                cursor.close()
                QMessageBox.information(self, "Thanh toán", f"Đơn hàng {order_id} đã được đặt thành công!")
                self.switch_to_order_list()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi tạo đơn hàng: {e}")
            if conn:
                conn.rollback()
        finally:
            if conn and conn.is_connected():
                conn.close()

    def show_qr_dialog(self):
        """
        Hiển thị dialog QR code thanh toán.
        Sau khi đóng dialog, đơn hàng sẽ được lưu vào bảng DonHang và ChiTietDonHang.
        """
        try:
            from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel
            from PySide6.QtGui import QPixmap
            from PySide6.QtCore import Qt
            import qrcode

            total_amount = self.ui.label_total.text().replace("Tổng tiền:", "").replace("VND", "").replace(",", "").strip()

            # Nội dung QR code với thông tin thanh toán
            qr_content = f"""Ngân hàng: Vietcombank
    Số tài khoản: 1234567890
    Chủ tài khoản: SHOP THU CUNG ABC
    Số tiền: {total_amount} VND
    Nội dung: Thanh toan don hang """

            # Tạo QR code
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(qr_content)
            qr.make(fit=True)
            qr_image = qr.make_image(fill_color="black", back_color="white")

            # Lưu QR code tạm thời
            qr_path = "temp_qr.png"
            qr_image.save(qr_path)

            # Tạo dialog hiển thị QR code với kích thước nhỏ gọn và CSS đẹp
            dialog = QDialog(self)
            dialog.setWindowTitle("Quét mã QR để thanh toán")
            dialog.setModal(True)
            dialog.resize(300, 400)
            dialog.setStyleSheet("""
                QDialog {
                    background-color: #ffffff;
                    border: 1px solid #ccc;
                    border-radius: 10px;
                }
                QLabel {
                    font-family: Arial;
                    color: #333333;
                }
            """)

            layout = QVBoxLayout()
            instruction_label = QLabel(
                "Quét mã QR bằng ứng dụng ngân hàng để thanh toán:")
            instruction_label.setAlignment(Qt.AlignCenter)
            instruction_label.setStyleSheet(
                "font-size: 12pt; margin-bottom: 10px;")
            layout.addWidget(instruction_label)

            qr_label = QLabel()
            qr_pixmap = QPixmap(qr_path).scaled(
                200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            qr_label.setPixmap(qr_pixmap)
            qr_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(qr_label)

            info_label = QLabel(f"""Thông tin chuyển khoản:
    - Ngân hàng: Vietcombank
    - Số tài khoản: 1234567890
    - Chủ tài khoản: SHOP THU CUNG ABC
    - Số tiền: {total_amount} VND
    - Nội dung: Thanh toan don hang """)
            info_label.setAlignment(Qt.AlignCenter)
            info_label.setStyleSheet("font-size: 10pt; margin-top: 10px;")
            layout.addWidget(info_label)

            dialog.setLayout(layout)

            # Hiển thị dialog và chờ người dùng đóng
            dialog.exec()

            # Xóa file QR tạm
            import os
            if os.path.exists(qr_path):
                os.remove(qr_path)

            # Sau khi dialog đóng, lưu đơn hàng vào DonHang và ChiTietDonHang
            try:
                conn = connect_db()
                if conn.is_connected():
                    cursor = conn.cursor()
                    # 1) Chèn đơn hàng vào bảng DonHang.
                    # Giả sử: MaKH = self.user_id, MaNV = 1 (bạn có thể thay đổi), TongTien = total_amount,
                    # TrangThai = 'Đã thanh toán'
                    insert_order = """
                        INSERT INTO DonHang (MaKH, MaNV, TongTien, TrangThai)
                        VALUES (%s, %s, %s, %s)
                    """
                    total_amount_float = float(total_amount)
                    cursor.execute(insert_order, (0, 2,
                                total_amount_float, 'Đã thanh toán'))
                    conn.commit()
                    order_id = cursor.lastrowid  # Lấy MaDH vừa insert

                    # 2) Chèn các chi tiết đơn hàng từ tableWidget_menu.
                    row_count = self.ui.tableWidget_menu.rowCount()
                    for row in range(row_count):
                        ma_sp_item = self.ui.tableWidget_menu.item(row, 0)
                        if not ma_sp_item:
                            continue
                        try:
                            ma_sp = int(ma_sp_item.text())
                        except:
                            continue
                        quantity_item = self.ui.tableWidget_menu.item(row, 3)
                        so_luong = int(quantity_item.text(
                        )) if quantity_item and quantity_item.text().isdigit() else 1
                        price_item = self.ui.tableWidget_menu.item(row, 5)
                        if price_item:
                            price_str = price_item.text().replace("VND", "").replace(",", "").strip()
                            don_gia = float(price_str) if price_str else 0.0
                        else:
                            don_gia = 0.0

                        # Chèn chi tiết đơn hàng vào bảng ChiTietDonHang
                        insert_detail = """
                            INSERT INTO ChiTietDonHang (MaDH, MaSP, SoLuong, DonGia)
                            VALUES (%s, %s, %s, %s)
                        """
                        cursor.execute(insert_detail, (order_id, ma_sp, so_luong, don_gia))
                        
                        # Cập nhật số lượng tồn trong bảng SanPham
                        update_product = """
                            UPDATE SanPham 
                            SET SoLuongTon = SoLuongTon - %s 
                            WHERE MaSP = %s AND SoLuongTon >= %s
                        """
                        cursor.execute(update_product, (so_luong, ma_sp, so_luong))
                    conn.commit()
                    cursor.close()
                    QMessageBox.information(
                        self, "Thanh toán", f"Đơn hàng {order_id} đã được đặt thành công!")
                else:
                    QMessageBox.critical(
                        self, "Error", "Không kết nối được tới cơ sở dữ liệu!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Lỗi khi đặt hàng: {e}")
                if conn:
                    conn.rollback()
            finally:
                if conn and conn.is_connected():
                    conn.close()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi tạo mã QR: {e}")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = OrderPage()
#     window.show()
#     sys.exit(app.exec())
