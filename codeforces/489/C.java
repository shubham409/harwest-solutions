import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
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
        CGivenLengthAndSumOfDigits solver = new CGivenLengthAndSumOfDigits();
        solver.solve(1, in, out);
        out.close();
    }

    static class CGivenLengthAndSumOfDigits {
        public void solve(int testNumber, Scanner in, PrintWriter out) {

            int no_of_digit = in.nextInt();
            int sum_of_digit = in.nextInt();
            if (sum_of_digit == 0 && no_of_digit == 1) {
                out.println("0 0");
                return;
            }
            if (sum_of_digit > 9 * no_of_digit || sum_of_digit < 1) {
                out.println("-1 -1");
                return;
            }

            StringBuilder st = getmax(no_of_digit, sum_of_digit);
            StringBuilder ts = getmin(st.toString());
            out.println(ts + " " + st);
        }

        public StringBuilder getmax(int m, int s) {
            StringBuilder obj = new StringBuilder("");
            for (int i = 0; i < m; i++) {
                if (s >= 9) {
                    obj.append(9);
                    s -= 9;
                } else if (s != 0) {
                    obj.append(s);
                    s -= s;
                } else {
                    obj.append(0);
                }
            }
            return obj;
        }

        public StringBuilder getmin(String m) {
            StringBuilder max = new StringBuilder(m);
            boolean isLeadingZero = max.charAt(max.length() - 1) == '0';
            StringBuilder min = max.reverse();
            if (isLeadingZero) {
//            need to fix that last zero that will come at first and make it leading zero that we don't want
                int lastNonZeroIndex = -1;
                char lastNonZeroValue = '0';
                for (int i = min.length() - 1; i >= 0; i--) {
                    char current = min.charAt(i);
                    if (current != '0') {
                        lastNonZeroValue = current;
                        lastNonZeroIndex = i;
                    } else {
                        break;
                    }
                }
//            we put 1 at first position and decrease 1 from last non zero position
                if (lastNonZeroIndex == -1) {
                    return min;
                } else {
                    min.replace(0, 1, "1");
                    min.replace(lastNonZeroIndex, lastNonZeroIndex + 1, String.valueOf(Integer.parseInt(String.valueOf(lastNonZeroValue)) - 1));
                    return min;
                }

            } else {

                return min;
            }

        }

    }
}

