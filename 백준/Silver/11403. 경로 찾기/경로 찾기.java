import java.util.Scanner;

class Node{
    int data;
    Node next = null;
    public Node(int data){
        this.data = data;
    }

    Node findlast(){
        Node Last = this ;
        if(next == null) return this;
        else Last = next.findlast();
        return Last;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        Node [] arr = new Node[n];
        for(int i =0; i<n; i++){
            arr[i] = new Node(0);
        }

        int [][] resultArr = new int[n][n];
        boolean[][] mark = new boolean[n][n];

        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++) {
                int data = sc.nextInt();
                if(data==1)
                    arr[i].findlast().next = new Node(j);
               resultArr[i][j] = data;
            }
        }

        for(int i=0; i<n; i++){
            resetMark(mark);
         dfs(arr, i,i,  resultArr, mark);
        }

        //print result
        for(int i=0; i<n; i++) {
            for (int j = 0; j < n; j++) {
            System.out.print(resultArr[i][j]+" ");
        }
            System.out.println();
        }
    }

    static void dfs(Node[] arr, int start, int previos, int [][] resultArr, boolean[][] mark){
        Node cursor = arr[start];
        while(true){
            if(cursor.next!=null){
                cursor = cursor.next;
                if(mark[start][cursor.data]==false) {
                    resultArr[start][cursor.data] = 1;
                    resultArr[previos][cursor.data] = 1;
                    
                    mark[start][cursor.data] = true;
                    dfs(arr, cursor.data, previos, resultArr, mark);

                }
            }else break;
        }
    }
    static void resetMark(boolean[][] mark){
        for(int i =0 ;i < mark.length; i++){
            for(int j = 0; j<mark.length; j++)
                mark[i][j] = false;
        }
    }
}
