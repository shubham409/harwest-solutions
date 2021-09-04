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
        B1BooksExchangeEasyVersion solver = new B1BooksExchangeEasyVersion();
        solver.solve(1, in, out);
        out.close();
    }

    static class B1BooksExchangeEasyVersion {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int t = in.nextInt();
            for (int i = 0; i < t; i++) {
                fun(in, out);
            }

        }

        private void fun(Scanner in, PrintWriter out) {
            int n = in.nextInt();
            int[] group1 = new int[n];
            for (int i = 0; i < n; i++) {
                group1[i] = in.nextInt();
            }
            int[] group2 = new int[n];
            for (int i = 0; i < n; i++) {
                group2[i] = i + 1;
            }
            int[] days = new int[n + 1];
            DSU obj = new DSU(group1, group2, days, n, in, out);
            obj.filldays();
            obj.show();
        }

    }

    static class DSU {
        int[] group1;
        int[] group2;
        int[] parent;
        int[] days;
        int n;
        Scanner in;
        PrintWriter out;

        public DSU(int[] group1, int[] group2, int[] days, int n, Scanner in, PrintWriter out) {
            this.group1 = group1;
            this.group2 = group2;
            this.days = days;
            this.n = n;
            this.in = in;
            this.out = out;
            parent = new int[n + 1];
            for (int i = 0; i <= n; i++) {
                parent[i] = i;
            }
            for (int i = 0; i <= n; i++) {
                days[i] = 0;
            }
        }

        int merge(int a, int b) {
            int p1 = findparent(a);
            int p2 = findparent(b);
            int f1 = Math.min(p1, p2);
            int f2 = Math.max(p1, p2);
            if (p1 != p2) {
                parent[f2] = f1;
            }
            return f1;
        }

        boolean iscyclic(int a, int b) {
            int p1 = findparent(a);
            int p2 = findparent(b);
            return p1 == p2;
        }

        int findparent(int a) {
            if (parent[a] == a)
                return a;
            else
                return findparent(parent[a]);
        }

        void filldays() {
            for (int i = 0; i < n; i++) {
                if (iscyclic(group1[i], group2[i])) {
                    int val = findparent(group1[i]);
                    days[val] = days[val] + 1;
                } else {
                    int f = findparent(group1[i]);
                    int s = findparent(group2[i]);
                    int val = merge(group1[i], group2[i]);
                    if (val == s) {
                        days[s] = days[f] + 1 + days[s];
                    } else {
                        days[f] = days[s] + 1 + days[f];
                    }
                }
            }
            for (int i = 0; i < n; i++) {
                int val = findparent(i + 1);
                days[i + 1] = days[val];
            }
        }

        void show() {
            for (int i = 1; i < n + 1; i++) {
                if (i == n) {
                    out.println(days[i]);
                } else out.print(days[i] + " ");
            }
        }

    }
}

