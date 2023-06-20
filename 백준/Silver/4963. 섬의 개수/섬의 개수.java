import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> result = new ArrayList<>();

        while (true) {
            int n1 = sc.nextInt();
            int n2 = sc.nextInt();
            if (n1 == 0 && n2 == 0) break;

            int[][] arr = new int[n2][n1];
            boolean[][] mark = new boolean[n2][n1];
            for (int i = 0; i < n2; i++)
                for (int j = 0; j < n1; j++) arr[i][j] = sc.nextInt();

            int count = 0;
            for (int i = 0; i < n2; i++)
                for (int j = 0; j < n1; j++)count+=search(arr, mark, i, j);

            result.add(count);

        }
        for (int i = 0; i < result.size(); i++) {
            System.out.println(result.get(i));
        }
    }

    static int search(int[][] arr, boolean[][] mark, int i, int j) {

        if (arr[i][j] == 0 || mark[i][j]) {
            return 0;
        }
        else {
            //arr[i][j]==1

            mark[i][j] = true;

            if(j>0&& arr[i][j-1]==1 && !mark[i][j-1]) search(arr, mark, i, j-1);
            if(i>0 && arr[i-1][j]==1 && !mark[i-1][j]) search(arr, mark, i-1, j);
            if(i>0&&j>0&&arr[i-1][j-1]==1 && !mark[i-1][j-1]) search(arr, mark, i-1, j-1);
            if(i>0 && j< mark[0].length-1&&arr[i-1][j+1]==1 && !mark[i-1][j+1]) search(arr,mark,i-1,j+1);
            if(j< mark[0].length-1 && arr[i][j+1]==1 && !mark[i][j+1])
                search(arr, mark, i, j+1);
            if(i< mark.length-1 && j< mark[0].length-1 && arr[i+1][j+1]==1 && !mark[i+1][j+1]) search(arr, mark, i+1, j+1);
            if(i< mark.length-1 && arr[i+1][j]==1 && !mark[i+1][j]) search(arr, mark, i+1, j);
            if(i< mark.length-1 && j>0 && arr[i+1][j-1]==1 && !mark[i+1][j-1]) search(arr, mark, i+1, j-1);
            return 1;


        }

    }
}
