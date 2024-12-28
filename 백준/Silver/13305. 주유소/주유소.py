n = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))
min_cost = 0
price_idx = 0
roads_idx = 0

while roads_idx < n - 1:
    min_cost += prices[price_idx] * roads[roads_idx]
    roads_idx += 1

    if prices[price_idx] > prices[price_idx + 1]:
        price_idx += 1
    elif prices[price_idx] > prices[roads_idx]:
        price_idx = roads_idx

print(min_cost)
