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
        CKeshiIsThrowingAParty solver = new CKeshiIsThrowingAParty();
        solver.solve(1, in, out);
        out.close();
    }

    static class CKeshiIsThrowingAParty {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int testcases = in.nextInt();
            for (int i = 0; i < testcases; i++) {
                ans(in, out);
            }
        }

        private void ans(Scanner in, PrintWriter out) {
            int size = in.nextInt();
            int[] richer_required = new int[size];
            int[] poor_required = new int[size];
            for (int i = 0; i < size; i++) {
                richer_required[i] = in.nextInt();
                poor_required[i] = in.nextInt();
            }
            int start = 0;
            int end = size;
//        using binary search on maximum people that we can select
            int mid = 0;
            while (start <= end) {
                int temp = (start + end) / 2;
                boolean boolean_val = checkIsitpossible(richer_required, poor_required, temp);
                if (boolean_val) {
                    start = temp + 1;
                    mid = temp;
                } else {
                    end = temp - 1;
                }
            }
            out.println(mid);
        }

        private boolean checkIsitpossible(int[] richer_required, int[] poor_required, int total_we_select) {
            int selected_so_far = 0;
            for (int i = 0; i < richer_required.length; i++) {
                int poor_below_this_person = selected_so_far;
                int rich_above_this_person = (total_we_select - selected_so_far - 1);
                if (richer_required[i] >= rich_above_this_person && poor_required[i] >= poor_below_this_person) {
//                this person is selected for our party
                    selected_so_far += 1;
                }
            }
            return selected_so_far >= total_we_select;
        }

    }
}
