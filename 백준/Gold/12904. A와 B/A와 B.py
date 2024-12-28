s = input()
t = input()

while len(s) < len(t):
    if t[len(t) - 1] == 'A':
        t = t[:len(t) - 1]
    elif t[len(t) - 1] == 'B':
        t = t[:len(t) - 1]
        tmp = t[::-1]
        t = tmp
    else:
        print(-1)
        exit(0)

if s == t:
    print(1)
else:
    print(0)