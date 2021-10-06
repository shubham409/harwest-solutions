import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Scanner;

/**
 * @author Shubham
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        CKTree solver = new CKTree();
        solver.solve(1, in, out);
        out.close();
    }

    static class CKTree {
        int required_sum;
        int k;
        int minimum;
        int mod = 1_000_000_007;
        int[][] dp;

        public void solve(int testNumber, Scanner in, PrintWriter out) {
            this.required_sum = in.nextInt();
            this.k = in.nextInt();
            this.minimum = in.nextInt();
            dp = new int[required_sum + 1][3];
            for (int i = 0; i < dp.length; i++) {
                for (int j = 0; j < dp[0].length; j++) {
                    dp[i][j] = -1;

                }
            }
            out.println(recursion(required_sum, false));
        }
//    using memoization to calculate no of path available for required value wit edge needed or not
        public int recursion(int required, boolean is_present) {
            if (required < 0)
                return 0;
            else if (required == 0) {
                if (is_present) {
                    return 1;
                } else {
                    return 0;
                }
            } else {
                int bool_value = 0;
                if (is_present) {
                    bool_value = 1;
                } else {
                    bool_value = 0;
                }
                if (dp[required][bool_value] == -1) {
                    int ans = 0;
                    for (int i = 1; i <= k; i++) {
                        ans = (ans + recursion(required - i, is_present || i >= minimum)) % mod;
                    }
                    dp[required][bool_value] = ans;
                    return dp[required][bool_value];
                } else {
                    return dp[required][bool_value];
                }

            }
        }

    }
}

