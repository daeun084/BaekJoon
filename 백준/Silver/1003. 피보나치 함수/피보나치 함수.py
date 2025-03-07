import sys
input = sys.stdin.readline

t = int(input())
input_arr = [int(input()) for _ in range(t)]
fibonacci = [[0, 0] for _ in range(max(input_arr) + 1)]

fibonacci[0] = [1, 0]
if max(input_arr) != 0:
    fibonacci[1] = [0, 1]

for i in range(2, max(input_arr) + 1):
    z1, o1 = fibonacci[i - 1]
    z2, o2 = fibonacci[i - 2]
    fibonacci[i] = [z1 + z2, o1 + o2]

for _ in range(t):
    z, o = fibonacci[input_arr[_]]
    print(z, o)