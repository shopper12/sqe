# Upload Status

Last updated: 2026-07-04

## Uploaded

Cloud handoff and project documents:

- `README.md`
- `CLOUD_CONVERSATION.md`
- `MANIFEST.md`
- `CLOUD_TASK_PROMPT.md`
- `docs/SOURCES.md`
- `docs/REGENERATION.md`
- `docs/NEXT_STEPS.md`

Study documents:

- `study/SQE1_30일_시작계획.md`
- `study/SQE1_Day1_진단수업.md`
- `study/SQE1_공부기록.md` public sanitized version
- `study/SQE1_공개소스_맵.md`
- `study/SQE1_운영대시보드.md` public sanitized version
- `study/SQE1_교재_자료_비교표.md`

Prompt archive:

- `prompts/SQE1_합격_마스터프롬프트.md`

Generator scripts:

- `tools/build_sqe1_workbook.py` full local script uploaded
- `tools/build_sqe1_issue_atlas.py` full local script uploaded

## Still Not Uploaded

Large/root generator:

- `tools/build_sqe1_coursebook.py`

Generated HTML outputs:

- Coursebook HTML versions v0.1-v0.4
- Workbook HTML versions v0.1-v0.2
- Issue atlas HTML v0.1

Generated PDF outputs:

- Coursebook PDF versions v0.1-v0.4
- Workbook PDF versions v0.1-v0.2
- Issue atlas PDF v0.1

Excluded intentionally:

- `tools/__pycache__/*.pyc`

## Current Blocker

The local environment currently has neither `git` nor `gh` available on PATH. The GitHub REST upload path also cannot proceed because the shell environment no longer exposes a GitHub authorization header. The GitHub connector can create and update UTF-8 text files, but it does not accept local file paths for binary PDFs or large HTML artifacts.

Two smaller Python generator scripts were updated through the GitHub connector. The large coursebook generator and generated PDF/HTML outputs still require one of the following:

1. Install/use local Git or GitHub CLI and push the files normally.
2. Upload the remaining files through the GitHub web UI.
3. Provide a usable GitHub token/authenticated CLI environment in the local shell.
4. Make the repository private and use a broader trusted upload mechanism if available.

## Verified

- `tools/build_sqe1_workbook.py` now starts with the real local imports and generator code.
- `tools/build_sqe1_issue_atlas.py` now starts with the real local imports and generator code.
- Repository remains public: `shopper12/sqe`.
