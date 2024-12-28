n = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))
min_cost = 0
min_idx = 0

# 1. 최소 값 vertex idx 구함
for i in range(0, n - 1):
    if prices[min_idx] > prices[i]:
        min_idx = i

# 2. 처음 ~ 최소 vertex까지 움직임
for i in range(0, min_idx):
    min_cost += prices[0] * roads[i]

# 3. 최소 vertex ~ 끝까지 움직임
for i in range(min_idx, n - 1):
    min_cost += prices[min_idx] * roads[i]

print(min_cost)
