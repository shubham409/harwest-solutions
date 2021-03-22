import java.util.*;
import java.math.*;
public class Cp1 {
    static <T> void print(T obj){
        System.out.println(obj);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        solve(sc);
    }

    private static void solve(Scanner sc ) {
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            Double val = (double)sc.nextInt();
            print((int)Math.ceil((val/2))-1);
        }
    }
}
