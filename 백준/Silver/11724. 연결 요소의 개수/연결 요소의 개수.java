import java.util.Scanner;
import java.util.Stack;

public class Main {
    static int count = 1;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        boolean [][] graph = new boolean[n][n];
        while (m-->0){
            int v1 = sc.nextInt();
            int v2 = sc.nextInt();
            graph[v1-1][v2-1] = true;
            graph[v2-1][v1-1] =true;
        }

        Stack<Integer> stack = new Stack<>();
        boolean[] marked = new boolean[n];
        search(graph, 1, marked, stack);
        check(graph, 0, marked, stack);
        System.out.println(count);

    }
    static void search(boolean[][] graph, int start, boolean[] marked, Stack stack){
        if(!stack.contains(start)) stack.push(start);
        marked[start-1] = true;
        //dfs

        for(int i=0; i<marked.length; i++){
            if(graph[start-1][i]==true && marked[i]==false)
                search(graph, i+1, marked, stack);
        }
        stack.pop();
    }
    static void check(boolean[][] graph, int start, boolean[] marked, Stack stack){
        for(int i=0; i<marked.length; i++){
            if(marked[i]==false){
                    count++;
                    search(graph, i + 1, marked, stack);
            }
        }}
    }


