import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;

        Deque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{0, numbers[0], 0});
        
        while (!q.isEmpty()) {
            int[] v = q.poll();
            
            if (v[2] == numbers.length - 1) {
                if (v[0] + v[1] == target || v[0] - v[1] == target) {
                    answer++;
                }
                continue;
            }
            
            q.add(new int[]{v[0] + v[1], numbers[v[2] + 1], v[2] + 1});
            q.add(new int[]{v[0] - v[1], numbers[v[2] + 1], v[2] + 1});
        }
        
        return answer;
    }
}