n = int(input())
N = int(input())
count = 0


for i in range(n, N + 1):
    if i%3==0:
        count += 1

print(count)