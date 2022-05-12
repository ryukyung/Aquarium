import java.util.Scanner;

public class B11720 {
    public static void main(String[] arg) {
        Scanner input = new Scanner(System.in);

        int max = input.nextInt();
        String num = input.next();

        int sum = 0;
        for (int i = max; i > 0; i--) {
            if (i == 1) {
                sum += Integer.parseInt(num.substring(max - 1));
            } else {
                sum += Integer.parseInt(num.substring(max - i, max - i + 1));
            }

        }
        System.out.println(sum);

        input.close();
    }
}// 너무 큰 수를 입력받는 경우가 있음 -> string타입으로 입력 받아야 하는듯? 아니면 float? -> 수 변형이 옴
 // string 타입! 사용해야함