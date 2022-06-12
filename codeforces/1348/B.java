import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.stream.IntStream;
import java.util.Arrays;
import java.util.stream.Stream;
import java.util.Iterator;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.TreeSet;
import java.util.ArrayList;

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
        BPhoenixAndBeauty solver = new BPhoenixAndBeauty();
        solver.solve(1, in, out);
        out.close();
    }

    static class BPhoenixAndBeauty {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int t = in.nextInt();
            for (int i = 0; i < t; i++) {
                solution(in, out);
            }
        }

        private void solution(Scanner in, PrintWriter out) {
            int length = in.nextInt();
            int cycle = in.nextInt();
//        only way to not get ans is if no. of different no. presnet in array are more than cycle size

            int ar[] = new int[length];
            TreeSet<Integer> different = new TreeSet<>();
//        using arraylist as we dont know size
            ArrayList<Integer> ans = new ArrayList<>();
            int[] cycle_elements = new int[cycle];

            for (int i = 0; i < ar.length; i++) {
                ar[i] = in.nextInt();
                different.add(ar[i]);
            }
//        no if different no. is more than cycle size ans is no.
            if (cycle < different.size()) {
                out.println(-1);
                return;
            }

//        yes , it can be done time to make cycle
            Iterator<Integer> iterator = different.iterator();
            int ind = 0;
            while (iterator.hasNext()) {
                cycle_elements[ind] = iterator.next();
                ind++;
            }

            for (int i = 0; i < cycle; i++) {
                if (cycle_elements[i] == 0) {
                    cycle_elements[i] = 1;
                }
            }
            for (int i = 0; i < length; i++) {
                ans.addAll(Arrays.stream(cycle_elements).boxed().collect(Collectors.toList()));
            }
            out.println(ans.size());
            for (int i = 0; i < ans.size(); i++) {
                out.print(ans.get(i) + " ");
            }
            out.println();
        }

    }
}

