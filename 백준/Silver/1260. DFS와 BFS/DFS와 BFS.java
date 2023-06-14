import java.util.Scanner;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int v = sc.nextInt();

        boolean[][] graph = new boolean[n][n];

        while (m-- > 0) {
            int v1 = sc.nextInt();
            int v2 = sc.nextInt();
            graph[v1 - 1][v2 - 1] = true;
            graph[v2 - 1][v1 - 1] = true;
        }

        boolean[] dfsMarked = new boolean[n];
        boolean[] bfsMarked = new boolean[n];

        List<Integer> queue = new ArrayList<>();
        queue.add(0, v);
        Stack<Integer> stack = new Stack<>();

        dfs(graph, v, dfsMarked, stack);
        System.out.println();
        bfs(graph, v, bfsMarked, queue);

    }

    static void bfs(boolean[][] graph, int start, boolean[] marked, List queue) {

        marked[start-1] = true;
        for (int i = 0; i < marked.length; i++) {
            if (graph[start - 1][i] == true && marked[i] == false)
                if(!queue.contains(i+1)) {
                    queue.add(queue.size(), i+1);

                }


        }
        System.out.print(start+" ");
        queue.remove(0);
        if(queue.size()!=0)
            bfs(graph, (int)queue.get(0), marked, queue);

    }

    static void dfs(boolean[][] graph, int start, boolean[] marked, Stack stack) {
        if (!stack.contains(start))
            stack.push(start);

        marked[start - 1] = true;
        System.out.print(start + " ");

        for (int i = 0; i < marked.length; i++) {
            if (graph[start - 1][i] == true && marked[i] == false) {
                dfs(graph, i + 1, marked, stack);
            }
        }
        stack.pop();
    }
}
