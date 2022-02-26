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
        CTernaryXOR solver = new CTernaryXOR();
        solver.solve(1, in, out);
        out.close();
    }

    static class CTernaryXOR {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int t = in.nextInt();
            for (int i = 0; i < t; i++) {
                solution(in, out);
            }

        }

        private void solution(Scanner in, PrintWriter out) {
            int n = in.nextInt();
            String str = in.next();
            char one = '1';
            char two = '2';
            char zero = '0';
            StringBuilder bigger = new StringBuilder();
            StringBuilder smaller = new StringBuilder();

            boolean has_one_come_before = false;
            for (int i = 0; i < n; i++) {
                char current = str.charAt(i);
                if (current == zero) {
                    bigger.append('0');
                    smaller.append('0');
                } else if (current == one) {
                    if (has_one_come_before) {
                        bigger.append('0');
                        smaller.append('1');
                    } else {
                        bigger.append('1');
                        smaller.append('0');
                        has_one_come_before = true;
                    }
                } else {
                    if (has_one_come_before) {
                        bigger.append('0');
                        smaller.append('2');
                    } else {
                        bigger.append('1');
                        smaller.append('1');
                    }
                }

            }
            out.println(bigger);
            out.println(smaller);
        }

    }
}

