canh1 = int(input("nhập độ dài cạnh 1:"))
canh2 = int(input("nhập độ dài cạnh 2:"))
canh3 = int(input("nhập độ dài cạnh 3:"))
if canh1 == canh2 == canh3:
    print("tam giác đều")
elif canh1 == canh2 or canh2 ==  canh3 or canh1 == canh3:
    print("tam giác cân")
elif canh1**2 + canh2**2 == canh3**2:
    print("tam giác vuông")
else:
    print("k")
