n, k = map(int, input().split())

a = 1
for i in range(1, n):
    a = a * i

b = 1
for i in range(1, k):
    b = b * i
for i in range(1, n - k + 1):
    b = b * i

print(a // b)