import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []

    for _ in range(n):
        x, y = map(int, input().split())
        arr.append([x, y])

    # 내림차순 정렬
    arr = sorted(arr, key=lambda arr: (arr[0], arr[1]))

    max_x, max_y = arr[0]
    idx = 0
    max_emp = 0

    while idx < n:
        x, y = arr[idx]
        idx += 1

        if x > max_x and y > max_y:
            continue

        max_x, max_y = x, y
        max_emp += 1

    print(max_emp)