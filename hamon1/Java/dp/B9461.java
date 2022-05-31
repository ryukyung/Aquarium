import java.util.Scanner;

public class B9461 {
    static Long dp[];
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int t = input.nextInt();
        for (int i = 0; i<t; i++) {
            int n = input.nextInt();
            dp = new Long[n+6];
            dp[0] = 0L;
            dp[1] = 1L;
            dp[2] = 1L;
            dp[3] = 1L;
            dp[4] = 2L;
            dp[5] = 2L;

            System.out.println(C(n));
        }
        input.close();
    }

    static Long C(int i) {
        if (dp[i] == null) {
            if (i <= 5) {
                return dp[i];
            }
            else {
                dp[i] = C(i-1) + C(i-5);
                return dp[i];
            }
        }
        return dp[i];
    }
}
