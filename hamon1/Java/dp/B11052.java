import java.util.Scanner;

public class B11052 {
    static int dp[];
    static int p[];

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        dp = new int[n + 1];
        p = new int[n + 1];
        for (int i = 1; i < n + 1; i++) {
            p[i] = input.nextInt();
        }
        input.close();
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j <= i; j++) {
                dp[i] = Math.max(dp[i], p[j] + dp[i - j]);
            }
        }

        System.out.println(dp[n]);

    }
}