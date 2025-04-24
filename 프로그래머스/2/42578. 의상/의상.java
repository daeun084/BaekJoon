import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> hash = new HashMap<>();
        
        // hash 생성 및 종류 개수 카운팅 
        for (int i = 0; i < clothes.length; i++) {
            String type = clothes[i][1];
            
            if (hash.containsKey(type)) {
                hash.put(type, hash.get(type) + 1);
            } else {
                hash.put(type, 1);
            }
        }
        
        // 조합의 수 구하기
        for (String key : hash.keySet()) {
            answer *= (hash.get(key) + 1);
        }
        
        return answer - 1;
    }
}