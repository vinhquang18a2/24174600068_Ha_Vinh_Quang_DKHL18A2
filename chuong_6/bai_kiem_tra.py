def xem_danh_sach(mat_hang):
    if not mat_hang:
        print("Danh sách mặt hàng rỗng.")
    else:
        for mat_hang in mat_hang:
            print(f"{mat_hang['ma_hang']} - {mat_hang['ten_hang']} - {mat_hang['don_vi_tinh']} - {mat_hang['don_gia']} - {mat_hang['so_luong']} - {mat_hang['thanh_tien']} - {mat_hang['thue_vat']}")

def nhap_mat_hang():
    try:
        ma_hang = input("Nhập mã hàng: ")
        ten_hang = input("Nhập tên hàng: ")
        don_vi_tinh = input("Nhập đơn vị tính: ")
        don_gia = float(input("Nhập đơn giá: "))
        assert don_gia > 0, "Đơn giá phải là số dương"
        
        so_luong = int(input("Nhập số lượng: "))
        assert so_luong >= 0, "Số lượng phải là số nguyên không âm"

        thanh_tien = don_gia * so_luong
        thue_vat = thanh_tien * 0.1
        
        return {
            'ma_hang': ma_hang,
            'ten_hang': ten_hang,
            'don_vi_tinh': don_vi_tinh,
            'don_gia': don_gia,
            'so_luong': so_luong,
            'thanh_tien': thanh_tien,
            'thue_vat': thue_vat
        }
    
    except ValueError:
        print("Lỗi: Nhập sai định dạng dữ liệu (số thực cho đơn giá và số nguyên cho số lượng).")
    except AssertionError as e:
        print(f"Lỗi: {e}")
    return None

def tim_kiem_mat_hang(mat_hangs, ma_hang):
    for mat_hang in mat_hangs:
        if mat_hang['ma_hang'] == ma_hang:
            return mat_hang
    return None

def xoa_mat_hang(mat_hangs, ma_hang):
    mat_hang = tim_kiem_mat_hang(mat_hangs, ma_hang)
    if mat_hang:
        mat_hangs.remove(mat_hang)
        print(f"Đã xóa mặt hàng với mã {ma_hang}.")
    else:
        print("Không tìm thấy mặt hàng.")

def chinh_sua_mat_hang(mat_hangs, ma_hang):
    mat_hang = tim_kiem_mat_hang(mat_hangs, ma_hang)
    if mat_hang:
        try:
            mat_hang['ten_hang'] = input("Nhập lại tên hàng: ")
            mat_hang['don_vi_tinh'] = input("Nhập lại đơn vị tính: ")
            mat_hang['don_gia'] = float(input("Nhập lại đơn giá: "))
        assert mat_hang['don_gia'] > 0, "Đơn giá phải là số dương"
        mat_hang['so_luong'] = int(input("Nhập lại số lượng: "))
        assert mat_hang['so_luong'] >= 0, "Số lượng phải là số nguyên không âm"   
        mat_hang['thanh_tien'] = mat_hang['don_gia'] * mat_hang['so_luong']
        mat_hang['thue_vat'] = mat_hang['thanh_tien'] * 0.1
        print("Đã chỉnh sửa thông tin mặt hàng.")
        except ValueError
        print("Lỗi: Nhập sai định dạng dữ liệu (số thực cho đơn giá và số nguyên cho số lượng).")  
    else:
        print("Không tìm thấy mặt hàng.")
def sap_xep_danh_sach(mat_hangs):
    mat_hangs.sort(key=lambda x: x['ten_hang'])
    print("Danh sách mặt hàng đã được sắp xếp theo tên:")
    def menu():
       mat_hangs = []
    while True:
        print("\n1. Xem danh sách mặt hàng")
        print("2. Nhập thông tin mặt hàng")
        print("3. Tính thành tiền và thuế VAT cho các mặt hàng")
        print("4. Tìm kiếm và xóa mặt hàng")
        print("5. Tìm kiếm và chỉnh sửa thông tin mặt hàng")
        print("6. Sắp xếp danh sách mặt hàng theo tên")
        print("0. Thoát")
        
   

if __name__ == "__main__":
    menu()