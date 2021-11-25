import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Scanner;

/**
 * @author Shubham Kumar Mishra
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        BKalindromeArray solver = new BKalindromeArray();
        solver.solve(1, in, out);
        out.close();
    }

    static class BKalindromeArray {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int n = in.nextInt();
            for (int i = 0; i < n; i++) {
                ans(in, out);
            }
        }

        private void ans(Scanner in, PrintWriter out) {
            int size = in.nextInt();
            int[] ar = new int[size];
            for (int i = 0; i < size; i++) {
                ar[i] = in.nextInt();
            }

            int start = 0;
            int end = size - 1;
            while (start <= end) {
                int start_val = ar[start];
                int end_val = ar[end];
                if (start_val != end_val) {
                    if (possible(ar, start, end)) {
                        out.println("YES");
                        return;
                    } else {
                        out.println("NO");
                        return;
                    }
                } else {
                    start++;
                    end--;
                }
            }
            out.println("YES");

        }

        private boolean possible(int[] ar, int start, int end) {
            int store_start = start;
            int store_end = end;
            int remove_start_val = ar[start];
            int remove_end_val = ar[end];
//        lets remove start val
            boolean ans = true;
            while (start < end) {
                int start_val = ar[start];
                int end_val = ar[end];
                if (start_val == remove_start_val) {
                    start++;
                } else if (end_val == remove_start_val) {
                    end--;
                } else {
                    if (start_val == end_val) {
                        start++;
                        end--;
                    } else {
                        ans = false;
                        break;
                    }
                }
            }
            if (ans) {
                return true;
            }
//            we did not get as expecte result from removing first element lets try removing second elemenyt
            ans=true;
//        lets remove end val
            start = store_start;
            end = store_end;
            while (start < end) {
                int start_val = ar[start];
                int end_val = ar[end];
                if (start_val == remove_end_val) {
                    start++;
                } else if (end_val == remove_end_val) {
                    end--;
                } else {
                    if (start_val == end_val) {
                        start++;
                        end--;
                    } else {
                        ans = false;
                        break;
                    }
                }
            }
            return ans;

        }

    }
}
