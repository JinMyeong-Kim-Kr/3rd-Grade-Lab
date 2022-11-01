package HW2_Recursion.Fibo;
import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int cnt = scanner.nextInt();
        int n;
        for(int i = 0; i < cnt; i++){
            n = scanner.nextInt();
            System.out.println(fibo(n));
        }
    }
    static int fibo(int n){
        return n <= 1 ? n : fibo(n - 1) + fibo(n - 2);
    }
}
