A, P = map(int, input().split())
arr = [A]
pv_num = A

while 1:
    num = 0
    while pv_num > 0:
        num += (pv_num % 10) ** P
        pv_num = pv_num // 10

    if arr.__contains__(num):
        idx = arr.index(num)
        arr = arr[:idx]
        break
    else:
        pv_num = num
        arr.append(num)

print(len(arr))