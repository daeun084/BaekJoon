k, n = map(int, input().split())
lens = [int(input()) for _ in range(k)]

result = 0
l = 1
r = max(lens)
while l <= r:
    mid = (l + r) // 2

    sum = 0
    for len in lens:
        sum += len // mid

    if sum >= n:
        if result < mid:
            result = mid
        l = mid + 1
    else:
        r = mid - 1

print(result)