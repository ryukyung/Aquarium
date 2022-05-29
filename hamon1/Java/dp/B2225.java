import java.util.Scanner;

public class B2225 {
    static Integer dp[][];
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        int k = input.nextInt();
        input.close();

        dp = new Integer[n+1][k+1];
        
        for (int i = 1; i<=n; i++) {
            dp[i][1] = 1;
        }
        for(int i = 1; i<=k; i++) {
            dp[1][i] = i;
        }

        for(int i = 2; i<=n; i++) {
            for(int j = 2; j<=k; j++) {
                dp[i][j] = (dp[i][j-1] + dp[i-1][j])%1000000000;
            }
        }
        System.out.println(dp[n][k]);
    }
}