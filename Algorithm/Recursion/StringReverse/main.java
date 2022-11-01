package HW2_Recursion.StringReverse;

import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int cnt = scanner.nextInt();
        for(int i = 0; i < cnt; i++){
            String msg = scanner.next();
            String[] answer = reverseArray(msg.split(""), 0, msg.length() - 1);
            for(int j = 0; j < answer.length; j++){
                System.out.print(answer[j]);
            }
            System.out.println();
        }
    }
    static String[] reverseArray(String[] message, int first, int last){
        if(first < last) {
            swap(message, first, last);
            reverseArray(message, first + 1, last - 1);
        }
        else{
            return message;
        }
        return message;
    }

    static void swap(String[] msg, int a, int b){
        String tmp = msg[a];
        msg[a] = msg[b];
        msg[b] = tmp;
    }
}
