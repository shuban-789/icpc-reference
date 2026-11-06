import java.util.*;

class Lists {
    static <T> void operations(T x, T y) {
        ArrayList<T> a = new ArrayList<>();
        a.add(x);          // append
        a.add(0, y);       // insert, shifting suffix
        T first = a.get(0);
        a.set(0, x);       // replace
        int size = a.size();
        boolean found = a.contains(x);
        a.remove(0);      // remove by index
        a.remove(x);      // remove first equal value
        // For ArrayList<Integer>, remove value 7:
        // a.remove(Integer.valueOf(7));
        for (T value : a) System.out.println(value);
    }
}
