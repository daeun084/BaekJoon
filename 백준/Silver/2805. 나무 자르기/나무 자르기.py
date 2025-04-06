import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

l = 1
r = max(arr)
result = 0
while l <= r:
    mid = (l + r) // 2

    sum = 0
    for i in arr:
        sub = i - mid
        if sub > 0:
            sum += sub

    if sum >= m:
        if result < mid:
            result = mid
        l = mid + 1
    else:
        r = mid - 1

print(result)