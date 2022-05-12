import java.util.Scanner;

public class B10991 {
    public static void main(String[] arg) {
        Scanner input = new Scanner(System.in);

        int num = input.nextInt();

        for (int i = 0; i < num; i++) {
            for (int j = 0; j < num - i - 1; j++) {
                System.out.print(" ");
            }
            for (int k = 0; k < 1 + (i)*2; k++) {
                if (k % 2 == 0) {
                    System.out.print("*");
                }
                else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
        input.close();
    }
}
