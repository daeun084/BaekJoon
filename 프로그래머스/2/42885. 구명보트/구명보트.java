import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        int small_idx = 0;
        Arrays.sort(people);
        
        for (int i = people.length - 1; i >= 0; i--) {
            if (small_idx > i) {
                continue;
            }
            if (people[small_idx] + people[i] <= limit) {
                small_idx += 1;
            }
            
            answer += 1;            
        }
        return answer;
    }
}