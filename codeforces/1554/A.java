import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.PrintStream;
import java.util.Scanner;

/**
 * @author shubham
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        ACherry solver = new ACherry();
        solver.solve(1, in, out);
        out.close();
    }

    static class ACherry {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int t = in.nextInt();
            for (int i = 0; i < t; i++) {
                ans(in, out);
            }

        }

        private void ans(Scanner in, PrintWriter out) {
            int n = in.nextInt();
            long ar[] = new long[n];
            long ans = Integer.MIN_VALUE;
            for (int i = 0; i < n; i++) {
                ar[i] = in.nextInt();
                if (i > 0) {
                    ans = Long.max(ans, ar[i] * ar[i - 1]);
                }
            }
            System.out.println(ans);
        }

    }
}

