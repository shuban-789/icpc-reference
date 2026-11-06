# Source coverage

The source PDF is retained unchanged at the repository root. Repeated demo data,
large blank areas, repeated imports in examples, and screenshot chrome have been
condensed into parameterized snippets and concise notes. All source topics are
represented; KACTL now supplies geometry, modular arithmetic and the other advanced topics.
See the KACTL integration details below.

| Supplied material | Reference destination |
| --- | --- |
| `cpp/sol.cpp`, all input/output/debug/vector helpers | `cpp/template.cpp` |
| PDF p. 1, Java and Python entry points | `java/Main.java`, `python/template.py` |
| pp. 2–3, four-neighbor flood fill | `topics/graphs/FloodFill.java` |
| p. 4, target and boundary binary search | `topics/search/binary_search.py` |
| pp. 4–5, array sort/search and matrix iteration | `topics/collections/ArraysReference.java` |
| p. 6, Kadane | `topics/dynamic_programming/kadane.py` |
| pp. 7–10, DFS in Python and Java | `topics/graphs/` |
| pp. 11–13, BFS and the ArrayDeque screenshot | `topics/graphs/`; `topics/collections/Queues.java` |
| pp. 14–16, Python set and Java HashSet | `topics/collections/` |
| pp. 17–21, dictionaries, HashMap and iteration methods | `topics/collections/` |
| pp. 21–24, queue and stack | `topics/collections/Queues.java` |
| pp. 24–25, ArrayList | `topics/collections/Lists.java` |
| pp. 25–28, Java arrays, Python lists/primitive arrays | `topics/collections/` |
| pp. 28–32, parity, flags, XOR swap, shifts, unique value | `topics/bitwise/Bitwise.java` |
| pp. 32–37, binary and general base conversion, including screenshots | `topics/numeral_systems/` |
| p. 38, image-only input-size/complexity table | Catalogue's complexity topic |

## Adaptations and corrections

- Sample globals and hardcoded graph sizes become explicit arguments. Snippets
  are independent Java classes or Python functions; the C++ starter preserves its helpers and adds KACTL macros, aliases and an explicit cassert include.
- Java's input wrapper reads tokens across lines and handles blank lines/EOF.
- DFS and flood fill use explicit stacks. These preserve reachability/region
  counts, but DFS order is not promised to match the recursive source.
- BFS marks on enqueue, preventing duplicate work on converging paths/cycles.
  Distance routines are included alongside the original forest traversal use.
- Boundary search receives a monotone predicate rather than an unfinished `pass`.
- Kadane requires a nonempty array and handles negative-only inputs. Its loop
  avoids a copied slice.
- Java array length, collection size, absent-key behavior, removal overloads and
  empty-deque behavior are stated explicitly. Stray braces and undefined names
  from the PDF's fragments are repaired.
- Python primitive arrays also support append/pop. Matrix rows are independent.
- Shift notes distinguish overflow, negative rounding and Java shift-count
  masking; the source's blanket performance claims are not repeated.
- Python general-base formatting handles zero/negative values and validates the
  radix. Java notes distinguish signed conversion from two's complement binary.
- The complexity thresholds are retained as rough guidance, with their limits
  stated. They are not guaranteed runtime bounds for a judge.

Run `make check` to compile all snippets and exercise searches, negative-only
Kadane, cycles, repeated edges, disconnected graphs, a deep chain, empty and
large flood-fill grids, collection examples, bit operations, and base conversions.

## Additional C++ and modular reference

The C++17 API examples are in `topics/collections/cpp_containers.hpp`,
`topics/strings/cpp_strings.hpp`, and `topics/search/cpp_sort_lambdas.hpp`.
The catalogue supplies their complexity, iterator, capture and comparator notes.
`topics/modular_arithmetic/modular.hpp` adds normalization, safe arithmetic,
binary exponentiation, extended-Euclidean inverses and linear congruences for a
runtime modulus. Its catalogue notes cover division, cancellation, exponent
reduction, CRT compatibility, factorial/inverse-factorial binomials and geometric
sums. `make check` executes the API examples and checks modular helpers against
brute force for small moduli and at signed 64-bit boundaries under UBSan.

## KACTL integration

The source snapshot and provenance are in [vendor/kactl/UPSTREAM.md](../vendor/kactl/UPSTREAM.md).
All 135 active non-template imports from its default chapters are included,
alongside the mathematical prose and diagrams. The original `kactl.pdf` remains
at the root. The duplicate KACTL starter is consolidated into `cpp/template.cpp`;
Java and Python starters live in `java/Main.java` and `python/template.py`.

The PDFs have twelve shared sections: Programming languages; Contest & debugging;
Mathematics; Data structures & collections; Numerical algorithms; Number theory
& modular arithmetic; Combinatorics; Graphs & grids; Geometry; Strings; Search, DP
& optimization; and Algorithm checklist. `doc/topics.pdf` omits only Programming
languages. Both PDFs include a clickable first-page section index.

The page limit is enforced for both outputs, including their index pages.
All pages are landscape. Builds fail on unresolved references, missing glyphs,
non-embedded fonts, layout overflow, or more than 25 pages. The output PDFs are
copied into `doc/` only after these checks pass.
