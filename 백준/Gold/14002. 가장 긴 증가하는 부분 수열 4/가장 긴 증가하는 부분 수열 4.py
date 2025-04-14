import bisect

n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n + 1)]
l = [0 for _ in range(n + 1)]
len = 0

for i in range(n):
    pos = bisect.bisect_left(l, arr[i], 1, len + 1)

    dp[i] = pos
    l[pos] = arr[i]

    if len < pos:
        len += 1

result = [0 for _ in range(len + 1)]
for i in range(n - 1, -1, -1):
    pos = dp[i]

    if arr[i] > result[pos]:
        if pos == len or arr[i] < result[pos + 1]:
            result[pos] = arr[i]

print(len)
for i in range(1, len + 1):
    print(result[i], end=' ')