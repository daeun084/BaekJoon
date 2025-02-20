from collections import deque
import sys
input = sys.stdin.readline

q = deque()
n = int(input())

homes = []
result = []

for i in range(n):
    homes.append(list(map(int, input().strip())))

while any(any(row) for row in homes):
    # 각 행의 처음 1 push
    for x in range(n):
        for y in range(n):
            if homes[x][y]:
                q.append((x, y))
                break
        if q:
           break

    count = 0
    while q:
        i, j = q.popleft()
        count += 1
        homes[i][j] = 0

        for j2 in range(j + 1, n):
            if not homes[i][j2]:
                break
            homes[i][j2] = 0
            q.append((i, j2))

        if j < n - 1 and homes[i][j + 1]:
            homes[i][j + 1] = 0
            q.append((i, j + 1))

        if i < n - 1 and homes[i + 1][j]:
            homes[i + 1][j] = 0
            q.append((i + 1, j))

        if i > 0 and homes[i - 1][j]:
            homes[i - 1][j] = 0
            q.append((i - 1, j))

        if j > 0 and homes[i][j - 1]:
            homes[i][j - 1] = 0
            q.append((i, j - 1))

    if count:
        result.append(count)

result = sorted(result)
print(len(result))
for i in result:
    print(i)