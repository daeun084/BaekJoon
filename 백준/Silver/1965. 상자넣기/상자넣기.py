n = int(input())
box = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if box[i] > box[j] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1

print(max(dp))