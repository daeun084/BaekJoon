import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        
        Arrays.sort(people);
        int small_idx = 0;
        
        for (int i = people.length - 1; i >= 0; i--) {
            if (people[i] == 0) {
                continue;
            }
            
            if (people[small_idx] + people[i] <= limit) {
                answer += 1;
                people[small_idx] = 0;
                people[i] = 0;
                small_idx += 1;
            } else {
                answer += 1;
                people[i] = 0;
            }
        }
        return answer;
    }
}