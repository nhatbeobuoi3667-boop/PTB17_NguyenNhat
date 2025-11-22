name = input("Nhập tên của bạn:")
d_toan = int (input("Nhập số điểm toán của bro:"))
d_van = int (input("Nhập số điểm văn của bro:"))
d_trung_binh_2_mon = (d_toan + d_van) / 2
print("học sinh:",name)
print("toán:",d_toan)
print("văn",d_van)
print("Điểm trung bình:", d_trung_binh_2_mon)

# tính tiền Việt sang đô
VND = int (input("Nhập số tiền của bạn:"))
USD = VND / 25000
print("Tiền đô là", USD, "dollars")
# tính chu vi, diện tích HCN
# chieu_dai = int (input("Nhập chiều dài:"))
# chieu_rong = int (input("Nhập chiều rộng:"))
# chu_vi = (chieu_dai + chieu_rong) * 2
# dien_tich = chieu_dai * chieu_rong
# print("chu vi HCN là",chu_vi)
# print("dien tich HCN là",dien_tich)