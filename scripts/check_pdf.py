#!/usr/bin/env python3
"""Enforce the page cap, landscape orientation, and resolved index links."""
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
config = json.loads((ROOT / "doc/reference.json").read_text())
limit = config["layout"]["max_pages"]
for name in ("reference", "topics"):
    pdf = ROOT / f"build/latex/{name}.pdf"
    info = subprocess.check_output(["pdfinfo", str(pdf)], text=True)
    pages = int(re.search(r"^Pages:\s+(\d+)", info, re.M)[1])
    if pages > limit:
        raise SystemExit(f"{name}.pdf: {pages} pages exceeds the {limit}-page limit")
    boxes = subprocess.check_output(["pdfinfo", "-f", "1", "-l", str(pages), str(pdf)], text=True)
    sizes = re.findall(r"size:\s+([\d.]+) x ([\d.]+) pts", boxes)
    if len(sizes) != pages or any(float(w) <= float(h) for w, h in sizes):
        raise SystemExit(f"{name}.pdf: every page must be landscape")
    log = (ROOT / f"build/latex/{name}.log").read_text()
    if any(term in log for term in ("undefined references", "Missing character:", "Overfull ")):
        raise SystemExit(f"{name}.pdf: unresolved references, missing glyphs or overflow; inspect its log")
    fonts = subprocess.check_output(["pdffonts", str(pdf)], text=True).splitlines()
    embedded_column = fonts[0].index("emb")
    if not any("Inconsolata" in line for line in fonts[2:]) or any(
            line[embedded_column:embedded_column+3] != "yes" for line in fonts[2:] if line.strip()):
        raise SystemExit(f"{name}.pdf: code font missing or fonts not embedded")
    print(f"{name}.pdf: {pages}/{limit} pages, all landscape; index resolved; fonts embedded")
