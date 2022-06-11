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
            for (int i = 0; i < n; i++) {
                ar[i] = in.nextInt();
            }
//       using two pointer approach used in editorial
//        approach move last pointer (to take more number = more sum ) till sum is less , when sum is greater increase front pointer(to take less number = less sum)
            int first = 0;
            int last = 0;
            int sum_of_window = 0; // between sum of first and last
//        we are only finding contiguious sum
            int count = 0;
            int current_size_window = 0;
            while (last < n) {
                if (sum_of_window + ar[last] > time) {
//                increase front to lessen sum

//                it is not necessary that removing one from front will solve problem e.g. 1 in left 50 in right
                    while (first < last && sum_of_window + ar[last] > time) {
                        sum_of_window -= ar[first];
                        first += 1;
                        current_size_window -= 1;
                    }
//                no is disruptive ( time available 4 min but book require 70 minute )
                    if (first == last && sum_of_window + ar[last] > time) {
                        last += 1;
                        first += 1;
                    } else {
//                    increase first pointer (already done in loop ) and include last
                        sum_of_window += ar[last];
                        last += 1;
                        current_size_window += 1;
                        count = Integer.max(count, current_size_window);

                    }
                    count = Integer.max(count, current_size_window);
                } else {
                    sum_of_window += ar[last];
                    last += 1;
                    current_size_window += 1;
                    count = Integer.max(count, current_size_window);
                }
            }
            out.println(count);

        }

    }
}

