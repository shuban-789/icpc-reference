import java.util.Arrays;


public class ArrayExample {
    public static void main(String[] args) {
      String[] employees = {"Charlie", "Bob", "Alice", "Dan"};

        // 1. Sort it first!
        Arrays.sort(employees); // Now: ["Alice", "Bob", "Charlie", "Dan"]


        // 2. Search it!
        int targetIndex = Arrays.binarySearch(employees, "Bob");


        if (targetIndex >= 0) {
            System.out.println("Found Bob at position " + targetIndex);
        } else {
            System.out.println("Employee not found.");
        }
    }
}


int[][] emptyMatrix = new int[2][3];

// Rows are accessed via .length, columns via matrix[i].length
for (int i = 0; i < matrix.length; i++) {
    for (int j = 0; j < matrix[i].length; j++) {
        System.out.print(matrix[i][j] + " ");
    }
    System.out.println();
}
