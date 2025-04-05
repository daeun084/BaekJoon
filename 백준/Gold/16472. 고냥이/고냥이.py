import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
langs = input().strip('\n')
lang_len = len(langs)
result = 0

left = 0
right = 0
alpha_count = defaultdict(int)
while right < lang_len:
    alpha_count[langs[right]] += 1

    # 알파벳 초과 시 오른쪽으로 이동
    while len(alpha_count) > n:
        alpha_count[langs[left]] -= 1
        if alpha_count[langs[left]] == 0:
            del alpha_count[langs[left]]
        left += 1

    result = max(result, right - left + 1)
    right += 1

print(result)