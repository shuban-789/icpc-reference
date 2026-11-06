def to_base(num, base):
    if not 2 <= base <= 36:
        raise ValueError("base must be in [2, 36]")
    if num == 0:
        return "0"
    sign = "-" if num < 0 else ""
    num = abs(num)
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    result = []
    while num:
        num, rem = divmod(num, base)
        result.append(digits[rem])
    return sign + "".join(reversed(result))


def from_base(text, base):
    return int(text, base)  # bases 2..36


# bin(13) == '0b1101'; format(13, 'b') == '1101'
# int('1101', 2) == 13; int('42', 5) == 22
# int('zz', 36) == 1295; to_base(1295, 36) == 'zz'
