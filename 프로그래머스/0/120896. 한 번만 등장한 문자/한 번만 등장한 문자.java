import java.util.*;

class Solution {
    public String solution(String s) {
        Dictionary<Character, Integer> alpha = new Hashtable<>();
        for (int i = 0; i < 26; i++) {
            alpha.put((char)('a' + i), 0);
        }

        for (int i = 0; i < s.length(); i++) {
            alpha.put(s.charAt(i), alpha.get(s.charAt(i)) + 1);
        }

        List<Character> result = new ArrayList();
        for (int i = 0; i < alpha.size(); i++) {
            if (alpha.get((char)('a' + i)) == 1) {
                result.add((char)('a' + i));
            }
        }
            
        String resultStr = "";
        for (int i = 0; i < result.size(); i++) {
            resultStr = resultStr.concat(String.valueOf(result.get(i)));
        }
        
        return resultStr;
    }
}