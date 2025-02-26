from collections import deque

# 전체 F층, 사무실은 G층, S층에서 G층으로 이동하기 위해 누르는 버튼 수 최솟값
f, s, g, u, d = map(int, input().split())
graph = [0 for i in range(f + 1)]

q = deque()
q.append(s)
graph[s] = 1

while q:
    v = q.popleft()
    count = graph[v]
    if v == g:
        print(count - 1)
        exit(0)

    for next in (v+u, v-d):
        if 0 < next < f + 1 and not graph[next]:
            graph[next] = count + 1
            q.append(next)

print('use the stairs')