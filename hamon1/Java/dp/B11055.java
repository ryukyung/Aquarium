import java.util.Scanner;

public class B11055 {
    static Integer dp[];
    static Integer list[];
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        dp = new Integer[n+1];
        list = new Integer[n+1];
        for(int i = 1; i<=n; i++) {
            list[i] = input.nextInt();
        }
        input.close();
        dp[1] = list[1];

        for(int i = 1; i <= n; i++) {
            C(i);
        }

        int max = dp[1];

        for(int i = 1; i<=n; i++) {
            max = Math.max(max, dp[i]);
        }
        System.out.println(max);


    }
    static int C(int n) {
        if (dp[n] == null) {
            dp[n] = list[n];
            if (n == 1) return dp[n];
            for (int i = n; i> 0; i--) {
                if(list[i] < list[n]) {
                    dp[n] = Math.max(dp[n], C(i) + list[n]);
                }
            }
        }
        return dp[n];
    }
}
