import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

results = [-1] * n
stack = []

for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        idx = stack.pop()
        results[idx] = arr[i]
    stack.append(i)

for nge in results:
    print(nge, end=' ')