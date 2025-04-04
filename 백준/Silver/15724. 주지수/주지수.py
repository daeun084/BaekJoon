n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

mem = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for h in range(1, n + 1):
    for w in range(1, m + 1):
        mem[h][w] = mem[h][w - 1] + matrix[h - 1][w - 1]
for h in range(1, n + 1):
    for w in range(1, m + 1):
        mem[h][w] += mem[h - 1][w]

k = int(input())
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    print(mem[x2][y2] + mem[x1 - 1][y1 - 1] - mem[x2][y1 - 1] - mem[x1 - 1][y2])