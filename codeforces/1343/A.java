import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.HashSet;
import java.io.PrintStream;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        ACandies solver = new ACandies();
        solver.solve(1, in, out);
        out.close();
    }

    static class ACandies {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int t = in.nextInt();
            int powers = 1;
            HashSet<Integer> hs = new HashSet<>();
            for (int i = 1; i < 31; i++) {
                powers += (int) Math.pow(2, i);
                hs.add(powers);
            }
            for (int k = 0; k < t; k++) {
                int val = in.nextInt();
                for (int a : hs) {
                    if (val % a == 0) {
                        System.out.println(val / a);
                        break;
                    }
                }
            }
        }

    }
}

