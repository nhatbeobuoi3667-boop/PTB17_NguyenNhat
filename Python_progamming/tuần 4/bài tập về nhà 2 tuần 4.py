minh = float and int(input("nhập chiều cao của Minh:"))
an = float and int(input("nhập chiều cao của An:"))
lan = float and int(input("nhập chiều cao của Lan:"))
if  minh < an < lan:
    print("Lan là người cao nhất")
elif minh > an > lan:
    print("Minh là người cao nhất")
elif an > minh > lan:
    print("An là người cao nhất")
else:
    print("ba người bằng nhau")