t = int(input())

while t > 0:
    n = int(input())
    arr = sorted(list(map(int, input().split()))) # 오름차순 정렬
    result = []

    # 홀수번째 먼저 넣음
    for i in range(0, n, 2):
        result.append(arr[i])

    # reverse
    if len(arr) % 2 == 1:
        arr.pop(len(arr)-1)
        n -= 1

    arr.sort(reverse=True)

    # 짝수번째 넣음
    for i in range(0, n, 2):
        result.append(arr[i])

    gap = []
    for i in range(1, len(result)):
        gap.append(abs(result[i] - result[i-1]))

    print(max(gap))
    t -= 1