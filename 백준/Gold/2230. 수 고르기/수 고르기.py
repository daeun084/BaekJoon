n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

idx = [0 for _ in range(n)]
result = max(arr) - min(arr)
for i in range(n - 1):
    if i == 0:
        idx[i] = 1
    else:
        idx[i] = idx[i - 1]

    while idx[i] < n - 1 and arr[idx[i]] - arr[i] < m:
        idx[i] += 1

    if m <= arr[idx[i]] - arr[i] < result:
        result = arr[idx[i]] - arr[i]

print(result)