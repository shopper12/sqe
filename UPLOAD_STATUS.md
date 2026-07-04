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

## Not Yet Uploaded

Generator scripts:

- `tools/build_sqe1_coursebook.py`
- `tools/build_sqe1_workbook.py`
- `tools/build_sqe1_issue_atlas.py`

Generated HTML outputs:

- Coursebook HTML versions v0.1-v0.4
- Workbook HTML versions v0.1-v0.2
- Issue atlas HTML v0.1

Generated PDF outputs:

- Coursebook PDF versions v0.1-v0.4
- Workbook PDF versions v0.1-v0.2
- Issue atlas PDF v0.1

## Reason

The available GitHub text-file connector can safely upload reviewed UTF-8 text files. A direct recursive upload of the whole workspace, including unreviewed binaries, was blocked by security review because the repository is public.

## Next Safe Options

1. Upload the remaining files one by one after review.
2. Make the repository private, then upload the complete workspace.
3. Use local Git or GitHub web upload manually for binary PDFs.
4. Give explicit approval for publishing the full remaining workspace, including scripts, HTML, PDFs, and possible embedded metadata, to the public repository.
