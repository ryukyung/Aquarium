import java.util.*;

public class B11057 {
    static Integer dp[][];
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int num = input.nextInt();
        dp = new Integer[num+1][10];

        for (int i = 0; i < 10; i++) {
            dp[0][i] = 1;
        }

        for (int i = 1; i < num+1; i++) {
            for (int j = 0; j < 10; j++) {
                dp[i][j] = 0;
                for (int k = j; k < 10; k++) {
                    dp[i][j] += dp[i-1][k];
                    dp[i][j] %= 10007;
                }
            }
        }

        System.out.println(dp[num][0]%10007);

        input.close();

    }
}
