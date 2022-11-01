package HW2_Recursion.Hanoi;

import java.util.Scanner;

public class main {
    static int[] top = new int[11];
    static int idx = 0;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numOfTest = scanner.nextInt();
        for(int i = 0; i < numOfTest; i++) {
            int numOfHanoi = scanner.nextInt();
            top = new int[11]; idx = 0;
            top[0] = 0;
            Hanoi(numOfHanoi, 1, 2, 3);
            System.out.println();
        }
    }
    static void Hanoi(int n, int a, int b, int c){
        if(n > 0){
            Hanoi(n - 1, a, c, b);
            if(c == 3){ // Move a to 3
                idx += 1;
                top[idx] = n;
                System.out.printf("%d ", top[idx]);
            }
            else if(a == 3 && idx == 1){ // Move 3 to c && 0
                idx = 0;
                System.out.printf("%d ", top[0]);
            }
            else if(a == 3){ // Move 3 to c
                idx -= 1;
                System.out.printf("%d ", top[idx]);
            }
            Hanoi(n - 1, b, a, c);
        }
    }
}
