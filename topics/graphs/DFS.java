import java.util.*;

class DFS {
    static List<List<Integer>> graph(int n) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++)
            adj.add(new ArrayList<>());
        return adj; // adj.get(u).add(v)
    }
    static void dfs(List<List<Integer>> adj, int s,
                    boolean[] seen) {
        Deque<Integer> stack = new ArrayDeque<>();
        seen[s] = true;
        stack.push(s);
        while (!stack.isEmpty()) {
            int u = stack.pop(); // process u here
            for (int v : adj.get(u)) {
                if (seen[v]) continue;
                seen[v] = true;
                stack.push(v);
            }
        }
    }
    static boolean[] forest(List<List<Integer>> adj) {
        boolean[] seen = new boolean[adj.size()];
        for (int u = 0; u < adj.size(); u++)
            if (!seen[u]) dfs(adj, u, seen);
        return seen;
    }
}
