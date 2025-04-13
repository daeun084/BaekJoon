a = int(input())
x = int(input())
mod = 1000000007

p, result = a, 1
for i in range(100):
    wari = 1 << i
    if (x // wari) % 2 == 1:
        result = result * p % mod
    p = p * p % mod

print(result)