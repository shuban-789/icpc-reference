# binary_search

```python
def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
      mid = left + (right - left) // 2
      if arr[mid] == target:
        return mid
      elif arr[mid] < target:
        left = mid + 1
      else:
        right = mid - 1
    return -1


def binary_search_boundary(arr: list) -> int:
    def condition(value) -> bool:
      pass # Returns True/False evaluation


    left, right = 0, len(arr)
    while left < right:
      mid = left + (right - left) // 2
      if condition(mid):
        right = mid
      else:
        left = mid + 1
    return left
```
