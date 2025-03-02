from collections import deque

n, k = map(int, input().split())
graph = [0 for _ in range(100001)]
q = deque()
q.append((n, 0))
graph[n] = 1

while q:
    x, time = q.popleft()
    if x == k:
        print(time)
        exit(0)

    if 0 <= x + 1 < 100001 and not graph[x + 1]:
        graph[x + 1] = 1
        q.append((x + 1, time + 1))
    if 0 <= x - 1 < 100001 and not graph[x - 1]:
        graph[x - 1] = 1
        q.append((x - 1, time + 1))
    if 0 <= 2 * x < 100001 and not graph[2 * x]:
        graph[2 * x] = 1
        q.append((2 * x, time + 1))