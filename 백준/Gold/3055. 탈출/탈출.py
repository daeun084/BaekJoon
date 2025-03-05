from collections import deque
r, c = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]
rocks = []

s = d = (0, 0)
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            s = (i, j)
        if graph[i][j] == 'D':
            d = (i, j)
        if graph[i][j] == '*':
            rocks.append((i, j))

q = deque()
positions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
q.append((s, 0, rocks))
visited[s[0]][s[1]] = 1
while q:
    (x, y), time, rocks = q.popleft()

    if d == (x, y):
        print(time)
        exit(0)

    new_rocks = set(rocks)
    for nx, ny in list(rocks):
        is_arround = False
        for dx, dy in positions:
            new_x, new_y = dx + nx, dy + ny
            if (new_x, new_y) == (x, y):
                is_arround = True
            if 0 <= new_x < r and 0 <= new_y < c:
                if graph[new_x][new_y] == '.':
                    new_rocks.add((new_x, new_y))

        if not is_arround:
            new_rocks.discard((nx, ny))
    rocks = list(new_rocks)

    for dx, dy in positions:
        if 0 <= dx + x < r and 0 <= dy + y < c and (dx + x, dy + y) not in rocks and not visited[x + dx][y + dy]:
            if graph[dx + x][dy + y] != 'X':
                visited[dx + x][dy + y] = 1
                q.append(((dx + x, dy + y), time + 1, rocks))

print('KAKTUS')