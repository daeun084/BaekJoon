from collections import defaultdict
n, s = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = 0
dict = defaultdict(int)

# 비트 완전 탐색
def cal_arr_sum(arr):
    arr_sum = []
    for i in range(1 << len(arr)): # 2 ^ len(arr)개
        total = 0
        for j in range(len(arr)):
            if i & (1 << j): # j번째 요소가 포함되면
                total += arr[j]
        arr_sum.append(total)
    return sorted(arr_sum)

left_arr = cal_arr_sum(arr[:n // 2])
right_arr = cal_arr_sum(arr[n // 2:])

for item in right_arr:
    dict[item] += 1

right_arr = list(set(right_arr))

for item in left_arr:
    k = s - item
    result += dict[k]

if s == 0:
    result -= 1
    
print(result)