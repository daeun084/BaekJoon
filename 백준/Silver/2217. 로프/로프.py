n = int(input())
weights = sorted([int(input()) for _ in range(n)], reverse=True)
max_weight = 0

for i in range(n):
    tmp_weight = weights[i] * (i + 1)
    if tmp_weight >= max_weight:
        max_weight = tmp_weight

print(max_weight)