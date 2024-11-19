chuoi_ki_tu = input("Nhập vào chuỗi kí tự: ")
def is_brinary_string(brinary_string):
   if chuoi_ki_tu not in('0','1'):
       print("vui lòng nhập chuỗi nhị phân")
   else:
      chuyen_sang_nhi_phan = int(chuoi_ki_tu, 2)
      print(f"{chuoi_ki_tu}: là số nhị phân,chuyen sang thập phân: {chuyen_sang_nhi_phan}")