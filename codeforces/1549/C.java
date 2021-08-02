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
        CWebOfLies solver = new CWebOfLies();
        solver.solve(1, in, out);
        out.close();
    }

    static class CWebOfLies {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int nodes = in.nextInt();
            int friendships = in.nextInt();
            int weak[] = new int[nodes + 1];
            int strong[] = new int[nodes + 1];
            int alive = nodes;
            for (int i = 0; i < friendships; i++) {
                int u = in.nextInt();
                int v = in.nextInt();
                int min = Math.min(u, v);
                int max = Math.max(u, v);
                if (strong[min] < 1) {
                    alive--;
                }
                weak[max] += 1;
                strong[min] += 1;
            }
            int querry = in.nextInt();
            for (int i = 0; i < querry; i++) {
                int type = in.nextInt();
                if (type == 3) {
                    out.println(alive);
                } else if (type == 2) {
//              remove
                    int u = in.nextInt();
                    int v = in.nextInt();
                    int min = Math.min(u, v);
                    int max = Math.max(u, v);
                    weak[max] -= 1;
                    strong[min] -= 1;
                    if (strong[min] < 1) {
                        alive++;
                    }
                } else {
//              add
                    int u = in.nextInt();
                    int v = in.nextInt();
                    int min = Math.min(u, v);
                    int max = Math.max(u, v);
                    if (strong[min] < 1) {
                        alive--;
                    }
                    weak[max] += 1;
                    strong[min] += 1;
                }
            }

        }

    }
}

