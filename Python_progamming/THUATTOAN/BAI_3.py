
arr = list(map(int, input().split()))

cnt_pos = cnt_neg = cnt_zero = 0

for num in arr:
    if num > 0:
        cnt_pos += 1
    elif num < 0:
        cnt_neg += 1
    else:
        cnt_zero += 1

print(cnt_pos, cnt_neg, cnt_zero)

