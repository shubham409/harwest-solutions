import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Scanner;
import java.util.Comparator;
import java.util.Collections;
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
        BKuriyamaMiraisStones solver = new BKuriyamaMiraisStones();
        solver.solve(1, in, out);
        out.close();
    }

    static class BKuriyamaMiraisStones {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            solution(in, out);
        }

        private void solution(Scanner in, PrintWriter out) {
            int n = in.nextInt();
            ArrayList<Integer> integers = new ArrayList<>();
            long prefixSum = 0;
            long[] originalPrefixSum = new long[n];
            for (int i = 0; i < n; i++) {
                int val = in.nextInt();
                integers.add(val);
                if (i == 0) {
                    prefixSum = val;
                    originalPrefixSum[i] = prefixSum;
                } else {
                    prefixSum += val;
                    originalPrefixSum[i] = prefixSum;
                }
            }
            prefixSum = 0;
            long[] sortedPrefixSum = new long[n];
            ArrayList<Integer> sorted = new ArrayList<>(integers);
            Collections.sort(sorted, new MyComparator());

            for (int i = 0; i < n; i++) {
                int val = sorted.get(i);
                if (i == 0) {
                    prefixSum = val;
                    sortedPrefixSum[i] = prefixSum;
                } else {
                    prefixSum += val;
                    sortedPrefixSum[i] = prefixSum;
                }
            }

            int query = in.nextInt();
            for (int i = 0; i < query; i++) {
                int type = in.nextInt();
                int start = in.nextInt();
                int end = in.nextInt();
                if (type == 1) {
                    long ans = query1(start, end, originalPrefixSum);
                    out.println(ans);
                } else {
                    long ans = query2(start, end, sortedPrefixSum);
                    out.println(ans);
                }
            }
        }

        private long query2(int start, int end, long[] sortedPrefixSum) {
            int startIndex = start - 1;
            int endIndex = end - 1;
            if (startIndex == 0) {
                return sortedPrefixSum[endIndex];
            } else {
                return sortedPrefixSum[endIndex] - sortedPrefixSum[startIndex - 1];
            }
        }

        private long query1(int start, int end, long[] originalPrefixSum) {
            int startIndex = start - 1;
            int endIndex = end - 1;
            if (startIndex == 0) {
                return originalPrefixSum[endIndex];
            } else {
                return originalPrefixSum[endIndex] - originalPrefixSum[startIndex - 1];
            }
        }

    }

    static class MyComparator implements Comparator<Integer> {
        public int compare(Integer o1, Integer o2) {
            return o1 - o2;
        }

    }
}

