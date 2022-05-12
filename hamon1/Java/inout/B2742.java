import java.util.Scanner;

public class B2742 {
    public static void main(String[] arg) {
        Scanner input = new Scanner(System.in);

        int max = input.nextInt();

        for (int i = 0; i < max; i++) {
            System.out.println(max-i);
        }
        input.close();
    }
}
