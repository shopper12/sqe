# SQE1 Project Cloud Conversation

Updated: 2026-07-04

This file is the portable continuation context for the SQE1 January 2027 project. It is not a verbatim export of the private chat transcript; the local environment does not expose a raw transcript export. It is a working cloud snapshot containing the user's goal, decisions made, files produced, and exact next steps so the project can be resumed from another computer.

## User Goal

The user is a Korean attorney preparing for SQE1 in early 2027 and intends to request SQE2 exemption. The requested end state is a comprehensive SQE1 study system with subject-by-subject lecture-style theory materials, question books, schedule monitoring, and daily study operation.

Important legal boundary established during the conversation:

- Do not copy, reproduce, scrape, or transform paid textbooks, paid question banks, private courses, leaked exams, or reconstructed questions.
- Use official SQE/SRA sources, public legislation, public case-law indexes, and clean-room original explanations/questions.
- All questions generated in this workspace are original training questions, not copied official or commercial questions.

## Current Official Dates and Exam Context

Confirmed from official SQE pages during the work:

- Target sitting: SQE1 January 2027.
- FLK1: 2027-01-11 to 2027-01-15.
- FLK2: 2027-01-18 to 2027-01-22.
- Examinable law and practice cut-off: 2026-09-11.
- Booking opening/closing/results: TBC at the time checked.
- SQE1 uses single best answer MCQs.
- Each FLK has 180 questions; two sessions of 90 questions, 2 hours 33 minutes each.

Primary official/public sources:

- SQE assessment dates and booking windows: https://sqe.sra.org.uk/booking/assessment-dates-locations/booking-windows
- SQE assessment topics: https://sqe.sra.org.uk/about/sqe-assessment-topics
- SQE1 Assessment Specification: https://sqe.sra.org.uk/assessments/sqe1-assessments/sqe1-specification
- SQE1 single best answer questions: https://sqe.sra.org.uk/assessments/sqe1-assessments/sqe1-single-best-answer
- SQE1 sample questions: https://sqe.sra.org.uk/assessments/sqe1-assessments/sqe1-sample-questions
- SQE reports: https://sqe.sra.org.uk/sqe-results/reports
- SRA Standards and Regulations: https://www.sra.org.uk/solicitors/standards-regulations/
- SRA SQE exemptions: https://www.sra.org.uk/become-solicitor/qualified-lawyers/sqe-exemptions/
- legislation.gov.uk: https://www.legislation.gov.uk/
- Civil Procedure Rules: https://www.justice.gov.uk/courts/procedure-rules/civil
- Criminal Procedure Rules: https://www.gov.uk/guidance/rules-and-practice-directions-2020
- PACE Codes: https://www.gov.uk/guidance/police-and-criminal-evidence-act-1984-pace-codes-of-practice
- Supreme Court judgments: https://www.supremecourt.uk/decided-cases/
- BAILII public judgments: https://www.bailii.org/

## Generated Local Artifacts

The workspace contains these main generated artifacts:

- Master prompt: local file `SQE1_합격_마스터프롬프트.md`
- 30-day plan: local file `SQE1_30일_시작계획.md`
- Day 1 diagnostic lesson: local file `SQE1_Day1_진단수업.md`
- Study log: local file `SQE1_공부기록.md`
- Materials comparison table: local file `SQE1_교재_자료_비교표.md`
- Public source map: local file `SQE1_공개소스_맵.md`
- Operating dashboard: local file `SQE1_운영대시보드.md`
- `tools/build_sqe1_coursebook.py`
- `tools/build_sqe1_workbook.py`
- `tools/build_sqe1_issue_atlas.py`

Generated outputs in `output/`:

- Coursebook v0.4 PDF: local Korean filename `SQE1_강의식_총정리_교재_v0.4.pdf`
- Coursebook v0.4 HTML: local Korean filename `SQE1_강의식_총정리_교재_v0.4.html`
- `sqe1_coursebook_v04.html`
- Workbook v0.2 PDF: local Korean filename `SQE1_원문복제없는_문제집_v0.2.pdf`
- Workbook v0.2 HTML: local Korean filename `SQE1_원문복제없는_문제집_v0.2.html`
- `sqe1_workbook_v02.html`
- Issue atlas v0.1 PDF: local Korean filename `SQE1_과목별_쟁점_총망라_지도_v0.1.pdf`
- Issue atlas v0.1 HTML: local Korean filename `SQE1_과목별_쟁점_총망라_지도_v0.1.html`
- `sqe1_issue_atlas_v01.html`

Verification already performed locally:

- Coursebook v0.4 PDF: `%PDF-1.4`, 690 internal page objects, 6,435,718 bytes.
- Workbook v0.2 PDF: `%PDF-1.4`, 553 internal page objects, 4,864,524 bytes, 612 original questions in HTML.
- Issue atlas v0.1 PDF: `%PDF-1.4`, 145 internal page objects, 761,780 bytes.
- Python generators passed `py_compile`.

## Current Study Materials

### Coursebook v0.4

Lecture-style SQE1 coursebook containing:

- Overall SQE1 map.
- SBA time strategy.
- Subject-by-subject public source anchors.
- Authority briefing.
- Rule sheets.
- Answer elimination method.
- Original mini MCQ bank.
- Long fact-pattern seminar.
- Topic-level lecture pages.

### Workbook v0.2

Clean-room original question book containing:

- 612 original MCQs.
- Subject-by-subject drill questions.
- Answer keys and teaching explanations.
- FLK1 full timed mock: 180 questions.
- FLK2 full timed mock: 180 questions.

### Issue Atlas v0.1

Revision atlas containing:

- 14 subject final rule grids.
- Trigger maps.
- Korean-law pitfall tables.
- Source anchors.
- Last-day checklists.
- 84 issue cards.
- 7-pass revision loop.

## Automation Status

The user stated on 2026-07-04 that all scheduled automations were deleted. The current direction is to focus on making course materials only.

## Important Implementation Notes

- Local `git` command was not available in PATH during the session.
- GitHub connector was available and repository `shopper12/sqe` was found.
- GitHub connector text-file API can upload UTF-8 text files. It cannot directly upload binary PDFs through the used wrapper.
- Therefore, upload text sources and HTML artifacts to GitHub. PDFs can be regenerated locally from scripts/HTML.
- `tools/build_sqe1_issue_atlas.py` includes a pure-Python PDF fallback path because browser PDF conversion hit an approval/usage limit.

## Next Best Work

1. Push/update all key text files, generators, and HTML artifacts to `shopper12/sqe`.
2. Add a root `README.md` explaining how to resume from another computer.
3. Optionally add a `MANIFEST.md` with artifact inventory and regeneration commands.
4. Continue expanding coursebook v0.5 with deeper statute/case treatment by subject.
5. Continue expanding workbook v0.3 with error-type remediation sets: R/F/E/P/ETH.
6. Add SQE2 exemption evidence checklist and Korean attorney evidence mapping.

## Regeneration Commands

From the project root:

```powershell
python tools\build_sqe1_coursebook.py
python tools\build_sqe1_workbook.py
python tools\build_sqe1_issue_atlas.py
```

Browser-based PDF conversion was previously used for coursebook/workbook, but if unavailable, use the HTML files directly or extend the pure-Python PDF fallback used by `build_sqe1_issue_atlas.py`.
