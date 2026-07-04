# SQE1 January 2027 Project

This repository is the cloud handoff for the SQE1 January 2027 study-material project.

## What This Contains

- Lecture-style SQE1 coursebook generator.
- Clean-room original SQE1 workbook generator.
- Subject issue atlas generator.
- Study plan, source map, operating dashboard, and continuation context.

The project deliberately does **not** copy paid textbooks, commercial question banks, leaked exams, or reconstructed questions. Materials are based on official SQE/SRA sources, public legal sources, and original explanations/questions.

## Start Here

Read:

1. `CLOUD_CONVERSATION.md`
2. `SQE1_운영대시보드.md` locally, or the dashboard section in `CLOUD_CONVERSATION.md`
3. `SQE1_공개소스_맵.md` locally, or the source section in `CLOUD_CONVERSATION.md`
4. `SQE1_30일_시작계획.md` locally, or the plan summary in `CLOUD_CONVERSATION.md`

## Current Main Artifacts

Generated locally before cloud handoff:

- Coursebook v0.4: lecture-style theory material.
- Workbook v0.2: 612 original questions, including FLK1/FLK2 180-question mocks.
- Issue atlas v0.1: trigger/rule/trap revision map.

The HTML versions and generator scripts are intended to be kept in GitHub. Binary PDFs may need to be regenerated locally.

Portable ASCII aliases used in GitHub:

- `output/sqe1_coursebook_v04.html`
- `output/sqe1_workbook_v02.html`
- `output/sqe1_issue_atlas_v01.html`

## Regenerate

From the repository root:

```powershell
python tools\build_sqe1_coursebook.py
python tools\build_sqe1_workbook.py
python tools\build_sqe1_issue_atlas.py
```

## Official Sources

- https://sqe.sra.org.uk/booking/assessment-dates-locations/booking-windows
- https://sqe.sra.org.uk/about/sqe-assessment-topics
- https://sqe.sra.org.uk/assessments/sqe1-assessments/sqe1-specification
- https://sqe.sra.org.uk/assessments/sqe1-assessments/sqe1-single-best-answer
- https://sqe.sra.org.uk/assessments/sqe1-assessments/sqe1-sample-questions
- https://sqe.sra.org.uk/sqe-results/reports
- https://www.sra.org.uk/solicitors/standards-regulations/
