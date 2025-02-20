n = int(input())
rect = [[] for _ in range(n)]
dp = [[] for _ in range(n)]
for i in range(n):
    rect[i] = list(map(int, input().split()))
    dp[i] = [0 for _ in range(i + 1)]

dp[0] = rect[0]
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + rect[i][j]
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + rect[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + rect[i][j]

print(max(dp[n - 1]))
