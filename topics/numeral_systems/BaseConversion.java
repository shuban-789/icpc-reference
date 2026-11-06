class BaseConversion {
    static String toBase(int value, int base) {
        if (base < 2 || base > 36)
            throw new IllegalArgumentException("base");
        return Integer.toString(value, base);
    }
    static int fromBase(String text, int base) {
        return Integer.parseInt(text, base);
    }
    // Integer.toBinaryString(13) == "1101"
    // Integer.parseInt("1101", 2) == 13
    // Integer.parseInt("15", 7) == 12
    // Integer.parseInt("abc", 36) == 13368
    // Integer.toString(13368, 36).equals("abc")
    // Use Long.parseLong / Long.toString for long.
}
