import java.util.Scanner;

public class B8393 {
    public static void main(String[] arg) {
        Scanner input = new Scanner(System.in);

        int max = input.nextInt();
        int sum = 0;

        for (int i = 1; i <= max; i++) {
            sum += i;
        }
        System.out.println(sum);

        input.close();
    }
}
