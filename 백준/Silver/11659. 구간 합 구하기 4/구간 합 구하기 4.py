import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
mem = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    mem[i] += mem[i - 1] + nums[i - 1]

for _ in range(m):
    i, j = map(int, input().split())
    print(mem[j] - mem[i - 1])