/**
 * 2*n의 스티커가 있다. 스티커 하나를 사용하면 상하좌우의 스티커가 손상된다.
 * 사용가능한 스티커 합의 최대값을 구하여라
 * 
 * 
 * 가능한 모든 합을 구해서 최대값을 찾는다?
 * 
 * 그렇다면 어떻게?
 * 모든 조합을 찾는 알고리즘
 * 
 * 
 */

import java.util.Scanner;

public class B9465 {
    static Integer sticker[][];
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int max = in.nextInt();
        int col = in.nextInt();

        sticker = new Integer[2][col];
        for(int i = 0; i<2; i++) {
            for(int j = 0; j<col; j++) {
                sticker[i][j] = in.nextInt();
            }
        }


    }
}