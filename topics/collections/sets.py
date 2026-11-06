def set_operations(values, x, more):
    s = set(values)          # {} is an empty dict
    s.add(x)                # duplicates have no effect
    s.update(more)          # add an iterable
    present = x in s
    s.remove(x)             # KeyError if absent
    s.discard(x)            # safe if absent
    item = s.pop() if s else None  # arbitrary item
    size = len(s)
    empty = not s
    for value in s:
        print(value)
    s.clear()
    return present, item, size, empty
