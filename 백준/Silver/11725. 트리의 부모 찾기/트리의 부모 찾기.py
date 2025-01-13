import sys, heapq

input = sys.stdin.readline
# 재귀 한계 설정
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n + 1)]
roots = [0] * (n + 1)
visited = [0] * (n + 1)


def dfs(node):
    if visited[node]:
        return
    visited[node] = 1

    for next in graph[node]:
        if not visited[next]:
            roots[next] = node
            dfs(next)


if __name__ == "__main__":
    for i in range(0, n - 1):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    dfs(1)

    for i in range(2, n + 1):
        print(roots[i])
