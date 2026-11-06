# prefix_sums

```cpp
// C++17; half-open ranges [l,r) and [r1,r2) throughout.
struct PrefixSum {
  vector<long long> p;
  explicit PrefixSum(const vector<long long>& a) : p(a.size()+1) {
    for (int i = 0; i < (int)a.size(); ++i) p[i+1] = p[i] + a[i];
  }
  long long sum(int l, int r) const { return p[r] - p[l]; }
};

struct PrefixSum2D {
  vector<vector<long long>> p;
  explicit PrefixSum2D(const vector<vector<long long>>& a)
      : p(a.size()+1, vector<long long>(a.empty() ? 1 : a[0].size()+1)) {
    for (int i = 0; i < (int)a.size(); ++i)
      for (int j = 0; j < (int)a[i].size(); ++j)
        p[i+1][j+1] = a[i][j] + p[i][j+1] + p[i+1][j] - p[i][j];
  }
  long long sum(int r1, int c1, int r2, int c2) const {
    return p[r2][c2] - p[r1][c2] - p[r2][c1] + p[r1][c1];
  }
};
```
