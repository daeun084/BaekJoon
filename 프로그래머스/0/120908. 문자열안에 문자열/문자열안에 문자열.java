class Solution {
    public int solution(String str1, String str2) {
        
        int str2_idx = 0;
        
        for (int i = 0; i < str1.length(); i++) {
            if (str2_idx < str2.length() && str1.charAt(i) == str2.charAt(str2_idx)) {
                str2_idx += 1;
                
                if (str2_idx == str2.length()) {
                    return 1;
                }
            } else {
                str2_idx = 0;
            }
        }
        
        if (str2_idx == str2.length()) {
            return 1;
        } else {
            return 2;
        }
    }
}