import java.util.Scanner;

public class B2751 {
    static int list[];

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();

        list = new int[n+1];
        for (int i = 1; i<=n; i++) {
            list[i] = input.nextInt();
        }

        int a;

        for(int i = 1; i<=n; i++) {
            a = list[i];
            for (int j = 1; j<=n; j++) {
                if(list[j] >= list[i]) {
                    if(j == 1) {
                        list[i] = list[j];
                        list[j] = a;
                        break;
                    }
                    list[i] = list[j-1];
                    list[j-1] = a;
                    break;
                }
            }
        }

        for(int i = 0; i<n; i++) {
            System.out.println(list[i+1]);
        }
    }
}