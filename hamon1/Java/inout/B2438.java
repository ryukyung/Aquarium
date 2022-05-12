import java.util.Scanner;

public class B2438 {
    public static void main(String[] arg) {
        Scanner input = new Scanner(System.in);

        int num = input.nextInt();

        for (int i = 0; i < num; i++) {
            for (int j = i+1; j >0; j--) {
                System.out.print("*");
            }
            System.out.println();
        }

        input.close();
    }
}
