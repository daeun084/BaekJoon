import java.util.*;

class Solution {
    public int solution(int[] citations) {
        
        Arrays.sort(citations);
        int answer = 0;
        int idx = 0;
        
        for (int min_c = 0; min_c <= citations[citations.length - 1]; min_c++) {
            if (min_c > citations[idx]) {
                idx += 1;
            }
            
            if (citations.length - idx < min_c) {
                break;
            }
            
            answer = Math.max(answer, min_c);
        }
        
        return answer;
    }
}