n, m = map(int, input().split())
m_input = list(map(int, input().split()))
v_input = list(map(int, input().split()))
memories = [0] + m_input
values = [0] + v_input

sum_value = sum(values)
dp = [[0 for _ in range(sum_value + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(sum_value + 1):
        if j < values[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - values[i]] + memories[i])
            
for i in range(sum_value + 1):
    if dp[n][i] >= m:
        print(i)
        break