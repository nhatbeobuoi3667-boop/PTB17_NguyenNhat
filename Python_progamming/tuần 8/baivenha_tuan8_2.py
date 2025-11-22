mon = int(input("enter a month:"))
while mon > 12 or mon < 1:
    print("invalid month, try again")
    mon = input("enter a month:")
if mon in [1,3,5,7,8,10,12]:
    print("this month has 31 days")
elif mon in [4,6,9,11]:
    print("this month has 30 days")
else:
    print("this month has 28 or 29 days")