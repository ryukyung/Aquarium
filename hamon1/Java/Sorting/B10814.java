import java.util.Scanner;
import java.util.Arrays;
import java.util.Comparator;

public class B10814 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();

        String[][] array = new String[n][2];

        for(int i = 0; i < n; i++) {
            array[i][0] = input.next();
            array[i][1] = input.next();
        }
        input.close();

        Arrays.sort(array, new Comparator<String[]>() {
            public int compare(String[] s1, String[] s2) {
                return Integer.parseInt(s1[0]) - Integer.parseInt(s2[0]);
            }
        });

        for(int i = 0; i<n; i++) {
            System.out.println(array[i][0] + " " + array[i][1]);
        }
    }
}
