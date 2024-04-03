#include <iostream>
#include <map>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m;
    string x;
    map<string, bool> map;

    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        cin >> x;
        map[x] = false;
    }
    for (int i = 0; i < m; i++) {
        cin >> x;
        map.find(x)->second = true;
    }

    int count = 0;
    for (auto &[k, v]: map) {
        if (map.find(k)->second) count++;
    }

    cout << count << "\n";
    for (auto &[k, v]: map) {
        if (map.find(k)->second) cout << k << "\n";
    }

    return 0;
}
