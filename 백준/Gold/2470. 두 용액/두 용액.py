n = int(input())
arr = sorted(list(map(int, input().split())))

left_v = min(arr)
right_v = max(arr)
result = abs(left_v + right_v)

left = 0
right = n - 1
while left < right:
    val = abs(arr[left] + arr[right])
    if val <= result:
        left_v = arr[left]
        right_v = arr[right]
        result = val

        if abs(right_v) > abs(left_v):
            right -= 1
        else:
            left += 1
    elif val > result:
        if abs(arr[right]) > abs(arr[left]):
            right -= 1
        else:
            left += 1
    else:
        right -= 1
        left += 1

print(left_v, right_v, end=' ')