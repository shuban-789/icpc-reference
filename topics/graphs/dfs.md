# dfs

```python
import sys


sys.setrecursionlimit(10**5) # Python has a default recursion limit of 1000


n=6
visited = [False] * n


"""
Define adjacency list and read in problem-specific input here.


In this example, we've provided "dummy input" that's
reflected in the GIF above to help illustrate the
order of the recursive calls.
"""
adj = [[] for _ in range(n)]
adj[0] = [1, 2, 4]
adj[1] = [3, 4]
adj[2] = [5]



def dfs(current_node):
       visited[current_node] = True
       for neighbor in adj[current_node]:
               if not visited[neighbor]:
                       dfs(neighbor)



for i in range(n):
       if not visited[i]:
               dfs(i)
```
