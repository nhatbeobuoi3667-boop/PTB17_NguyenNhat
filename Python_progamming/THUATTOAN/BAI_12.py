n = input()
n2 = input()
count = 0
n,n2 = int(n), int(n2)



for x in range(n, n2):
    isprime = True
    i = 2
    while i * i <= x :
        if i%2==0:
            isprime = False
            break
        i += 1
    
if isprime == True:
    count += 1

print(count)