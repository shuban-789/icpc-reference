import java.util.*;

class Maps {
    static <K, V> void operations(K key, V value,
                                 V fallback) {
        HashMap<K, V> map = new HashMap<>();
        V old = map.put(key, value); // insert/overwrite
        V got = map.get(key);        // null if absent
        V safe = map.getOrDefault(key, fallback);
        boolean hasKey = map.containsKey(key);
        boolean hasValue = map.containsValue(value);
        for (Map.Entry<K, V> e : map.entrySet())
            System.out.println(e.getKey()+" "+e.getValue());
        for (K k : map.keySet()) System.out.println(k);
        for (V v : map.values()) System.out.println(v);
        int size = map.size();
        V removed = map.remove(key);
        boolean empty = map.isEmpty();
        map.clear();
    }
}
