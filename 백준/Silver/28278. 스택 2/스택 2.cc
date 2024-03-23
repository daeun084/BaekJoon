#include <iostream>
#include <stack>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, num, op;
    stack<int> s;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> op;

        if (op == 1) { //push
            cin >> num;
            s.push(num);
        } else if (op == 2) { //pop
            if (s.empty())
                cout << "-1" << "\n";
            else {
                cout << s.top() << "\n";
                s.pop();
            }
        } else if (op == 3)  //size
            cout << s.size() << "\n";
        else if (op == 4)  //empty
            cout << (s.empty() ? 1 : 0) << "\n";
        else if (op == 5)  //top
            cout << (s.empty() ? -1 : s.top()) << "\n";
    }
    return 0;
}
