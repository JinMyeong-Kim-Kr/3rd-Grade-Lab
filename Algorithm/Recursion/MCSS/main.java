package HW2_Recursion.MCSS;

import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numOfTest = scanner.nextInt();
        for(int i = 0; i < numOfTest; i++) {
            int n = scanner.nextInt();
            int[] array = new int[n];
            for(int j = 0; j < n; j++)  array[j] = scanner.nextInt();
            int answer = findMaximumSubArray(array, 0, n - 1);
            if(answer < 0)  System.out.println(0);
            else System.out.println(answer);

        }
    }
    static int findMaximumSubArray(int[] array, int start, int end){
        if(start == end)    return array[start];
        else{
            int mid = (start + end) / 2;
            int leftMaxSum = findMaximumSubArray(array, start, mid);
            int rightMaxSum = findMaximumSubArray(array, mid + 1, end);
            int centerCrossSum = findCenterCross(array, start, mid, end);

            if(leftMaxSum < centerCrossSum && rightMaxSum < centerCrossSum) return centerCrossSum;
            else if(rightMaxSum < leftMaxSum && centerCrossSum < leftMaxSum) return leftMaxSum;
            else return rightMaxSum;
        }
    }
    static int findCenterCross(int[] array, int start, int mid, int end){
        int leftMaxSum = -1001;
        int tmpSum = 0;
        for(int i = mid; i >= start; i--){
            tmpSum += array[i];
            if(leftMaxSum < tmpSum)
                leftMaxSum = tmpSum;
        }

        tmpSum = 0;
        int rightMaxSum = -1001;
        for(int j = mid + 1; j < end + 1; j++){
            tmpSum += array[j];
            if(rightMaxSum < tmpSum)
                rightMaxSum = tmpSum;
        }
        return leftMaxSum + rightMaxSum;
    }

}
