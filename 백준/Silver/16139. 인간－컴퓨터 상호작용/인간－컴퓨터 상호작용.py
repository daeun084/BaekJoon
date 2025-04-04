s = list(map(str, input().strip()))

mem = [[0 for _ in range(len(s) + 1)] for _ in range(28)]
for i in range(len(s) + 1):
    for j in range(1, 28):
        if ord(s[i - 1]) - 96 == j: # ascii
            mem[j][i] = mem[j][i - 1] + 1
        else:
            mem[j][i] = mem[j][i - 1]

q = int(input())
for _ in range(q):
    a, l, r = map(str, input().split())
    alpha = mem[ord(a) - 96]
    print(alpha[int(r) + 1] - alpha[int(l)])