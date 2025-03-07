x = int(input())
dp = [[0 for _ in range(3)] for _ in range(x + 1)]
if x == 1:
    print(0)
    print(1)
    exit(0)
elif x < 4:
    print(1)
    print(x, 1)
    exit(0)

dp[2] = [float('inf'), 1, 1]
dp[3] = [1, float('inf'), 2]

for i in range(4, x + 1):
    dp[i][0] = min(dp[i // 3]) + 1 if i % 3 == 0 else float('inf')
    dp[i][1] = min(dp[i // 2]) + 1 if i % 2 == 0 else float('inf')
    dp[i][2] = min(dp[i - 1]) + 1

print(min(dp[x]))

while x > 1:
    print(x, end=' ')
    idx = dp[x].index(min(dp[x]))

    if idx == 0:
        x = x // 3
    elif idx == 1:
        x = x // 2
    else:
        x = x - 1
print(1)