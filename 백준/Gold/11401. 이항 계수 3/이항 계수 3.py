n, k = map(int, input().split())
mod = 1000000007

a = 1
for i in range(1, n + 1):
    a = a * i % mod

b = 1
for i in range(1, k + 1):
    b = b * i % mod
for i in range(1, n - k + 1):
    b = b * i % mod

power = 1 # b ^ (mod - 2)
p = b
for i in range(30):
    wari = 1 << i
    if ((mod - 2) // wari) % 2 == 1:
        power = power * p % mod
    p = p * p % mod

print(a * power % mod)