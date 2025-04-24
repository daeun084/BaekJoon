import java.util.*;

class Solution {
    public int solution(int[] citations) {
        
        Arrays.sort(citations);
        int max_c = citations[citations.length - 1];
        int answer = 0;
        int idx = 0;
        
        for (int min_c = 0; min_c <= max_c; min_c++) {
            if (min_c > citations[idx]) {
                idx += 1;
            }
            
            int h_idx = citations.length - idx;
            if (h_idx < min_c) {
                break;
            }
            
            if (answer < min_c) {
                answer = min_c;
            }        
        }
        
        return answer;
    }
}