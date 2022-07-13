import java.util.Scanner;
import java.util.Arrays;

public class B11650 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();

        int[][] array = new int[n+1][2];

        for(int i = 1; i <= n; i++) {
            array[i][0] = input.nextInt();
            array[i][1] = input.nextInt();
        }
        input.close();

        Arrays.sort(array, (e1, e2) -> {
            if(e1[0] == e2[0]) {
                return e1[1] - e2[1];
            } else {
                return e1[0] - e2[0];
            }
        });

        for(int i = 1; i<=n; i++) {
            System.out.println(array[i][0] + " " + array[i][1]);
        }
    }
}
