package HW2_Recursion.Permutation;

import java.util.Scanner;

public class main {
    static int cnt;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        for(int i = 0; i < num; i++){
            String msg = scanner.next();
            char[] charArray = msg.toCharArray();
            cnt = 0;
            permute(charArray);
            System.out.println(cnt);
        }
    }
    static void permuteString(char[] str, int begin, int end){
        int range = end - begin;
        int weight = 0;
        if (range == 1){
            // print @str
            for(int j = 0; j < str.length; j++){
                weight += calcWeight(str[j], j);
            }
            if(weight > 0){
                cnt += 1;
            }
        }
        else{
            for(int i = 0; i < range; i++){
                swap(str, begin, begin + i);
                permuteString(str, begin + 1, end);
                swap(str, begin, begin + i);
            }
        }
    }
    static void permute(char[] str){
        permuteString(str, 0, str.length);
    }
    static int calcWeight(char str, double j){
        double weight = Math.pow(-1, j) * ((int)str - 'a');
        return (int)weight;
    }
    static void swap(char[] msg, int begin, int end){
        char tmp = msg[begin];
        msg[begin] = msg[end];
        msg[end] = tmp;
    }
}
