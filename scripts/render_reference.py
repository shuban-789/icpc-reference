#!/usr/bin/env python3
"""Build topic-based LaTeX/text, including a pinned KACTL source snapshot."""
import contextlib
import importlib.util
import io
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "doc"


def tex_escape(value):
    escape = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%",
              "$": r"\$", "#": r"\#", "_": r"\_", "{": r"\{",
              "}": r"\}", "~": r"\textasciitilde{}",
              "^": r"\textasciicircum{}", "<": r"\textless{}",
              ">": r"\textgreater{}"}
    return "".join(escape.get(c, c) for c in str(value))


def write_if_changed(path, text):
    if not path.exists() or path.read_text() != text:
        path.write_text(text)


class Kactl:
    def __init__(self, config):
        self.root = ROOT / config["content"]
        self.exclude = set(config["exclude"])
        self.manifest = {}
        self.cache = {}
        spec = importlib.util.spec_from_file_location(
            "kactl_preprocessor", self.root / "tex/preprocessor.py")
        self.processor = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.processor)
        self.processor.addref = lambda caption, output: None

    def snippet(self, path, options):
        relative = str(path.relative_to(self.root))
        if relative in self.exclude:
            return "", ""
        source = path.read_text()
        rendered = io.StringIO()
        lang = re.search(r"-l\s+(\w+)", options)
        lang = lang.group(1) if lang else path.suffix.lstrip(".")
        with contextlib.chdir(self.root.parent):
            if lang in {"h", "hpp", "cpp", "java", "py"}:
                listing = {"java": "Java", "py": "Python"}.get(lang, "C++")
                self.processor.processwithcomments(
                    path.name, io.StringIO(source), rendered, listing)
            else:
                listing = {"sh": "bash", "rawcpp": "C++"}.get(lang, "raw")
                self.processor.processraw(
                    path.name, io.StringIO(source), rendered, listing)
        result = rendered.getvalue()
        result = result.replace("{content/", "{../vendor/kactl/content/")
        result = result.replace("\\defdescription{\\\\", "\\defdescription{")
        # Upstream's hand-positioned figures collide with compact headings.
        result = re.sub(r"\\vspace\{-[\d.]+mm\}", "", result)
        result = re.sub(r"\\begin\{minipage\}\{(\d+mm)\}",
                        lambda m: r"\begin{minipage}[t]{" + m[1]
                        + r"}\vspace{0pt}", result)
        if path.name == "Tridiagonal.h":
            result = re.sub(r"\\\[(.*?)\\\]",
                            lambda m: r"\FitDisplay{" + m[1] + "}", result, flags=re.S)
            result = re.sub(r"\\begin\{align\*\}(.*?)\\end\{align\*\}",
                            lambda m: r"\FitDisplay{\begin{aligned}" + m[1]
                            + r"\end{aligned}}", result, flags=re.S)
        if r"\kactlerror" in result:
            raise ValueError(result)
        meta = re.search(r"\\rightcaption\{([^}]+)\}", result)
        result = re.sub(r"\\rightcaption\{[^}]+\}\n?", "", result)
        result = re.sub(r"caption=\{[^}]*\},?\s*", "", result)
        result = result.replace(",]", "]")
        head = rf"\KactlSnippet{{{tex_escape(path.name)}}}{{{tex_escape(meta.group(1) if meta else '')}}}"
        self.manifest[relative] = {"path": str(path.relative_to(ROOT)),
                                   "language": listing, "metadata": meta.group(1) if meta else ""}
        if relative == "appendix/techniques.txt":
            # Retain every checklist item, but flow related items as prose.
            groups = []
            for line in source.splitlines():
                if not line.strip():
                    continue
                if not line[0].isspace():
                    groups.append([line.strip(), []])
                else:
                    groups[-1][1].append(line.strip())
            result = "\n".join(
                r"\ReferenceFact{" + tex_escape(title) + "} "
                + tex_escape("; ".join(items)) + r"\par"
                for title, items in groups)
        return head + "\n" + result, f"KACTL: {relative}\n{source}\n"

    def chapter(self, name):
        if name in self.cache:
            return self.cache[name]
        folder = self.root / name
        text = (folder / "chapter.tex").read_text()
        text = "\n".join(line for line in text.splitlines()
                         if not line.lstrip().startswith("%"))
        text = re.sub(r"\\chapter\{[^}]+\}|\\appendix\b", "", text)
        text = re.sub(r"\\(subsubsection|subsection|section)\b",
                      lambda m: {"section": r"\subsection",
                                 "subsection": r"\subsubsection",
                                 "subsubsection": r"\paragraph"}[m[1]], text)
        text = text.replace("{content/", "{../vendor/kactl/content/")
        text = re.sub(r"\\import\{([^}]+)\}",
                      lambda m: (folder / m[1]).read_text(), text)
        plain = []
        pattern = r"\\kactlimport(?:\[([^]]*)\])?\{([^}]+)\}"
        def replace(match):
            code, raw = self.snippet(folder / match[2], match[1] or "")
            plain.append(raw)
            return code
        rendered = re.sub(pattern, replace, text)
        prose = re.sub(pattern, "", text)
        self.cache[name] = rendered, prose + "\n" + "\n".join(plain)
        return self.cache[name]


def local_block(block, languages, registered):
    tex, text = [], []
    if block.get("notes"):
        tex.append(r"\TopicNote{" + tex_escape(block["notes"]) + "}")
        text += [block["notes"], ""]
    for fact in block.get("facts", []):
        tex.append(r"\ReferenceFact{" + tex_escape(fact["title"]) + "} "
                   + fact.get("latex", tex_escape(fact["text"])) + r"\par")
        text += [fact["title"] + ": " + fact["text"], ""]
    for entry in block.get("snippets", []):
        path = Path(entry["path"])
        if path.is_absolute() or ".." in path.parts or path in registered:
            raise ValueError(f"Invalid/duplicate snippet path: {path}")
        registered.add(path)
        lang = languages[entry["language"]]
        source = (ROOT / path).read_text()
        tex += [rf"\Snippet{{{tex_escape(entry['title'])}}}{{{lang['label']}}}"
                + "{" + tex_escape(entry.get("notes", "")) + "}",
                rf"\lstinputlisting[language={{{lang['listings']}}}]{{../{path}}}"]
        text += [f"{entry['title']} [{lang['label']}]", f"File: {path}",
                 entry.get("notes", ""), source, ""]
    if "table" in block:
        table = block["table"]
        tex += [r"\smallskip\begin{tabular*}{\linewidth}{@{}l@{\extracolsep{\fill}}l@{}}\toprule",
                " & ".join(tex_escape(c) for c in table["headers"]) + r"\\\midrule"]
        rows = table.get("latex_rows", [[tex_escape(c) for c in row] for row in table["rows"]])
        if len(rows) != len(table["rows"]):
            raise ValueError("Table row counts disagree")
        tex += [" & ".join(row) + r"\\" for row in rows]
        tex += [r"\bottomrule\end{tabular*}\par"]
        text += [" | ".join(table["headers"])] + [" | ".join(row) for row in table["rows"]]
    return "\n".join(tex), "\n".join(text)


def render(data, topics, name, kactl):
    cfg = data["layout"]
    settings = {"Paper": cfg["paper"], "Orientation": cfg["orientation"],
                "Columns": cfg["columns"], "Margin": cfg["margin_mm"],
                "ColumnGap": cfg["column_gap_mm"], "BodySize": cfg["body_size_pt"],
                "BodyLeading": cfg["body_leading_pt"], "CodeSize": cfg["code_size_pt"],
                "CodeLeading": cfg["code_leading_pt"],
                "CodeEmptyLines": cfg.get("code_empty_lines", 0),
                "SheetHeader": tex_escape(cfg["header"])}
    tex = ["% Generated; edit doc/reference.json, topics/, or the language templates."]
    tex += [rf"\def\{key}{{{value}}}" for key, value in settings.items()]
    tex += [r"\input{layout.tex}", r"\begin{document}\normalsize",
            r"\begin{multicols}{\Columns}", r"\StartMenu"]
    for i, topic in enumerate(topics, 1):
        tex.append(rf"\MenuEntry{{{i}}}{{{tex_escape(topic['title'])}}}{{{topic['id']}}}")
    upstream = data["kactl"]
    url = upstream["repository"] + "/tree/" + upstream["commit"]
    tex += [r"\par\smallskip {\small Source: \href{" + url + "}{KACTL "
            + upstream["commit"][:7] + r"} + supplied team notes. "
            + r"Templates and prerequisites: Programming languages in the full reference.}\par\smallskip"]
    registered, plain = set(), [cfg["header"], ""]
    for topic in topics:
        tex.append(rf"\Topic{{{tex_escape(topic['title'])}}}{{{topic['id']}}}")
        plain += [topic["title"], "=" * len(topic["title"])]
        t, p = local_block(topic, data["languages"], registered)
        tex.append(t); plain.append(p)
        for block in topic.get("blocks", []):
            tex.append(r"\subsection{" + tex_escape(block["title"]) + "}")
            t, p = local_block(block, data["languages"], registered)
            tex.append(t); plain += [block["title"], p]
        if topic.get("kactl_chapter"):
            t, p = kactl.chapter(topic["kactl_chapter"])
            tex.append(t); plain.append(p)
    tex += [r"\end{multicols}\label{last-page}", r"\end{document}", ""]
    write_if_changed(DOC / f"{name}.tex", "\n".join(tex))
    write_if_changed(DOC / f"{name}.txt", "\n".join(plain))
    return registered


def main():
    data = json.loads((DOC / "reference.json").read_text())
    kactl = Kactl(data["kactl"])
    registered = render(data, data["topics"], "reference", kactl)
    render(data, [t for t in data["topics"] if t["id"] != "programming-languages"], "topics", kactl)
    expected = {p.relative_to(ROOT) for base in [*data["languages"], "topics"]
                for p in (ROOT / base).rglob("*") if p.suffix in {".cpp", ".hpp", ".java", ".py"}}
    if registered != expected:
        raise ValueError(f"Catalogue coverage mismatch: {registered ^ expected}")
    for lang in data["languages"]:
        files = [p for p in (ROOT / lang).rglob("*") if p.is_file()]
        if len(files) != 1:
            raise ValueError(f"{lang}/ must contain only its base template: {files}")
    write_if_changed(DOC / "kactl-manifest.json", json.dumps(kactl.manifest, indent=2) + "\n")
    print(f"Generated full/topic references: {len(registered)} team snippets, "
          f"{len(kactl.manifest)} KACTL entries, {len(data['topics'])} shared sections")


if __name__ == "__main__":
    main()
