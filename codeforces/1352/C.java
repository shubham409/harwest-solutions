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
        CKThNotDivisibleByN solver = new CKThNotDivisibleByN();
        solver.solve(1, in, out);
        out.close();
    }

    static class CKThNotDivisibleByN {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int n = in.nextInt();
            for (int i = 0; i < n; i++) {
                solution(in, out);
            }
        }

        private void solution(Scanner in, PrintWriter out) {
            long divisor = in.nextInt();
            long n_the_non_divisible_number = in.nextInt();
            long countNonDivisibleTillNow = divisor - 1;

//        first case when nuber itself is smaller than divisor-1 example diviser
            if (countNonDivisibleTillNow >= n_the_non_divisible_number) {
                out.println(n_the_non_divisible_number);
                return;
            }
//        else use division and reach to that number
            long times = n_the_non_divisible_number / countNonDivisibleTillNow;
            long remainder = n_the_non_divisible_number % countNonDivisibleTillNow;
            if (remainder == 0) {
                out.println((divisor * times - 1));
            } else {
                out.println((divisor * times + remainder));
            }
        }

    }
}

