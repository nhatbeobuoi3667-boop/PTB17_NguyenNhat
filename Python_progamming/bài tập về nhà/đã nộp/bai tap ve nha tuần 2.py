chieu_dai = int (input("Nhập chiều dài:"))
chieu_rong = int (input("Nhập chiều rộng:"))
chu_vi = (chieu_dai + chieu_rong) * 2
dien_tich = chieu_dai * chieu_rong
if chieu_dai <= chieu_rong:
    print("số nhập không hợp lệ với độ dài hình chữ nhật")
else:
    print("Chiều dài là", chieu_dai)
    print("chiều rộng là", chieu_rong)
    print("Chu vi hình chữ nhật là",chu_vi)
    print("Diện tích hình chữ nhật là",dien_tich)