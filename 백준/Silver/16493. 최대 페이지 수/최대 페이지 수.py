n, m = map(int, input().split())
days = [_ for _ in range(m + 1)]
pages = [_ for _ in range(m + 1)]
for i in range(1, m + 1):
    days[i], pages[i] = map(int, input().split())

dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(n + 1):
        if j < days[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - days[i]] + pages[i])

print(max(dp[m]))