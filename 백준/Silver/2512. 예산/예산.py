n = int(input())
arr = list(map(int, input().split()))
m = int(input())

def check(x):
    sum = 0
    for i in arr:
        if i <= x:
            sum += i
        else:
            sum += x
    return sum

l = 1
r = max(arr)
while l <= r:
    mid = (l + r) // 2
    val = check(mid)
    if val <= m:
        l = mid + 1
    else:
        r = mid - 1
print(r)