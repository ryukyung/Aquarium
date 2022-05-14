import java.util.*;

public class B10844 {
    static Long dp[][];
    static int num;

    public static void main(String[] arg) {
        Scanner input = new Scanner(System.in);

        num = input.nextInt();

        dp = new Long[num + 1][10];
        for (int i = 0; i < 10; i++) {
            dp[1][i] = 1L;
        }

        int sum = 0;

        for (int i = 1; i < 10; i++) {
            sum += count(num, i);
        }

        System.out.println(sum % 1000000000);

    }

    static long count(int n, int x) {

        if (n == 1) {
            return dp[n][x];
        }
        if (dp[n][x] == null) {
            if (x == 0) {
                dp[n][0] = count(n-1, 1);
            } else if (x == 9) {
                dp[n][9] = count(n-1, 8);
            } else {
                dp[n][x] = count(n-1, x+1) + count(n-1, x-1);
            }
        }
        return dp[n][x] % 1000000000;
    }
}
