n = int(input())
cost = []
for _ in range(n):
    r, g, b = map(int, input().split())
    cost.append([r, g, b])

dp = [[0 for _ in range(3)] for _ in range(n)]
for i in range(3):
    dp[0][i] = cost[0][i]

for i in range(1, n):
        dp[i][0] = cost[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = cost[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = cost[i][2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[n-1]))