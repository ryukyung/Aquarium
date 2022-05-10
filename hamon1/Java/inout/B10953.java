import java.util.Scanner;

public class B10953 {
	public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    int max = input.nextInt();
    
    int sum = 0;

    for (int i = max; i>0; i--) {
        String s = input.next();
        String[] array = s.split(",");

        sum += Integer.parseInt(array[0]) + Integer.parseInt(array[1]);
        System.out.println(sum);
        sum = 0;
    }
    input.close();
    }
}
