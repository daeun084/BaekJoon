import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())
heights = list(map(int, input().split()))

# 각 요소 간의 차이값 계산
gaps = [heights[i + 1] - heights[i] for i in range(n - 1)]

# 최대 힙 생성
max_heap = [-gap for gap in gaps]
heapq.heapify(max_heap)

# 가장 큰 k개의 차이 제거
for _ in range(k - 1):
    heapq.heappop(max_heap)

# 나머지 값들 간의 합
result = -sum(max_heap)
print(result)
