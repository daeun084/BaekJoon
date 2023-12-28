#include <iostream>
#include <algorithm>

int compare(const void* a, const void* b) {
    if (*(int*)a > *(int*)b)
        return 1;
    if (*(int*)a == *(int*)b)
        return 0;
    return -1;
}

int binarySearch(int* ary, int n, int num) {
    int low = 0, mid, high = n - 1;

    while (low <= high) {
        mid = (low + high) / 2;
        if (ary[mid] == num)
            return 1;
        else if (ary[mid] < num)
            low = mid + 1;
        else if (ary[mid] > num)
            high = mid - 1;
    }
    return 0;
}

int main() {
    int n1, n2, num;
    
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    std::cin >> n1;
    int* ary = new int[n1];
    for (int i = 0; i < n1; i++)
        std::cin >> ary[i];

    std::sort(ary, ary + n1);

    std::cin >> n2;
    for (int i = 0; i < n2; i++) {
        std::cin >> num;
        std::cout << binarySearch(ary, n1, num) << "\n";
    }

    delete[] ary;
    return 0;
}
