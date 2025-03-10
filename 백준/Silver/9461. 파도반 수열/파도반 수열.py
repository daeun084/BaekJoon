t = int(input())
for _ in range(t):
    n = int(input())
    dp = [1 for _ in range(n)]

    for i in range(3, n):
        dp[i] = dp[i - 2] + dp[i - 3]

    print(dp[n - 1])