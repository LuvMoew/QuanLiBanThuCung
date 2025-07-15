from PySide6.QtWidgets import (QMainWindow, QLabel, QMessageBox, QTableWidgetItem, QGraphicsView, QGraphicsSimpleTextItem,
                               QGraphicsScene, QWidget, QHBoxLayout, QHeaderView, QTableWidget, QFrame)
from PySide6.QtGui import QPainter, QFont
from ui.ui_sidebar2 import Ui_MainWindow
import numpy as np
from config.connectDB import connect_db
from PySide6.QtCore import Qt
from PySide6.QtCharts import QChart, QChartView, QBarSeries, QBarSet, QValueAxis, QBarCategoryAxis, QLineSeries

class MySidebar(QMainWindow, Ui_MainWindow):
    def __init__(self, user_role=None, user_id=None):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Pet Shop")
        self.user_role = user_role  # Lưu role của user
        self.user_id = user_id 
        self.icon_name_widget.setHidden(True)
        self.cart_icon.setHidden(True)
        self.account_icon.setHidden(True)
        self.fishFrame.setHidden(True)
        self.birdLabel.setText("Hamster")
        self.birdCount.setText(str(self.count_pets_by_type("Hamster")))
        self.dogCount.setText(str(self.count_pets_by_type("Chó")))
        self.catCount.setText(str(self.count_pets_by_type("Mèo")))
        

        # Nếu user là customer, ẩn các mục không cho phép
        if self.user_role == "customer":
            self.pushButton_14.setHidden(True)
            self.lineEdit.setHidden(True)
            self.customer_icon.setHidden(True)
            self.customer_name.setHidden(True) 
            self.employee_icon.setHidden(True)
            self.employee_name.setHidden(True)
            self.cart_icon.setHidden(False)
            self.pay_icon.setHidden(True)
            self.pay_name.setHidden(True)
            self.account_icon.setHidden(False)
            self.pay_page.setHidden(False)
            self.user_icon.setHidden(True)
            self.user_name.setHidden(True)
            
        # Gán sự kiện cho các icon và label
        self.pay_page.setHidden(True)
        self.home_icon.clicked.connect(self.switch_to_homePage)
        self.customer_icon.clicked.connect(self.switch_to_customerPage)
        self.employee_icon.clicked.connect(self.switch_to_employeePage)
        self.pet_icon.clicked.connect(self.switch_to_petPage)
        self.accessories_food_icon.clicked.connect(self.switch_to_accessoriesFoodPage)
        self.service_icon.clicked.connect(self.switch_to_servicePage)
        self.pay_icon.clicked.connect(self.switch_to_orderPage)
        self.account_icon.clicked.connect(self.switch_to_accountPage)
        self.pushButton_6.clicked.connect(self.switch_to_loginPage)
        self.cart_icon.clicked.connect(self.switch_to_cartPage)
        self.user_icon.clicked.connect(self.switch_to_userPage)

        self.home_name.clicked.connect(self.switch_to_homePage)
        self.customer_name.clicked.connect(self.switch_to_customerPage)
        self.employee_name.clicked.connect(self.switch_to_employeePage)
        self.pet_name.clicked.connect(self.switch_to_petPage)
        self.accessories_food_name.clicked.connect(self.switch_to_accessoriesFoodPage)
        self.service_name.clicked.connect(self.switch_to_servicePage)
        self.pay_name.clicked.connect(self.switch_to_orderPage)
        self.pushButton_10.clicked.connect(self.switch_to_loginPage)
        self.user_name.clicked.connect(self.switch_to_userPage)
        
        self.switch_to_homePage()
        self.lineEdit.returnPressed.connect(self.search_database)
        self.pushButton_14.clicked.connect(self.search_database)
        self.plot_revenue_and_orders()

    def plot_revenue_and_orders(self):
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor(dictionary=True)

                # Truy vấn doanh thu theo tháng
                revenue_query = """
                    SELECT MONTH(NgayDat) AS month, SUM(TongTien) AS revenue 
                    FROM DonHang 
                    WHERE TrangThai = 'Đã thanh toán'
                    GROUP BY MONTH(NgayDat)
                    ORDER BY month
                """
                cursor.execute(revenue_query)
                revenue_results = cursor.fetchall()

                # Truy vấn số lượng đơn hàng theo tháng
                orders_query = """
                    SELECT MONTH(NgayDat) AS month, COUNT(*) AS order_count 
                    FROM DonHang 
                    WHERE TrangThai = 'Đã thanh toán'
                    GROUP BY MONTH(NgayDat)
                    ORDER BY month
                """
                cursor.execute(orders_query)
                orders_results = cursor.fetchall()

                if not revenue_results and not orders_results:
                    QMessageBox.warning(self, "Thông báo", "Không có dữ liệu để hiển thị.")
                    return

                # Dữ liệu mặc định cho 12 tháng
                months = [str(i) for i in range(1, 13)]
                revenues = [0] * 12
                order_counts = [0] * 12
                total_revenue = 0

                # Gán dữ liệu từ SQL vào danh sách
                for r in revenue_results:
                    month_index = r["month"] - 1
                    revenues[month_index] = r["revenue"]
                    total_revenue += r["revenue"]

                for o in orders_results:
                    month_index = o["month"] - 1
                    order_counts[month_index] = o["order_count"]

                # Xóa nội dung cũ của revenueFrame
                layout = self.revenueFrame.layout()
                if layout is not None:
                    while layout.count():
                        item = layout.takeAt(0)
                        if item.widget():
                            item.widget().deleteLater()

                # Tạo biểu đồ cột cho doanh thu
                revenue_set = QBarSet("Doanh thu (VND)")
                revenue_set.append(revenues)
                bar_series = QBarSeries()
                bar_series.append(revenue_set)

                # Tạo biểu đồ đường cho số đơn hàng
                order_series = QLineSeries()
                order_series.setName("Số đơn hàng")
                for i, order in enumerate(order_counts):
                    order_series.append(i, order)

                # Tạo biểu đồ
                chart = QChart()
                chart.addSeries(bar_series)
                chart.addSeries(order_series)
                chart.setTitle("Biểu đồ Doanh Thu & Số Đơn Hàng theo Tháng")
                chart.setAnimationOptions(QChart.SeriesAnimations)

                # Cấu hình trục X (12 tháng)
                axis_x = QBarCategoryAxis()
                axis_x.append(months)
                axis_x.setTitleText("Tháng")
                chart.addAxis(axis_x, Qt.AlignBottom)
                bar_series.attachAxis(axis_x)
                order_series.attachAxis(axis_x)

                # Cấu hình trục Y cho doanh thu
                axis_y = QValueAxis()
                axis_y.setLabelFormat("%i")
                axis_y.setTitleText("Doanh thu (VND)")
                chart.addAxis(axis_y, Qt.AlignLeft)
                bar_series.attachAxis(axis_y)

                # Cấu hình trục Y cho số đơn hàng (bên phải)
                axis_y2 = QValueAxis()
                axis_y2.setLabelFormat("%i")
                axis_y2.setTitleText("Số đơn hàng")
                chart.addAxis(axis_y2, Qt.AlignRight)
                order_series.attachAxis(axis_y2)

                # **Tạo QChartView để hiển thị biểu đồ**
                chart_view = QChartView(chart)
                chart_view.setRenderHint(QPainter.Antialiasing, True)

                # **Thêm QChartView vào revenueFrame**
                layout.addWidget(chart_view)

                # Cập nhật tổng doanh thu
                self.revenueLabel_2.setText(f"Tổng doanh thu: {total_revenue:,} VND")

        except Exception as e:
            print(e)
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi vẽ biểu đồ: {e}")
        finally:
            if conn and conn.is_connected():
                conn.close()

    def count_pets_by_type(self, pet_type: str) -> int:
        """
        Đếm số lượng thú cưng theo loài (pet_type) trong bảng ThuCung.
        pet_type: chuỗi chứa "Chó", "Mèo", "Hamster", v.v.
        Trả về số lượng thú cưng tương ứng, nếu có lỗi trả về 0.
        """
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                query = "SELECT COUNT(*) FROM ThuCung WHERE Loai = %s"
                cursor.execute(query, (pet_type,))
                result = cursor.fetchone()
                count = result[0] if result else 0
                cursor.close()
                return count
        except Exception as e:
            print("Error in count_pets_by_type:", e)
            return 0
        finally:
            if conn and conn.is_connected():
                conn.close()

    def switch_to_homePage(self):
        self.stackedWidget.setCurrentWidget(self.home_page)

    def switch_to_customerPage(self):
        if self.user_role == "customer":
            self.pushButton_14.setHidden(True)
            self.lineEdit.setHidden(True)
        else:
            self.lineEdit.setPlaceholderText("Tìm kiếm theo Email hoặc SDT")
            self.lineEdit.setHidden(False)
            self.pushButton_14.setHidden(False)
        from customer import CustomerPage
        self.customer_page = CustomerPage()
        if self.stackedWidget.indexOf(self.customer_page) == -1:
            self.stackedWidget.addWidget(self.customer_page)
        self.stackedWidget.setCurrentWidget(self.customer_page)

    def switch_to_employeePage(self):
        if self.user_role == "customer":
            self.pushButton_14.setHidden(True)
            self.lineEdit.setHidden(True)
        else:
            self.lineEdit.setPlaceholderText("Tìm kiếm theo Email hoặc SDT")
            self.lineEdit.setHidden(False)
            self.pushButton_14.setHidden(False)
        from employee import EmployeePage
        self.employee_page = EmployeePage()
        if self.stackedWidget.indexOf(self.employee_page) == -1:
            self.stackedWidget.addWidget(self.employee_page)
        self.stackedWidget.setCurrentWidget(self.employee_page)
        
    def switch_to_accountPage(self):
        self.pushButton_14.setHidden(True)
        self.lineEdit.setHidden(True)
        from info import InfoWindow
        # Truyền user_id từ phiên đăng nhập vào InfoWindow
        self.account_page = InfoWindow(user_id=self.user_id)
        if self.stackedWidget.indexOf(self.account_page) == -1:
            self.stackedWidget.addWidget(self.account_page)
        self.stackedWidget.setCurrentWidget(self.account_page)
        
    def switch_to_petPage(self):
        if self.user_role == "customer":
            self.pushButton_14.setHidden(True)
            self.lineEdit.setHidden(True)
        else:
            self.lineEdit.setPlaceholderText("Tìm kiếm theo tên")
            self.lineEdit.setHidden(False)
            self.pushButton_14.setHidden(False)
        from pet import PetPage
        self.pet_page = PetPage(user_role=self.user_role)
        if self.stackedWidget.indexOf(self.pet_page) == -1:
            self.stackedWidget.addWidget(self.pet_page)
        self.stackedWidget.setCurrentWidget(self.pet_page)

    def switch_to_payPage(self):
        self.pushButton_14.setHidden(True)
        self.lineEdit.setHidden(True)
        from pay import PaymentPage
        self.pay_page = PaymentPage(user_id=self.user_id)
        if self.stackedWidget.indexOf(self.pay_page) == -1:
            self.stackedWidget.addWidget(self.pay_page)
        self.stackedWidget.setCurrentWidget(self.pay_page)

    def switch_to_orderPage(self):
        self.pushButton_14.setHidden(True)
        self.lineEdit.setHidden(True)
        from order import OrderPage
        self.order_page = OrderPage()
        if self.stackedWidget.indexOf(self.order_page) == -1:
            self.stackedWidget.addWidget(self.order_page)
        self.stackedWidget.setCurrentWidget(self.order_page)

    def switch_to_servicePage(self):
        if self.user_role == "customer":
            self.pushButton_14.setHidden(True)
            self.lineEdit.setHidden(True)
        else:
            self.lineEdit.setPlaceholderText("Tìm kiếm theo tên")
            self.lineEdit.setHidden(False)
            self.pushButton_14.setHidden(False)
        from service import ServicePage
        self.service_page = ServicePage(user_role=self.user_role, user_id=self.user_id)
        if self.stackedWidget.indexOf(self.service_page) == -1:
            self.stackedWidget.addWidget(self.service_page)
        self.stackedWidget.setCurrentWidget(self.service_page)

    def switch_to_cartPage(self):
        self.pushButton_14.setHidden(True)
        self.lineEdit.setHidden(True)
        from cart import CartPage
        self.cart_page = CartPage(user_id=self.user_id)
        if self.stackedWidget.indexOf(self.cart_page) == -1:
            self.stackedWidget.addWidget(self.cart_page)
        self.stackedWidget.setCurrentWidget(self.cart_page)
    
    def switch_to_accessoriesFoodPage(self):
        if self.user_role == "customer":
            self.pushButton_14.setHidden(True)
            self.lineEdit.setHidden(True)
        else: 
            self.lineEdit.setPlaceholderText("Tìm kiếm theo tên")
            self.lineEdit.setHidden(False)
            self.pushButton_14.setHidden(False)
        from product import ProductPage
        self.accessories_food_page = ProductPage(user_role=self.user_role,user_id=self.user_id)
        if self.stackedWidget.indexOf(self.accessories_food_page) == -1:
            self.stackedWidget.addWidget(self.accessories_food_page)
        self.stackedWidget.setCurrentWidget(self.accessories_food_page)
        
    def switch_to_userPage(self):
        if self.user_role == "customer":
            self.pushButton_14.setHidden(True)
            self.lineEdit.setHidden(True)
        else:
            self.lineEdit.setPlaceholderText("Tìm kiếm theo email")
            self.lineEdit.setHidden(False)
            self.pushButton_14.setHidden(False)
        from user import UserManagement
        self.user_page = UserManagement()
        if self.stackedWidget.indexOf(self.user_page) == -1:
            self.stackedWidget.addWidget(self.user_page)
        self.stackedWidget.setCurrentWidget(self.user_page)

    def switch_to_loginPage(self):
        from login import LoginWindow
        self.login_window = LoginWindow()  
        self.login_window.show()         
        self.close() 

    def search_database(self):
        """
        Tìm kiếm dữ liệu trong database dựa theo từ khóa nhập từ QLineEdit và hiển thị kết quả
        trong bảng tương ứng trên từng trang.
        """
        from customer import CustomerPage
        from employee import EmployeePage
        from pet import PetPage
        from product import ProductPage
        from service import ServicePage
        from user import UserManagement
        search_term = self.lineEdit.text().strip()
        if not search_term:
            QMessageBox.information(self, "Thông báo", "Vui lòng nhập từ khóa tìm kiếm!")
            return

        # Xác định trang hiện hành từ stackedWidget
        current_page = self.stackedWidget.currentWidget()
        sql = ""
        params = ()

        # Xác định câu truy vấn SQL dựa trên trang hiện tại
        if isinstance(current_page, CustomerPage):
            sql = """SELECT * 
                    FROM KhachHang 
                    WHERE Email LIKE %s OR SDT LIKE %s"""
            params = (f"%{search_term}%", f"%{search_term}%")
            
        elif isinstance(current_page, EmployeePage):
            sql = """SELECT * 
                    FROM NhanVien 
                    WHERE Email LIKE %s OR SDT LIKE %s"""
            params = (f"%{search_term}%", f"%{search_term}%")
            
        elif isinstance(current_page, PetPage):
            sql = """SELECT *
                    FROM ThuCung 
                    WHERE TenThuCung LIKE %s"""
            params = (f"%{search_term}%",)
            
        elif isinstance(current_page, ProductPage):
            sql = """SELECT *
                    FROM SanPham 
                    WHERE TenSP LIKE %s"""
            params = (f"%{search_term}%",)
        elif isinstance(current_page, ServicePage):
            sql = """SELECT *
                    FROM DichVu 
                    WHERE TenDV LIKE %s"""
            params = (f"%{search_term}%",)
        elif isinstance(current_page, UserManagement):
            sql = """SELECT *
                    FROM users 
                    WHERE email LIKE %s"""
            params = (f"%{search_term}%",)
        else:
            QMessageBox.information(self, "Thông báo", "Chức năng tìm kiếm không khả dụng trên trang này!")
            return

        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor(dictionary=True)
                cursor.execute(sql, params)
                results = cursor.fetchall()
                
                if not results:
                    QMessageBox.information(self, "Thông báo", "Không tìm thấy kết quả phù hợp!")
                    return
                    
                # Cập nhật bảng tương ứng trên từng trang
                if isinstance(current_page, CustomerPage):
                    current_page.ui.customerTable.setRowCount(0) 
                    for row, data in enumerate(results):
                        current_page.ui.customerTable.insertRow(row)
                        current_page.ui.customerTable.setItem(row, 0, QTableWidgetItem(str(data['MaKH'])))
                        current_page.ui.customerTable.setItem(row, 1, QTableWidgetItem(data['HoTen']))
                        current_page.ui.customerTable.setItem(row, 2, QTableWidgetItem(data['SDT']))
                        current_page.ui.customerTable.setItem(row, 3, QTableWidgetItem(data['Email']))
                        current_page.ui.customerTable.setItem(row, 4, QTableWidgetItem(data['DiaChi']))
                        current_page.ui.customerTable.setItem(row, 5, QTableWidgetItem(data['Anh']))
                        current_page.ui.customerTable.setItem(row, 6, QTableWidgetItem(str(data['NgayDangKy'])))
                        
                elif isinstance(current_page, EmployeePage):
                    current_page.ui.employeeTable.setRowCount(0)
                    for row, data in enumerate(results):
                        current_page.ui.employeeTable.insertRow(row)
                        current_page.ui.employeeTable.setItem(row, 0, QTableWidgetItem(str(data['MaNV'])))
                        current_page.ui.employeeTable.setItem(row, 1, QTableWidgetItem(data['HoTen']))
                        current_page.ui.employeeTable.setItem(row, 2, QTableWidgetItem(data['SDT']))
                        current_page.ui.employeeTable.setItem(row, 3, QTableWidgetItem(data['Email']))
                        current_page.ui.employeeTable.setItem(row, 4, QTableWidgetItem(data['ChucVu']))
                        current_page.ui.employeeTable.setItem(row, 5, QTableWidgetItem(data['Luong']))
                        current_page.ui.employeeTable.setItem(row, 6, QTableWidgetItem(data['Anh']))
                        current_page.ui.employeeTable.setItem(row, 7, QTableWidgetItem(str(data['NgayVaoLam'])))
                        
                elif isinstance(current_page, PetPage):
                    current_page.ui.tablePets.setRowCount(0)
                    for row, data in enumerate(results):
                        current_page.ui.tablePets.insertRow(row)
                        current_page.ui.tablePets.setItem(row, 0, QTableWidgetItem(str(data['MaThuCung'])))
                        current_page.ui.tablePets.setItem(row, 1, QTableWidgetItem(data['TenThuCung']))
                        current_page.ui.tablePets.setItem(row, 2, QTableWidgetItem(data['Loai']))
                        current_page.ui.tablePets.setItem(row, 3, QTableWidgetItem(str(data['GioiTinh'])))
                        current_page.ui.tablePets.setItem(row, 4, QTableWidgetItem(str(data['NgaySinh'])))
                        current_page.ui.tablePets.setItem(row, 5, QTableWidgetItem(str(data['GiaBan'])))
                        current_page.ui.tablePets.setItem(row, 6, QTableWidgetItem(data['TinhTrang']))
                        current_page.ui.tablePets.setItem(row, 7, QTableWidgetItem(data['MoTa']))
                        current_page.ui.tablePets.setItem(row, 8, QTableWidgetItem(data['Anh']))
                        
                elif isinstance(current_page, ProductPage):
                    current_page.ui.tableProducts.setRowCount(0)
                    for row, data in enumerate(results):
                        current_page.ui.tableProducts.insertRow(row)
                        current_page.ui.tableProducts.setItem(row, 0, QTableWidgetItem(str(data['MaSP'])))
                        current_page.ui.tableProducts.setItem(row, 1, QTableWidgetItem(data['TenSP']))
                        current_page.ui.tableProducts.setItem(row, 2, QTableWidgetItem(data['LoaiSP']))
                        current_page.ui.tableProducts.setItem(row, 3, QTableWidgetItem(str(data['GiaBan'])))
                        current_page.ui.tableProducts.setItem(row, 4, QTableWidgetItem(str(data['SoLuongTon'])))
                        current_page.ui.tableProducts.setItem(row, 5, QTableWidgetItem(data['MoTa']))
                        current_page.ui.tableProducts.setItem(row, 6, QTableWidgetItem(data['Anh']))
                
                elif isinstance(current_page, ServicePage):
                    current_page.ui.tblDichVuPage1.setRowCount(0)
                    for row, data in enumerate(results):
                        current_page.ui.tblDichVuPage1.insertRow(row)
                        current_page.ui.tblDichVuPage1.setItem(row, 0, QTableWidgetItem(str(data['MaDV'])))
                        current_page.ui.tblDichVuPage1.setItem(row, 1, QTableWidgetItem(data['TenDV']))
                        current_page.ui.tblDichVuPage1.setItem(row, 2, QTableWidgetItem(str(data['Gia'])))
                        current_page.ui.tblDichVuPage1.setItem(row, 3, QTableWidgetItem(str(data['MoTa'])))
                        
                elif isinstance(current_page, UserManagement):
                    current_page.ui.tableWidget.setRowCount(0)
                    for row, data in enumerate(results):
                        current_page.ui.tableWidget.insertRow(row)
                        current_page.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(data['id'])))
                        current_page.ui.tableWidget.setItem(row, 1, QTableWidgetItem(data['name']))
                        current_page.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(data['email'])))
                        current_page.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(data['pass'])))
                        current_page.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(data['created_at'])))
                        current_page.ui.tableWidget.setItem(row, 5, QTableWidgetItem(str(data['updated_at'])))
                        current_page.ui.tableWidget.setItem(row, 6, QTableWidgetItem(str(data['role'])))
                
            else:
                QMessageBox.critical(self, "Error", "Không kết nối được tới cơ sở dữ liệu!")
                
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi tìm kiếm: {e}")
            
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()