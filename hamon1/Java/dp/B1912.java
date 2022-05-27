import java.util.Scanner;

public class B1912 {
    static Integer[] dp;
    static int[] list;
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        list = new int[n+1];
        dp = new Integer[n+1];
        for (int i = 0; i<n; i++) {
            list[i+1] = input.nextInt();
        }

        int max = 0;
        dp[0] = 0;
        dp[1] = max = list[1];

        for (int i = 1; i<=n; i++) {
            dp[i] = Math.max(dp[i-1]+list[i], list[i]);
            max = Math.max(max, dp[i]);
        }
        
        System.out.println(max);


    }

}
