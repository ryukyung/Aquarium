import java.util.Scanner;

public class B11722 {
    static int[] list;
    static Integer[] dp;
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int  n = input.nextInt();
        list = new int[n+1];
        dp = new Integer[n+1];
        for(int i = 0; i < n; i++) {
            list[i+1] = input.nextInt();
        }

        for(int i = 1; i <= n; i++) {
            C(i);
        }

        int max = dp[1];

        for(int i = 1; i<=n; i++) {
            max = Math.max(max, dp[i]);
        }
        System.out.println(max);


    }
    static int C(int n) {
        if(dp[n] == null) {
            dp[n] = 1;

            for(int i = n; i > 0; i--) {
                if(list[i] > list[n]) {
                    dp[n] = Math.max(dp[n], C(i) + 1);
                }
            }
        }
        return dp[n];
    }
}
