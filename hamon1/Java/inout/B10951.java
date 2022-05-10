import java.util.Scanner;

public class B10951 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		int sum;
		
		while(in.hasNextInt()) {
			sum = 0;
			for (int j = 0; j < 2; j++) {
				sum += in.nextInt();
			}
			
			System.out.println(sum);
		}

	}

}