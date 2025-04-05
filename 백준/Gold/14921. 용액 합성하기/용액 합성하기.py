n = int(input())
arr = sorted(list(map(int, input().split())))
result = min(arr) + max(arr)

left = 0
right = n - 1
while left < right:
    val = arr[left] + arr[right]
    if abs(val) <= abs(result):
        result = val

    if abs(arr[right]) > abs(arr[left]):
        right -= 1
    else:
        left += 1

print(result, end=' ')