ten = input("Nhập tên của bạn: ")
tuoi = int(input("Nhập tuổi của bạn: "))

# Suy ra cấp học
if tuoi <= 11:
    print("Bạn vào cấp 1")
elif tuoi == 12 or tuoi <= 17:
    print("Bạn vào cấp 2")
elif tuoi == 18 or tuoi <= 22:
    print("Bạn vào đại học")
else:
    print("bạn béo")
# Nhập điểm 3 môn
toan = int(input("Nhập điểm Toán:"))
van = int(input("Nhập điểm Văn: "))
anh = int(input("Nhập điểm Anh: "))

# Tính điểm trung bình
dtb = (toan + van + anh) / 3

# Xếp loại học lực
if 90 <= dtb <= 100:
    print("Bạn là học sinh xuất sắc")
elif 80 <= dtb < 90:
    print("Bạn là học sinh giỏi")
elif 70 <= dtb < 80:
    print("Bạn là học sinh khá")
elif 50 <= dtb < 70:
    print("Bạn là học sinh trung bình")
else:
    print("Bạn là học sinh yếu")
