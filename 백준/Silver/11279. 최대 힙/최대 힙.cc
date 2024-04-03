#include <iostream>
#include <queue>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, x;
    priority_queue<int> pq; // max heap
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> x;
        if (x != 0) {
            pq.push(x);
            continue;
        }
        if (pq.empty()) cout << "0\n";
        else {
            cout << pq.top() << "\n";
            pq.pop();
        }
    }
    return 0;
}