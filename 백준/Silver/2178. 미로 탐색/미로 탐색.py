from collections import deque
import sys
input = sys.stdin.readline

q = deque()
n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
mem = [[0 for _ in range(m)] for _ in range(n)]

positions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
q.append((0, 0, 1))
while q:
    x, y, dist = q.popleft()

    if x == n - 1 and y == m - 1:
        print(dist)
        exit(0)

    for dx, dy in positions:
        if 0 <= x + dx < n and 0 <= y + dy < m and graph[x + dx][y + dy] and not mem[x + dx][y + dy]:
            q.append((x + dx, y + dy, dist + 1))
            mem[x + dx][y + dy] = 1
