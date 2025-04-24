import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList();
        Stack<int[]> stack = new Stack();
        
        for (int i = progresses.length - 1; i >= 0; i--) {
            stack.push(new int[]{progresses[i], speeds[i]});
        }
        
        while (!stack.empty()) {
            int[] c = stack.pop();
            int days = (100 - c[0] + c[1] - 1) / c[1]; 
            int count = 1;
            
            while (!stack.empty() && stack.peek()[1] * days + stack.peek()[0] >= 100) {
                stack.pop();
                count += 1;
            }
            answer.add(count);
        }
        
        int[] result = new int[answer.size()];
        for(int i = 0; i < answer.size(); i++) {
            result[i] = answer.get(i);
        }
        
        return result;
    }
}