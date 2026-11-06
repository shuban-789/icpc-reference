import java.util.*;

class ArraysReference {
    static int sortAndSearch(int[] a, int target) {
        Arrays.sort(a); // mutates a; ascending order
        int i = Arrays.binarySearch(a, target);
        // i >= 0: a match; duplicates: any match.
        // i < 0: insertion point = -i - 1.
        return i;
    }
    static void arrays(int n, int rows, int cols) {
        int[] a = new int[n]; // initially zero
        String[] names = {"Alice", "Bob"};
        int size = names.length; // field, no ()
        String first = names[0];
        names[0] = "Charlie";
        System.out.println(Arrays.toString(names));
        int[][] matrix = new int[rows][cols];
        for (int r = 0; r < matrix.length; r++) {
            for (int c = 0; c < matrix[r].length; c++)
                System.out.print(matrix[r][c] + " ");
            System.out.println();
        }
    }
}
