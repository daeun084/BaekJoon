# N = 5 * A + 3 * B 식의 A + B의 최소값 찾기
n = int(input())

# 1. N % 5 == 0
if n % 5 == 0:
    print(int(n / 5))
else:
    # 2. ((N - 3M) % 5 == 0
    m = 1
    while n >= n - 3 * m > 0:
        if (n - 3 * m) % 5 == 0:
            print(m + int((n - 3 * m) / 5))
            exit(0)
        m += 1

    # 3. N & 3 == 0
    if n % 3 == 0:
        print(int(n / 3))
    else:
        print(-1)