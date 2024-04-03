#include <iostream>
#include <stack>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, num;
    string op;
    stack<int> s;
    cin >> n;


    for (int i = 0; i < n; i++) {
        cin >> op;

        if (op.compare("push") == 0) {
            cin >> num;
            s.push(num);
        } else if (op.compare("pop") == 0) {
            if (s.empty()) cout << "-1" << "\n";
            else {
                cout << s.top() << "\n";
                s.pop();
            }
        } else if (op.compare("size") == 0) {
            cout << s.size() << "\n";
        } else if (op.compare("empty") == 0) {
            if (s.empty()) cout << "1" << "\n";
            else cout << "0" << "\n";
        } else if (op.compare("top") == 0) {
            if (s.empty()) cout << "-1" << "\n";
            else cout << s.top() << "\n";
        }
    }
    return 0;
}