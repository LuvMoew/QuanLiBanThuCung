import os
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem, QWidget, QLineEdit
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from config.connectDB import connect_db
from ui.ui_cart2 import Ui_ShoppingCart  # File UI được tạo từ cart.ui

class CartPage(QMainWindow):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        self.user_id = user_id
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.ui = Ui_ShoppingCart()
        self.ui.setupUi(self.central_widget) 
        self.setWindowTitle("Shopping Cart")

        # Thiết lập cấu trúc bảng giỏ hàng
        self.initialize_cart()
        
        # Kết nối các nút
        self.ui.updateCartButton.clicked.connect(self.update_cart)
        self.ui.returnButton.clicked.connect(self.return_to_product)
        self.ui.checkoutButton.clicked.connect(self.checkout)
        self.ui.deleteButton.clicked.connect(self.delete_cart_item)

        # Tải giỏ hàng của user
        self.load_cart()

    def initialize_cart(self):
        """Thiết lập bảng giỏ hàng với tiêu đề cột và độ rộng cột."""
        self.ui.cartTable.setColumnCount(7)
        headers = ["ID", "Product Image", "Product Title", "Price", "Quantity", "Total", "Order Details"]
        self.ui.cartTable.setHorizontalHeaderLabels(headers)
        self.ui.cartTable.setColumnWidth(0, 50)    # ID
        self.ui.cartTable.setColumnWidth(1, 100)   # Product Image
        self.ui.cartTable.setColumnWidth(2, 200)   # Product Title
        self.ui.cartTable.setColumnWidth(3, 100)   # Price
        self.ui.cartTable.setColumnWidth(4, 80)    # Quantity
        self.ui.cartTable.setColumnWidth(5, 100)   # Total
        self.ui.cartTable.setColumnWidth(6, 150)   # Order Details

    def load_cart(self):
        """
        Lấy danh sách sản phẩm trong giỏ hàng từ bảng Cart theo user_id và hiển thị vào cartTable.
        """
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor(dictionary=True)
                query = """
                    SELECT id, product_image, product_title, price, quantity, total, order_details 
                    FROM Cart
                    WHERE user_id = %s 
                """
                cursor.execute(query, (self.user_id,))
                records = cursor.fetchall()

                # Xóa hết các dòng cũ
                self.ui.cartTable.setRowCount(0)
                total_cart = 0
                for record in records:
                    row = self.ui.cartTable.rowCount()
                    self.ui.cartTable.insertRow(row)
                    
                    # Column 0: ID
                    self.ui.cartTable.setItem(row, 0, QTableWidgetItem(str(record.get("id", ""))))
                    
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
                        self.ui.cartTable.setCellWidget(row, 1, image_label)
                    else:
                        # Nếu không có ảnh hoặc đường dẫn không tồn tại, ta đặt text "No Image"
                        self.ui.cartTable.setItem(row, 1, QTableWidgetItem("No Image"))
                    
                    # Column 2: Product Title
                    self.ui.cartTable.setItem(row, 2, QTableWidgetItem(record.get("product_title", "")))
                    
                    # Column 3: Price
                    price = float(record.get("price", 0))
                    self.ui.cartTable.setItem(row, 3, QTableWidgetItem("{:,.2f} VND".format(price)))
                    
                    # Column 4: Quantity
                    quantity = int(record.get("quantity", 1))
                    self.ui.cartTable.setItem(row, 4, QTableWidgetItem(str(quantity)))
                    
                    # Column 5: Total
                    total_item = float(record.get("total", 0))
                    self.ui.cartTable.setItem(row, 5, QTableWidgetItem("{:,.2f} VND".format(total_item)))
                    
                    # Column 6: Order Details
                    self.ui.cartTable.setItem(row, 6, QTableWidgetItem(record.get("order_details", "")))
                    
                    total_cart += total_item

                    # Điều chỉnh chiều cao của hàng để ảnh không bị cắt
                    self.ui.cartTable.setRowHeight(row, 90)

                # Cập nhật tổng tiền giỏ hàng
                self.ui.subtotalValue.setText("{:,.2f} VND".format(total_cart))
                self.ui.totalValue.setText("{:,.2f} VND".format(total_cart))
                cursor.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi tải giỏ hàng: {e}")
        finally:
            if conn.is_connected():
                conn.close()

    def update_cart(self):
        """
        Cập nhật số lượng (quantity) trong bảng Cart,
        tính lại total và cập nhật database.
        """
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                row_count = self.ui.cartTable.rowCount()

                for row in range(row_count):
                    # Lấy id (cột 0)
                    item_id = self.ui.cartTable.item(row, 0)
                    if not item_id:
                        continue
                    cart_id = item_id.text().strip()

                    if not cart_id:
                        continue  # Nếu không có id thì bỏ qua

                    # Lấy giá (cột 3) để tính lại total
                    price_item = self.ui.cartTable.item(row, 3)
                    if price_item:
                        price_str = price_item.text().replace(",", "").replace("VND", "").strip()
                        price = float(price_str) if price_str else 0.0
                    else:
                        price = 0.0

                    new_quantity_str = self.ui.editSL.text().strip()
                    new_quantity = int(new_quantity_str) if new_quantity_str.isdigit() else 1
                
                    # Tính lại total
                    new_total = price * new_quantity

                    # Cập nhật database
                    update_query = """
                        UPDATE Cart
                        SET quantity = %s,
                            total = %s
                        WHERE id = %s
                    """
                    cursor.execute(update_query, (new_quantity, new_total, cart_id))
                    conn.commit()

                QMessageBox.information(self, "Update Cart", "Giỏ hàng đã được cập nhật!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi cập nhật giỏ hàng: {e}")
        finally:
            if conn.is_connected():
                conn.close()

        # Tải lại giỏ hàng sau khi cập nhật xong
        self.load_cart()

    def return_to_product(self):
        from pet_sidebar import MySidebar
        current_parent = self.parent()
        while current_parent and not isinstance(current_parent, MySidebar):
            current_parent = current_parent.parent()
            
        if current_parent and isinstance(current_parent, MySidebar):
            current_parent.switch_to_accessoriesFoodPage()  

    def delete_cart_item(self):
        """
        Xóa sản phẩm được chọn khỏi giỏ hàng.
        """
        # Lấy các item được chọn trong bảng
        selected_items = self.ui.cartTable.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Warning", "Vui lòng chọn sản phẩm cần xóa!")
            return

        # Giả sử ID của sản phẩm nằm ở cột 0 của dòng được chọn
        row = selected_items[0].row()
        cart_id_item = self.ui.cartTable.item(row, 0)
        if cart_id_item is None:
            QMessageBox.warning(self, "Warning", "Không xác định được sản phẩm cần xóa!")
            return

        cart_id = cart_id_item.text().strip()
        reply = QMessageBox.question(
            self,
            "Xác nhận xóa",
            "Bạn có chắc chắn muốn xóa sản phẩm này khỏi giỏ hàng?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            try:
                conn = connect_db()
                if conn.is_connected():
                    cursor = conn.cursor()
                    delete_query = "DELETE FROM Cart WHERE id = %s"
                    cursor.execute(delete_query, (cart_id,))
                    conn.commit()
                    cursor.close()
                    QMessageBox.information(self, "Success", "Sản phẩm đã được xóa khỏi giỏ hàng!")
                    self.load_cart()  # Tải lại giỏ hàng sau khi xóa
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Lỗi khi xóa sản phẩm: {e}")
            finally:
                if conn.is_connected():
                    conn.close()

    def checkout(self):
        """
        Hàm thanh toán: thực hiện logic thanh toán và chuyển sang trang pay_page.
        """
        if self.ui.cartTable.rowCount() == 0:
            QMessageBox.warning(self, "Checkout", "Giỏ hàng trống!")
            return

        reply = QMessageBox.question(
            self,
            "Xác nhận thanh toán",
            "Bạn có chắc chắn muốn thanh toán?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            # Lấy parent widget cho đến khi tìm thấy MySidebar
            from pet_sidebar import MySidebar
            current_parent = self.parent()
            while current_parent and not isinstance(current_parent, MySidebar):
                current_parent = current_parent.parent()
                
            if current_parent and isinstance(current_parent, MySidebar):
                current_parent.switch_to_payPage()                                    
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = CartPage(user_id=2)
#     window.show()
#     sys.exit(app.exec())
                             