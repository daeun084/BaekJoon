n, m = map(int, input().split())
maze = [[] for _ in range(n + 1)]
for i in range(n):
    maze[i] = list(map(int, input().split()))

positions = [(1, 0), (0, 1), (1, 1)]
dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = maze[0][0]

for i in range(n):
    for j in range(m):
        for dx, dy in positions:
            x = i + dx
            y = j + dy
            if x < n and y < m:
                dp[x][y] = max(dp[x][y], dp[i][j] + maze[x][y])
                
print(dp[n - 1][m - 1])