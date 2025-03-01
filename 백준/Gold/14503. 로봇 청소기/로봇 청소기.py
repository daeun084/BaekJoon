from collections import deque
n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
positions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

q = deque()
q.append((r, c))
visited = set()

while q:
    # 해당 칸 청소
    x, y = q.popleft()
    if not graph[x][y] and (x, y) not in visited:
        visited.add((x, y))

    # 청소되지 않은 빈 칸 처리
    for _ in range(4):
        if d == 0:
            d = 3
        else:
            d = d - 1

        dx, dy = positions[d]
        if 0 <= dx + x < n and 0 <= dy + y < m \
                and not graph[dx + x][dy + y] \
                and (dx + x, dy + y) not in visited:
            q.append((dx + x, dy + y))
            break

    # 주변에 청소되지 않은 빈 칸이 없는 경우
    if not q:
        dx, dy = positions[d]
        if 0 <= -dx + x < n and 0 <= -dy + y < m \
            and not graph[-dx + x][-dy + y]:
            q.append((-dx + x, -dy + y))


print(len(visited))