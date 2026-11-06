# base_conversion

```python
# ==========================================


# 1. BASE 10 ---> BASE 2 (Decimal to Binary)


# ==========================================


decimal_num = 13


# Built-in method: bin()


# Note: This returns a string starting with '0b' (e.g., '0b1101')


binary_str_with_prefix = bin(decimal_num)


# Clean string without the '0b' prefix


binary_str = format(decimal_num, 'b')


print(f"Decimal 13 to Binary: {binary_str}") # Output: "1101"


# ==========================================


# 2. BASE 2 ---> BASE 10 (Binary to Decimal)


# ==========================================


binary_input = "1101"


# Built-in method: int(string, base)


decimal_output = int(binary_input, 2)


print(f"Binary 1101 to Decimal: {decimal_output}") # Output: 13
```
