n, k = map(int, input().split())
values = [int(input()) for _ in range(n)]

# 합이 dp[i]가 되는 동전 최소 개수
dp = [float('inf') for _ in range(k + 1)]
dp[0] = 0

for i in range(1, k + 1):
    for coin in values:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])