n = int(input('enter a integer num:'))

tong = 0

dem = []

for i in range(1, n + 1):
	
	if i % 2== 1:
		tong += i
		dem.append(i)

print(f"sum of the odd nums from t to {n}: {tong}, {dem}")
