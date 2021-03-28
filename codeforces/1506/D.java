import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.PrintStream;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Set;
import java.util.HashMap;
import java.util.ArrayList;

/**
 * @author shubham
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        DEpicTransformation solver = new DEpicTransformation();
        solver.solve(1, in, out);
        out.close();
    }

    static class DEpicTransformation {
        public void solve(int testNumber, Scanner in, PrintWriter out) {

            int t = in.nextInt();
            for (int k = 0; k < t; k++) {
                HashMap<Integer, Integer> hm = new HashMap<>();
                int n = in.nextInt();
                ArrayList<Integer> al = new ArrayList<>(n);
                for (int i = 0; i < n; i++) {
                    int v = in.nextInt();
                    al.add(v);
                }
                for (int i = 0; i < n; i++) {
                    int val = al.get(i);
                    if (hm.containsKey(val)) {
                        hm.put(val, hm.get(val) + 1);
                    } else {
                        hm.put(val, 1);
                    }
                }
                int ans = n;
                Set<Integer> st = hm.keySet();
                PriorityQueue<Pair> pq = new PriorityQueue<>();
                for (Integer val : st) {
                    Pair p = new Pair();
                    p.setKey(val);
                    p.setValue(hm.get(val));
                    pq.add(p);

                }
                while (pq.size() >= 2) {
                    Pair p1 = pq.poll();
                    Integer p1_value = p1.getValue();
                    Integer p1_key = p1.getKey();
                    Pair p2 = pq.poll();
                    Integer p2_value = p2.getValue();
                    Integer p2_key = p2.getKey();
                    p1_value--;
                    p2_value--;
                    ans -= 2;
                    if (p1_value != 0) {
                        pq.add(new Pair(p1_key, p1_value));
                    }
                    if (p2_value != 0) {
                        pq.add(new Pair(p2_key, p2_value));
                    }
                }
                System.out.println(ans);
            }
        }

    }

    static class Pair implements Comparable<Pair> {
        Integer key;
        Integer value;

        Pair() {
        }

        Pair(Integer k, Integer v) {
            key = k;
            value = v;
        }

        public Integer getKey() {
            return key;
        }

        public void setKey(Integer key) {
            this.key = key;
        }

        public Integer getValue() {
            return value;
        }

        public void setValue(Integer value) {
            this.value = value;
        }

        public int compareTo(Pair o) {
            return Integer.compare(o.value, this.value);
        }

    }
}

