#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, res = 0;
    cin >> n;
    vector<int> v;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        v.push_back(x);
    }
    sort(v.begin(), v.end());

    do {
        int sum = 0;
        for (int i = 0; i < n - 1; i++) {
            sum += abs(v[i] - v[i + 1]);
        }
        res = max(res, sum);
    } while (next_permutation(v.begin(), v.end()));

    cout << res << "\n";

}
