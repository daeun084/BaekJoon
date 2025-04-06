n = int(input())
arr = list(map(int, input().split()))

k = []
for a in arr:
    if not k or k[-1] < a:
        k.append(a)
        continue

    l, r = 0, len(k) - 1
    while l <= r:
        mid = (l + r) // 2
        if k[mid] == a:
            break
        elif k[mid] < a:
            l = mid + 1
        else:
            r = mid - 1

    if k[mid] != a:
        k[l] = a

print(len(k))