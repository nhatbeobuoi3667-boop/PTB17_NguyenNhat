chieu_dai = int(input("nhập chiều dài:"))
chieu_rong = int(input("nhập chiều rộng"))
chu_vi = (chieu_dai + chieu_rong) * 2  
canh_hinhv = chu_vi / 2
chu_vi_hinh_vuong = canh_hinhv * 4
cong_2_hinh = chu_vi_hinh_vuong + chu_vi
print("chu vi HCN là", chu_vi)
print("cạnh HV là", canh_hinhv)
print("chu vi HV là", chu_vi_hinh_vuong)
print("tổng chu vi hai hình là", cong_2_hinh)