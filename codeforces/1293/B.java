import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
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
        BJOEIsOnTV solver = new BJOEIsOnTV();
        solver.solve(1, in, out);
        out.close();
    }

    static class BJOEIsOnTV {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int s = in.nextInt();
            float ans = 0;
            while (s != 0) {
                ans += (float) 1 / s;
                s--;
            }
            out.format("%.12f", ans);
        }

    }
}

