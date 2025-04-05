import sys
input = sys.stdin.readline
t = int(input())

max_num = 1000000
nums = [0 for _ in range(max_num + 1)]
for i in range(1, max_num + 1):
    for j in range(1, max_num // i + 1):
        nums[i * j] += i
    nums[i] += nums[i - 1]

for _ in range(t):
    n = int(input())
    print(nums[n])