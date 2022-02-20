import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Scanner;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author NoobCoder
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        BTernaryString solver = new BTernaryString();
        solver.solve(1, in, out);
        out.close();
    }

    static class BTernaryString {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int n = in.nextInt();
            for (int i = 0; i < n; i++) {
                solution(in, out);
            }
        }

        private void solution(Scanner in, PrintWriter out) {
            String str = in.next();
            char current = '0';
            int start = -1;
            int mid = -1;
            int end = -1;

            int ans = Integer.MAX_VALUE;
            for (int i = 0; i < str.length(); i++) {
                // to initialise three different value at three pointers
                if (start == -1) {
                    start = i;
                    continue;
                }
                if (mid == -1) {
                    if (str.charAt(i) != str.charAt(start)) {
                        mid = i;
                    } else {
                        start++;
                    }
                    continue;
                }
                if (end == -1) {
                    if (str.charAt(i) != str.charAt(mid) && str.charAt(i) != str.charAt(start)) {
                        end = i;
                        ans = Integer.min(ans, end - start + 1);
                    } else {
                        if (str.charAt(i) == str.charAt(start)) {
                            start = mid;
                            mid = i;
                        } else {
                            mid++;
                        }
                    }
                    continue;
                }

                // now we have set up all three different pointer different place
                if (str.charAt(i) == str.charAt(end)) {
                    // equal to end
                    ans = Integer.min(ans, end - start + 1);
                    start = mid;
                    mid = end + 1;
                    end = -1;
                } else if (str.charAt(i) == str.charAt(mid)) {
                    // equal to mid
                    ans = Integer.min(ans, end - start + 1);
                    start = end;
                    mid = i;
                    end = -1;
                } else {
                    // equal to start
                    ans = Integer.min(ans, end - start + 1);
                    start = mid;
                    mid = end;
                    end = i;
                    ans = Integer.min(ans, end - start + 1);
                }

            }
            if (ans == Integer.MAX_VALUE) {
                out.println(0);
            } else {
                out.println(ans);
            }

        }

    }
}

