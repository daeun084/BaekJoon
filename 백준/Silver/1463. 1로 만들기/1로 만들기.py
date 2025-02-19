result = [-1] * 1000001
n = int(input())

for i in range(1, n + 1):
    if i == 2 or i == 3:
        result[i] = 1
        continue
    elif i == 1:
        result[i] = 0
        continue

    result[i] = result[i - 1] + 1

    if i % 2 == 0:
        result[i] = min(result[i], result[i // 2] + 1)
    if i % 3 == 0:
        result[i] = min(result[i], result[i // 3] + 1)

print(result[n])
