a, b = map(int, input().split())

while a != 0 and b != 0:
    if a >= b:
        a = a % b
    else:
        b = b % a

print('1' * max(a, b))