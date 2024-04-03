#include <iostream>
#include <deque>
#include <vector>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    deque<int> dq;
    vector<int> v;
    int n, x;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> x;
        v.push_back(x);
    }

    for (int i = n - 1; i >= 0; i--) {
        if (v[i] == 1) {
            dq.push_front(n - i);
        } else if (v[i] == 2) {
            int tmp = dq.front();
            dq.pop_front();
            dq.push_front(n - i);
            dq.push_front(tmp);
        } else if (v[i] == 3) {
            dq.push_back(n - i);
        }
    }

    for (int i = 0; i < n; i++) {
        cout << dq[i] << " ";
    }
}
