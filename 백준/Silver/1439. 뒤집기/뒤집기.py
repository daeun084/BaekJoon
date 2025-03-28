arr = list(map(str, input().strip()))
min_result = 0

zero = 0
one = 0
if arr[0] == '0':
    zero += 1
else:
    one += 1

for i in range(1, len(arr)):
    if arr[i] == '0' and arr[i - 1] == '1':
        zero += 1
    elif arr[i] == '1' and arr[i - 1] == '0':
        one += 1

print(min(one, zero))