import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())
result = 0

left = 0
right = n - 1
while left < right:
    val = arr[left] + arr[right]
    if val == x:
        result += 1
        right -= 1
        left += 1
    elif val > x:
        right -= 1
    else:
        left += 1

print(result)