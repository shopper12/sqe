# SQE1 January 2027 Project

This repository is the cloud handoff for the SQE1 January 2027 study-material project.

## Purpose

The project builds a practical SQE1 study system for a Korean-qualified lawyer preparing for SQE1 and considering SQE2 exemption. The focus is on original, structured learning material based on official SQE/SRA pages and public legal sources.

## Start here

1. `CLOUD_CONVERSATION.md` — prior context and next steps.
2. `MANIFEST.md` — complete file inventory.
3. `SQE1_public_source_map.md` — source anchors.
4. `SQE1_dashboard.md` — operating dashboard.
5. `textbooks/SQE1_THEORY_TEXTBOOK.md` — theory source.
6. `question_banks/SQE1_PRACTICE_QUESTION_BANK.md` — practice workbook source.

## Main artifacts

| Path | Purpose |
|---|---|
| `SQE1_master_prompt.md` | Rebuild specification |
| `SQE1_30_day_plan.md` | Starter schedule |
| `SQE1_day1_diagnostic_lesson.md` | First diagnostic lesson |
| `SQE1_study_log.md` | Error-log template |
| `SQE1_materials_comparison.md` | Source/material comparison |
| `SQE1_public_source_map.md` | Public source map |
| `SQE1_dashboard.md` | Operating dashboard |
| `reports/SQE1_REBUILD_AUDIT.md` | Quality audit |
| `textbooks/SQE1_THEORY_TEXTBOOK.md` | Theory textbook source |
| `question_banks/SQE1_PRACTICE_QUESTION_BANK.md` | Practice workbook source |
| `output/sqe1_coursebook_v04.html` | Portable coursebook HTML |
| `output/sqe1_workbook_v02.html` | Portable workbook HTML |
| `output/sqe1_issue_atlas_v01.html` | Portable issue atlas HTML |

## Regenerate HTML

```powershell
python tools\build_sqe1_materials.py
```

or individually:

```powershell
python tools\build_sqe1_coursebook.py
python tools\build_sqe1_workbook.py
python tools\build_sqe1_issue_atlas.py
```

## Official sources

- https://sqe.sra.org.uk/assessments/sqe1-assessments/sqe1-specification
- https://sqe.sra.org.uk/assessments/sqe1-assessments/sqe1-single-best-answer
- https://sqe.sra.org.uk/assessments/sqe1-assessments/sqe1-sample-questions
- https://sqe.sra.org.uk/sqe-results/reports
- https://www.sra.org.uk/solicitors/standards-regulations/

## Current limitation

This upload uses the available GitHub text-file connector. Markdown, Python, and HTML artifacts are stored in GitHub. PDF outputs should be regenerated locally or through a later GitHub Actions workflow.
