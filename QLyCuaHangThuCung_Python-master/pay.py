import os
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem, QWidget, QPlainTextEdit, QVBoxLayout, QDialog
from config.connectDB import connect_db
from PySide6.QtCore import Qt, QMarginsF, QSizeF
from PySide6.QtGui import QPixmap, QTextDocument, QPageLayout, QPageSize
from datetime import datetime
from PySide6.QtPrintSupport import QPrinter
from PySide6.QtGui import QTextDocument
from ui.ui_pay import Ui_PaymentPage  # File UI được tạo từ pay.ui

class PaymentPage(QMainWindow):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        self.user_id = user_id
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.ui = Ui_PaymentPage()
        self.ui.setupUi(self.central_widget)
        self.setWindowTitle("The Store - Payment")
        
        # Thiết lập sự kiện cho các nút
        self.ui.placeOrderButton.clicked.connect(self.place_order)
        self.ui.exportButton.clicked.connect(self.export_receipt_pdf)
        
        # Tải dữ liệu đơn hàng (cart) từ database và hiển thị vào bảng itemTable
        self.load_payment_details()
        self.update_cart_count()
    
    
    def update_cart_count(self):
        """
        Hàm đếm số lượng sản phẩm trong giỏ hàng của customer từ bảng Cart theo user_id
        và cập nhật số lượng lên self.cartCountLabel.
        """
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                query = "SELECT COUNT(*) FROM cart WHERE user_id = %s"
                cursor.execute(query, (self.user_id,))
                result = cursor.fetchone()
                count = result[0] if result else 0
                cursor.close()
                self.ui.itemLabel.setText("Giỏ hàng ("+str(count)+")")
                self.ui.itemLabel.adjustSize()
            else:
                self.ui.itemLabel.setText("0")
        except Exception as e:
            print("Error updating cart count:", e)
            self.cartCountLabel.setText("0")
        finally:
            if conn and conn.is_connected():
                conn.close()

       
    def load_payment_details(self):
        """
        Lấy danh sách sản phẩm trong giỏ hàng (Cart) của user từ database và hiển thị vào itemTable.
        Giả sử bảng Cart có các trường: MaSP, product_image, product_title, price, quantity, total, order_details.
        """
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor(dictionary=True)
                query = """
                    SELECT MaSP, product_image, product_title, price, quantity, total, order_details 
                    FROM Cart
                    WHERE user_id = %s
                """
                cursor.execute(query, (self.user_id,))
                records = cursor.fetchall()

                # Xóa hết các dòng cũ
                self.ui.itemTable.setRowCount(0)
                total_cart = 0
                for record in records:
                    row = self.ui.itemTable.rowCount()
                    self.ui.itemTable.insertRow(row)
                    
                    # Column 0: ID
                    self.ui.itemTable.setItem(row, 0, QTableWidgetItem(str(record.get("MaSP", ""))))
                    
                    # Column 1: Product Image -> Dùng setCellWidget với QLabel hiển thị ảnh
                    image_path = record.get("product_image", "")
                    if image_path and os.path.exists(image_path):
                        from PySide6.QtWidgets import QLabel
                        from PySide6.QtGui import QPixmap
                        image_label = QLabel()
                        # Scale ảnh (ví dụ: 80x80)
                        pixmap = QPixmap(image_path)
                        scaled_pix = pixmap.scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                        image_label.setPixmap(scaled_pix)
                        image_label.setAlignment(Qt.AlignCenter)
                        self.ui.itemTable.setCellWidget(row, 1, image_label)
                    else:
                        # Nếu không có ảnh hoặc đường dẫn không tồn tại, ta đặt text "No Image"
                        self.ui.itemTable.setItem(row, 1, QTableWidgetItem("No Image"))
                    
                    # Column 2: Product Title
                    self.ui.itemTable.setItem(row, 2, QTableWidgetItem(record.get("product_title", "")))
                    
                    # Column 3: Price
                    price = float(record.get("price", 0))
                    self.ui.itemTable.setItem(row, 3, QTableWidgetItem("{:,.2f} VND".format(price)))
                    
                    # Column 4: Quantity
                    quantity = int(record.get("quantity", 1))
                    self.ui.itemTable.setItem(row, 4, QTableWidgetItem(str(quantity)))
                    
                    # Column 5: Total
                    total_item = float(record.get("total", 0))
                    self.ui.itemTable.setItem(row, 5, QTableWidgetItem("{:,.2f} VND".format(total_item)))
                    
                    # Column 6: Order Details
                    self.ui.itemTable.setItem(row, 6, QTableWidgetItem(record.get("order_details", "")))
                    
                    total_cart += total_item

                    # Điều chỉnh chiều cao của hàng để ảnh không bị cắt
                    self.ui.itemTable.setRowHeight(row, 90)

                # Cập nhật tổng tiền giỏ hàng
                self.ui.totalValue.setText("{:,.2f} VND".format(total_cart))
                self.ui.cartTotalValue.setText("{:,.2f} VND".format(total_cart))
                cursor.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi tải giỏ hàng: {e}")
        finally:
            if conn.is_connected():
                conn.close()
    
    def place_order(self):
        """
        Xử lý đơn hàng, hiển thị QR code thanh toán, 
        rồi chuyển dữ liệu từ Cart -> DonHang -> ChiTietDonHang.
        """
        if self.ui.itemTable.rowCount() == 0:
            QMessageBox.warning(self, "Checkout", "Giỏ hàng trống!")
            return

        # Lấy tổng tiền cần thanh toán (loại bỏ "VND" và dấu phẩy)
        total_amount_str = self.ui.totalValue.text().replace("VND", "").replace(",", "").strip()
        try:
            total_amount = float(total_amount_str)
        except:
            total_amount = 0.0

        try:
            import qrcode
            from PySide6.QtWidgets import QLabel, QVBoxLayout, QDialog
            from PySide6.QtGui import QPixmap
            from PySide6.QtCore import Qt

            # Tạo nội dung QR code với thông tin chuyển khoản
            qr_content = f"""Ngân hàng: Vietcomebank
    Số tài khoản: 0123456789 
    Chủ tài khoản: SHOP THU CUNG ABC
    Số tiền: {total_amount} VND
    Nội dung: Thanh toan don hang {self.user_id}"""

            # Tạo QR code
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(qr_content)
            qr.make(fit=True)
            qr_image = qr.make_image(fill_color="black", back_color="white")

            # Lưu QR code tạm thời
            qr_path = "temp_qr.png"
            qr_image.save(qr_path)

            # Tạo dialog hiển thị QR code với kích thước nhỏ gọn
            dialog = QDialog(self)
            dialog.setWindowTitle("Quét mã QR để thanh toán")
            dialog.setModal(True)
            dialog.resize(300, 400)
            # Áp dụng stylesheet cho dialog và các thành phần bên trong
            dialog.setStyleSheet("""
                QDialog {
                    background-color: #ffffff;
                    border: 1px solid #ccc;
                    border-radius: 10px;
                }
                QLabel {
                    color: #333333;
                    font-family: Arial;
                }
            """)

            layout = QVBoxLayout()

            # Label hướng dẫn
            instruction_label = QLabel("Vui lòng quét mã QR bằng ứng dụng ngân hàng để thanh toán:")
            instruction_label.setAlignment(Qt.AlignCenter)
            instruction_label.setStyleSheet("font-size: 12pt; margin-bottom: 10px;")
            layout.addWidget(instruction_label)

            # Label hiển thị QR code
            qr_label = QLabel()
            qr_pixmap = QPixmap(qr_path).scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            qr_label.setPixmap(qr_pixmap)
            qr_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(qr_label)

            # Label thông tin chuyển khoản
            info_label = QLabel(f"""Thông tin chuyển khoản:
    - Ngân hàng: Vietcomebank
    - Số tài khoản: 0123456789
    - Chủ tài khoản: SHOP THU CUNG ABC
    - Số tiền: {total_amount} VND
    - Nội dung: Thanh toan don hang {self.user_id}""")
            info_label.setAlignment(Qt.AlignCenter)
            info_label.setStyleSheet("font-size: 10pt; margin-top: 10px;")
            layout.addWidget(info_label)

            dialog.setLayout(layout)

            # Hiển thị dialog
            result = dialog.exec()

            # Xóa file QR tạm
            import os
            if os.path.exists(qr_path):
                os.remove(qr_path)

            # Nếu người dùng đóng dialog, ta coi như chấp nhận thanh toán
            # (Hoặc bạn có thể tùy chỉnh kết quả dialog để check QDialog.Accepted)
            if True:  # Hoặc if result == QDialog.Accepted:
                try:
                    conn = connect_db()
                    if conn.is_connected():
                        cursor = conn.cursor()
                        # 1) Tạo đơn hàng (DonHang)
                        # Giả sử MaNV = 1, NgayDat = CURRENT_DATE, TongTien = total_amount
                        # TrangThai = 'Đã thanh toán'
                        insert_donhang = """
                            INSERT INTO DonHang (MaKH, MaNV, TongTien, TrangThai)
                            VALUES (%s, %s, %s, %s)
                        """
                        # maNV = 2 - Quản lý 
                        cursor.execute(insert_donhang, (self.user_id, 2, total_amount, 'Đã thanh toán'))
                        conn.commit()
                        ma_dh = cursor.lastrowid  # Lấy MaDH vừa insert

                        # 2) Thêm chi tiết đơn hàng (ChiTietDonHang) cho từng sản phẩm trong cart
                        row_count = self.ui.itemTable.rowCount()
                        for row in range(row_count):
                            # Cột 0: ID (giả sử là MaSP)
                            item_id = self.ui.itemTable.item(row, 0)
                            ma_sp = int(item_id.text()) if item_id else 0

                            # Cột 3: Price
                            price_item = self.ui.itemTable.item(row, 3)
                            price_str = price_item.text().replace(",", "").replace("VND", "").strip()
                            don_gia = float(price_str) if price_str else 0.0

                            # Cột 4: Quantity
                            quantity_item = self.ui.itemTable.item(row, 4)
                            so_luong = int(quantity_item.text()) if quantity_item else 1

                            # Insert vào ChiTietDonHang
                            insert_ctdh = """
                                INSERT INTO ChiTietDonHang (MaDH, MaSP, SoLuong, DonGia)
                                VALUES (%s, %s, %s, %s)
                            """
                            cursor.execute(insert_ctdh, (ma_dh, ma_sp, so_luong, don_gia))
                            
                            # Update số lượng tồn của sản phẩm trong bảng SanPham
                            update_product = """
                                    UPDATE SanPham 
                                    SET SoLuongTon = SoLuongTon - %s 
                                    WHERE MaSP = %s AND SoLuongTon >= %s
                                """
                            cursor.execute(update_product, (so_luong, ma_sp, so_luong))
                        
                        # 3) Xóa giỏ hàng sau khi thanh toán thành công
                        delete_query = "DELETE FROM Cart WHERE user_id = %s"
                        cursor.execute(delete_query, (self.user_id,))
                        conn.commit()
                        cursor.close()

                        QMessageBox.information(self, "Thanh toán", f"Đơn hàng {ma_dh} đã được đặt thành công!")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Lỗi khi đặt hàng: {e}")
                finally:
                    if conn and conn.is_connected():
                        conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi tạo mã QR: {e}")
                        
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
        total_amount = self.ui.totalValue.text()
        # Giả sử có một label hoặc tính toán giảm giá
        discount_amount = "-37,800" 
        final_amount = "151,200"
        
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
        row_count = self.ui.itemTable.rowCount()
        total_quantity = 0
        
        for row in range(row_count):
            product_title_item = self.ui.itemTable.item(row, 2)
            price_item = self.ui.itemTable.item(row, 3)
            quantity_item = self.ui.itemTable.item(row, 4)
            total_item = self.ui.itemTable.item(row, 5)
            
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
                   
# if __name__ == "__main__":
#     from PySide6.QtGui import QPixmap  # nếu cần
#     from PySide6.QtCore import Qt     # nếu cần
#     app = QApplication(sys.argv)
#     # Giả sử user_id là 1; bạn sẽ truyền user_id của khách hàng sau khi đăng nhập
#     window = PaymentPage(user_id=1)
#     window.show()
#     sys.exit(app.exec())
                
 
