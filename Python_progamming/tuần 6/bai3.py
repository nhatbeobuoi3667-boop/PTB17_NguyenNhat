n = int(input('enter a number'))
while n > 9 or n < 1:
	for i in range(1, 10):
		
		for x in range(1, 10):
			print(f"{n} x {x} =", n * i)

print("wrong number")