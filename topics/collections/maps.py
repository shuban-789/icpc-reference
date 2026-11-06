def map_operations(pairs, key, value, batch):
    d = dict(pairs)
    previous = d.get(key, 0)  # default if absent
    d[key] = value           # insert / overwrite
    d.update(batch)          # merge / overwrite
    present = key in d
    for k, v in d.items():
        print(k, v)
    for k in d.keys():
        print(k)
    for v in d.values():
        print(v)
    size = len(d)
    empty = not d
    removed = d.pop(key, None)
    d.clear()
    return previous, present, size, empty, removed
