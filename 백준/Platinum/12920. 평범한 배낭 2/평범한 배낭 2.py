n, m = map(int, input().split())
w, v = [0], [0]

for i in range(1, n + 1):
    weight, value, k = map(int, input().split())

    b = 1
    while k > 0:
        ix = min(b, k)
        w.append(weight * ix)
        v.append(value * ix)
        k -= ix
        b <<= 1  # b = b * 2

arr_len = len(w)
dp = [[0 for _ in range(m + 1)] for _ in range(arr_len)]

for i in range(1, arr_len):
    for j in range(m + 1):
        if j < w[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])

print(max(dp[arr_len - 1]))