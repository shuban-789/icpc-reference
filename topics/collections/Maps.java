import java.util.HashMap;
import java.util.Map;


public class HashMapExample {

  public static void main(String[] args) {

    // Initialization (Requires wrapper classes like Integer instead of int)
    HashMap<String, Integer> inventory = new HashMap<>();

    // 1. Adding elements using put()
    inventory.put("Apple", 50);
    inventory.put("Banana", 20);
    inventory.put("Orange", 35);

    // 2. Retrieving elements using get() and getOrDefault()
    int appleCount = inventory.get("Apple"); // Returns 50
    int grapeCount = inventory.getOrDefault("Grape", 0); // Returns 0 (not found)

// 3. Checking presence
boolean hasBanana = inventory.containsKey("Banana"); // true

// 4. Updating a value
inventory.put("Apple", 60); // Overwrites 50 with 60

// 5. Removing an item
inventory.remove("Orange");

// 6. Iterating using entrySet()
for (Map.Entry<String, Integer> entry : inventory.entrySet()) {
    System.out.println(entry.getKey() + " Quantity: " + entry.getValue());
}

// Check size
System.out.println("Total unique items: " + inventory.size());
    }
}
