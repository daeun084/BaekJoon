n = int(input())
m = int(input())

# init all value to infinite
G = [[float('inf')] * (n + 1) for _ in range(n + 1)]

# get input data and put graph data
for i in range(m):
    a, b, c = map(int, input().split())
    if G[a][b] > c:
        G[a][b] = c

# init diagonal to 0
for i in range(1, n + 1):
    G[i][i] = 0

# floyd algorithm
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if G[i][k] + G[k][j] < G[i][j]:
                G[i][j] = G[i][k] + G[k][j]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if G[i][j] == float('inf'):
            G[i][j] = 0

# print result
for i in range(1, n+1):
    for j in range(1, n+1):
        print(G[i][j], end=" ")
    print()