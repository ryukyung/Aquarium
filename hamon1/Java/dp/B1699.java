import java.util.Scanner;

public class B1699 {
    static Integer[] dp;
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        dp = new Integer[n+1];

        System.out.println(C(n));
    }
    static int C(int n) {
        if(dp[n] == null) {
            if (Math.sqrt(n)%1 == 0) {
                dp[n] = 1;
                return dp[n];
            }
            else {
                int a = (int)Math.sqrt(n);
                dp[n] = C(n-(a*a)) + 1;
                return dp[n];
            }
        }
        return dp[n];
    }
}
