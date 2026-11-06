#!/usr/bin/env python3
"""Compile included KACTL headers with the actual team template, independently."""
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    manifest = json.loads((ROOT / "doc/kactl-manifest.json").read_text())
    upstream_skips = set((ROOT / "vendor/kactl/skip_headers.txt").read_text().split())
    headers = [ROOT / entry["path"] for entry in manifest.values()
               if entry["path"].endswith(".h")]
    skipped = [p for p in headers if p.name in upstream_skips]
    headers = [p for p in headers if p.name not in upstream_skips]
    with tempfile.TemporaryDirectory(prefix="icpc-kactl-check-") as tmp:
        def check(path):
            unit = Path(tmp) / (path.parent.name + "-" + path.stem + ".cpp")
            unit.write_text(f'#include "{ROOT / "cpp/template.cpp"}"\n#include "{path}"\n')
            result = subprocess.run(["g++", "-std=c++17", "-fsyntax-only", str(unit)],
                                    text=True, capture_output=True)
            return path, result
        with ThreadPoolExecutor(max_workers=4) as pool:
            results = list(pool.map(check, headers))
    failures = [(p, r) for p, r in results if r.returncode]
    for path, result in failures:
        print(f"FAIL {path.relative_to(ROOT)}\n{result.stderr}")
    print(f"KACTL: {len(headers)-len(failures)}/{len(headers)} headers compiled with cpp/template.cpp")
    print("Upstream compile exclusions (problem-specific fragments): "
          + ", ".join(p.name for p in skipped))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
