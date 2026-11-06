import java.util.*;

class FloodFill {
    static int fill(int[][] grid, int r, int c,
                    boolean[][] seen) {
        int rows = grid.length;
        int cols = rows == 0 ? 0 : grid[0].length;
        if (r < 0 || r >= rows || c < 0 || c >= cols
                || seen[r][c]) return 0;
        int color = grid[r][c], size = 0;
        int[] dr = {0, 0, -1, 1};
        int[] dc = {1, -1, 0, 0};
        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[]{r, c});
        seen[r][c] = true;
        while (!stack.isEmpty()) {
            int[] p = stack.pop();
            size++;
            for (int k = 0; k < 4; k++) {
                int nr = p[0] + dr[k], nc = p[1] + dc[k];
                if (nr < 0 || nr >= rows || nc < 0
                        || nc >= cols || seen[nr][nc]
                        || grid[nr][nc] != color) continue;
                seen[nr][nc] = true;
                stack.push(new int[]{nr, nc});
            }
        }
        return size;
    }
    static List<Integer> components(int[][] grid) {
        int rows = grid.length;
        int cols = rows == 0 ? 0 : grid[0].length;
        boolean[][] seen = new boolean[rows][cols];
        List<Integer> sizes = new ArrayList<>();
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if (!seen[r][c])
                    sizes.add(fill(grid, r, c, seen));
        return sizes;
    }
}
