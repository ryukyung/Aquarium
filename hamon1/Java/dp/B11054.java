import java.util.Scanner;

public class B11054 {
    static int[] list;
    static Integer[] dp1;
    static Integer[] dp2;
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        list = new int[n+1];
        dp1 = new Integer[n+1];
        dp2 = new Integer[n+1];
        for (int i = 1; i<=n; i++) {
            list[i] = input.nextInt();
        }
        input.close();

        for(int i = 1; i <= n; i++) {
            C(i);
            X(i);
        }

        int max = dp1[1]+dp2[1];

        for(int i = 1; i<=n; i++) {
            max = Math.max(max, dp1[i] + dp2[i]);
        }

        System.out.println(max);



    }
    static int C(int n) {
        if(dp1[n] == null) {
            dp1[n] = 1;

            for(int i = n; i > 0; i--) {
                if(list[i] < list[n]) {
                    dp1[n] = Math.max(dp1[n], C(i) + 1);
                }
            }
        }
        return dp1[n];
    }
    static int X(int n) {
        if(dp2[n] == null) {
            dp2[n] = 0;

            for(int i = n; i < dp2.length; i++) {
                if(list[i] < list[n]) {
                    dp2[n] = Math.max(dp2[n], X(i) + 1);
                }
            }
        }
        return dp2[n];
    }
}
