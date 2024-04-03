#include <iostream>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, ary[10001] = {0}, num;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> num;
        ary[num]++;
    }

    for (int i = 0; i < 10001; i++) {
        if (ary[i] == 0) continue;

        for (int j = 0; j < ary[i]; j++)
            cout << i << "\n";
    }
    return 0;
}
