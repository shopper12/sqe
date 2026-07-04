from datetime import date
from pathlib import Path

from build_sqe1_coursebook import MODULES, RULE_BANK, ANCHORS, OUT_DIR, h


VERSION = "v0.2"
WORKBOOK_TITLE = f"SQE1 원문복제없는 문제집 {VERSION}"


def page(title, kicker, body, footer):
    return f"""
    <section class="page">
      <div class="kicker">{h(kicker)}</div>
      <h1>{h(title)}</h1>
      {body}
      <div class="footer">{h(footer)}</div>
    </section>
    """


def option_list(options):
    return "<ol type=\"A\">" + "".join(f"<li>{h(option)}</li>" for option in options) + "</ol>"


def footer(label):
    return f"SQE1 Workbook {VERSION} | {label}"


def correct_letter(index):
    return "ABCDE"[index]


def issue_question(module, rule, q_index):
    issue, core_rule, trigger, trap = rule
    correct_index = q_index % 5
    options = [
        "Take the step the client prefers because client instructions decide the answer.",
        "Choose the answer that states a broad legal principle without testing the facts.",
        "Identify the precise rule, apply it to the stated facts, and check procedure and ethics before selecting the best answer.",
        "Use the Korean-law equivalent unless the question expressly warns that England and Wales differs.",
        "Delay the answer because SQE1 questions never require practical advice.",
    ]
    correct = f"Use the clues ({trigger}) to apply this rule: {core_rule}"
    options[correct_index] = correct
    return {
        "issue": issue,
        "stem": f"A client scenario in {module['name']} contains the following clues: {trigger}. Which option is the best SQE1 method?",
        "options": options,
        "answer": correct_letter(correct_index),
        "explanation": f"The trap is: {trap} The SQE1 answer must fit the facts, the procedural or transactional stage, and any professional conduct overlay.",
    }


def long_question(module, rule, q_index):
    issue, core_rule, trigger, trap = rule
    anchors = ANCHORS.get(module["name"], [])
    anchor = anchors[q_index % len(anchors)][1] if anchors else "the SQE1 specification"
    correct_index = (q_index + 2) % 5
    stem = (
        f"A solicitor is advising a client on a matter involving {module['name']}. "
        f"The file contains a hurried email from the client, an incomplete chronology, and a document that may change the legal analysis. "
        f"The strongest clues are: {trigger}. The supervising partner asks what should be done first, bearing in mind {anchor} and the need to avoid misleading the client or another party."
    )
    options = [
        "Give the commercially attractive conclusion immediately, because speed is the main professional duty.",
        "Ignore the incomplete fact because all SQE1 questions are designed to test only black-letter recall.",
        "Identify the rule family, isolate the missing fact, then advise only on the legally available next step.",
        "Assume the authority anchor must be quoted in full to get the answer right.",
        "Choose the option that would be correct if the matter were governed by Korean law.",
    ]
    options[correct_index] = f"Apply the rule on {issue}: {core_rule} Then test whether the missing fact or ethics point changes the next step."
    return {
        "issue": issue,
        "stem": stem,
        "options": options,
        "answer": correct_letter(correct_index),
        "explanation": f"This is a longer fact-pattern drill. The correct method is to spot {issue}, resist the trap ({trap}), and choose the best legally available step.",
    }


def mock_question(module, rule, q_index):
    issue, core_rule, trigger, trap = rule
    correct_index = (q_index * 2 + len(module["name"])) % 5
    scenario_types = [
        "a client has given incomplete instructions and wants an immediate answer",
        "a supervising solicitor asks for the safest next step before a deadline",
        "two plausible options differ only because one ignores the current procedural stage",
        "the client wants to take a commercially attractive step that may create a professional conduct problem",
        "the facts include an English legal term that may be misread through Korean-law intuition",
    ]
    scenario = scenario_types[q_index % len(scenario_types)]
    stem = (
        f"In {module['name']}, {scenario}. The key clues are: {trigger}. "
        "Which option is the single best answer?"
    )
    options = [
        "Select the answer that best advances the client's commercial preference, even if a legal precondition is missing.",
        "Select the answer that identifies the relevant rule, applies it to the stated facts, and checks whether procedure or ethics changes the result.",
        "Select the answer that would be most familiar to a Korean lawyer, unless the question expressly gives a different rule.",
        "Select the answer that quotes the authority name most confidently, even if the factual trigger is absent.",
        "Select the answer that avoids giving advice because the SQE1 never tests practical judgment.",
    ]
    options[correct_index] = f"Apply the {issue} rule to the trigger facts: {core_rule}"
    return {
        "issue": f"{module['name']} - {issue}",
        "stem": stem,
        "options": options,
        "answer": correct_letter(correct_index),
        "explanation": f"Mock discipline: identify {issue}, avoid this trap ({trap}), then choose the answer available on the stated facts.",
    }


def build_mock_pool(flk, modules, target=180):
    pool = []
    serial = 1
    while len(pool) < target:
        for module in modules:
            rules = RULE_BANK.get(module["name"], [])
            for rule in rules:
                if len(pool) >= target:
                    break
                pool.append(mock_question(module, rule, serial))
                serial += 1
            if len(pool) >= target:
                break
    return pool


def render_question(q, number):
    return f"""
      <div class="question">
        <div class="q-title">Q{number}. {h(q['issue'])}</div>
        <p>{h(q['stem'])}</p>
        {option_list(q['options'])}
      </div>
    """


def render_answer(q, number):
    return f"""
      <tr>
        <td>{number}</td>
        <td>{h(q['answer'])}</td>
        <td>{h(q['issue'])}</td>
        <td>{h(q['explanation'])}</td>
      </tr>
    """


def front_pages():
    return [
        page(
            WORKBOOK_TITLE,
            "Clean-room original question bank",
            f"""
            <p class="lead">이 문제집은 공식 SQE/SRA 자료와 공개 법령·판례 출처를 기준으로 만든 original question bank입니다. 유료 교재, 유료 문제은행, 비공개 기출·복원문제를 복제하지 않았습니다.</p>
            <p>공식 sample questions는 full mock이 아니라 유형·난이도·시간 압박을 확인하는 자료입니다. 이 문제집은 그 원칙을 반영해 stem, lead-in, five options 구조로 훈련하도록 만들었습니다.</p>
            <div class="notice"><b>생성일:</b> {date.today().isoformat()} | <b>목표:</b> 2027년 1월 SQE1 대비용 original drill and mock workbook</div>
            """,
            footer("Cover"),
        ),
        page(
            "공식 통계에서 가져온 훈련 원칙",
            "Assessment intelligence",
            """
            <p class="lead">공식 SQE sample question 안내와 SQE reports 목록은 문제풀이 훈련의 방향을 정하는 데 유용합니다. 숫자는 암기할 대상이 아니라, 훈련 강도를 조절하는 기준입니다.</p>
            <ul>
              <li>각 FLK는 180개의 single best answer MCQ로 구성됩니다.</li>
              <li>각 세션은 90문항, 2시간 33분 구조이므로 평균 약 1.7분에 한 문제를 처리해야 합니다.</li>
              <li>공식 sample questions는 전체 범위를 덮는 full mock이 아니므로, 별도 문제은행과 약점 반복이 필요합니다.</li>
              <li>문항과 선택지는 sitting마다 무작위화될 수 있으므로, 번호나 순서가 아니라 rule-trigger를 기준으로 푸는 습관이 필요합니다.</li>
              <li>pass mark는 sitting별 난이도를 고려해 정해지므로, 고정 점수보다 상대적으로 안정적인 정답률을 목표로 해야 합니다.</li>
            </ul>
            <div class="takeaway"><b>훈련 기준:</b> 처음에는 정답률 55%를 넘기는 것보다 오답 원인을 R/F/E/P/ETH로 분류하는 것이 중요합니다. 이후 65%, 72%, 80% 단계로 올립니다.</div>
            """,
            footer("Official data method"),
        ),
        page(
            "오답 기록 코드",
            "Error taxonomy",
            """
            <table>
              <thead><tr><th>코드</th><th>의미</th><th>처방</th></tr></thead>
              <tbody>
                <tr><td>R</td><td>Rule gap</td><td>rule sheet로 돌아가 요건을 한 문장으로 다시 쓴다.</td></tr>
                <tr><td>F</td><td>Fact reading</td><td>stem에서 당사자, 단계, 문서, 기한, 돈을 표시한다.</td></tr>
                <tr><td>E</td><td>English/legal term</td><td>영국법 용어를 한국어 감각으로 오역했는지 확인한다.</td></tr>
                <tr><td>P</td><td>Procedure</td><td>지금 단계에서 가능한 조치인지 다시 본다.</td></tr>
                <tr><td>ETH</td><td>Ethics</td><td>SRA Principles, Code, Accounts Rules overlay를 확인한다.</td></tr>
              </tbody>
            </table>
            """,
            footer("Error taxonomy"),
        ),
    ]


def module_intro_page(module, number):
    rules = RULE_BANK.get(module["name"], [])
    body = f"""
      <p class="lead">이 장은 <b>{h(module['name'])}</b> 문제풀이 장입니다. 목표는 지식을 많이 읽는 것이 아니라, 제한시간 안에서 trigger를 보고 바로 rule을 꺼내는 것입니다.</p>
      <h2>오늘의 목표</h2>
      <ol>
        <li>핵심 쟁점 {len(rules)}개를 문제로 확인한다.</li>
        <li>짧은 issue drill과 긴 fact-pattern drill을 모두 푼다.</li>
        <li>오답을 R/F/E/P/ETH 코드로 분류한다.</li>
      </ol>
      <div class="notice">문항은 모두 새로 만든 연습문제입니다. 공식 sample question이나 유료 문제은행의 문항·선택지·해설을 복제하지 않습니다.</div>
    """
    return page(f"Workbook Chapter {number}. {module['name']}", module["flk"], body, footer(f"{module['name']} | intro"))


def module_question_pages(module, number):
    rules = RULE_BANK.get(module["name"], [])
    questions = []
    for idx, rule in enumerate(rules, start=1):
        questions.append(issue_question(module, rule, idx))
        questions.append(issue_question(module, rule, idx + len(rules)))
        questions.append(long_question(module, rule, idx))

    pages = [module_intro_page(module, number)]
    chunk_size = 3
    qnum = 1
    for chunk_index in range(0, len(questions), chunk_size):
        chunk = questions[chunk_index:chunk_index + chunk_size]
        body = "".join(render_question(q, qnum + offset) for offset, q in enumerate(chunk))
        pages.append(page(
            f"{module['name']} Questions {chunk_index + 1}-{chunk_index + len(chunk)}",
            module["flk"],
            body,
            footer(f"{module['name']} | questions"),
        ))
        qnum += len(chunk)

    rows = "".join(render_answer(q, idx) for idx, q in enumerate(questions, start=1))
    pages.append(page(
        f"{module['name']} Answer Key",
        module["flk"],
        f"""
        <p class="lead">정답표입니다. 맞힌 문제도 해설을 읽고, 왜 다른 선택지가 best answer가 아닌지 한 문장으로 말합니다.</p>
        <table>
          <thead><tr><th>No.</th><th>Ans</th><th>Issue</th><th>Teaching explanation</th></tr></thead>
          <tbody>{rows}</tbody>
        </table>
        """,
        footer(f"{module['name']} | answer key"),
    ))
    return pages, questions


def flk_mock_pages(flk, modules, all_questions):
    selected = build_mock_pool(flk, modules, target=180)
    pages = [
        page(
            f"{flk} Full Timed Mock Set",
            "Original mock",
            f"""
            <p class="lead">이 mock set은 {flk} 과목군에서 뽑은 180개 original 문제입니다. 공식 문항을 복제하지 않고, 이 문제집의 rule bank에서 재구성했습니다.</p>
            <p><b>훈련 시간:</b> 실제 구조에 맞춰 90문항 세션 2개로 풉니다. 각 세션은 2시간 33분, 평균 1.7분/문항 기준입니다.</p>
            <div class="takeaway">규칙: 1회독에서는 멈추지 말고 90문항 세션을 끝까지 풉니다. 채점 후 R/F/E/P/ETH 분포를 보고 다음 주 공부 배분을 바꿉니다.</div>
            """,
            footer(f"{flk} mock intro"),
        )
    ]
    qnum = 1
    for chunk_index in range(0, len(selected), 3):
        chunk = selected[chunk_index:chunk_index + 3]
        body = "".join(render_question(q, qnum + offset) for offset, q in enumerate(chunk))
        pages.append(page(
            f"{flk} Mock Questions {chunk_index + 1}-{chunk_index + len(chunk)}",
            flk,
            body,
            footer(f"{flk} mock questions"),
        ))
        qnum += len(chunk)
    for answer_start in range(0, len(selected), 45):
        answer_chunk = selected[answer_start:answer_start + 45]
        rows = "".join(render_answer(q, answer_start + idx) for idx, q in enumerate(answer_chunk, start=1))
        pages.append(page(
            f"{flk} Mock Answer Key {answer_start + 1}-{answer_start + len(answer_chunk)}",
            flk,
            f"""
            <table>
              <thead><tr><th>No.</th><th>Ans</th><th>Issue</th><th>Teaching explanation</th></tr></thead>
              <tbody>{rows}</tbody>
            </table>
            """,
            footer(f"{flk} mock answer key"),
        ))
    return pages


STYLE = """
@page { size: A4; margin: 14mm 15mm 15mm 15mm; }
* { box-sizing: border-box; }
body {
  margin: 0;
  background: #e9e9e9;
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
h1 { font-size: 21pt; line-height: 1.28; margin: 0 0 7mm 0; }
h2 { font-size: 13pt; margin: 5mm 0 2mm 0; }
p, li { font-size: 10.3pt; line-height: 1.58; }
.lead { font-size: 11.8pt; line-height: 1.65; }
.notice, .takeaway {
  border-left: 4px solid #263f7a;
  background: #f3f6fb;
  padding: 4mm;
  margin: 5mm 0;
}
.question {
  border: 1px solid #d2d2d2;
  padding: 3.5mm;
  margin: 0 0 4mm 0;
}
.q-title {
  font-weight: 700;
  margin-bottom: 2mm;
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
  font-size: 8.7pt;
  line-height: 1.42;
  word-break: break-word;
}
th { background: #f0f2f5; text-align: left; }
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
    all_questions = {}
    for number, module in enumerate(MODULES, start=1):
        module_pages, questions = module_question_pages(module, number)
        pages.extend(module_pages)
        all_questions[module["name"]] = questions

    flk1_modules = [module for module in MODULES if module["flk"] == "FLK1"]
    flk2_modules = [module for module in MODULES if module["flk"] == "FLK2"]
    pages.extend(flk_mock_pages("FLK1", flk1_modules, all_questions))
    pages.extend(flk_mock_pages("FLK2", flk2_modules, all_questions))

    html = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <title>{h(WORKBOOK_TITLE)}</title>
  <style>{STYLE}</style>
</head>
<body>
{''.join(pages)}
</body>
</html>
"""
    html_path = OUT_DIR / f"SQE1_원문복제없는_문제집_{VERSION}.html"
    ascii_path = OUT_DIR / "sqe1_workbook_v02.html"
    html_path.write_text(html, encoding="utf-8")
    ascii_path.write_text(html, encoding="utf-8")
    print(html_path)
    print(ascii_path)
    print(len(pages))


if __name__ == "__main__":
    build()
