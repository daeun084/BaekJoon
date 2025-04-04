s, p = map(int, input().split())
dna = list(map(str, input().strip()))
a, c, g, t = map(int, input().split())

mem = [[0 for _ in range(s + 1)] for _ in range(4)]
alpha = ['A', 'C', 'G', 'T']

# 알바펫별 누적합
for i in range(4):
    arr = mem[i]
    for j in range(1, s + 1):
        if dna[j - 1] == alpha[i]:
            arr[j] = arr[j - 1] + 1
        else:
            arr[j] = arr[j - 1]

answer = 0
for i in range(p, s + 1):
    if mem[0][i] - mem[0][i - p] >= a \
            and mem[1][i] - mem[1][i - p] >= c \
            and mem[2][i] - mem[2][i - p] >= g \
            and mem[3][i] - mem[3][i - p] >= t:
        answer += 1

print(answer)