# Regeneration Guide

This page explains how to continue the project from another computer.

## Expected Local Structure

Recommended folder layout after cloning or downloading this repository:

```text
sqe/
  README.md
  CLOUD_CONVERSATION.md
  MANIFEST.md
  docs/
  tools/
  output/
```

The original working machine had generated PDF and HTML artifacts under `output/`, plus Python generator scripts under `tools/`.

## Generated Materials To Recreate

1. Coursebook
   - Target: `SQE1_강의식_총정리_교재_v0.4.pdf`
   - Purpose: lecture-style theory book for SQE1.
   - Approximate verified size: 690 PDF pages.

2. Workbook
   - Target: `SQE1_원문복제없는_문제집_v0.2.pdf`
   - Purpose: original MCQ workbook with explanations.
   - Approximate verified size: 553 PDF pages, 612 generated question blocks.

3. Issue Atlas
   - Target: `SQE1_과목별_쟁점_총망라_지도_v0.1.pdf`
   - Purpose: subject-by-subject issue map.
   - Approximate verified size: 145 PDF pages.

## Generator Scripts

The local workspace contained these scripts:

```text
tools/build_sqe1_coursebook.py
tools/build_sqe1_workbook.py
tools/build_sqe1_issue_atlas.py
```

When the scripts are available, run them from the repository root. Exact command names may vary depending on Python installation:

```powershell
python tools/build_sqe1_coursebook.py
python tools/build_sqe1_workbook.py
python tools/build_sqe1_issue_atlas.py
```

## Validation Checklist

After regenerating:

- Confirm each PDF starts with `%PDF-`.
- Confirm output file size is non-trivial.
- Open each PDF and inspect Korean text rendering.
- Check that the workbook questions are original and not copied from a commercial bank.
- Re-check current SQE1 dates, fees, and booking instructions from official sources before using any schedule.

## Next Build Priorities

- Upload or recreate the generator scripts in this repository.
- Add a lightweight data folder for source notes by subject.
- Create v0.5 of the coursebook with clearer FLK1/FLK2 mapping.
- Create v0.3 of the workbook with more timed mixed sets.
- Add a daily study log template that can be used without automations.
