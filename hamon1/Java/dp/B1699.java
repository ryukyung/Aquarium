import java.util.Scanner;

public class B1699 {
    static Integer[] dp;
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        input.close();
        dp = new Integer[n+1];

        dp[0] = 0;

        for (int i = 1; i<=n; i++) {
            dp[i] = i;
            for(int j = 1; j*j <= i; j++) {
                if(dp[i] > dp[i-(j*j)]+1) {
                    dp[i] = dp[i-(j*j)] +1;
                }
            }
        }

        System.out.println(dp[n]);
    }
}
