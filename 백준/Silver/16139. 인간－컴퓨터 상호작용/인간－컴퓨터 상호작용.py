import sys
input = sys.stdin.readline

s = input().rstrip()
mem = [[0 for _ in range(len(s) + 1)] for _ in range(26)]
for i in range(len(s) + 1):
    alpha = ord(s[i - 1]) - 97 # ascii
    for j in range(26):
        mem[j][i] = mem[j][i - 1]
    mem[alpha][i] += 1

q = int(input())
for _ in range(q):
    a, l, r = input().split()
    alpha = mem[ord(a) - 97]
    print(alpha[int(r) + 1] - alpha[int(l)])