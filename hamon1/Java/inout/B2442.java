import java.util.Scanner;

public class B2442 {
    public static void main(String[] arg) {
        Scanner input = new Scanner(System.in);

        int num = input.nextInt();

        for (int i = 0; i < num; i++) {
            for (int j = num - i - 1; j > 0; j--) {
                System.out.print(" ");
            }
            for (int k = 1; k <= i*2 + 1; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
        input.close();
    }
}
