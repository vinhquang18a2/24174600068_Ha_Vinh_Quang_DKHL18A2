a =int(input("nhập vào số nguyên dương a: "))
b = int(input("nhập vào số nguyên dương b: "))
if a > 0 and b > 0:
    ucln = 1
    for i in range(1,min(a, b) + 1):
      if a % i == 0 and b % i == 0 :
        ucln = i 
        print(f"ước chung lớn nhấtlà: ,{ucln}")
      else:
        print("nhập vào số nguyên dương")


