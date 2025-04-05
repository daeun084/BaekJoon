import sys
from collections import defaultdict
input = sys.stdin.readline
dict = defaultdict(int)

n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
ask = list(map(int, input().split()))

for card in cards:
    dict[card] += 1

for a in ask:
    print(dict[a], end=' ')