import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();


        int[] answer = new int[t];

        for (int testcase = 0; testcase < t; testcase++) {
            int m = sc.nextInt(); //가로
            int n = sc.nextInt(); //세로
            int k = sc.nextInt();

            boolean[][] mark = new boolean[n][m];

            int[][] arr = new int[n][m];
            for (int i = 0; i < k; i++) {
                int h = sc.nextInt();
                int w = sc.nextInt();
                arr[w][h] = 1;
            }
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (mark[i][j] == false){
                        answer[testcase] += search(arr, mark, i, j);
                    }
                }
            }

        }

        for (int i = 0; i < t; i++) System.out.println(answer[i]);

    }

    static int search(int[][] arr, boolean[][] mark, int i, int j) {

        if (arr[i][j] == 1) {
            mark[i][j] = true;


            if (i < arr.length - 1 && arr[i + 1][j] == 1 && mark[i + 1][j] == false) {
                search(arr, mark, i + 1, j);
            }
            if (j < arr[0].length - 1 && arr[i][j + 1] == 1 && mark[i][j + 1] == false) {
                search(arr, mark, i, j + 1);
            }
            if (i > 0 && arr[i - 1][j] == 1 && mark[i - 1][j] == false) {
                search(arr, mark, i - 1, j);
            }
            if (j > 0 && arr[i][j - 1] == 1 && mark[i][j - 1] == false) {
                search(arr, mark, i, j - 1);
            }

            return 1;
        }


        return 0;
    }
}
