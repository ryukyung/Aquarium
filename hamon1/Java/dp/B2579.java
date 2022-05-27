import java.util.Scanner;

public class B2579 {
    static Integer[] dp;
    static int[] num;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        num = new int[n + 1];
        dp = new Integer[n + 1];

        for (int i = 1; i <= n; i++) {
            num[i] = input.nextInt();
        }
        input.close();

        dp[0] = num[0];
        dp[1] = num[1];

        System.out.println(C(n));


    }

    static int C(int n) {
        if (dp[n] == null) {
            if (n == 2) {
                dp[2] = num[1] + num[2];
                return dp[n];
            }
            dp[n] = Math.max(C(n - 2), C(n - 3) + num[n - 1]) + num[n];
        }
        return dp[n];
    }
}
