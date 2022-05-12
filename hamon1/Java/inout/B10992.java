import java.util.Scanner;

public class B10992 {
    public static void main(String[] arg) {
        Scanner input = new Scanner(System.in);

        int num = input.nextInt();

        for (int i = 0; i < num; i++) {
            for (int j = 0; j < num - i - 1; j++) {
                System.out.print(" ");
            }
            for (int k = 0; k < 1 + i * 2; k++) {
                if (i == num - 1) {
                    System.out.print("*");
                } else {
                    if (k == 0) {
                        System.out.print("*");
                    } else if (k == i * 2) {
                        System.out.print("*");
                    } else {
                        System.out.print(" ");
                    }
                }

            }
            System.out.println();
        }
        input.close();
    }
}
