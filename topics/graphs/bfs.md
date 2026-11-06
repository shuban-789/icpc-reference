# bfs

```python
from collections import deque


"""
Define adjacency list and read in problem-specific input


In this example, we've provided "dummy input" that's
reflected in the GIF above to help illustrate the
order of the recursive calls.
"""


n=6
adj = [[] for _ in range(n)]
visited = [False] * n


adj[0] = [1, 2, 4]
adj[1] = [3, 4]
adj[2] = [5]


for i in range(n):
         # iterate over all connected components in the graph
         if not visited[i]:
                 q = deque([i])


                 while q:
                         node = q.popleft()
                         visited[node] = True


                         for neighbor in adj[node]:
                                  if not visited[neighbor]:
                                          q.append(neighbor)
```
