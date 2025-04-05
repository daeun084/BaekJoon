n = int(input())
result = n // 2 + 1

l = 1
r = n // 2 + 1
while l <= r:
    mid = (l + r) // 2
    val = mid ** 2
    
    if val == n:
        result = mid
        break
    elif val > n:
        if mid < result:
            result = mid
        r = mid - 1
    else:
        l = mid + 1

if n == 0:
    print(0)
else:
    print(result)