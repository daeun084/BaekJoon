from collections import deque

n = int(input())
graph = []
positions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
for i in range(n):
    graph.append(list(map(int, input().split())))

max_height = max(list(map(max, graph)))
min_height = min(list(map(min, graph)))
max_result = 1
for cur_height in range(min_height - 1, max_height):
    q = deque()
    mem = [[0 for _ in range(n)] for _ in range(n)]
    result = 0

    for x in range(n):
        for y in range(n):
            if not mem[x][y] and graph[x][y] > cur_height:
                q.append((x, y))
                mem[x][y] = 1
                result += 1

            while q:
                x2, y2 = q.popleft()

                for dx, dy in positions:
                    if 0 <= x2+dx < n and 0 <= y2+dy < n:
                        if not mem[x2+dx][y2+dy] and graph[x2+dx][y2+dy] > cur_height:
                            q.append((x2+dx, y2+dy))
                            mem[x2+dx][y2+dy] = 1

    if result > max_result:
        max_result = result

print(max_result)