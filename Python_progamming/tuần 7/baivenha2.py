passw = 'toilet'
w = input("enter your password:")
solan = 3


while solan > 0:
    
    if w == passw:
        
        print("success")

        break

    else:
       
       solan -= 1
       
       print("wrong, try again")

       w = input("enter your password:")
       
if solan == 0:
    
    print("you have been locked")