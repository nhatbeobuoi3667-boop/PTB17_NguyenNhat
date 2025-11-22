n = list(map(int, input("enter three side:").split()))

if n[0] + n[1] > n[2] and n[1] + n[2] > n[0] and n[0] + n[2] > n[1]:
    print("this is a triangle")
else:
    print("this isnt a triangle")