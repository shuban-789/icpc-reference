# KACTL snapshot

- Repository: https://github.com/kth-competitive-programming/kactl
- Commit: `45ee3fa7e5263c0085e2dcee42c100eb1c30121a` (2026-11-02).
- Download: the GitHub source archive for that exact commit.
- `content/` and `README.md` are copied unchanged from that archive.
- `skip_headers.txt` is upstream's `doc/scripts/skip_headers` compile exclusion list.

The supplied `../../kactl.pdf` remains unchanged as a source reference. The new
PDFs typeset the pinned source snapshot above, using every active import in its
default chapters, including the algorithm checklist. The only excluded active
import is the duplicate C++ contest starter; its required macros/aliases are in
`../../cpp/template.cpp`. The printed KACTL import manifest is
`../../doc/kactl-manifest.json` (135 entries).

Original author, source, license, status and dependency comments are retained in
the source files. See upstream's README and each file for their license notices.
No blanket license is substituted for individual source licenses.

## Rendering adaptations

`scripts/render_reference.py` runs the upstream preprocessor before LaTeX,
retaining its printed code, dependency captions and six-character checksums.
It suppresses upstream's temporary page-header bookkeeping. LaTeX does not need
shell escape. Source code, inline notes and mathematical content remain available
in the generated text/LaTeX and in this snapshot.

The renderer uses shared topic headings; removes the cover and duplicate starter;
fixes relative paths to diagrams; aligns diagram minipages at the top without
negative offsets; and fits the tridiagonal displays to the column width. These
are presentation changes; the vendored sources remain unchanged.
The algorithm checklist is flowed as grouped prose, preserving every item in
order. Blank code lines are suppressed in the PDF to leave room for the team
API notes without decreasing the code font size; text/source copies retain them.

## Verification scope

`make check-kactl` compiles the 123 included C++ headers that upstream considers
independently compilable, using this repository's C++ starter. Seven included
fragments use upstream's documented compile exclusions: MoQueries, SolveLinear2,
NumberTheoreticTransform, ModInverse, ModSqrt, MinCostMaxFlow, and
DivideAndConquerDP. These need problem-specific choices or supporting definitions.
This check is a compilation check, not a rerun of upstream's algorithm stress tests.
