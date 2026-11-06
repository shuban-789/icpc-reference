from array import array


def array_operations(values, rows, cols):
    a = list(values)         # dynamic, mixed types
    a.append(0)
    first = a[0]
    a[0] = 1
    removed = a.pop(0)       # shift later elements
    size = len(a)
    ints = array('i', [90, 85, 77])  # C signed ints
    grid = [[0] * cols for _ in range(rows)]
    return a, first, removed, size, ints, grid
