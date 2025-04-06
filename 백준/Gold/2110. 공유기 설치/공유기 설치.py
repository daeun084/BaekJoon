n, c = map(int, input().split())
positions = sorted([int(input()) for _ in range(n)])

def check(x):
    cnt = 1
    last_p = 0
    for i in range(1, n):
        if positions[i] - positions[last_p] >= x:
            cnt += 1
            last_p = i
    return cnt >= c

l = 1
r = max(positions) - min(positions)
result = 1
while l <= r:
    mid = (l + r) // 2

    if check(mid):
        result = max(result, mid)
        l = mid + 1
    else:
        r = mid - 1

print(result)