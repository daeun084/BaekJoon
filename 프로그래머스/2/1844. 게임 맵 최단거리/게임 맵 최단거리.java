import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        
        int[][] positions = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
        int width = maps[0].length;
        int height = maps.length;
        int[][] mem = new int[height][width];
        
        Deque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{0, 0, 1});
        mem[0][0] = 1;
        
        while (!q.isEmpty()) {
            int[] data = q.poll();
            int y = data[0];
            int x = data[1];
            int dist = data[2];
            
            if (x == width - 1 && y == height - 1) {
                return dist;
            }
            
            for (int[] p : positions) {
                if (0 <= p[1] + x && p[1] + x < width && 0 <= p[0] + y && p[0] + y < height) {
                    if (maps[p[0] + y][p[1] + x] == 1 && mem[p[0] + y][p[1] + x] == 0) {
                        q.add(new int[]{p[0] + y, p[1] + x, dist + 1});
                        mem[p[0] + y][p[1] + x] = 1;
                    }
                }
            }
        }
        return -1;
    }
}