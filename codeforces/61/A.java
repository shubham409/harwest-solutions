
import java.util.Scanner;

public class Cp1 {
    static <T> void print(T obj){
        System.out.println(obj);
    }
    static String stringOps(String s1 ,String s2){
        StringBuilder stringBuffer = new StringBuilder();
        for(int i=0;  i< s1.length();i++){
            stringBuffer.append((s1.charAt(i))^(s2.charAt(i)));
        }
        return stringBuffer.toString();

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String st1=sc.nextLine();
        String st2=sc.nextLine();
        print(stringOps(st1,st2));

    }
}