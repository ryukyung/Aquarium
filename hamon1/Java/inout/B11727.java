import java.util.*;

public class B11727 {
    static Integer[] dp;

    public static void main(String[] arg) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        dp = new Integer[n + 1];
        dp[0] = 0;

        System.out.println(count(n));

    }

    public static int count(int n) {
        if (n == 2) {
            dp[n] = 3;
        }
        else if (n == 1) {
            dp[n] = 1;
        }
        else if (dp[n] == null) {
            dp[n] = ((count(n-2))*2 + count(n-1))%10007;
        }
        return dp[n];
    }
}
