import java.util.Scanner;

public class B2133 {
    static int dp[];

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        input.close();
        dp = new int[n + 2];

        dp[0] = 1;
        dp[1] = 0;
        dp[2] = 3;

        int result = 0;
        if (n % 2 == 1) {
            result = 0;
        } else {
            for (int i = 4; i <= n; i += 2) {
                dp[i] = dp[i - 2] * dp[2];
                for (int j = i - 4; j >= 0; j -= 2) {
                    dp[i] = dp[i] + (dp[j] * 2);
                }
            }
            result = dp[n];
        }
        System.out.println(result);

    }
}
