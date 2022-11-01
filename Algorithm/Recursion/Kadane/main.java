package HW2_Recursion.Kadane;

import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int cnt = scanner.nextInt();
        for(int i = 0; i < cnt; i++){
            int n = scanner.nextInt();
            int[] array = new int[n];
            for(int j = 0; j < n; j++)  array[j] = scanner.nextInt();
            Kadane(array, n);
        }
    }
    static void Kadane(int[] array, int num){
        int maxSum = 0; int thisSum = 0;
        int start = -1; int end = -1;

        for(int s = 0, e = 0; e < num; e++){
            thisSum += array[e];
            if(thisSum > maxSum){
                maxSum = thisSum;
                start = s;
                end = e;
            }
            else if(thisSum < 0){
                // initialize @s.
                s = e + 1;
                thisSum = 0;
            }
        }
        if(maxSum > 0 && array[start] == 0)   start += 1;
        if(maxSum < 0) System.out.printf("%d %d %d \n", maxSum, start, end);
        else System.out.printf("%d %d %d \n", maxSum, start, end);
    }
}
