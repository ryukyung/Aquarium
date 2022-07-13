import java.util.*;

public class B2751 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int n = input.nextInt();

        ArrayList<Integer>list = new ArrayList<>();
        for (int i = 1; i<=n; i++) {
            list.add(input.nextInt());
        }
        input.close();

        Collections.sort(list);

        for (int i : list) {
            sb.append(i).append('\n');
        }
        System.out.println(sb);
    }
}