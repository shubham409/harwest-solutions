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
        BBooks solver = new BBooks();
        solver.solve(1, in, out);
        out.close();
    }

    static class BBooks {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int n = in.nextInt();
            int ar[] = new int[n];
            int time = in.nextInt();
            int count = 0;
            for (int i = 0; i < n; i++) {
                ar[i] = in.nextInt();
            }
//       using binary search with starting i and find a prefix sum that is less than or equal to time
            int prefix[] = new int[n + 1];
            for (int i = 0; i < n; i++) {
                if (i == 0) {
                    prefix[i + 1] = ar[i];
                } else {
                    prefix[i + 1] = prefix[i] + ar[i];
                }
            }
            for (int i = 0; i < n; i++) {
//            we will find max index for which prefix sum between i and that index is less than the time
                int first = i;
                int last = n - 1;
                int accepted = -1;
                while (first <= last) {
                    int mid = (first + last) / 2;
                    int sum_till_mid = prefix[mid + 1] - prefix[i];
                    if (sum_till_mid <= time) {
                        first = mid + 1;
                        accepted = mid;
                    } else {
                        last = mid - 1;
                    }
                }
                if (accepted != -1) {
                    count = Integer.max(count, accepted - i + 1);
                }
            }
            out.println(count);
        }

    }
}

