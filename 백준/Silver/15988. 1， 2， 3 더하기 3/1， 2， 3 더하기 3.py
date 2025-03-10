import sys
input = sys.stdin.readline

t = int(input())
dp = [1 for _ in range(1000000)]
dp[1] = 2
dp[2] = 4
mem = 3

for _ in range(t):
    n = int(input())

    if dp[n - 1] != 1:
        print(dp[n - 1])
        continue

    for i in range(mem, n):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

    print(dp[n - 1])
    mem = n