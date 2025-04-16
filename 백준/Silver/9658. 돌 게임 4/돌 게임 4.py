n = int(input())
dp = ['CY' for _ in range(n + 1)]
nums = [1, 3, 4]

for i in range(1, n + 1):
    for num in nums:
        if i - num > 0 and dp[i - num] == 'CY':
            dp[i] = 'SK'
            break

print(dp[n])