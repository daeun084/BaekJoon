n = int(input())
arr = sorted(list(map(int, input().split())))
result = 0

for i in range(n):
    left = 1 if i == 0 else 0
    right = n - 2 if i == n - 1 else n - 1

    while left < right:
        if left == i:
            left += 1
            continue
        elif right == i:
            right -= 1
            continue

        val = arr[left] + arr[right]
        if val == arr[i]:
            result += 1
            break
        elif val > arr[i]:
            right -= 1
        else:
            left += 1

print(result)