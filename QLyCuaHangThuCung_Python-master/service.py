
import os
import pandas as pd
from PySide6.QtWidgets import (
    QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem, QApplication, QPushButton
)
from PySide6.QtCore import QDate, Qt, QTime
import datetime
import sys
from config.connectDB import connect_db
from ui.ui_service import Ui_ServiceWindow  # Đảm bảo file này tồn tại và đúng tên

class ServicePage(QMainWindow):
    def __init__(self, user_role=None,user_id = None, parent=None):
        super().__init__(parent)
        self.user_role = user_role
        self.user_id = user_id
        self.ui = Ui_ServiceWindow()
        self.ui.setupUi(self)
        self.ui.tblDanhSachDV.verticalHeader().setDefaultSectionSize(50)
        self.ui.tblLichHen.itemClicked.connect(self.load_appointment_details)
        self.load_combos()
        self.check_and_update_appointment_status()
        
        self.load_appointments()
        # Nếu user là customer, ẩn trang quản lý dịch vụ
        if self.user_role == "customer":
            self.ui.pageQuanLyDV.hide()
            self.ui.pageDatLichHen.hide()
            self.ui.btnBack.clicked.connect(self.switch_to_serviceManagerCustomerPage)
            self.ui.stackedWidget.setCurrentWidget(self.ui.pageDanhSachDV)
            # Kết nối sự kiện tìm kiếm:
            self.ui.txtTimKiem.returnPressed.connect(self.search_services)
            self.ui.cboLocLoai.currentIndexChanged.connect(self.search_services)
            # Load dữ liệu ban đầu (tất cả)
            self.search_services()
            self.ui.btnThemLichHen.clicked.connect(self.add_appointment)
            self.ui.btnXoaLichHen.clicked.connect(self.cancel_appointment)
            
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.pageQuanLyDV)
            self.ui.btnThem.clicked.connect(self.add_service)
            self.ui.btnSua.clicked.connect(self.edit_service)
            self.ui.btnXoa.clicked.connect(self.delete_service)
            self.ui.btnExcel.clicked.connect(self.import_from_excel)
            self.ui.btnQLyLichHen.clicked.connect(self.switch_to_managerServiceAppointmentsPage)
            self.ui.btnBack.clicked.connect(self.switch_to_serviceManagerPage)
            self.ui.tblDichVuPage1.itemClicked.connect(self.load_service_details)
            self.load_services()

    def check_and_update_appointment_status(self):
        """
        Kiểm tra thời gian các lịch hẹn và cập nhật trạng thái thành 'Hoàn thành' 
        nếu đã qua 1 tiếng kể từ thời gian hẹn và trạng thái hiện tại là 'Đã đặt'.
        """
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                
                # Lấy thời gian hiện tại
                current_time_query = "SELECT NOW()"
                cursor.execute(current_time_query)
                current_time = cursor.fetchone()[0]
                
                # Tìm các lịch hẹn có trạng thái 'Đã đặt' và đã qua 1 tiếng so với thời gian hẹn
                query = """
                UPDATE LichHenDichVu
                SET TrangThai = 'Hoàn thành'
                WHERE TrangThai = 'Đã đặt'
                AND CONCAT(NgayHen, ' ', GioHen) < DATE_SUB(NOW(), INTERVAL 1 HOUR)
                """
                
                cursor.execute(query)
                conn.commit()
                
                # Lấy số lượng bản ghi được cập nhật
                updated_count = cursor.rowcount
                
                cursor.close()
                conn.close()
                
                return updated_count
                
        except Exception as e:
            log_error = f"Lỗi khi cập nhật trạng thái lịch hẹn: {str(e)}"
            print(log_error)  # In ra console để debug
            
            # Ghi log lỗi nếu cần
            with open("error_log.txt", "a", encoding="utf-8") as log_file:
                log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {log_error}\n")
                
            return -1  # Trả về -1 nếu có lỗi

    def load_combos(self):
        """Nạp danh sách dịch vụ, nhân viên và khách hàng vào các combo box."""
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                query = "SELECT MaDV, TenDV, Gia FROM DichVu"
                cursor.execute(query)
                self.ui.cboDichVu.clear()
                for row in cursor.fetchall():
                    # Thêm tên dịch vụ, data mặc định là MaDV
                    self.ui.cboDichVu.addItem(row[1], row[0])
                    # Lưu giá (Gia) vào item data với role Qt.UserRole+1
                    index = self.ui.cboDichVu.count() - 1
                    self.ui.cboDichVu.setItemData(index, row[2], Qt.UserRole + 1)
                cursor.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi load dịch vụ: {e}")
        finally:
            if conn.is_connected():
                conn.close()

        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                #Chỉ nạp nhân viên có vai trò chăm sóc
                query = "SELECT MaNV, HoTen FROM NhanVien WHERE ChucVu = 'Nhân viên chăm sóc'"
                cursor.execute(query)
                self.ui.cboNhanVien.clear()
                for row in cursor.fetchall():
                    self.ui.cboNhanVien.addItem(row[1], row[0])
                cursor.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi load nhân viên: {e}")
        finally:
            if conn.is_connected():
                conn.close()

        self.ui.cboKhachHang.clear()
        if self.user_role == "customer":
            try:
                conn = connect_db()
                if conn.is_connected():
                    cursor = conn.cursor()
                    query = "SELECT MaKH, HoTen FROM KhachHang WHERE MaKH = %s"
                    cursor.execute(query, (self.user_id,))
                    result = cursor.fetchone()
                    if result:
                        self.ui.cboKhachHang.addItem(result[1], result[0])
                    cursor.close()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Lỗi khi load khách hàng: {e}")
            finally:
                if conn.is_connected():
                    conn.close()
        else:
            self.ui.cboKhachHang.addItem("Khách vãng lai", 0)

        # --- Combo Trạng Thái ---
        self.ui.cboTrangThai.clear()
        self.ui.cboTrangThai.addItem("Đã đặt")
        self.ui.cboTrangThai.addItem("Hoàn thành")
        self.ui.cboTrangThai.addItem("Hủy")

        # Nếu admin, kết nối signal để hiển thị giá dịch vụ
        if self.user_role != "customer":
            self.ui.cboDichVu.currentIndexChanged.connect(self.update_service_price)
            # Hiển thị giá ban đầu nếu có dịch vụ được chọn
            if self.ui.cboDichVu.count() > 0:
                self.update_service_price(self.ui.cboDichVu.currentIndex())

    def update_service_price(self, index):
        """
        Khi admin chọn dịch vụ từ combo cboDichVu, hiển thị giá dịch vụ tương ứng vào txtGiaDV.
        Giá được lưu trong item data với role Qt.UserRole + 1.
        """
        if index < 0:  # Kiểm tra index hợp lệ
            self.ui.txtGiaDV.clear()
            return
            
        price = self.ui.cboDichVu.itemData(index, Qt.UserRole + 1)
        if price is not None:
            # Định dạng giá tiền với dấu phân cách hàng nghìn
            self.ui.txtGiaDV.setText("{:,.0f} VND".format(float(price)))
        else:
            self.ui.txtGiaDV.clear()
    def load_appointments(self):
        """Nạp tất cả lịch hẹn từ bảng LichHenDichVu vào bảng tblLichHen."""
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                if self.user_role == "customer":
                    makh = self.user_id
                    query = "SELECT MaLichHen, MaKH, MaNV, MaDV, NgayHen, GioHen, TrangThai FROM LichHenDichVu WHERE MaKH = %s"
                    params = (makh,)
                else:
                    query = "SELECT MaLichHen, MaKH, MaNV, MaDV, NgayHen, GioHen, TrangThai FROM LichHenDichVu"
                    params = ()
                cursor.execute(query, params)
                self.ui.tblLichHen.setRowCount(0)
                for row in cursor.fetchall():
                    row_num = self.ui.tblLichHen.rowCount()
                    self.ui.tblLichHen.insertRow(row_num)
                    self.ui.tblLichHen.setItem(row_num, 0, QTableWidgetItem(str(row[0])))
                    self.ui.tblLichHen.setItem(row_num, 1, QTableWidgetItem(str(row[1])))
                    self.ui.tblLichHen.setItem(row_num, 2, QTableWidgetItem(str(row[2])))
                    self.ui.tblLichHen.setItem(row_num, 3, QTableWidgetItem(str(row[3])))
                    
                    # Xử lý Ngày hẹn
                    if row[4]:
                        if isinstance(row[4], datetime.timedelta):
                            # Giả sử row[4] là số ngày kể từ 1970-01-01
                            base_date = datetime.date(1970, 1, 1)
                            date_obj = base_date + row[4]
                            ngay = date_obj.strftime("%Y-%m-%d")
                        else:
                            ngay = row[4].strftime("%Y-%m-%d")
                    else:
                        ngay = ""
                    self.ui.tblLichHen.setItem(row_num, 4, QTableWidgetItem(ngay))
                    
                    # Xử lý Giờ hẹn
                    if row[5]:
                        if hasattr(row[5], "strftime"):
                            gio = row[5].strftime("%H:%M:%S")
                        else:
                            gio = str(row[5])
                    else:
                        gio = ""
                    self.ui.tblLichHen.setItem(row_num, 5, QTableWidgetItem(gio))
                    
                    self.ui.tblLichHen.setItem(row_num, 6, QTableWidgetItem(row[6]))
                    self.ui.tblLichHen.setItem(row_num, 7, QTableWidgetItem(""))
                cursor.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi tải lịch hẹn: {e}")
        finally:
            if conn.is_connected():
                conn.close()

    def add_appointment(self):
        """Thêm lịch hẹn mới vào cơ sở dữ liệu."""
        ngay_hen = self.ui.dateNgayHen.date().toString("yyyy-MM-dd")
        gio_hen = self.ui.timeGioHen.time().toString("HH:mm:ss")
        # Lấy MaKH, MaNV, MaDV từ combo (dữ liệu được lưu trong itemData)
        ma_kh = self.ui.cboKhachHang.currentData()
        ma_nv = self.ui.cboNhanVien.currentData()
        ma_dv = self.ui.cboDichVu.currentData()
        trang_thai = self.ui.cboTrangThai.currentText()
        ghi_chu = self.ui.txtGhiChu.toPlainText().strip()

        # Nếu user không phải customer (admin) thì MaKH luôn = 0
        if self.user_role != "customer":
            ma_kh = 0

        # Kiểm tra dữ liệu cần thiết
        if not (ngay_hen and gio_hen and ma_dv and (ma_nv is not None)):
            QMessageBox.warning(self, "Warning", "Vui lòng điền đầy đủ thông tin lịch hẹn!")
            return

        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                query = """
                    INSERT INTO LichHenDichVu (MaKH, MaNV, MaDV, NgayHen, GioHen, TrangThai, GhiChu)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, (ma_kh, ma_nv, ma_dv, ngay_hen, gio_hen, trang_thai, ghi_chu))
                conn.commit()
                QMessageBox.information(self, "Success", "Lịch hẹn đã được thêm thành công!")
                self.clear_fields()
                self.load_appointments()
                cursor.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi thêm lịch hẹn: {e}")
        finally:
            if conn.is_connected():
                conn.close()

    def cancel_appointment(self):
        """Hủy lịch hẹn đã chọn bằng cách cập nhật trạng thái thành 'Hủy'."""
        ma_lich_hen = self.ui.txtMaLichHen.text().strip()
        if not ma_lich_hen:
            QMessageBox.warning(self, "Warning", "Vui lòng chọn lịch hẹn cần hủy!")
            return

        reply = QMessageBox.question(
            self, "Xác nhận", "Bạn có chắc chắn muốn hủy lịch hẹn này?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            try:
                conn = connect_db()
                if conn.is_connected():
                    cursor = conn.cursor()
                    query = "UPDATE LichHenDichVu SET TrangThai = 'Hủy' WHERE MaLichHen = %s"
                    cursor.execute(query, (ma_lich_hen,))
                    conn.commit()
                    QMessageBox.information(self, "Success", "Lịch hẹn đã được hủy!")
                    self.clear_fields()
                    self.load_appointments()
                    cursor.close()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Lỗi khi hủy lịch hẹn: {e}")
            finally:
                if conn.is_connected():
                    conn.close()

    def clear_fields(self):
        """Xóa nội dung các ô nhập trên trang đặt lịch hẹn."""
        self.ui.txtMaLichHen.clear()
        self.ui.txtGhiChu.clear()
        self.ui.dateNgayHen.setDate(QDate.currentDate())
        self.ui.timeGioHen.setTime(QTime.currentTime())
        self.ui.cboKhachHang.setCurrentIndex(0)
        self.ui.cboNhanVien.setCurrentIndex(0)
        self.ui.cboDichVu.setCurrentIndex(0)
        self.ui.cboTrangThai.setCurrentIndex(0)

    def load_appointment_details(self, item):
        """
        Khi người dùng click vào một dòng trong bảng lịch hẹn, hàm này sẽ lấy dữ liệu từ dòng đó
        và đổ lên các trường nhập:
        - txtMaLichHen: Mã lịch hẹn
        - cboKhachHang: Chọn khách hàng (theo MaKH)
        - cboNhanVien: Chọn nhân viên (theo MaNV)
        - cboDichVu: Chọn dịch vụ (theo MaDV)
        - dateNgayHen: Ngày hẹn (định dạng yyyy-MM-dd)
        - timeGioHen: Giờ hẹn (định dạng HH:mm:ss)
        - cboTrangThai: Trạng thái lịch hẹn
        - txtGhiChu: Ghi chú (nếu có)
        """
        row = item.row()
        
        # Mã lịch hẹn
        maLichHen = self.ui.tblLichHen.item(row, 0).text()
        self.ui.txtMaLichHen.setText(maLichHen)
        
        # Khách hàng: lấy MaKH từ cột 1 và tìm trong cboKhachHang (giá trị được lưu trong itemData)
        maKH_str = self.ui.tblLichHen.item(row, 1).text()
        try:
            maKH = int(maKH_str)
        except Exception:
            maKH = None
        if maKH is not None:
            index = self.ui.cboKhachHang.findData(maKH)
            if index != -1:
                self.ui.cboKhachHang.setCurrentIndex(index)
        
        # Nhân viên: lấy MaNV từ cột 2
        maNV_str = self.ui.tblLichHen.item(row, 2).text()
        try:
            maNV = int(maNV_str)
        except Exception:
            maNV = None
        if maNV is not None:
            index = self.ui.cboNhanVien.findData(maNV)
            if index != -1:
                self.ui.cboNhanVien.setCurrentIndex(index)
        
        # Dịch vụ: lấy MaDV từ cột 3
        maDV_str = self.ui.tblLichHen.item(row, 3).text()
        try:
            maDV = int(maDV_str)
        except Exception:
            maDV = None
        if maDV is not None:
            index = self.ui.cboDichVu.findData(maDV)
            if index != -1:
                self.ui.cboDichVu.setCurrentIndex(index)
        
        # Ngày hẹn: cột 4 (định dạng "yyyy-MM-dd")
        ngay_str = self.ui.tblLichHen.item(row, 4).text()
        if ngay_str:
            date_obj = QDate.fromString(ngay_str, "yyyy-MM-dd")
            if date_obj.isValid():
                self.ui.dateNgayHen.setDate(date_obj)
        
        # Giờ hẹn: cột 5 (định dạng "HH:mm:ss")
        gio_str = self.ui.tblLichHen.item(row, 5).text()
        if gio_str:
            time_obj = QTime.fromString(gio_str, "HH:mm:ss")
            if time_obj.isValid():
                self.ui.timeGioHen.setTime(time_obj)
        
        # Trạng thái: cột 6
        trangThai_str = self.ui.tblLichHen.item(row, 6).text()
        index = self.ui.cboTrangThai.findText(trangThai_str)
        if index != -1:
            self.ui.cboTrangThai.setCurrentIndex(index)
        
        # Ghi chú: cột 7 (nếu có)
        ghiChu_item = self.ui.tblLichHen.item(row, 7)
        ghiChu_str = ghiChu_item.text() if ghiChu_item is not None else ""
        self.ui.txtGhiChu.setPlainText(ghiChu_str)

    def switch_to_managerServiceAppointmentsPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageDatLichHen)
    
    def switch_to_serviceManagerPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageQuanLyDV)
        
    def switch_to_serviceManagerCustomerPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageDanhSachDV)
    
    def search_services(self):
        """Tìm kiếm dịch vụ theo tên và theo mức giá được chọn."""
        search_text = self.ui.txtTimKiem.text().strip()
        price_filter = self.ui.cboLocLoai.currentText().strip()

        # Xây dựng câu lệnh SQL với điều kiện
        query = "SELECT MaDV, TenDV, Gia, MoTa FROM DichVu WHERE 1=1"
        params = []

        if search_text:
            query += " AND TenDV LIKE %s"
            params.append(f"%{search_text}%")

        if price_filter == "Dưới 100k":
            query += " AND Gia < %s"
            params.append(100000)
        elif price_filter == "Từ 100k - 300k":
            query += " AND Gia BETWEEN %s AND %s"
            params.extend([100000, 300000])
        elif price_filter == "Từ 300k - 500k":
            query += " AND Gia BETWEEN %s AND %s"
            params.extend([300000, 500000])
        elif price_filter == "Trên 500k":
            query += " AND Gia > %s"
            params.append(500000)

        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute(query, tuple(params))
                results = cursor.fetchall()
                cursor.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi tìm kiếm dịch vụ: {e}")
            return
        finally:
            if conn.is_connected():
                conn.close()

        # Load dữ liệu tìm được vào bảng tblDanhSachDV
        self.ui.tblDanhSachDV.setRowCount(0)
        for row_data in results:
            row_num = self.ui.tblDanhSachDV.rowCount()
            self.ui.tblDanhSachDV.insertRow(row_num)
            # Cột 0: MaDV
            self.ui.tblDanhSachDV.setItem(row_num, 0, QTableWidgetItem(str(row_data[0])))
            # Cột 1: Tên dịch vụ
            self.ui.tblDanhSachDV.setItem(row_num, 1, QTableWidgetItem(row_data[1]))
            # Cột 2: Giá (định dạng)
            formatted_price = "{:,.2f} VND".format(float(row_data[2]))
            self.ui.tblDanhSachDV.setItem(row_num, 2, QTableWidgetItem(formatted_price))
            # Cột 3: Mô tả
            self.ui.tblDanhSachDV.setItem(row_num, 3, QTableWidgetItem(row_data[3]))
            # Cột 4: (Dành cho mục đích khác)
            self.ui.tblDanhSachDV.setItem(row_num, 4, QTableWidgetItem(""))
            # Cột 5: Nút "Đặt lịch hẹn"
            btnDatLich = QPushButton("Đặt lịch hẹn")
            btnDatLich.setStyleSheet(
                "background-color: #e74f44; color: white; border: none; padding: 5px; border-radius: 4px; margin: 5px"
            )
            # Truyền cả MaDV, TenDV và Gia sang hàm chuyển trang
            btnDatLich.clicked.connect(
                lambda _, ma=row_data[0], ten=row_data[1], gia=row_data[2]: self.switch_to_datLichHen(ma, ten, gia)
            )
            self.ui.tblDanhSachDV.setCellWidget(row_num, 5, btnDatLich)

    def switch_to_datLichHen(self, maDV, tenDV, giaDV):
        """
        Khi nhấn nút 'Đặt lịch hẹn', chuyển sang trang đặt lịch hẹn.
        Preselect dịch vụ được chọn trong combo và hiển thị giá dịch vụ.
        """
        # Chuyển sang trang đặt lịch hẹn
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageDatLichHen)
        
        # Preselect dịch vụ trong combo box
        index = self.ui.cboDichVu.findData(maDV)
        if index != -1:
            self.ui.cboDichVu.setCurrentIndex(index)
        else:
            # Nếu không tìm thấy, thêm mục mới (nếu cần)
            self.ui.cboDichVu.addItem(tenDV, maDV)
            self.ui.cboDichVu.setCurrentIndex(self.ui.cboDichVu.count() - 1)
        
        # Cập nhật giá dịch vụ vào ô txtGiaDV (chỉ hiển thị, ô này thường ở chế độ read-only)
        self.ui.txtGiaDV.setText("{:,.2f} VND".format(float(giaDV)))

    def load_services(self):
        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                query = "SELECT MaDV, TenDV, Gia, MoTa FROM DichVu"
                cursor.execute(query)
                rows = cursor.fetchall()
                self.ui.tblDichVuPage1.setRowCount(0)
                for row in rows:
                    row_num = self.ui.tblDichVuPage1.rowCount()
                    self.ui.tblDichVuPage1.insertRow(row_num)
                    self.ui.tblDichVuPage1.setItem(row_num, 0, QTableWidgetItem(str(row[0])))
                    self.ui.tblDichVuPage1.setItem(row_num, 1, QTableWidgetItem(row[1]))
                    formatted_price = "{:,.2f}".format(float(row[2]))
                    self.ui.tblDichVuPage1.setItem(row_num, 2, QTableWidgetItem(formatted_price))
                    self.ui.tblDichVuPage1.setItem(row_num, 3, QTableWidgetItem(row[3]))
                    self.ui.tblDichVuPage1.setItem(row_num, 4, QTableWidgetItem(""))
                cursor.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi tải dữ liệu dịch vụ: {e}")
        finally:
            if conn.is_connected():
                conn.close()

    def load_service_details(self, item):
        row = item.row()
        self.ui.txtMaDV.setText(self.ui.tblDichVuPage1.item(row, 0).text())
        self.ui.txtTenDV.setText(self.ui.tblDichVuPage1.item(row, 1).text())
        self.ui.txtGia.setText(self.ui.tblDichVuPage1.item(row, 2).text())
        self.ui.txtMoTa.setPlainText(self.ui.tblDichVuPage1.item(row, 3).text())

    def add_service(self):
        ten = self.ui.txtTenDV.text().strip()
        gia = self.ui.txtGia.text().strip()
        mota = self.ui.txtMoTa.toPlainText().strip()
        if not ten or not gia:
            QMessageBox.warning(self, "Warning", "Vui lòng nhập tên và giá dịch vụ!")
            return

        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                query = "INSERT INTO DichVu (TenDV, Gia, MoTa) VALUES (%s, %s, %s)"
                cursor.execute(query, (ten, gia, mota))
                conn.commit()
                QMessageBox.information(self, "Success", "Dịch vụ đã được thêm thành công!")
                self.clear_fields()
                self.load_services()
                cursor.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi thêm dịch vụ: {e}")
        finally:
            if conn.is_connected():
                conn.close()

    def edit_service(self):
        ma = self.ui.txtMaDV.text().strip()
        if not ma:
            QMessageBox.warning(self, "Warning", "Vui lòng chọn dịch vụ cần sửa!")
            return

        ten = self.ui.txtTenDV.text().strip()
        gia = self.ui.txtGia.text().strip()
        mota = self.ui.txtMoTa.toPlainText().strip()
        if not ten or not gia:
            QMessageBox.warning(self, "Warning", "Vui lòng nhập tên và giá dịch vụ!")
            return

        try:
            conn = connect_db()
            if conn.is_connected():
                cursor = conn.cursor()
                query = "UPDATE DichVu SET TenDV = %s, Gia = %s, MoTa = %s WHERE MaDV = %s"
                cursor.execute(query, (ten, gia, mota, ma))
                conn.commit()
                QMessageBox.information(self, "Success", "Dịch vụ đã được cập nhật thành công!")
                self.clear_fields()
                self.load_services()
                cursor.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi cập nhật dịch vụ: {e}")
        finally:
            if conn.is_connected():
                conn.close()

    def delete_service(self):
        ma = self.ui.txtMaDV.text().strip()
        if not ma:
            QMessageBox.warning(self, "Warning", "Vui lòng chọn dịch vụ cần xóa!")
            return

        reply = QMessageBox.question(
            self, "Xác nhận", "Bạn có chắc chắn muốn xóa dịch vụ này?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            try:
                conn = connect_db()
                if conn.is_connected():
                    cursor = conn.cursor()
                    query = "DELETE FROM DichVu WHERE MaDV = %s"
                    cursor.execute(query, (ma,))
                    conn.commit()
                    QMessageBox.information(self, "Success", "Dịch vụ đã được xóa thành công!")
                    self.clear_fields()
                    self.load_services()
                    cursor.close()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Lỗi khi xóa dịch vụ: {e}")
            finally:
                if conn.is_connected():
                    conn.close()

    def import_from_excel(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Chọn file Excel", "", "Excel Files (*.xlsx *.xls)"
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
                    ten = str(row['TenDV']).strip() if 'TenDV' in row.index else ""
                    gia = str(row['Gia']).strip() if 'Gia' in row.index else ""
                    mota = str(row['MoTa']).strip() if 'MoTa' in row.index else ""
                    if not ten or not gia:
                        continue
                    query = "INSERT INTO DichVu (TenDV, Gia, MoTa) VALUES (%s, %s, %s)"
                    cursor.execute(query, (ten, gia, mota))
                conn.commit()
                QMessageBox.information(self, "Success", "Dữ liệu dịch vụ đã được nhập từ Excel thành công!")
                self.load_services()
                cursor.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi khi nhập dữ liệu từ Excel: {e}")
        finally:
            if conn.is_connected():
                conn.close()

    def clear_fields(self):
        self.ui.txtMaDV.clear()
        self.ui.txtTenDV.clear()
        self.ui.txtGia.clear()
        self.ui.txtMoTa.clear()
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = ServicePage(user_role="customer")  # ví dụ: role customer
#     window.show()
#     sys.exit(app.exec())
