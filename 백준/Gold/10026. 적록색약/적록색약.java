import java.util.*;

public class Main {
    static int origin_ = 0, new_ = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        char[][] arr = new char[n][n];
        boolean[][] mark_origin = new boolean[n][n];
        boolean[][] mark_new = new boolean[n][n];

        for (int i = 0; i < n; i++) {
            String str = sc.next();
            for (int j = 0; j < n; j++)
                arr[i][j] = str.charAt(j);
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                origin_ += search_origin(arr, i, j, mark_origin);
                new_ += search_new(arr, i, j, mark_new);
            }
        }
        System.out.print(origin_ + " " + new_);
    }

    static int search_origin(char[][] arr, int i, int j, boolean[][] mark) {
        if (mark[i][j] == true) return 0;
        char now = arr[i][j];
        mark[i][j] = true;


        if (i < 0 || j < 0 || i >= arr.length || j >= arr.length)
            return 0;


        if (i > 0 && now == arr[i - 1][j] && !mark[i - 1][j]) {
            search_origin(arr, i - 1, j, mark);
        }
        if (j > 0 && now == arr[i][j - 1] && !mark[i][j - 1]) {
            search_origin(arr, i, j - 1, mark);
        }
        if (j < arr.length - 1 && now == arr[i][j + 1] && !mark[i][j + 1]) {
            search_origin(arr, i, j + 1, mark);
        }
        if (i < arr.length - 1 && now == arr[i + 1][j] && !mark[i + 1][j]) {
            search_origin(arr, i + 1, j, mark);
        }
        return 1;
    }

    static int search_new(char[][] arr, int i, int j, boolean[][] mark) {
        //R, G는 같은 구역
        if (mark[i][j]) return 0;
        if (i < 0 || j < 0 || i >= arr.length || j >= arr.length) return 0;

        char now = arr[i][j];
        mark[i][j] = true;


        if (now == 'B') {
            if (i > 0 && now == arr[i - 1][j] && !mark[i - 1][j]) {
                search_new(arr, i - 1, j, mark);
            }
            if (j > 0 && now == arr[i][j - 1] && !mark[i][j - 1]) {
                search_new(arr, i, j - 1, mark);
            }
            if (j < arr.length - 1 && now == arr[i][j + 1] && !mark[i][j + 1]) {
                search_new(arr, i, j + 1, mark);
            }
            if (i < arr.length - 1 && now == arr[i + 1][j] && !mark[i + 1][j]) {
                search_new(arr, i + 1, j, mark);
            }

            return 1;
        } else {
            //arr[i][j] == 'R' or 'G'
            if (i > 0 && 'B' != arr[i - 1][j] && !mark[i - 1][j]) {
                search_new(arr, i - 1, j, mark);
            }
            if (j > 0 && 'B' != arr[i][j - 1] && !mark[i][j - 1]) {
                search_new(arr, i, j - 1, mark);
            }
            if (j < arr.length - 1 && 'B' != arr[i][j + 1] && !mark[i][j + 1]) {
                search_new(arr, i, j + 1, mark);
            }
            if (i < arr.length - 1 && 'B' != arr[i + 1][j] && !mark[i + 1][j]) {
                search_new(arr, i + 1, j, mark);
            }

            return 1;

        }
    }
}
