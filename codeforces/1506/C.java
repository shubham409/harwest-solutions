import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.HashSet;
import java.io.PrintStream;
import java.util.Scanner;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author shubham
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        CDoubleEndedStrings solver = new CDoubleEndedStrings();
        solver.solve(1, in, out);
        out.close();
    }

    static class CDoubleEndedStrings {
        public void solve(int testNumber, Scanner sc, PrintWriter out) {
            int t = sc.nextInt();
            for (int k = 0; k < t; k++) {
                String s1 = sc.next();
                String s2 = sc.next();
                int l1 = s1.length();
                int l2 = s2.length();
                HashSet<String> hs = new HashSet<>();
                for (int i = 1; i <= l1; i++) {
                    for (int j = 0; j <= l1 - i; j++) {
                        hs.add(s1.substring(j, j + i));
                    }
                }
//            System.out.println(hs);
                int max = 0;
                for (int i = 1; i <= l2; i++) {
                    for (int j = 0; j <= l2 - i; j++) {
                        if (hs.contains(s2.substring(j, j + i))) {
//                        System.out.println(s2.substring(j,j+i));
                            max = Math.max(max, i);
                        }
                    }
                }
//            System.out.println(max);
                System.out.println(l1 + l2 - (2 * max));
//            if (l1>max && l2>max){
//
//            }
//            else{
//                if(l1==max && l2==max){
//                    System.out.println(0);
//                    break;
//                }
//                if(l1==max ){
//                    System.out.println(l2-max);
//                    break;
//                }
//                if( l2==max){
//                    System.out.println(l1-max);
//                    break;
//                }
//            }
            }
        }

    }
}

