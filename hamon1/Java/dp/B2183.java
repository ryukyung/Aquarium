import java.util.Scanner;

public class B2183 {
    static Long[] dp;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        input.close();

        dp = new Long[n + 1];

        System.out.println(count(n));

    }
    public static long count(int n) {
        if(n == 1) {
            dp[n] = 1L;
            return dp[n];
        }
        else if(n == 2) {
            dp[n] = 1L;
            return dp[n];
        }
        if(dp[n] == null) {
            dp[n] = count(n-1) + count(n-2);
        }
        return dp[n];
    }
}