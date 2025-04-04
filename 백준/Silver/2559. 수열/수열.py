import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temps = list(map(int, input().split()))

sum_v = sum(temps[:k])
max_v = sum_v

for i in range(k, n):
    sum_v += temps[i] - temps[i - k]
    max_v = max(max_v, sum_v)
print(max_v)