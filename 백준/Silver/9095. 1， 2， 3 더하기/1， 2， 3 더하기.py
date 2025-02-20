t = int(input())
t_case = []
for _ in range(t):
    t_case.append(int(input()))

dp = [0] * (max(t_case) + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in t_case:

    for n in range(4, i + 1):
        if not dp[n]:
            dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

    print(dp[i])