n, s = map(int, input().split())
arr = list(map(int, input().split()))
mem = [0 for _ in range(n + 1)]
idx = [0 for _ in range(n + 1)]
min_len = n

for i in range(1, n + 1):
    mem[i] += mem[i - 1] + arr[i - 1]

for i in range(1, n + 1):
    if i == 1:
        idx[i] = 1
    else:
        idx[i] = idx[i - 1]

    while idx[i] < n and mem[idx[i]] - mem[i - 1] < s:
        idx[i] += 1

    if idx[i] - i + 1 < min_len and mem[idx[i]] - mem[i - 1] >= s:
        min_len = idx[i] - i + 1

if sum(arr) < s and min_len == n:
    print(0)
else:
    print(min_len)