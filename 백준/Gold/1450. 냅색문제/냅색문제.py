from collections import defaultdict
from bisect import bisect_right

n, c = map(int, input().split())
weights = list(map(int, input().split()))
result = 0
dict = defaultdict(int)

def cal_weight_sum(arr):
    result = []
    for i in range(1 << len(arr)):
        total = 0
        for j in range(len(arr)):
            if i & (1 << j):
                total += arr[j]
        result.append(total)
    return sorted(result)

left_arr = cal_weight_sum(weights[:n // 2])
right_arr = cal_weight_sum(weights[n // 2:])

for left in left_arr:
    x = c - left
    count = bisect_right(right_arr, x) # x 이하 개수
    result += count

if c == 0:
    print(1)
else:
    print(result)