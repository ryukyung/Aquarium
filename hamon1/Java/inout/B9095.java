import java.util.*;

public class B9095 {
    static Integer dp[];
    public static void main(String[] arg) {
        Scanner input = new Scanner(System.in);

        int max = input.nextInt();
        dp = new Integer[11];
        dp[0] = 0;

        for (int i = 0; i<max; i++) {
            int num = input.nextInt();

            System.out.println(count(num));

        }
    }
    public static int count(int n) {
        if (n == 1) {
            dp[n] = 1;
        }
        else if (n == 2) {
            dp[n] = 2;
        }
        else if (n == 3) {
            dp[n] = 4;
        }
        else if (dp[n] == null) {
            dp[n] = count(n-1) + count(n-2) + count(n-3);
        }
        return dp[n];
    }
}
