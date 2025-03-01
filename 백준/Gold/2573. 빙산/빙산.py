from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
positions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

q = deque()
year = 0

while 1:
    count = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    arround_arr = []

    # 빙산 개수 카운트
    for i in range(n):
        for j in range(m):
            if graph[i][j] and not visited[i][j]:
                q.append((i, j))
                visited[i][j] = True
                count += 1

                # 주변 바다 개수 카운트
                while q:
                    x, y = q.popleft()
                    arround = 0

                    for dx, dy in positions:
                        if 0 <= x + dx < n and 0 <= y + dy < m:
                            if not graph[x + dx][y + dy]:
                                arround += 1
                            elif not visited[x + dx][y + dy]:
                                q.append((x + dx, y + dy))
                                visited[x + dx][y + dy] = True

                    if arround > 0:
                        arround_arr.append((x, y, arround))

    if count >= 2:
        print(year)
        break

    # 빙산 높이 감소
    for x, y, arround in arround_arr:
        graph[x][y] = max(0, graph[x][y] - arround)

    if max(list(map(max, graph))) == 0:
        print(0)
        exit(0)

    year += 1