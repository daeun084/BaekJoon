#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

void dfs(vector<vector<int>>& graph, vector<bool>& visited, int start);
void bfs(vector<vector<int>>& graph, vector<bool>& visited, int start);

int main() {
    int N, M, V;
    cin >> N >> M >> V;

    // 그래프 초기화
    vector<vector<int>> graph(N + 1);
    for (int i = 0; i < M; ++i) {
        int v1, v2;
        cin >> v1 >> v2;
        graph[v1].push_back(v2);
        graph[v2].push_back(v1);
    }

    // 정점 번호가 작은 순서로 정렬
    for (int i = 1; i <= N; ++i) {
        sort(graph[i].begin(), graph[i].end());
    }

    // DFS와 BFS에 사용할 방문 여부 배열
    vector<bool> visited(N + 1, false);

    // DFS 실행 및 결과 출력
    dfs(graph, visited, V);
    cout << endl;

    // BFS 실행 및 결과 출력
    fill(visited.begin(), visited.end(), false); // 방문 여부 배열 초기화
    bfs(graph, visited, V);

    return 0;
}

void dfs(vector<vector<int>>& graph, vector<bool>& visited, int start) {
    stack<int> s;
    s.push(start);

    while (!s.empty()) {
        int current = s.top();
        s.pop();

        if (!visited[current]) {
            visited[current] = true;
            cout << current << " ";

            for (int i = graph[current].size() - 1; i >= 0; --i) {
                int next = graph[current][i];
                if (!visited[next]) {
                    s.push(next);
                }
            }
        }
    }
}

void bfs(vector<vector<int>>& graph, vector<bool>& visited, int start) {
    queue<int> q;
    q.push(start);
    visited[start] = true;

    while (!q.empty()) {
        int current = q.front();
        q.pop();

        cout << current << " ";

        for (int i = 0; i < graph[current].size(); ++i) {
            int next = graph[current][i];
            if (!visited[next]) {
                visited[next] = true;
                q.push(next);
            }
        }
    }
}
