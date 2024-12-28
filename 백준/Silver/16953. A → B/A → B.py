a, b = map(int, input().split())
count = 0

while b > a:
    if b % 10 == 1 and a <= (b - 1) / 10:
        b = int((b - 1) / 10)
    elif b % 2 == 0 and a <= b / 2:
        b = int(b / 2)
    else:
        print(-1)
        exit(0)
    count += 1

print(count + 1)