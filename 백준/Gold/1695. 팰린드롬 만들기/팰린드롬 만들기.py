n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

for len in range(1, n):
    for l in range(1, n - len + 1):
        r = l + len

        if arr[l] != arr[r]:
            if len == 1:
                dp[l][r] = 1
            else:
                dp[l][r] = min(dp[l][r - 1] + 1, dp[l + 1][r] + 1)
        else:
            dp[l][r] = dp[l + 1][r - 1]

print(dp[1][n])