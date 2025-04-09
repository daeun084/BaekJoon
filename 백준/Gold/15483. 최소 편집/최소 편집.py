s = [0] + list(input().strip())
t = [0] + list(input().strip())
dp = [[0]*len(t) for _ in range(len(s))]

# init value
for i in range(len(s)):
    dp[i][0] = i
for i in range(len(t)):
    dp[0][i] = i

# edit distance algorithm
for i in range(1, len(s)):
    for j in range(1, len(t)):
        cost = 0 if s[i] == t[j] else 1
        dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)

print(dp[-1][-1])