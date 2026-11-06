class Bitwise {
    static boolean isEven(int x) {
        return (x & 1) == 0;
    }
    static boolean hasAll(int mask, int flags) {
        return (mask & flags) == flags;
    }
    static int[] flags(int mask, int bit) {
        int flag = 1 << bit; // 0 <= bit < 32
        return new int[]{mask | flag, // set
                         mask & ~flag, // clear
                         mask ^ flag}; // toggle
    }
    static int unique(int[] a) {
        int result = 0;
        for (int x : a) result ^= x;
        return result;
    }
    static int[] xorSwap(int x, int y) {
        x ^= y; y ^= x; x ^= y;
        return new int[]{x, y};
    }
    static int[] shifts(int x, int k) {
        // Java int shift count is k & 31.
        return new int[]{x << k, x >> k, x >>> k};
    }
    // READ=1, WRITE=2, EXECUTE=4;
    // mask = READ | WRITE; (mask & WRITE) != 0
    // 20 << 1 == 40; 20 >> 1 == 10; 20 << 2 == 80
}
