from __future__ import annotations

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"

SOURCES = {
    "sqe1_coursebook_v04.html": ROOT / "textbooks" / "SQE1_THEORY_TEXTBOOK.md",
    "sqe1_workbook_v02.html": ROOT / "question_banks" / "SQE1_PRACTICE_QUESTION_BANK.md",
    "sqe1_issue_atlas_v01.html": ROOT / "SQE1_dashboard.md",
}


def markdown_to_simple_html(text: str, title: str) -> str:
    lines = []
    in_list = False
    in_code = False
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            if in_code:
                lines.append("</pre>")
                in_code = False
            else:
                lines.append("<pre>")
                in_code = True
            continue
        if in_code:
            lines.append(escape(line))
            continue
        if line.startswith("# "):
            if in_list:
                lines.append("</ul>")
                in_list = False
            lines.append(f"<h1>{escape(line[2:])}</h1>")
        elif line.startswith("## "):
            if in_list:
                lines.append("</ul>")
                in_list = False
            lines.append(f"<h2>{escape(line[3:])}</h2>")
        elif line.startswith("### "):
            if in_list:
                lines.append("</ul>")
                in_list = False
            lines.append(f"<h3>{escape(line[4:])}</h3>")
        elif line.startswith("- "):
            if not in_list:
                lines.append("<ul>")
                in_list = True
            lines.append(f"<li>{escape(line[2:])}</li>")
        elif line.strip() == "":
            if in_list:
                lines.append("</ul>")
                in_list = False
        else:
            if in_list:
                lines.append("</ul>")
                in_list = False
            lines.append(f"<p>{escape(line)}</p>")
    if in_list:
        lines.append("</ul>")
    if in_code:
        lines.append("</pre>")
    body = "\n".join(lines)
    return f"<!doctype html>\n<html><head><meta charset='utf-8'><title>{escape(title)}</title></head><body>\n{body}\n</body></html>\n"


def build_one(output_name: str) -> None:
    src = SOURCES[output_name]
    text = src.read_text(encoding="utf-8")
    html = markdown_to_simple_html(text, output_name)
    OUTPUT.mkdir(exist_ok=True)
    (OUTPUT / output_name).write_text(html, encoding="utf-8")


def main() -> None:
    for output_name in SOURCES:
        build_one(output_name)
    print(f"Built {len(SOURCES)} HTML files in {OUTPUT}")


if __name__ == "__main__":
    main()
