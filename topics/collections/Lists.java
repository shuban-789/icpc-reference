import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {

      // Create an ArrayList
      ArrayList<String> fruits = new ArrayList<>();

      // 1. Add elements
      fruits.add("Apple");
      fruits.add("Banana");
      fruits.add(1, "Mango"); // Inserts at index 1

      // 2. Access and modify
      String firstFruit = fruits.get(0); // "Apple"
      fruits.set(2, "Blackberry");    // Replaces "Banana" with "Blackberry"

        // 3. Information
        int totalItems = fruits.size(); // 3
        boolean hasApple = fruits.contains("Apple"); // true

        // 4. Remove elements
        fruits.remove(1);               // Removes "Mango"
        fruits.remove("Apple");           // Removes "Apple"

        // 5. Functional Loop (Java 8+)
        for (String fruit : fruits) {
            System.out.println("Fruit name: " + fruit);
        }
    }
}
