import java.util.*;

class Solution {
    
    private void dfs(int i, int j, int[][] mem, int n, int[][] computers) {
        mem[i][j] = 1;
        for (int next = 0; next < n; next++) {
            if (next != j && mem[j][next] == 0 && computers[j][next] == 1) {
                dfs(j, next, mem, n, computers);
            }
        }
    }
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        int[][] mem = new int[n][n];
        
        for (int i = 0; i < n; i++) {
            boolean isAllZero = true;

            for (int j = 0; j < n; j++) {
                if (i != j && mem[i][j] == 0 && computers[i][j] == 1) {
                    dfs(i, j, mem, n, computers);
                    answer++;
                }
                if (computers[i][j] == 1 && i != j) {
                    isAllZero = false;
                }
            }
            
            if (isAllZero) {
                answer++;
            }
        }
        
        return answer;
    }
}