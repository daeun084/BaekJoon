s = [0] + list(input().strip())
t = [0] + list(input().strip())
dp = [[0]*len(t) for _ in range(len(s))]

for i in range(len(s)):
    for j in range(len(t)):
        if i == j == 0:
            continue

        if s[i] == t[j]:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1)
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])