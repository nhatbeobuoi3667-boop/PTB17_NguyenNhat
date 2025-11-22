num = "123"
n = input("guess the number:")

while not n.isdigit():
    
    print("you cant type a word or special syntax")

    n = input("guess the number:")

while n != num:
    
    if n > num:
       
        print("too high")
        
        n = input("guess the number:")

        while not n.isdigit():
    
            print("you cant type a word or special syntax")

            n = input("guess the number:")
    else:

        print("too low")

        n = input("guess the number:")

        while not n.isdigit():
    
            print("you cant type a word or special syntax")

            n = input("guess the number:")

print("you got it!")