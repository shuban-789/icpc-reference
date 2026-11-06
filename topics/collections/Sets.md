# Sets

```java
import java.util.HashSet;


public class HashSetExample {
  public static void main(String[] args) {
    // Create a HashSet
    HashSet<String> programmingLanguages = new HashSet<>();

    // 1. add()
    programmingLanguages.add("Java");
    programmingLanguages.add("Python");
    programmingLanguages.add("C++");
    boolean isAdded = programmingLanguages.add("Java"); // Will return false (duplicate)

    // 2. contains()
    System.out.println("Contains Python? " + programmingLanguages.contains("Python")); // true

    // 3. size()
    System.out.println("Set size: " + programmingLanguages.size()); // 3

    // 4. remove()
    programmingLanguages.remove("C++");

    // 5. isEmpty()
    System.out.println("Is set empty? " + programmingLanguages.isEmpty()); // false

    // 6. Iterating using an enhanced for-loop
    System.out.println("Remaining items:");
    for (String lang : programmingLanguages) {
        System.out.println(lang);
    }

    // 7. clear()
    programmingLanguages.clear();
    System.out.println("Size after clear: " + programmingLanguages.size()); // 0
    }
}
```
