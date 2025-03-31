n, k = map(int, input().split())
wt_size = 1
new_water = 0

while bin(n).count('1') > k:
    if n % 2 == 1:
        new_water += wt_size
        n += 1

    n //= 2
    wt_size *= 2

print(new_water)