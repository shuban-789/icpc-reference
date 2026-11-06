# BFS

```java
import java.util.*;


public class BFSDemo{
      public static void main(String[] args) {
             int n = 6;
             boolean[] visited = new boolean[n];
             List<Integer>[] adj = new ArrayList[6];
             for (int i = 0; i < n; i++) { adj[i] = new ArrayList<>(); }
             adj[0] = new ArrayList<>(Arrays.asList(1, 2, 4));
             adj[1] = new ArrayList<>(Arrays.asList(3, 4));
             adj[2] = new ArrayList<>(Arrays.asList(5));

             /*
              * Define adjacency list and read in problem-specific input
              *
              * In this example, we've provided "dummy input" that's
              * reflected in the GIF above to help illustrate the
              * order of the recursive calls.
              */
             for (int i = 0; i < n; i++) {
                     // iterate over all connected components in the graph
                     if (!visited[i]) {
                             Queue<Integer> q = new LinkedList<Integer>();
                             q.add(i);

                             while (q.size() > 0) {
                                      int currentNode = q.peek();
                                      q.poll();

                                      visited[currentNode] = true;

                                      for (int neighbor : adj[currentNode]) {
                                               if (!visited[neighbor]) { q.add(neighbor); }
                                      }
                             }
                     }
             }
      }
}
```
