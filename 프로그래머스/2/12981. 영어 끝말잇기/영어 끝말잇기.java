import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int cnt = 0;
        Set<String> set = new HashSet<>();
        
        while (cnt < words.length) {
            cnt += 1;
            String word = words[cnt - 1];
            
            if (cnt > 1) {
                String p_word = words[cnt - 2];

                if (word.charAt(0) != p_word.charAt(p_word.length() -1)) {
                    return handleAnswer(n, cnt);
                }
            }
            
            if (!set.add(word)) {
                return handleAnswer(n, cnt);
            }
        }
        
       return new int[]{0, 0};
    }
    
    private int[] handleAnswer(int n, int cnt) {
        if (cnt % n == 0) {
            return new int[]{n, cnt / n};
        } else {
            return new int[]{cnt % n, cnt / n + 1};   
        }
    }
}
                                       