n, x = map(int, input().split())
visits = list(map(int, input().split()))

sums = [visits[i] for i in range(n)]
for i in range(1, n):
    sums[i] += sums[i - 1]

max_visit = 0
visit_count = 0

for i in range(x - 1, n):
    if i - x < 0:
        res = sums[i]
    else:
        res = sums[i] - sums[i - x]
        
    if res > max_visit:
        max_visit = res
        visit_count = 1
    elif res == max_visit:
        visit_count += 1

if max_visit == 0:
    print('SAD')
else:
    print(max_visit)
    print(visit_count)