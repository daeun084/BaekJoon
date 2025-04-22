class Solution {
    public int solution(int n) {
        
    int[] arr = new int[n + 1];
        
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n / i; j++) {
            arr[i * j] += i;
        }
            
    }
     
        return arr[n];
    }
}