package HW2_Recursion.FastPowers;

import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int cnt = scanner.nextInt();
        int n; double x;
        for(int i = 0; i < cnt; i++){
            n = scanner.nextInt();
            x = scanner.nextDouble();
            System.out.println((int)computePowers(n, x));
        }
    }
    static double computePowers (int n, double x){
        if(x == 0){
            return 1.0;
        }
        else if(x % 2 != 0){ // odd
            double tmp = computePowers(n, (x - 1) / 2);
            return (n * tmp * tmp) % 1000;
        }
        else{ // even
            double tmp = computePowers(n, x / 2);
            return (tmp * tmp) % 1000;
        }
    }
}
