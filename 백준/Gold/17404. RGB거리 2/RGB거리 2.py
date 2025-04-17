n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = [[float('inf') for _ in range(3)] for _ in range(n)]
result = float('inf')

# 첫 집 선택
for first in range(3):
    for i in range(n):
        if i == 0:
            for color in range(0, 3):
                if color == first:
                    dp[i][color] = cost[i][color]
                else:
                    dp[i][color] = float('inf')
        else:
            dp[i][0] = cost[i][0] + min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = cost[i][1] + min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = cost[i][2] + min(dp[i - 1][0], dp[i - 1][1])

    for i in range(3):
        if i == first:
            continue
        result = min(result, dp[n - 1][i])

print(result)