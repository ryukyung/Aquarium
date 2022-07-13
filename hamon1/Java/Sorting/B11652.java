import java.util.Arrays;
import java.io.*;

public class B11652 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        long[] nums = new long[n];
        for (int i = 0; i<n; i++) {
            nums[i] = Long.parseLong(br.readLine());
        }
        Arrays.sort(nums);

        int count = 1;
        int max = 1;
        int maxIdx = 0;
        for(int i = 1; i<n;i++) {
            if(nums[i] == nums[i-1]) count++;
            else count = 1;

            if(count > max) {
                max = count;
                maxIdx = i;
            }
        }
        System.out.print(nums[maxIdx]);
    }
}
