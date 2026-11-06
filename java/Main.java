import java.util.*;
import java.io.*;


public class JavaTemplate {


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // BufferedReader br = new BufferedReader(new FileReader("testfile.in"));
        PrintWriter pw = new PrintWriter(System.out);


        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());


        int[] arr = new int[T];
        ArrayList<Integer> arrLs = new ArrayList<Integer>();


        pw.close();
    }


}
