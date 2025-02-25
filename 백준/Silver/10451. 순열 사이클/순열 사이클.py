t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    mem = [0 for _ in range(n + 1)]
    result = 0

    def dfs(node):
        mem[node] = 1
        v = arr[node - 1]
        if not mem[v]:
            dfs(v)

    for i in arr:
        if not mem[i]:
            result += 1
            dfs(i)

    print(result)