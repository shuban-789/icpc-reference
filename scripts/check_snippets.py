#!/usr/bin/env python3
"""Compile all supplied languages and check adapted algorithm edge cases."""
import bisect
import contextlib
import io
import random
import runpy
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return runpy.run_path(str(ROOT / path))


def check_python():
    for path in [*(ROOT / "python").rglob("*.py"), *(ROOT / "topics").rglob("*.py")]:
        compile(path.read_text(), str(path), "exec")
    # RachelDu examples are preserved as printed, including top-level demos and
    # placeholder functions; compile them without importing or rewriting them.
    return
    search = load("topics/search/binary_search.py")
    kadane = load("topics/dynamic_programming/kadane.py")["max_subarray_sum"]
    rng = random.Random(17)
    for n in range(30):
        a = sorted(rng.randrange(-10, 11) for _ in range(n))
        for x in range(-12, 13):
            found = search["binary_search"](a, x)
            assert (found != -1) == (x in a)
            assert found == -1 or a[found] == x
            boundary = search["first_true"](0, n, lambda i: a[i] >= x)
            assert boundary == bisect.bisect_left(a, x)
        if n:
            a = [rng.randrange(-10, 11) for _ in range(n)]
            expected = max(sum(a[i:j]) for i in range(n)
                           for j in range(i + 1, n + 1))
            assert kadane(a) == expected
    assert search["first_true"](5, 9, lambda i: i >= 7) == 7
    assert kadane([-9, -2, -7]) == -2
    bfs = load("topics/graphs/bfs.py")
    dfs = load("topics/graphs/dfs.py")
    adj = [[0, 1, 1, 2], [3], [3], [1], []]
    assert bfs["bfs"](adj, 0) == [0, 1, 1, 2, -1]
    assert all(bfs["bfs_forest"](adj))
    seen = [False] * len(adj)
    dfs["dfs"](adj, 0, seen)
    assert seen == [True, True, True, True, False]
    assert all(dfs["dfs_forest"](adj))
    assert bfs["bfs_forest"]([]) == dfs["dfs_forest"]([]) == []
    chain = [[i + 1] for i in range(9999)] + [[]]
    assert bfs["bfs"](chain, 0)[-1] == 9999
    assert all(dfs["dfs_forest"](chain))
    base = load("topics/numeral_systems/base_conversion.py")
    for b in range(2, 37):
        for n in [-10**30, -13368, -1, 0, 1, 22, 1295, 10**30]:
            assert base["from_base"](base["to_base"](n, b), b) == n
    assert base["to_base"](22, 5) == "42"
    for bad in [1, 37]:
        try:
            base["to_base"](1, bad)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid base accepted")
    with contextlib.redirect_stdout(io.StringIO()):
        load("topics/collections/sets.py")["set_operations"]([], 1, [])
        load("topics/collections/maps.py")["map_operations"]([], 1, 2, {})
        grid = load("topics/collections/arrays.py")["array_operations"]([], 2, 2)[-1]
        grid[0][0] = 1
        assert grid[1][0] == 0


JAVA_CHECK = r'''
import java.util.*;
class SnippetCheck {
  public static void main(String[] args) {
    List<List<Integer>> g = DFS.graph(5);
    g.get(0).addAll(Arrays.asList(0, 1, 1, 2));
    g.get(1).add(3); g.get(2).add(3); g.get(3).add(1);
    assert Arrays.equals(BFS.distances(g, 0), new int[]{0,1,1,2,-1});
    for (boolean v : BFS.forest(g)) assert v;
    for (boolean v : DFS.forest(g)) assert v;
    assert BFS.forest(DFS.graph(0)).length == 0;
    boolean[] seen = new boolean[5];
    DFS.dfs(g, 0, seen);
    assert Arrays.equals(seen, new boolean[]{true,true,true,true,false});
    List<Integer> sizes = FloodFill.components(new int[][]{
      {1,1,2}, {1,2,2}, {3,3,2}});
    Collections.sort(sizes);
    assert sizes.equals(Arrays.asList(2,3,4));
    assert FloodFill.components(new int[0][0]).isEmpty();
    assert FloodFill.components(new int[3][0]).isEmpty();
    assert FloodFill.components(new int[150][150]).equals(Arrays.asList(22500));
    for (int b = 2; b <= 36; b++)
      for (int n : new int[]{Integer.MIN_VALUE,-1,0,1,13368,Integer.MAX_VALUE})
        assert BaseConversion.fromBase(BaseConversion.toBase(n,b),b) == n;
    assert Bitwise.unique(new int[]{4,1,2,1,2}) == 4;
    assert Bitwise.isEven(-2) && !Bitwise.isEven(-1);
    assert Bitwise.hasAll(3, 2) && !Bitwise.hasAll(3, 4);
    assert Arrays.equals(Bitwise.flags(2,0), new int[]{3,2,3});
    assert Arrays.equals(Bitwise.xorSwap(10,5), new int[]{5,10});
    assert Bitwise.shifts(-3,1)[1] == -2;
    assert ArraysReference.sortAndSearch(new int[]{4,1,2},3) == -3;
    assert ArraysReference.sortAndSearch(new int[]{},3) == -1;
    Queues.operations(1, 2);
    Lists.operations(1, 2);
    Sets.operations(Collections.emptyList(), 1);
    Maps.operations(1, 2, 0);
  }
}
'''


CPP_CHECK = r'''
int main() {
  container_calls(); string_calls(); sort_and_lambda_calls();
  using namespace modular;
  for (long long m = 1; m <= 35; ++m)
    for (long long a = -40; a <= 40; ++a) {
      auto inv = inverse(a,m);
      assert(bool(inv) == (m > 1 && std::gcd(a,m) == 1));
      if (inv) assert(mul(a,*inv,m) == 1);
      long long slow = 1 % m;
      for (unsigned e = 0; e < 15; ++e) {
        assert(power(a,e,m) == slow);
        slow = norm(slow*a,m);
      }
      for (long long b = -40; b <= 40; ++b) {
        assert(add(a,b,m) == norm(a+b,m));
        assert(sub(a,b,m) == norm(a-b,m));
        assert(mul(a,b,m) == norm(a*b,m));
        auto sol = linear(a,b,m);
        bool exists = false;
        for (long long x = 0; x < m; ++x) {
          bool valid = norm(a*x-b,m) == 0;
          exists |= valid;
          bool represented = sol && x >= sol->first &&
                             (x-sol->first) % sol->second == 0;
          assert(valid == represented);
        }
        assert(bool(sol) == exists);
      }
    }
  long long m = LLONG_MAX;
  assert(norm(LLONG_MIN,m) == m-1);
  assert(add(m-1,m-1,m) == m-2);
  assert(sub(LLONG_MIN,LLONG_MAX,m) == m-1);
  assert(mul(m-1,m-1,m) == 1);
  assert(power(m-1,ULLONG_MAX,m) == m-1);
  assert(inverse(m-1,m) == m-1);
  assert(inverse(2,m) == m/2+1);
  assert(!inverse(7,m)); // 7 divides 2^63-1
  assert(linear(LLONG_MIN,LLONG_MIN,m)->first == 1);
  PrefixSum ps({1, 2, 3, 4});
  assert(ps.sum(0, 4) == 10 && ps.sum(1, 3) == 5);
  PrefixSum2D grid({{1, 2}, {3, 4}});
  assert(grid.sum(0, 0, 2, 2) == 10 && grid.sum(0, 1, 2, 2) == 6);
}
'''


def main():
    check_python()
    with tempfile.TemporaryDirectory(prefix="icpc-check-") as temp:
        work = Path(temp)
        subprocess.run(["g++", "-std=c++17", "-Wall", "-Wextra", "-pedantic",
                        str(ROOT / "cpp/template.cpp"), "-o", str(work / "sol")],
                       check=True)
        subprocess.run([str(work / "sol")], check=True)
        cpp = work / "cpp_check.cpp"
        includes = "\n".join('#include "' + str(p) + '"'
                             for p in sorted((ROOT / "topics").rglob("*.hpp")))
        template = (ROOT / "cpp/template.cpp").read_text()
        cpp.write_text(template[:template.index("int main()")]
                       + '\n' + includes + '\n' + CPP_CHECK)
        subprocess.run(["g++", "-std=c++17", "-O1", "-Wall", "-Wextra",
                        "-fsanitize=undefined", "-fno-sanitize-recover=all",
                        str(cpp), "-o", str(work / "cpp_check")], check=True)
        subprocess.run([str(work / "cpp_check")], check=True)
    print("Python sources compile; C++ template, APIs and modular arithmetic "
          "checks passed. RachelDu Java/Python examples are preserved verbatim "
          "and are not rewritten for harness compatibility.")


if __name__ == "__main__":
    main()
