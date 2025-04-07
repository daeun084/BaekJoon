n = int(input())
weights = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))
max_v = max(max(arr) + 1, sum(weights) + 1)

dp = [[0 for _ in range(max_v)] for _ in range(n + 1)]
dp[0][0] = 1

for i in range(1, n + 1):
    for j in range(max_v):
        if dp[i - 1][j]:
            dp[i][j] = 1

            if 0 <= abs(j - weights[i - 1]) < max_v:
                dp[i][abs(j - weights[i - 1])] = 1

            if 0 <= j + weights[i - 1] < max_v:
                dp[i][j + weights[i - 1]] = 1

for result in arr:
    if dp[n][result]:
        print('Y', end=' ')
    else:
        print('N', end=' ')