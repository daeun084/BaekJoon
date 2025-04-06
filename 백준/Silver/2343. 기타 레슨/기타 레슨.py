n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr_sum = sum(arr)
result = arr_sum

def check(x):
    sum = 0
    group = 0
    for a in arr:
        if sum + a <= x:
            sum += a
        else:
            group += 1
            sum = a
    if group >= m or sum > x:
        return False
    else:
        return True

l = max(arr)
r = arr_sum
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        if result > mid:
            result = mid
        r = mid - 1
    else:
        l = mid + 1

print(result)