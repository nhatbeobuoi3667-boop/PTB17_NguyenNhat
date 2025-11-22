n = int(input("enter a integer num:"))

sum = 0

for i in range(1, n + 1):
    
    if i%2==0:

        sum += i

print(f"sum of even numbers from 1 to {n}: {sum}")
        