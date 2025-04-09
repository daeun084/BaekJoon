n = int(input())
arr = [0] + list(map(int, input().split()))
m = int(input())
s, e = [0 for _ in range(m)], [0 for _ in range(m)]
for i in range(m):
    s[i], e[i] = map(int, input().split())

dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

for i in range(1, n + 1):
    dp[i][i] = 1

for len in range(1, n):
    for l in range(1, n - len + 1):
        r = l + len

        if arr[l] == arr[r]:
            if len > 1 and dp[l + 1][r - 1]:
                dp[l][r] = 1
            elif len == 1:
                dp[l][r] = 1

for i in range(m):
    print(dp[s[i]][e[i]])