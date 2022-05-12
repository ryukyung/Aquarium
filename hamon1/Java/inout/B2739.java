import java.util.Scanner;

public class B2739 {
    public static void main(String[] arg) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();

        for (int i = 1; i < 10; i++) {
            System.out.printf(n + " * %d = %d\n", i, n*i);
        }

        input.close();
    }
}
