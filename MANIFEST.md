# SQE1 Project Manifest

Repository: `shopper12/sqe`
Cloud handoff date: 2026-07-04
Project: SQE1 January 2027 pass project for a Korean-qualified lawyer seeking SQE2 exemption.

## Purpose

This repository is the cloud handoff for the SQE1 preparation project. It preserves the working conversation state, the legal research boundaries, the study-system decisions, and the artifact inventory so the project can continue from another computer.

## Uploaded Cloud Files

- `README.md`: project overview and continuation point.
- `CLOUD_CONVERSATION.md`: condensed conversation state and next-agent instructions.
- `MANIFEST.md`: artifact inventory and regeneration map.

## Local Files Created In The Workspace

Study planning and operations:

- `SQE1_합격_마스터프롬프트.md`
- `SQE1_30일_시작계획.md`
- `SQE1_Day1_진단수업.md`
- `SQE1_공부기록.md`
- `SQE1_교재_자료_비교표.md`
- `SQE1_공개소스_맵.md`
- `SQE1_운영대시보드.md`

Generators:

- `tools/build_sqe1_coursebook.py`
- `tools/build_sqe1_workbook.py`
- `tools/build_sqe1_issue_atlas.py`

Generated outputs:

- `output/SQE1_강의식_총정리_교재_v0.4.pdf`
- `output/SQE1_원문복제없는_문제집_v0.2.pdf`
- `output/SQE1_과목별_쟁점_총망라_지도_v0.1.pdf`
- Matching `.html` source files in `output/`

## Verification Snapshot

- Coursebook v0.4: valid PDF, about 690 pages, about 6.4 MB.
- Workbook v0.2: valid PDF, about 553 pages, 612 generated question blocks.
- Issue atlas v0.1: valid PDF, about 145 pages.
- Python compile check passed for all three generator scripts.

## Binary Artifact Note

The connector used in this session uploads UTF-8 text files. Binary PDFs were generated locally and should be uploaded later through normal Git, the GitHub web UI, or regenerated on the next machine.

## Legal Boundary

Do not use pirated books, copyrighted question banks, leaked materials, or copied proprietary SQE prep content. The generated materials should be original summaries, frameworks, and questions based on lawful public sources and official exam specifications.
