# DFS

```java
import java.io.*;
import java.util.*;


public class DFSDemo {
      static List<Integer>[] adj;
      static boolean[] visited;
      static int n = 6;


      public static void main(String[] args) throws IOException {
             visited = new boolean[n];

             /*
              * Define adjacency list and read in problem-specific input
              *
              * In this example, we've provided "dummy input" that's
              * reflected in the GIF above to help illustrate the
              * order of the recursive calls.
              */
             adj = new ArrayList[n];
             for (int i = 0; i < n; i++) { adj[i] = new ArrayList<>(); }
             adj[0] = new ArrayList<>(Arrays.asList(1, 2, 4));
             adj[1] = new ArrayList<>(Arrays.asList(3, 4));
             adj[2] = new ArrayList<>(Arrays.asList(5));

             for (int i = 0; i < n; i++) {
                     // iterate over all connected components in the graph
                     if (!visited[i]) { dfs(i); }
             }
      }

      static void dfs(int currentNode) {
             if (visited[currentNode]) { return; }
   visited[currentNode] = true;
   for (int neighbor : adj[currentNode]) { dfs(neighbor); }
   }
}
```
