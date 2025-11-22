s = int(input("nhập số giây:"))
gio = s // 3600
s = s % 3600
phut = s // 60
giay_con_lai = s % 60
print(gio,"giờ",phut,"phút",giay_con_lai,"giây")
