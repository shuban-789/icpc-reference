# cpp_sort_lambdas

```cpp
void sort_and_lambda_calls() {
  vector<int> v{4, 1, 4, 2};
  sort(v.begin(), v.end()); // ascending; O(n log n)
  sort(v.begin(), v.end(), greater<int>()); // descending
  sort(v.rbegin(), v.rend()); // also descending
  vector<pair<int,int>> pairs{{2, 1}, {1, 3}};
  sort(pairs.begin(), pairs.end()); // lexicographic
  stable_sort(pairs.begin(), pairs.end(),
    [](const auto& a, const auto& b) {
      return a.second < b.second; // ties keep input order
    });
  sort(v.begin(), v.end());
  v.erase(unique(v.begin(), v.end()), v.end());
  auto l = lower_bound(v.begin(), v.end(), 2); // >= 2
  auto r = upper_bound(v.begin(), v.end(), 2); // > 2
  int occurrences = int(r-l), rank = int(l-v.begin());
  bool found = binary_search(v.begin(), v.end(), 2);
  // Bounds/search require matching sorted order/comparator.
  int k = 1; // require 0 <= k < size
  nth_element(v.begin(), v.begin()+k, v.end());
  int kth = v[k]; // kth smallest; sides aren't sorted
  partial_sort(v.begin(), v.begin()+k, v.end());
  // First k smallest sorted: O(n log k); nth: avg O(n).
  int delta = 3;
  auto add = [delta](int x) { return x + delta; };
  auto bump = [&delta]() { ++delta; }; bump();
  auto fib = [](auto&& self, int n) -> int {
    return n < 2 ? n : self(self,n-1)+self(self,n-2);
  }; // recursion syntax only; exponential example
  (void)occurrences; (void)rank; (void)found; (void)kth;
  (void)add; (void)fib;
}
```
