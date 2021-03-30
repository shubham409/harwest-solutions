import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.PrintStream;
import java.util.SortedSet;
import java.util.Iterator;
import java.util.Scanner;
import java.util.Set;
import java.util.HashMap;
import java.util.Collections;
import java.util.TreeSet;
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        BBoxFitting solver = new BBoxFitting();
        solver.solve(1, in, out);
        out.close();
    }

    static class BBoxFitting {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int t = in.nextInt();
            for (int k = 0; k < t; k++) {
                int n, w;
                n = in.nextInt();
                w = in.nextInt();
                SortedSet<Integer> ts = new TreeSet<>(Collections.reverseOrder());
                HashMap<Integer, Integer> hm = new HashMap<>();
                for (int i = 0; i < n; i++) {
                    int var = in.nextInt();
                    ts.add(var);
                    if (hm.containsKey(var)) {
                        hm.put(var, hm.get(var) + 1);
                    } else {
                        hm.put(var, 1);
                    }
                }
                int total = n;
                int ans = 0;
                while (total > 0) {
                    ans += 1;
                    Iterator<Integer> it = ts.iterator();
                    int width = w;
                    while (it.hasNext() && width > 0) {
                        int var = it.next();
                        int count = hm.get(var);
                        if (count > 0) {
                            if (var <= width) {
                                int times = width / var;
                                times = Math.min(count, times);
                                width -= var * times;
                                total -= times;
                                hm.put(var, count - times);
                            }
                        } else {
                            it.remove();
                        }
                    }
                }
                System.out.println(ans);


            }
        }

    }
}

