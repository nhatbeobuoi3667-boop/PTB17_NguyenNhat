x= int(input())
count=0
for num in range(1000,10000):
    sum=0
    for i in str(num):
        sum+=int(i)
    if sum==x:
        count+=1
print(count)