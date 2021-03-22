
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
        int s=sc.nextInt();
        int n = sc.nextInt();
        int [][] array = new int[n][2];
        for (int i = 0; i <array.length ; i++) {
            for (int j = 0; j <2 ; j++) {
                array[i][j]=sc.nextInt();
            }
        }
        Arrays.sort(array, (a, b) -> a[0] - b[0]);
        for (int i = 0; i < n; i++) {
            if(s>array[i][0]){
                s+=array[i][1];
                
            }
            else {
                print("NO");
                return;
            }
                
        }
        print("YES");

    }
}
