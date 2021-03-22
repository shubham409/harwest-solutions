import java.util.*;

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
        ArrayList<ArrayList<Integer>> obj = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            ArrayList<Integer>temp= new ArrayList<>();
            temp.add(sc.nextInt());
            temp.add(sc.nextInt());
            obj.add(temp);
        }
        int ans=0;
        for (int i = 0; i <n ; i++) {
            ArrayList<Integer>first=obj.get(i);
            int home_i= first.get(0);
            int guest_i= first.get(1);
            for (int j = i+1; j <n ; j++) {
                ArrayList<Integer>second=obj.get(j);
                int home_j= second.get(0);
                int guest_j= second.get(1);
                if(home_i==guest_j){
                    ans++;
                }
                if(home_j==guest_i){
                    ans++;
                }
            }
        }
        print(ans);
    }
}
