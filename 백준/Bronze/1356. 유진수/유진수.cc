
#include <iostream>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string n;
    cin >> n;

    for (int i = 1; i <= n.size(); i++) {
        string n1 = n.substr(0, i);
        string n2 = n.substr(i, n.size());

        int sum1 = n1[0] - '0', sum2 = n2[0] - '0';
        for (int j = 1; j < n1.size(); j++) {
            sum1 *= n1[j] - '0';
        }
        for (int j = 1; j < n2.size(); j++) {
            sum2 *= n2[j] - '0';
        }
        if (sum1 == sum2) {
            cout << "YES";
            return 0;
        }
    }
    cout << "NO";
}
