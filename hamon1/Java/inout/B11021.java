import java.util.Scanner;

public class B11021 {
        public static void main(String[] arg) {
            Scanner input = new Scanner(System.in);

            int max = input.nextInt();

            for(int i = max; i>0; i--) {
                int a = input.nextInt();
                int b = input.nextInt();

                System.out.printf("Case #%d: %d\n", max-i+1, a+b);
            }

            input.close();
        }
}