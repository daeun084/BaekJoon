from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
result = [0 for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n + 1):
    graph[i] = list(set(graph[i]))

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    visited[i] = True
    q = deque()

    for person in graph[i]:
        visited[person] = True
        q.append((person, 1))

    while q:
        person, count = q.popleft()
        result[i - 1] += count

        for next in graph[person]:
            if not visited[next]:
                visited[next] = True
                q.append((next, count + 1))

print(result.index(min(result)) + 1)
