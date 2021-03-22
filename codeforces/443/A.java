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
        String st=(sc.nextLine());
        st=st.substring(1,st.length()-1);
        HashSet<String>hs=new HashSet<>();
        String[] split = st.split(",");
        for (int i = 0; i < split.length; i++) {
            if(!split[i].trim().equals(""))
            hs.add(split[i].trim());
        }
        if(!hs.isEmpty())
            print(hs.size());
        else
            print(0);
    }
}
