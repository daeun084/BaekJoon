n = int(input())
arr = list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(1, n + 1):
    max_score = arr[i - 1]
    min_score = arr[i - 1]
    for j in range(i - 1, -1, -1):
        max_score = max(max_score, arr[j])
        min_score = min(min_score, arr[j])

        score_diff = max_score - min_score
        dp[i] = max(dp[i], dp[j] + score_diff)

print(dp[n])