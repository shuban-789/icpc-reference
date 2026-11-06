import java.util.*;

class Sets {
    static <T> void operations(Collection<T> xs, T x) {
        HashSet<T> s = new HashSet<>(xs);
        boolean added = s.add(x); // false if duplicate
        boolean found = s.contains(x);
        int size = s.size();
        boolean removed = s.remove(x);
        boolean empty = s.isEmpty();
        for (T value : s) System.out.println(value);
        s.clear();
    }
}
