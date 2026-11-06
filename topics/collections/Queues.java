import java.util.*;

class Queues {
    static <T> void operations(T x, T y) {
        Queue<T> q = new ArrayDeque<>();
        q.offer(x); q.offer(y); // enqueue at tail
        T head = q.peek();      // null when empty
        T served = q.poll();    // null when empty
        int size = q.size();
        boolean empty = q.isEmpty();

        Deque<T> stack = new ArrayDeque<>();
        stack.push(x); stack.push(y);
        T top = stack.peek();   // y; null when empty
        T popped = stack.pop();// y; throws if empty

        Deque<T> d = new ArrayDeque<>();
        d.addFirst(x); d.addLast(y);
        T front = d.removeFirst(); // x
        T back = d.removeLast();   // y
        // removeFirst/Last throw if empty.
        // pollFirst/Last return null if empty.
    }
}
