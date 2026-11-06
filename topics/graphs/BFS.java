import java.util.*;

class BFS {
    static int[] distances(List<List<Integer>> adj,
                           int start) {
        int[] dist = new int[adj.size()];
        Arrays.fill(dist, -1);
        Queue<Integer> q = new ArrayDeque<>();
        dist[start] = 0;
        q.offer(start);
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : adj.get(u)) {
                if (dist[v] != -1) continue;
                dist[v] = dist[u] + 1;
                q.offer(v);
            }
        }
        return dist;
    }
    static boolean[] forest(List<List<Integer>> adj) {
        boolean[] seen = new boolean[adj.size()];
        Queue<Integer> q = new ArrayDeque<>();
        for (int s = 0; s < adj.size(); s++) {
            if (seen[s]) continue;
            seen[s] = true;
            q.offer(s);
            while (!q.isEmpty()) {
                int u = q.poll();
                for (int v : adj.get(u)) {
                    if (seen[v]) continue;
                    seen[v] = true;
                    q.offer(v);
                }
            }
        }
        return seen;
    }
}
