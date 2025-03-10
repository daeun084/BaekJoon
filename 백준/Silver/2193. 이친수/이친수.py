n = int(input())
graph = [0 for _ in range(n)]
dp = [1 for _ in range(n)]

for i in range(2, n):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n - 1])