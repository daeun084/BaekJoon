import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
results = []

G = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if G[a][b] > c:
        G[a][b] = c

start, end = map(int, input().split())

length = G[start].copy()
touch = [start for _ in range(n + 1)]

# Dijkstra algorithm
vnear = 0
for _ in range(n - 1):
    # find min value
    min_v = float('inf')
    for i in range(1, n + 1):
        if 0 <= length[i] <= min_v:
            vnear = i
            min_v = length[i]

    for i in range(1, n + 1):
        if G[vnear][i] != float('inf') and length[vnear] + G[vnear][i] < length[i]:
            touch[i] = vnear
            length[i] = length[vnear] + G[vnear][i]

        if 0 <= length[end] != float('inf'):
            results.append(length[end])

    length[vnear] = -1

if len(results) == 0:
    print(0)
else:
    print(min(results))