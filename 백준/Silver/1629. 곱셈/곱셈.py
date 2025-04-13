a, b, c = map(int, input().split())
p, answer = a, 1

for i in range(32):
    wari = 1 << i
    if (b // wari) % 2 == 1:
        answer = answer * p % c
    p = p * p % c

print(answer)