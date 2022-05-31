import java.util.Scanner;

public class B2011 {
    static Integer dp[];
    static int code[];
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String n = input.next();
        input.close();
        code = new int[n.length()+1];
        dp = new Integer[n.length()+1];
        int result = -1;

        dp[0] = 1;
        dp[1] = 1;
        for (int i=1; i<=n.length(); i++) {
            code[i] = n.charAt(i-1)-'0';
        }

        if(code[1] == 0) result = 0;
        else {
            for(int i= 2; i<=n.length();i++) {
                if (code[i] == 0) {
                    if((code[i-1]>0)&&(code[i-1]<3)) dp[i] = dp[i-2];
                    else {
                        result = 0;
                        break;
                    }
                }
                else {
                    if(code[i-1]==1) dp[i]=(dp[i-1]+dp[i-2])%1000000;
                    else if ((code[i-1]==2)&&(code[i]>=1)&&(code[i]<=6)) {
                        dp[i] = (dp[i-1]+dp[i-2])%1000000;
                    }
                    else {
                        dp[i] = dp[i-1];
                    }
                }
            }
        }
        if(result != 0) result = dp[n.length()];
        System.out.println(result);
    }
}