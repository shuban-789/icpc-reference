from collections import deque


def bfs(adj, start):
    dist = [-1] * len(adj)
    dist[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


def bfs_forest(adj):
    seen = [False] * len(adj)
    for start in range(len(adj)):
        if seen[start]:
            continue
        seen[start] = True
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    q.append(v)
    return seen
