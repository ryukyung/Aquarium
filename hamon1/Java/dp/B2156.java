import java.util.Scanner;

public class B2156 {
    static Integer[] ar;
    static Integer[] dp;
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int max = input.nextInt();
        ar = new Integer[max+1];
        dp = new Integer[max+1];

        for (int i = 1; i<=max; i++) {
            ar[i] = input.nextInt();
        }
        input.close();
        dp[0] = 0;
        dp[1] = ar[1];

        System.out.println(count(max));

    }
    public static int count(int n) {
        if (dp[n] == null) {
            dp[0] = 0;
            if(n == 1) {
                return dp[n];
            }
            else if(n == 2) {
                dp[n] = ar[1] + ar[2];
                return dp[n];
            }
            else {
                dp[n] = Math.max(count(n-1), Math.max(count(n-2) + ar[n], count(n-3) + ar[n-1] + ar[n]));
                return dp[n];
            }
        }
        return dp[n];
    }
}
