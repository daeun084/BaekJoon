n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [arr[i] for i in range(n)]

if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0] + arr[1])
elif n == 3:
    print(max(arr[1] + arr[0], arr[2] + arr[0], arr[1] + arr[2]))
else:
    dp[n - 2] = arr[n - 2] + arr[n - 1]
    dp[n - 3] = max(arr[n - 2] + arr[n - 3], arr[n - 1] + arr[n - 3], arr[n - 2] + arr[n - 1])

    for i in range(n - 4, -1, -1):
        dp[i] = max(dp[i + 2] + arr[i], dp[i + 3] + arr[i + 1] + arr[i], dp[i + 1])

    print(dp[0])