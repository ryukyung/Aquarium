import java.util.*;

public class B9465 {
    static Integer sticker[][];
    static Integer dp[][];

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int max = in.nextInt();

        for (int a = 0; a < max; a++) {
            int col = in.nextInt();

            sticker = new Integer[2][col + 1];
            dp = new Integer[2][col + 1];

            for (int i = 0; i < 2; i++) {
                for (int j = 1; j <= col; j++) {
                    sticker[i][j] = in.nextInt();
                }
            }
            dp[1][0] = 0;
            dp[0][0] = 0;
            dp[0][1] = sticker[0][1];
            dp[1][1] = sticker[1][1];

            for (int k = 2; k <= col; k++) {
                dp[0][k] = Math.max(dp[1][k-1],dp[1][k-2]) + sticker[0][k];
                dp[1][k] = Math.max(dp[0][k-1],dp[0][k-2]) + sticker[1][k];
            }

            System.out.println(Math.max(dp[0][col], dp[1][col]));

        }
    }
}