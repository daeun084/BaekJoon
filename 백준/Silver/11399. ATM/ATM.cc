#include <iostream>
#include <algorithm>

int mul(int* ary, int n) {
    int result = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j <= i; j++)
            result += ary[j];

    return result;
}

int main() {
    int n, result;
    std::cin >> n;
    int* ary = new int[n];

    for (int i = 0; i < n; i++)
        std::cin >> ary[i];

    for (int i = 0; i < n; i++)
        for (int j = n - 1; j > i; j--) {
            if (ary[j] < ary[j - 1]) {
                int tmp = ary[j];
                ary[j] = ary[j - 1];
                ary[j - 1] = tmp;
            }
        }

    result = mul(ary, n);
    std::cout << result << std::endl;

    delete[] ary;
    return 0;
}
