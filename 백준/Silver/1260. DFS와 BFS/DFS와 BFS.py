from collections import deque
q = deque()

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
mem = [0 for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(n + 1):
    graph[i].sort()

def dfs(v):
    mem[v] = 1
    print(v, end=' ')

    for next in graph[v]:
        if not mem[next]:
            dfs(next)


def bfs(v):
    mem[v] = 1
    print(v, end=' ')
    q.append(v)

    while q:
        next = q.popleft()

        for i in graph[next]:
            if not mem[i]:
                mem[i] = 1
                print(i, end=' ')
                q.append(i)


dfs(v)
print()
mem[:] = [0] * (n + 1)
bfs(v)