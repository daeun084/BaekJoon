n = int(input())
m = int(input())
result = 1

# 가짓수
dp = [1 for _ in range(41)]
dp[2] = 2
for i in range(3, 41):
    dp[i] = dp[i - 1] + dp[i - 2]

prev = 0
for _ in range(m):
    vip = int(input())
    result *= dp[vip - prev - 1]
    prev = vip
result *= dp[n - prev]

if m == 0:
    print(dp[n])
else:
    print(result)