from collections import deque


def bfs():
    for _ in range(t):
        n = int(input())  # 편의점 개수
        home_x, home_y = map(int, input().split())  # 상근이의 집 좌표
        conv = [tuple(map(int, input().split())) for _ in range(n)]  # 편의점 좌표
        fstv_x, fstv_y = map(int, input().split())  # 페스티벌 좌표

        visited = set()
        q = deque()
        q.append((home_x, home_y))

        while q:
            x, y = q.popleft()

            if abs(x - fstv_x) + abs(y - fstv_y) <= 1000:
                return 'happy'

            for cx, cy in conv:
                if (cx, cy) not in visited and abs(x - cx) + abs(y - cy) <= 1000:
                    visited.add((cx, cy))
                    q.append((cx, cy))

        return 'sad'


t = int(input())
for _ in range(t):
    print(bfs())
