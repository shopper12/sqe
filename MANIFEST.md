# SQE1 Project Manifest

Repository: `shopper12/sqe`
Cloud handoff date: 2026-07-04
Project: SQE1 January 2027 study-material project.

## Uploaded files

### Core context

- `README.md`
- `CLOUD_CONVERSATION.md`
- `MANIFEST.md`

### Planning and operations

- `SQE1_master_prompt.md`
- `SQE1_30_day_plan.md`
- `SQE1_day1_diagnostic_lesson.md`
- `SQE1_study_log.md`
- `SQE1_materials_comparison.md`
- `SQE1_public_source_map.md`
- `SQE1_dashboard.md`

### Analysis

- `reports/SQE1_REBUILD_AUDIT.md`
- `reports/SQE1_DISPUTE_RESOLUTION_COVERAGE_AUDIT_V1.md`

### Main study materials

- `textbooks/SQE1_THEORY_TEXTBOOK.md`
- `question_banks/SQE1_PRACTICE_QUESTION_BANK.md`
- `textbooks/SQE1_DISPUTE_RESOLUTION_TEXTBOOK_V1.md`
- `question_banks/SQE1_DISPUTE_RESOLUTION_SBA_V1.md`

### Generators

- `tools/build_sqe1_materials.py`
- `tools/build_sqe1_coursebook.py`
- `tools/build_sqe1_workbook.py`
- `tools/build_sqe1_issue_atlas.py`

### Portable HTML outputs

- `output/sqe1_coursebook_v04.html`
- `output/sqe1_workbook_v02.html`
- `output/sqe1_issue_atlas_v01.html`
- `output/sqe1_dispute_resolution_study_pack_v1.html`

## Note on PDF handling

The current connector writes text files. The repository therefore stores Markdown, Python source, and HTML. PDF outputs should be regenerated locally or by a later CI workflow.

## Regeneration

```powershell
python tools\build_sqe1_materials.py
```

## Quality rule

Each topic must contain a rule, source anchor, trigger, trap, ethics angle, application example, or self-test item. Avoid generic repeated sections.

## Detailed subject status

- Business Law and Practice: prior v3 review completed; further consolidation remains in the project backlog.
- Dispute Resolution: v1 complete theory, 30 original SBA questions, coverage audit, and portable HTML added on 2026-07-11.
- Legal cutoff gate: recheck amendments made effective by 2026-09-11 before the January 2027 sitting.
