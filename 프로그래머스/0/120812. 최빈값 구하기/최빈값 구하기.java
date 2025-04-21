import java.util.*;

class Solution {
    public int solution(int[] array) {
        Map<Integer, Integer> dic = new HashMap();
        for (int i : array) {
            if (dic.containsKey(i)) {
                dic.put(i, dic.get(i) + 1);
            } else {
                dic.put(i, 1);
            }
        }
        
        int max_v = -1;
        int max_c = -1;
        Integer[] keys = dic.keySet().toArray(new Integer[0]);
        for (int i = 0; i < keys.length; i++) {
            if (dic.get(keys[i]) > max_c) {
                max_v = keys[i];
                max_c = dic.get(keys[i]);
            }
        }
        
        for (int i = 0; i < keys.length; i++) {
            if (keys[i] == max_v) {
                continue;
            }
            if (dic.get(keys[i]) == max_c) {
                return -1;
            }
        }

        return max_v;
    }
}