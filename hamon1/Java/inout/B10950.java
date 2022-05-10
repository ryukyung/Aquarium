import java.util.Scanner;

public class B10950 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		int max = in.nextInt();
		
		int[][] array = new int[max][2];
		
		for (int i = 0; i < max; i++) {
			for (int j = 0; j < 2; j++) {
				array[i][j] = in.nextInt();
			}
		}
		
		int sum;
		
		for (int i = 0; i < max; i++) {
			sum = 0;
			for (int j = 0; j < 2; j++) {
				sum += array[i][j];
			}
			System.out.println(sum);
		}

	}

}