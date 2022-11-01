package HW2_Recursion.Factorial;
import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int cnt = scanner.nextInt();
        int n;
        for(int i = 0; i < cnt; i++){
            n = scanner.nextInt();
            System.out.println(fact(n));
        }
    }
    static int fact(int n){
        if(n <= 1)  {return 1;}
        else {
            n = n * fact(n - 1);
            while(n % 10 == 0){
                n /= 10;
            }
         return n % 1000;
        }
    }
}
