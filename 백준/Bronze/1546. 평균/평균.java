import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        double [] arr = new double[n];
        double max = 0;
        double sum=0;

        for(int i=0; i<n; i++){
            arr[i] = sc.nextInt();
            if(max<arr[i]) max = arr[i];
        }
        for(int i=0; i<n; i++){
            arr[i] = arr[i]/max*100;
            sum+=arr[i];
        }
        System.out.println(sum/n);

    }
}
