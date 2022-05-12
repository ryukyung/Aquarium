import java.util.Scanner;

public class B2441 {
    public static void main(String[] arg) {
        Scanner input = new Scanner(System.in);

        int num = input.nextInt();

        for (int i = 0; i < num; i++) {
            for (int k = i; k>0; k--) {
                System.out.print(" ");
            }
            for (int j = num - i; j > 0; j--) {
                System.out.print("*");
            }
            
            System.out.println();
        }
        input.close();
    }
}
