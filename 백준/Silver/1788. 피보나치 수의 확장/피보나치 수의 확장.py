n = int(input())

fib = [i for i in range(abs(n) + 1)]
for i in range(2, abs(n) + 1):
    fib[i] = (fib[i - 1] + fib[i - 2]) % 1000000000

if fib[abs(n)] == 0:
    print(0)
elif n < 0 and abs(n) % 2 == 0:
    print(-1)
else:
    print(1)

print(fib[abs(n)])