import sys, heapq
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])

# 시작시간에 따라 정렬
arr.sort()

# 회의 종료 시간 저장 (최소힙)
rooms = []

for start, end in arr:
    # 사용 가능한 회의실 있다면 사용
    if rooms and start >= rooms[0]:
        heapq.heappop(rooms)

    # 종료 시간 추가
    heapq.heappush(rooms, end)

print(len(rooms))