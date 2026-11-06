import java.io.*;
import java.util.*;

public class Main {
    static class Input {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in));
        StringTokenizer st;
        String next() throws IOException {
            while (st == null || !st.hasMoreTokens()) {
                String line = br.readLine();
                if (line == null) return null;
                st = new StringTokenizer(line);
            }
            return st.nextToken();
        }
        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
    }
    public static void main(String[] args)
            throws Exception {
        Input in = new Input();
        PrintWriter out = new PrintWriter(System.out);
        // int n = in.nextInt();
        // int[] a = new int[n];
        // ArrayList<Integer> list = new ArrayList<>();
        // Solve here; out.println(answer).
        out.close();
    }
}
