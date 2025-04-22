class Solution {
    public int[] solution(int brown, int yellow) {
        
        int low = 1;
        int high = brown;
        while (low < high) {
            int w = high;
            int h = (brown + yellow) / w;
      
            int b = 4 + 2 * (w + h - 4);
            int y = (h - 2) * (w - 2);
            
            if (brown == b && yellow == y) {
                return new int[]{w, h};
            } else {
                high -= 1;
            }
        }
        return null;
    }
}