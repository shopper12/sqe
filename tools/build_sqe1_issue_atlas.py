from datetime import date
from html import unescape
import re
import unicodedata

from build_sqe1_coursebook import (
    ANCHORS,
    MODULES,
    OUT_DIR,
    RULE_BANK,
    SOURCE_URLS,
    anchor_source_url,
    h,
)


VERSION = "v0.1"
TITLE = f"SQE1 과목별 쟁점 총망라 지도 {VERSION}"


def page(title, kicker, body, footer):
    return f"""
    <section class="page">
      <div class="kicker">{h(kicker)}</div>
      <h1>{h(title)}</h1>
      {body}
      <div class="footer">{h(footer)}</div>
    </section>
    """


def footer(label):
    return f"SQE1 Issue Atlas {VERSION} | {label}"


def source_link(name):
    return SOURCE_URLS.get(name, "")


def front_pages():
    source_rows = [
        ("SQE1 specification", source_link("SQE1 Assessment Specification"), "출제 범위, closed book, functioning legal knowledge 기준"),
        ("Single best answer", source_link("SQE1 single best answer questions"), "stem, lead-in, five plausible options 구조"),
        ("Sample questions", source_link("SQE1 sample questions"), "문항 길이, 난이도, 시간 압박 감각"),
        ("SQE reports", "https://sqe.sra.org.uk/sqe-results/reports", "sitting별 통계와 준비 강도 판단"),
        ("SRA Standards", "https://www.sra.org.uk/solicitors/standards-regulations/", "윤리와 professional conduct overlay"),
    ]
    rows = "".join(f"<tr><td>{h(a)}</td><td><span>{h(b)}</span></td><td>{h(c)}</td></tr>" for a, b, c in source_rows)
    return [
        page(
            TITLE,
            "Clean-room revision atlas",
            f"""
            <p class="lead">이 자료는 교재와 문제집을 연결하는 회독용 쟁점 지도입니다. 유료 교재, 유료 문제은행, 비공개 기출·복원문제를 복제하지 않고, 공식 SQE/SRA 자료와 공개 법령·판례 앵커를 기준으로 직접 구성했습니다.</p>
            <p>목표는 과목별로 “trigger word → rule family → trap → answer discipline”을 빠르게 반복하는 것입니다. 긴 설명은 교재에서 읽고, 이 지도는 시험 직전과 오답 직후에 씁니다.</p>
            <div class="notice"><b>생성일:</b> {date.today().isoformat()} | <b>사용 시점:</b> 2회독 이후, mock 오답 복습, 시험 전 30일</div>
            """,
            footer("Cover"),
        ),
        page(
            "공식 출처 사용 방식",
            "Source method",
            f"""
            <p class="lead">이 지도는 원문을 길게 옮기는 자료가 아니라, 공식 기준과 공개 원자료를 어디에 연결해야 하는지 보여주는 색인입니다.</p>
            <table>
              <thead><tr><th>출처</th><th>URL</th><th>이 지도에서의 역할</th></tr></thead>
              <tbody>{rows}</tbody>
            </table>
            <div class="takeaway">SQE reports와 sample questions는 문항 복원이나 유출 추정에 쓰지 않습니다. 오직 시간 압박, 난이도, 준비 강도, 훈련 방식 판단에만 씁니다.</div>
            """,
            footer("Source method"),
        ),
        page(
            "7회독 사용법",
            "Revision loop",
            """
            <ol>
              <li>1회독: 과목별 dashboard에서 전체 쟁점 이름만 소리 내어 읽습니다.</li>
              <li>2회독: trigger map을 보며 어떤 단어가 어떤 rule을 여는지 표시합니다.</li>
              <li>3회독: trap column만 가리고 스스로 함정을 말합니다.</li>
              <li>4회독: 한국변호사 주의점을 읽고 한국법식 직관을 제거합니다.</li>
              <li>5회독: issue card를 보며 30초 안에 “rule → next step”을 말합니다.</li>
              <li>6회독: 문제집 오답과 R/F/E/P/ETH 코드를 연결합니다.</li>
              <li>7회독: last-day checklist만 보고 빈칸 없이 설명합니다.</li>
            </ol>
            <div class="notice">이 지도는 외우는 순서를 정해주는 자료입니다. 모르는 부분을 발견하면 교재 v0.4의 해당 과목 rule sheet와 문제집 v0.2의 해당 mock 문제로 돌아갑니다.</div>
            """,
            footer("Revision loop"),
        ),
    ]


def module_dashboard(module, number):
    rules = RULE_BANK.get(module["name"], [])
    anchors = ANCHORS.get(module["name"], [])
    anchor_list = "".join(f"<li>{h(title)} <span>({h(kind)})</span></li>" for kind, title, _ in anchors)
    issue_list = "".join(f"<li>{h(issue)}</li>" for issue, *_ in rules)
    body = f"""
      <p class="lead"><b>{h(module['name'])}</b>의 쟁점 대시보드입니다. 이 장의 목적은 모든 세부 설명을 다시 읽는 것이 아니라, 시험장에서 어떤 rule family를 먼저 꺼낼지 즉시 정하는 것입니다.</p>
      <h2>핵심 쟁점</h2>
      <ol>{issue_list}</ol>
      <h2>공개 권위자료 앵커</h2>
      <ul>{anchor_list}</ul>
      <h2>강사식 한 줄 전략</h2>
      <p>{h(module['exam_method'])}</p>
    """
    return page(f"{number}. {module['name']} Dashboard", module["flk"], body, footer(f"{module['name']} | dashboard"))


def rule_grid_page(module):
    rows = []
    for issue, core_rule, trigger, trap in RULE_BANK.get(module["name"], []):
        rows.append(
            f"<tr><td><b>{h(issue)}</b></td><td>{h(core_rule)}</td><td>{h(trigger)}</td><td>{h(trap)}</td></tr>"
        )
    body = f"""
      <p class="lead">이 표는 쟁점 이름, 핵심 법리, 문제 단서, 오답 함정을 한 줄로 묶은 final grid입니다.</p>
      <table>
        <thead><tr><th>쟁점</th><th>핵심 법리</th><th>Trigger</th><th>Trap</th></tr></thead>
        <tbody>{''.join(rows)}</tbody>
      </table>
    """
    return page(f"{module['name']} Final Rule Grid", module["flk"], body, footer(f"{module['name']} | final grid"))


def trigger_map_page(module):
    rows = []
    for issue, core_rule, trigger, trap in RULE_BANK.get(module["name"], []):
        trigger_bits = [bit.strip() for bit in trigger.split(",")]
        for bit in trigger_bits:
            rows.append(
                f"<tr><td>{h(bit)}</td><td>{h(issue)}</td><td>{h(core_rule)}</td><td>{h(trap)}</td></tr>"
            )
    body = f"""
      <p class="lead">Trigger map입니다. 문제를 읽을 때 아래 단어가 보이면 바로 오른쪽 쟁점으로 연결합니다.</p>
      <table>
        <thead><tr><th>보이는 단어</th><th>열리는 쟁점</th><th>먼저 꺼낼 rule</th><th>주의할 함정</th></tr></thead>
        <tbody>{''.join(rows)}</tbody>
      </table>
    """
    return page(f"{module['name']} Trigger Map", module["flk"], body, footer(f"{module['name']} | trigger map"))


def korean_law_pitfall_page(module):
    rules = RULE_BANK.get(module["name"], [])
    rows = []
    for issue, core_rule, trigger, trap in rules:
        rows.append(
            f"<tr><td>{h(issue)}</td><td>{h(module['korean_note'])}</td><td>{h(trap)}</td></tr>"
        )
    body = f"""
      <p class="lead">한국변호사 관점의 함정 정리입니다. 익숙한 개념일수록 더 위험합니다. 같은 단어가 같은 요건을 뜻하지 않을 수 있습니다.</p>
      <table>
        <thead><tr><th>쟁점</th><th>한국변호사 주의점</th><th>SQE식 함정</th></tr></thead>
        <tbody>{''.join(rows)}</tbody>
      </table>
    """
    return page(f"{module['name']} Korean-Law Pitfalls", module["flk"], body, footer(f"{module['name']} | Korean-law pitfalls"))


def source_anchor_page(module):
    rows = []
    for kind, title, point in ANCHORS.get(module["name"], []):
        url = anchor_source_url(kind, title)
        rows.append(f"<tr><td>{h(kind)}</td><td><b>{h(title)}</b></td><td>{h(point)}</td><td><span>{h(url)}</span></td></tr>")
    body = f"""
      <p class="lead">공개 권위자료 색인입니다. 판례명과 법령명은 긴 인용용이 아니라, rule family를 여는 표지판입니다.</p>
      <table>
        <thead><tr><th>구분</th><th>앵커</th><th>시험상 기능</th><th>확인처</th></tr></thead>
        <tbody>{''.join(rows)}</tbody>
      </table>
    """
    return page(f"{module['name']} Source Anchors", module["flk"], body, footer(f"{module['name']} | source anchors"))


def issue_cards(module):
    pages = []
    rules = RULE_BANK.get(module["name"], [])
    for idx in range(0, len(rules), 2):
        cards = []
        for issue, core_rule, trigger, trap in rules[idx:idx + 2]:
            cards.append(f"""
            <div class="card">
              <h2>{h(issue)}</h2>
              <p><b>Rule:</b> {h(core_rule)}</p>
              <p><b>Trigger:</b> {h(trigger)}</p>
              <p><b>Trap:</b> {h(trap)}</p>
              <p><b>30초 말하기:</b> 이 쟁점은 어떤 사실에서 시작하고, 지금 단계에서 어떤 답을 허용하는가?</p>
            </div>
            """)
        pages.append(page(
            f"{module['name']} Issue Cards {idx + 1}-{idx + len(rules[idx:idx + 2])}",
            module["flk"],
            "".join(cards),
            footer(f"{module['name']} | issue cards"),
        ))
    return pages


def last_day_checklist_page(module):
    topic_rows = "".join(f"<tr><td>{i}</td><td>{h(topic)}</td><td>□ rule □ trigger □ trap □ ethics/procedure</td></tr>" for i, topic in enumerate(module["topics"], start=1))
    body = f"""
      <p class="lead">시험 전날 체크리스트입니다. 체크가 비면 교재로 돌아가지 말고 먼저 issue atlas의 rule grid와 문제집 오답표를 봅니다.</p>
      <table>
        <thead><tr><th>No.</th><th>세부 주제</th><th>체크</th></tr></thead>
        <tbody>{topic_rows}</tbody>
      </table>
      <div class="takeaway"><b>마지막 질문:</b> {h(module['exam_method'])}</div>
    """
    return page(f"{module['name']} Last-Day Checklist", module["flk"], body, footer(f"{module['name']} | last-day checklist"))


def flk_overview_page(flk):
    modules = [module for module in MODULES if module["flk"] == flk]
    rows = []
    for module in modules:
        rows.append(
            f"<tr><td>{h(module['name'])}</td><td>{len(RULE_BANK.get(module['name'], []))}</td><td>{len(module['topics'])}</td><td>{h(module['exam_method'])}</td></tr>"
        )
    body = f"""
      <p class="lead">{flk} 전체 회독표입니다. 과목을 따로 보되, 실제 문제에서는 절차·윤리·실체법이 섞일 수 있다는 점을 계속 기억합니다.</p>
      <table>
        <thead><tr><th>과목</th><th>핵심 쟁점 수</th><th>세부 주제 수</th><th>풀이 전략</th></tr></thead>
        <tbody>{''.join(rows)}</tbody>
      </table>
    """
    return page(f"{flk} Overview", flk, body, footer(f"{flk} overview"))


def display_width(text):
    width = 0
    for ch in text:
        width += 2 if unicodedata.east_asian_width(ch) in {"W", "F"} else 1
    return width


def wrap_text(text, max_width=78):
    words = text.split()
    if not words:
        return [""]
    lines = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if display_width(candidate) <= max_width:
            current = candidate
            continue
        if current:
            lines.append(current)
        if display_width(word) <= max_width:
            current = word
            continue
        chunk = ""
        for ch in word:
            candidate = chunk + ch
            if display_width(candidate) > max_width:
                lines.append(chunk)
                chunk = ch
            else:
                chunk = candidate
        current = chunk
    if current:
        lines.append(current)
    return lines


def section_texts_from_html(html):
    sections = re.findall(r'<section class="page">(.*?)</section>', html, flags=re.S)
    texts = []
    for section in sections:
        section = re.sub(r"</(h1|h2|p|li|tr)>", "\n", section)
        section = re.sub(r"<br\s*/?>", "\n", section)
        section = re.sub(r"<[^>]+>", " ", section)
        section = unescape(section)
        lines = [re.sub(r"\s+", " ", line).strip() for line in section.splitlines()]
        texts.append([line for line in lines if line])
    return texts


def pdf_hex(text):
    return text.encode("utf-16-be").hex().upper()


def make_content_stream(lines):
    commands = []
    y = 805
    for raw in lines:
        if not raw:
            y -= 12
            continue
        size = 14 if y == 805 else 9.8
        leading = 17 if size >= 14 else 13.5
        for line in wrap_text(raw, 84):
            if y < 48:
                break
            commands.append(f"BT /F1 {size:.1f} Tf 42 {y:.1f} Td <{pdf_hex(line)}> Tj ET")
            y -= leading
    return ("\n".join(commands) + "\n").encode("ascii")


def build_pdf_from_sections(sections, pdf_path):
    page_line_limit = 54
    pdf_pages = []
    for section in sections:
        expanded = []
        for item in section:
            expanded.extend(wrap_text(item, 84))
            expanded.append("")
        for start in range(0, max(1, len(expanded)), page_line_limit):
            pdf_pages.append(expanded[start:start + page_line_limit])

    objects = []

    def add_object(data):
        objects.append(data)
        return len(objects)

    catalog_id = add_object(b"<< /Type /Catalog /Pages 2 0 R >>")
    pages_id = add_object(b"")
    font_descriptor_id = add_object(
        b"<< /Type /FontDescriptor /FontName /HYSMyeongJo-Medium /Flags 6 "
        b"/FontBBox [0 -148 1000 880] /ItalicAngle 0 /Ascent 880 /Descent -148 "
        b"/CapHeight 880 /StemV 80 >>"
    )
    cid_font_id = add_object(
        f"<< /Type /Font /Subtype /CIDFontType0 /BaseFont /HYSMyeongJo-Medium "
        f"/CIDSystemInfo << /Registry (Adobe) /Ordering (Korea1) /Supplement 2 >> "
        f"/FontDescriptor {font_descriptor_id} 0 R >>".encode("ascii")
    )
    font_id = add_object(
        f"<< /Type /Font /Subtype /Type0 /BaseFont /HYSMyeongJo-Medium "
        f"/Encoding /UniKS-UCS2-H /DescendantFonts [{cid_font_id} 0 R] >>".encode("ascii")
    )

    page_ids = []
    for lines in pdf_pages:
        stream = make_content_stream(lines)
        content_id = add_object(b"<< /Length " + str(len(stream)).encode("ascii") + b" >>\nstream\n" + stream + b"endstream")
        page_id = add_object(
            f"<< /Type /Page /Parent {pages_id} 0 R /MediaBox [0 0 595 842] "
            f"/Resources << /Font << /F1 {font_id} 0 R >> >> /Contents {content_id} 0 R >>".encode("ascii")
        )
        page_ids.append(page_id)

    kids = " ".join(f"{pid} 0 R" for pid in page_ids)
    objects[pages_id - 1] = f"<< /Type /Pages /Kids [{kids}] /Count {len(page_ids)} >>".encode("ascii")

    output = bytearray(b"%PDF-1.4\n%\xE2\xE3\xCF\xD3\n")
    offsets = [0]
    for i, obj in enumerate(objects, start=1):
        offsets.append(len(output))
        output.extend(f"{i} 0 obj\n".encode("ascii"))
        output.extend(obj)
        output.extend(b"\nendobj\n")
    xref_offset = len(output)
    output.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    output.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        output.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    output.extend(
        f"trailer\n<< /Size {len(objects) + 1} /Root {catalog_id} 0 R >>\n"
        f"startxref\n{xref_offset}\n%%EOF\n".encode("ascii")
    )
    pdf_path.write_bytes(output)
    return len(page_ids)


STYLE = """
@page { size: A4; margin: 14mm 15mm 15mm 15mm; }
* { box-sizing: border-box; }
body {
  margin: 0;
  background: #e8e8e8;
  font-family: "Malgun Gothic", "Noto Sans KR", Arial, sans-serif;
  color: #171717;
}
.page {
  width: 210mm;
  min-height: 297mm;
  padding: 17mm 18mm 16mm 18mm;
  margin: 0 auto 8mm auto;
  background: white;
  page-break-after: always;
  position: relative;
}
.kicker {
  text-transform: uppercase;
  letter-spacing: 0;
  font-size: 10pt;
  color: #555;
  border-bottom: 1px solid #222;
  padding-bottom: 4mm;
  margin-bottom: 7mm;
}
h1 { font-size: 20pt; line-height: 1.28; margin: 0 0 7mm 0; }
h2 { font-size: 13pt; margin: 4mm 0 2mm 0; }
p, li { font-size: 10.2pt; line-height: 1.58; }
.lead { font-size: 11.8pt; line-height: 1.65; }
.notice, .takeaway {
  border-left: 4px solid #263f7a;
  background: #f3f6fb;
  padding: 4mm;
  margin: 5mm 0;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin: 4mm 0;
  table-layout: fixed;
}
th, td {
  border: 1px solid #d6d6d6;
  padding: 2.2mm;
  vertical-align: top;
  font-size: 8.6pt;
  line-height: 1.42;
  word-break: break-word;
}
th { background: #f0f2f5; text-align: left; }
td span { color: #4a4a4a; font-size: 8pt; }
.card {
  border: 1px solid #d2d2d2;
  padding: 4mm;
  margin: 0 0 5mm 0;
  min-height: 105mm;
}
.footer {
  position: absolute;
  left: 18mm;
  right: 18mm;
  bottom: 8mm;
  border-top: 1px solid #ddd;
  padding-top: 3mm;
  font-size: 8.5pt;
  color: #666;
}
@media print {
  body { background: white; }
  .page { margin: 0; width: auto; min-height: auto; }
}
"""


def build():
    pages = front_pages()
    pages.append(flk_overview_page("FLK1"))
    pages.append(flk_overview_page("FLK2"))
    for number, module in enumerate(MODULES, start=1):
        pages.append(module_dashboard(module, number))
        pages.append(rule_grid_page(module))
        pages.append(trigger_map_page(module))
        pages.append(korean_law_pitfall_page(module))
        pages.append(source_anchor_page(module))
        pages.extend(issue_cards(module))
        pages.append(last_day_checklist_page(module))

    html = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <title>{h(TITLE)}</title>
  <style>{STYLE}</style>
</head>
<body>
{''.join(pages)}
</body>
</html>
"""
    html_path = OUT_DIR / f"SQE1_과목별_쟁점_총망라_지도_{VERSION}.html"
    ascii_path = OUT_DIR / "sqe1_issue_atlas_v01.html"
    pdf_path = OUT_DIR / f"SQE1_과목별_쟁점_총망라_지도_{VERSION}.pdf"
    html_path.write_text(html, encoding="utf-8")
    ascii_path.write_text(html, encoding="utf-8")
    pdf_pages = build_pdf_from_sections(section_texts_from_html(html), pdf_path)
    print(html_path)
    print(ascii_path)
    print(pdf_path)
    print(len(pages))
    print(pdf_pages)


if __name__ == "__main__":
    build()
