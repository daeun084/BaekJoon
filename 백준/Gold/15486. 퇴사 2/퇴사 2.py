import sys
input = sys.stdin.readline

n = int(input())
counsels = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n + 1)]

for i in range(n - 1, -1, -1):
    next, pay = counsels[i]

    if next + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(pay + dp[i + next], dp[i + 1])

print(max(dp))