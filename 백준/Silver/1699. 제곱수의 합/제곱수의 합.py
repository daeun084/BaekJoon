import math
import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for i in range(n + 1)]

if n <= 3:
    print(n)
    exit(0)

for i in range(1, n + 1):
    if not dp[i]:
        dp[i] = dp[i - 1] + 1
    for j in range(1, math.floor(i**(1/2)) + 1):
        if j * j <= i:
            dp[i] = min(1 + dp[i - j * j], dp[i])

print(dp[n])