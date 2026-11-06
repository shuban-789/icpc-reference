import java.util.Queue;
import java.util.ArrayDeque;

public class QueueExample {
    public static void main(String[] args) {
        // 1. Instantiate using ArrayDeque
        Queue<String> line = new ArrayDeque<>();

        // 2. Enqueue (Add elements to the tail)
        line.offer("Alice");
        line.offer("Bob");
        line.offer("Charlie");
        System.out.println("Queue: " + line); // Output: [Alice, Bob, Charlie]

        // 3. Inspect (Look at the head without removing)
      String nextUp = line.peek();
      System.out.println("Next in line: " + nextUp); // Output: Alice

      // 4. Dequeue (Remove and return the head)
      String served = line.poll();
      System.out.println("Served: " + served); // Output: Alice
      System.out.println("Remaining Queue: " + line); // Output: [Bob, Charlie]
  }
}

import java.util.Deque;
import java.util.ArrayDeque;

public class StackExample {
  public static void main(String[] args) {
      // Instantiate using Deque and ArrayDeque
      Deque<String> bookStack = new ArrayDeque<>();
      // 1. PUSH (Add element to the top)
      bookStack.push("Harry Potter");
      bookStack.push("The Hobbit");
      bookStack.push("1984");
    System.out.println("Stack: " + bookStack); // Output: [1984, The Hobbit, Harry Potter]

      // 2. PEEK (Look at the top element without removing)
      System.out.println("Top book: " + bookStack.peek()); // Output: 1984

      // 3. POP (Remove and return the top element)
      String removedBook = bookStack.pop();
      System.out.println("Popped: " + removedBook); // Output: 1984
    System.out.println("Remaining Stack: " + bookStack); // Output: [The Hobbit, Harry Potter]
  }
}
