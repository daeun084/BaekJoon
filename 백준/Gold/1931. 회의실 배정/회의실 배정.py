# 데이터 입력
n = int(input())
arr = []
count = 0

for i in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])

# 끝나는 시간 기준 오름차순 정렬
arr = sorted(arr, key=lambda arr: (arr[1], arr[0]))

last_end = 0
for start, end in arr:
    # 이전 회의 끝나는 시간 이후 시작하는 회의 카운트
    if start >= last_end:
        count += 1
        last_end = end

print(count)