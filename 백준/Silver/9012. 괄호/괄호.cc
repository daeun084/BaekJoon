#include <iostream>
#include <string>

int main() {
    int n;
    std::cin >> n;
    std::cin.ignore();

    while (n-- > 0) {
        std::string ary;
        std::getline(std::cin, ary);

        int len = ary.length();
        int id = -1;
        bool pass = false;

        for (int i = 0; i < len; i++) {
            if (ary[i] == '(') {
                id++;
            } else if (ary[i] == ')') {
                if (id < 0) {
                    std::cout << "NO\n";
                    pass = true;
                    break;
                } else {
                    id--;
                }
            }
        }

        if (!pass) {
            if (id != -1) {
                std::cout << "NO\n";
            } else {
                std::cout << "YES\n";
            }
        }
    }

    return 0;
}
