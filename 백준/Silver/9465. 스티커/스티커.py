t = int(input())
for _ in range(t):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(2)]
    dp = graph.copy()

    for i in range(1, n):
        dp[0][i] = max(dp[1][i - 1] + graph[0][i], dp[0][i - 1])
        dp[1][i] = max(dp[0][i - 1] + graph[1][i], dp[1][i - 1])

    print(max(dp[0][n - 1], dp[1][n - 1]))