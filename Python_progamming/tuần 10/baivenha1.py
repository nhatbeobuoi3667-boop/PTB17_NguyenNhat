test = int(input("Enter how many test: "))
point = list(map(int, input("Enter point for each test: ").split()))
while len(point) > test or len(point) < test:
    print("Doesnt fit with your test quantity")
    point = list(map(int, input("Enter point for each test: ").split()))
point.sort()
min_score = min(point)
count = point.count(min_score)
times_to_remove = 2 if count >=2 else 1
for i in range(times_to_remove):
    point.remove(min_score)
print(f"Your point after remove the smallest point: {point}")
count_high = sum(1 for p in point if p >= 8)
print("Number of points >= 8:", count_high)
