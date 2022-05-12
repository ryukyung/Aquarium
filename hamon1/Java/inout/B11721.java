import java.util.Scanner;

public class B11721 {
    public static void main(String[] arg) {
        Scanner input = new Scanner(System.in);

        String s = input.next();

        boolean end = true;
        int n = 0;
        while(end) {
            
            try {
                System.out.println(s.substring(n, n+10));
            } catch(Exception e) {
                System.out.println(s.substring(n));
                end = false;
                return;
            }
            n += 10;
        }
    }
}