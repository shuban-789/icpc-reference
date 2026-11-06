def max_subarray_sum(a):
    # Nonempty a; subarray must also be nonempty.
    best = ending = a[0]
    for i in range(1, len(a)):
        x = a[i]
        ending = max(x, ending + x)
        best = max(best, ending)
    return best
