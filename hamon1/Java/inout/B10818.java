import java.util.Scanner;
import java.util.Arrays;

public class B10818 {
    public static void main(String[] arg) {
        Scanner input = new Scanner(System.in);

        int max = input.nextInt();
        int[] num = new int[max];

        for(int i = 0; i < max; i++) {
            num[i] = input.nextInt();
        }
        Arrays.sort(num);

        System.out.println(num[0] + " " + num[max-1]);

        input.close();
    }
}