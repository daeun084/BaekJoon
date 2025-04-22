class Solution {
    public int[] solution(String s) {
        int count = 0;
        int zero_count = 0;
        
        do {
            count += 1;
            
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '0') {
                    zero_count += 1;
                }
            }
            
            s = s.replaceAll("0", "");
            int s_len = s.length();
            s = "";
            
            while (s_len > 0) {
                s = s.concat(String.valueOf(s_len % 2));
                s_len = s_len / 2;
            }
        } while (!s.equals("1"));
        
        return new int[]{count, zero_count};
    }
}