import java.util.*;

class Solution {
    public String solution(String rsp) {
        Map<Integer, Integer> res = new HashMap();
        res.put(2, 0);
        res.put(0, 5);
        res.put(5, 2);
        
        String answer = "";
        for (int i = 0; i < rsp.length(); i++) {
            int value = Integer.parseInt(String.valueOf(rsp.charAt(i)));
            answer = answer.concat(String.valueOf(res.get(value)));
        }
        return answer;
    }
}