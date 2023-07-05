import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static int count = 0;
    static boolean answer = false;
    static int p1, p2;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
         p1 = sc.nextInt();
         p2 = sc.nextInt();
        int m = sc.nextInt();


        ArrayList<ArrayList<Integer>> graph = new ArrayList<>(n+1);
        boolean[] mark = new boolean[n+1];

        for (int i = 0; i <= n; i++) graph.add(new ArrayList<Integer>());

        for (int i = 0; i < m; i++) {
            int n1 = sc.nextInt();
            int n2 = sc.nextInt();
            graph.get(n1).add(n2);
            graph.get(n2).add(n1);
        }

        search(graph, p1, mark);

        if(answer == false){
            System.out.println("-1");
        }

    }
    static void search(ArrayList<ArrayList<Integer>> graph, int start, boolean[] mark) {
        mark[start] = true;

        if(start == p2 ) {
            answer = true;
            System.out.println(count);
            return;
        }

        ArrayList<Integer> node = graph.get(start);

        if (checkForMark(mark, node)) {
            count--;
        }


        for (int i = 0; i < node.size(); i++) {
            if (!mark[node.get(i)]) {
                count +=1;
                search(graph, node.get(i), mark);

                if (checkForMark(mark, graph.get(start))) {
                    count--;
                }
            }
        }
    }
    static boolean checkForMark(boolean[] mark, ArrayList node){
        for(int i=0; i<node.size(); i++){
           int j = (int)node.get(i);
           if(mark[j]==false) {
               return false;
           }
        }
        return true;
        //모든 요소가 방문한 적이 있음 -> 그래프의 끝점
    }
}
