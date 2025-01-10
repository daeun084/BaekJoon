import sys, heapq
input = sys.stdin.readline

n = int(input())
arr = []
heapq.heapify(arr)
count = 0

for i in range(n):
    x = int(input())

    if x == 0:
        count += 1
        min = 0

        if len(arr) != 0:
            min = heapq.heappop(arr)

        count -= 1
        if count >= 0:
            print(min)
    else:
        heapq.heappush(arr, x)