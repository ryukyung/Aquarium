import java.util.Scanner;

public class B10952 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		int sum; boolean end = true;
		
		while(end) {
			sum = 0;
			for (int j = 0; j < 2; j++) {
				sum += in.nextInt();
			}
			
			if (sum == 0) break;
			System.out.println(sum);
			
		}

	}

}