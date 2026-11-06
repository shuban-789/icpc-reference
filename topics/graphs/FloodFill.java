public class Floodfill {
      private static int[][] grid; // the grid itself
      private static int rowNum;
      private static int colNum;                 // grid dimensions, rows and columns
      private static boolean[][] visited; // keeps track of which nodes have been
                              // visited
      private static int currSize = 0; // reset to 0 each time we start a new component

      public static void main(String[] args) {
             /*
              * input code and other problem-specific stuff here
              */
             for (int r = 0; r < rowNum; r++) {
                     for (int c = 0; c < colNum; c++) {
                           if (!visited[r][c]) {
                                   currSize = 0;
                                   /*
                                    * start a flood fill if the square hasn't already been
                                    * visited, and then store or otherwise use the component
                                    * size for whatever it's needed for
                                    */
                                   floodfill(r, c, grid[r][c]);
                           }
                     }
             }
      }

      private static void floodfill(int r, int c, int color) {
             if ((r < 0 || r >= rowNum || c < 0 || c >= colNum) // if out of bounds
                  || grid[r][c] != color                   // wrong color
                  || visited[r][c] // already visited this square
             )
             return;

   visited[r][c] = true; // mark current square as visited
   currSize++;          // increment the size for each square we visit

   // recursively call flood fill for neighboring squares
   floodfill(r, c + 1, color);
   floodfill(r, c - 1, color);
   floodfill(r - 1, c, color);
   floodfill(r + 1, c, color);
   }
}
