n = int(input())
N = int(input())
total = 0


for i in range(n, N):
    if i&2==0:
        total += i
        
print(f'sum of even numbers between {n} and {N}:{total}')   