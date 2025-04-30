import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        Deque<int[]> q = new ArrayDeque<>();
        
        for (int i = 0; i < priorities.length; i++) {
            // 우선순위를 우선순위큐에 저장
            pq.add(priorities[i]);
            // 우선순위와 현재 loc을 함께 저장
            q.add(new int[]{priorities[i], i});
        }
        
        int answer = 0;
        while (!pq.isEmpty()) {
            int[] priority = q.poll();
            
            // 우선순위가 가장 높다면
            if (priority[0] == pq.peek()) {
                answer ++;
                pq.poll();
                
                // 정답을 요하는 위치의 요소라면 정답 반환
                if (priority[1] == location) {
                    return answer;
                }
                
            } else {
                // 그렇지 않다면 다시 큐에 삽입
                q.add(new int[]{priority[0], priority[1]});
            }
        }
        
        return answer;
    }
}