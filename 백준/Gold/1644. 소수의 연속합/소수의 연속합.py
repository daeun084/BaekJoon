n = int(input())
result = 0
dec = [_ for _ in range(n + 1)]

# 에라토스테네스의 체
for i in range(2, n + 1):
    if not dec[i]:
        continue

    for j in range(2 * i, n + 1, i):
        dec[j] = 0

# 소수의 누적합
nums = [0]
for i in range(2, n + 1):
    if dec[i]:
        nums.append(dec[i])

nums_len = len(nums)
for i in range(1, nums_len):
    nums[i] += nums[i - 1]

# 투 포인터
idx = [1 for _ in range(n + 1)]
for i in range(1, n + 1):
    if i > 1:
        idx[i] = idx[i - 1]

    while idx[i] < nums_len and nums[idx[i]] - nums[i - 1] < n:
        idx[i] += 1

    if idx[i] < nums_len and nums[idx[i]] - nums[i - 1] == n:
        result += 1
        
print(result)