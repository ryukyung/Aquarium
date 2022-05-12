import java.util.Scanner;

public class B1924 {
    public static void main(String[] arg) {
        Scanner input = new Scanner(System.in);

        int month = input.nextInt();
        int day = input.nextInt();

        int[] mth = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int sum = 0;
        String[] result = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};

        for(int i = 0; i < month; i++) {
            sum += mth[i];
        }
        sum += day;

        System.out.println(result[sum%7]);
        
        input.close();
        }

}
