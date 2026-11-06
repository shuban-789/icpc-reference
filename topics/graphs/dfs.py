def dfs(adj, start, seen):
    stack = [start]
    seen[start] = True
    while stack:
        u = stack.pop()
        # Process u here.
        for v in adj[u]:
            if not seen[v]:
                seen[v] = True
                stack.append(v)


def dfs_forest(adj):
    seen = [False] * len(adj)
    for u in range(len(adj)):
        if not seen[u]:
            dfs(adj, u, seen)
    return seen
