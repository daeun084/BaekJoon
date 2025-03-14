import heapq, sys
input = sys.stdin.readline

n, e = map(int, input().split())
k = int(input())
G = [[] for _ in range(n + 1)]

for _ in range(e):
    u, v, w = map(int, input().split())
    G[u].append((v, w))

# set result list
results = [float('inf') for _ in range(n + 1)]
results[k] = 0

# make heqpq
queue = []
heapq.heappush(queue, (0, k))

while queue:
    min_v, vnear = heapq.heappop(queue)

    if min_v > results[vnear]:
        continue

    # find shortest path from vnear
    for next_node, next_value in G[vnear]:
        new_dist = min_v + next_value

        if new_dist < results[next_node]:
            results[next_node] = new_dist
            heapq.heappush(queue, (new_dist, next_node))

# print result
for i in range(1, n + 1):
    if results[i] == float('inf'):
        print('INF')
    else:
        print(results[i])