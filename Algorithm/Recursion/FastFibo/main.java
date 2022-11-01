package HW2_Recursion.FastFibo;

import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int cnt = scanner.nextInt();
        for(int i = 0; i < cnt; i++){
            int num = scanner.nextInt();
            if(num == 0)    System.out.println(0);
            else {
                int[][] fibo = {{1, 1}, {1, 0}};
                System.out.println(fastFibo(fibo, num)[0][1]);
            }
        }
    }

    static int[][] fastFibo(int[][] fibo, int n){
        if(n == 1) return fibo;
        else {
            fibo = fastFibo(fibo, n / 2);
            fibo = multipleMatrix(fibo, fibo);
            if (n % 2 != 0) { // odd
                int[][] tmp = {{1, 1}, {1, 0}};
                fibo = multipleMatrix(fibo, tmp);
            }
            return fibo;

        }
    }
    static int[][] multipleMatrix(int[][]fibo, int[][] m){
        int x =  fibo[0][0]*m[0][0] + fibo[0][1]*m[1][0];
        int y =  fibo[0][0]*m[0][1] + fibo[0][1]*m[1][1];
        int z =  fibo[1][0]*m[0][0] + fibo[1][1]*m[1][0];
        int w =  fibo[1][0]*m[0][1] + fibo[1][1]*m[1][1];
        m = new int[][]{{x % 1000 , y % 1000}, {z % 1000, w % 1000}};
        return m;
    }
}
