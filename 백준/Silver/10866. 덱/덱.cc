#include <iostream>
#include <deque>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, num;
    string op;
    deque<int> dq;
    
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> op;

        if (op.compare("push_front") == 0) {
            cin >> num;
            dq.push_front(num);
        } else if (op.compare("push_back") == 0) {
            cin >> num;
            dq.push_back(num);
        } else if (op.compare("pop_front") == 0) {
            if (dq.empty()) cout << "-1" << "\n";
            else {
                cout << dq.front() << "\n";
                dq.pop_front();
            }
        } else if (op.compare("pop_back") == 0) {
            if (dq.empty()) cout << "-1" << "\n";
            else {
                cout << dq.back() << "\n";
                dq.pop_back();
            }
        } else if (op.compare("size") == 0) {
            cout << dq.size() << "\n";
        } else if (op.compare("empty") == 0) {
            if (dq.empty()) cout << "1" << "\n";
            else cout << "0" << "\n";
        } else if (op.compare("front") == 0) {
            if (dq.empty()) cout << "-1" << "\n";
            else cout << dq.front() << "\n";
        } else if (op.compare("back") == 0) {
            if (dq.empty()) cout << "-1" << "\n";
            else cout << dq.back() << "\n";
        }
    }
    return 0;

}