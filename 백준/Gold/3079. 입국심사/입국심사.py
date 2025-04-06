n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]

l = 1
result = r = m * max(times)

while l <= r:
    mid = (l + r) // 2

    sum = 0
    for t in times:
        sum += mid // t

    if sum >= m:
        if mid < result:
            result = mid
        r = mid - 1
    else:
        l = mid + 1

print(result)