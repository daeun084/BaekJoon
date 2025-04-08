n, k = map(int, input().split())
weight = [_ for _ in range(n + 1)]
value = [_ for _ in range(n + 1)]

for i in range(1, n + 1):
    weight[i], value[i] = map(int, input().split())

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(k + 1):
        if j < weight[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])

print(max(dp[n]))