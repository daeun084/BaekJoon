import java.util.ArrayList;
import java.util.LinkedList;
import java.util.*;

public class Main {
    static  int [] visited;
    static int count=1;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int r = sc.nextInt();

        ArrayList<ArrayList<Integer>> graph = new ArrayList<>(n+1);
        boolean[] mark = new boolean[n+1];
        visited = new int[n+1];


        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<Integer>());
        }


        for (int i = 0; i < m; i++) {
            int n1 = sc.nextInt();
            int n2 = sc.nextInt();
            graph.get(n1).add(n2);
            graph.get(n2).add(n1);
        }
        for(int i=1; i<graph.size(); i++) Collections.sort(graph.get(i));

        search(graph, mark, r);

        for(int i=1; i< visited.length; i++){
            System.out.println(visited[i]);
        }

    }

    static void search(ArrayList<ArrayList<Integer>> graph, boolean[] mark, int start) {
       if(mark[start]==false){
           mark[start] = true;
           visited[start] = count++;
       }

            ArrayList<Integer> node = graph.get(start);
            for (int j = 0; j < node.size(); j++) {
                if (mark[node.get(j)] == false) {
                    search(graph, mark, node.get(j));

                }
        }

    }

}
