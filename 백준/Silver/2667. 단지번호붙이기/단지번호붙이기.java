
import java.util.*;


public class Main {
    static int count = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] arr = new int[n][n];
        boolean[][] mark = new boolean[n][n];

       int [] list = new int[n*n-n];

        for (int i = 0; i < n; i++) {
            String str = sc.next();
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(String.valueOf(str.charAt(j)));
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (mark[i][j] == false) {
                    count += search(arr, mark, i, j, list);
                    //전체 단지수
                }
            }
        }

       int []newArr = new int[count];
        for(int i=0; i<count; i++){
            newArr[i] = list[i];
        }

        //오름차순 정렬
        Arrays.sort(newArr);

        System.out.println(count);
        for(int i=0; i<count; i++){
            System.out.println(newArr[i]);
        }

    }

    static int search(int[][] arr, boolean[][] mark, int i, int j, int[] list) {
        if (arr[i][j] == 1) {
            if(mark[i][j]==false){
                list[count] +=1;
                mark[i][j] =true;
            }


            if (i < arr.length - 1 && arr[i + 1][j] == 1 && mark[i + 1][j] == false) {
                search(arr, mark, i + 1, j, list);
            }
            if (j < arr[0].length - 1 && arr[i][j + 1] == 1 && mark[i][j + 1] == false) {
                search(arr, mark, i, j + 1, list);
            }
            if (i > 0 && arr[i - 1][j] == 1 && mark[i - 1][j] == false) {
                search(arr, mark, i - 1, j, list);
            }
            if (j > 0 && arr[i][j - 1] == 1 && mark[i][j - 1] == false) {
                search(arr, mark, i, j - 1, list);
            }

            return 1;
        }
        return 0;
    }

}
