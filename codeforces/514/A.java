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
        AChewbascaAndNumber solver = new AChewbascaAndNumber();
        solver.solve(1, in, out);
        out.close();
    }

    static class AChewbascaAndNumber {
        StringBuilder ans = new StringBuilder();

        public void solve(int testNumber, Scanner in, PrintWriter out) {
            solution(in, out);
        }

        private void solution(Scanner in, PrintWriter out) {
            String str = in.next();
            for (int i = 0; i < str.length(); i++) {
                char current = str.charAt(i);
                int currentInt = Integer.valueOf(String.valueOf(current));
                if (currentInt > 4) {
                    if (currentInt == 9) {
                        if (i == 0) {
                            ans.append(9);
                        } else {
                            ans.append(0);
                        }
                    } else {
                        ans.append(9 - currentInt);
                    }

                } else {
                    ans.append(currentInt);
                }
            }
            out.println(ans);
        }

    }
}

