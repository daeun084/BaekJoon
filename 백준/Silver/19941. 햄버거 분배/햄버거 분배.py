n, k = map(int, input().split())
arr = list(input())
count = 0

idx = 0
for i in range(0, n):
    if arr[i] != 'P':
        continue

    for j in range(i - k, i + k + 1):
        if j < 0 or j >= n:
            continue

        if arr[j] == 'H':
            count += 1
            arr[j] = '-'
            break

print(count)

