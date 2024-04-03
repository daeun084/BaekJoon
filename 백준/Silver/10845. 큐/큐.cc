#include <iostream>
#include <queue>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, num;
    string op;
    queue<int> q;

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> op;

        if (op.compare("push") == 0) {
            cin >> num;
            q.push(num);
        } else if (op.compare("pop") == 0) {
            if (q.empty()) cout << "-1" << "\n";
            else {
                cout << q.front() << "\n";
                q.pop();
            }
        } else if (op.compare("size") == 0) {
            cout << q.size() << "\n";
        } else if (op.compare("empty") == 0) {
            if (q.empty()) cout << "1" << "\n";
            else cout << "0" << "\n";
        } else if (op.compare("front") == 0) {
            if (q.empty()) cout << "-1" << "\n";
            else cout << q.front() << "\n";
        } else if (op.compare("back") == 0) {
            if (q.empty()) cout << "-1" << "\n";
            else cout << q.back() << "\n";
        }
    }
    return 0;
}
