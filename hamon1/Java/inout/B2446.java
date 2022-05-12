import java.util.Scanner;

public class B2446 {
    public static void main(String[] arg) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                System.out.print(" ");
            }
            for (int k = 0; k < 2*n - (i)*2 - 1; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < i; j++) {
                System.out.print(" ");
            }
            for (int k = 0; k < 2*n - (i)*2 - 1; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
        input.close();
    }
}
