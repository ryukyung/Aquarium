import java.util.Scanner;

public class B11053 {
    static Integer[] list;
    static Integer[] dp;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();

        list = new Integer[n];
        for (int i = 0; i < n; i++) {
            list[i] = input.nextInt();
        }
        dp = new Integer[n];

        for(int i = 0; i < n; i++) {
            LIS(i);
        }

        int max = dp[0];

        for(int i = 1; i<n; i++) {
            max = Math.max(max, dp[i]);
        }
        System.out.println(max);

    }
    static int LIS(int n) {
        if(dp[n] == null) {
            dp[n] = 1;

            for(int i = n-1; i >= 0; i--) {
                if(list[i] < list[n]) {
                    dp[n] = Math.max(dp[n], LIS(i) + 1);
                }
            }
        }
        return dp[n];
    }

}
