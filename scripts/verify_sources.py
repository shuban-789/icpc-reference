#!/usr/bin/env python3
"""Check that Rachel-derived local listings contain only PDF source text."""
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def compact(value):
    return re.sub(r"\s+", "", value).replace("\u200b", "").replace("\ufeff", "")


def main():
    text = subprocess.check_output(
        ["pdftotext", "-layout", str(ROOT / "RachelDu_CodeTemplatesForICPC.pdf"), "-"],
        text=True,
    )
    source = compact(text)
    data = json.loads((ROOT / "doc/reference.json").read_text())
    checked = []
    for topic in data["topics"]:
        for block in [topic, *topic.get("blocks", [])]:
            for entry in block.get("snippets", []):
                if entry.get("source") == "SHUBAN" or entry["language"] == "cpp":
                    continue
                path = ROOT / entry["path"]
                if path.suffix not in {".java", ".py"}:
                    continue
                for lineno, line in enumerate(path.read_text().splitlines(), 1):
                    if line.strip() and compact(line) not in source:
                        raise SystemExit(f"Rachel mismatch: {path}:{lineno}: {line}")
                checked.append(path)
    print(f"Rachel provenance verified: {len(set(checked))} local listings")


if __name__ == "__main__":
    main()
