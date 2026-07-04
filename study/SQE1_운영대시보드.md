# SQE1 운영대시보드

기준일: 2026-07-03  
목표: SQE1 January 2027 합격 + SQE2 exemption 신청 준비

---

## 핵심 일정

| 항목 | 날짜 | 상태 |
|---|---|---|
| SQE1 January 2027 FLK1 | 2027-01-11 - 2027-01-15 | 공식 확인 |
| SQE1 January 2027 FLK2 | 2027-01-18 - 2027-01-22 | 공식 확인 |
| Examinable law and practice cut-off | 2026-09-11 | 공식 확인 |
| Booking opening | TBC | 주간 감시 |
| Booking closing | TBC | 주간 감시 |
| Results date | TBC | 주간 감시 |
| SQE1 fee from September 2026 | £2,006 | 공식 확인 |

---

## 운영 파일

| 파일 | 목적 |
|---|---|
| SQE1_합격_마스터프롬프트.md | 새 대화에 붙여 넣는 전체 운영 프롬프트 |
| SQE1_30일_시작계획.md | 첫 30일 공부 캘린더 |
| SQE1_공부기록.md | 로컬 공부기록 백업 |
| SQE1_교재_자료_비교표.md | 교재/강의/문제은행 비교표 |
| SQE1_Day1_진단수업.md | 첫날 90분 진단수업 |
| SQE1_공개소스_맵.md | 공식·공개 법령·판례 출처 지도 |
| output/SQE1_강의식_총정리_교재_v0.4.pdf | 권위자료 브리핑, SBA 시간전략, 긴 사실관계 세미나를 추가한 PDF |
| output/SQE1_원문복제없는_문제집_v0.2.pdf | 612개 original 문항, FLK1/FLK2 각 180문항 full mock 포함 문제집 |
| output/SQE1_과목별_쟁점_총망라_지도_v0.1.pdf | 과목별 trigger/rule/trap 회독용 쟁점 지도 |
| tools/build_sqe1_coursebook.py | 강의식 교재 생성기 |
| tools/build_sqe1_workbook.py | 원문복제없는 문제집 생성기 |
| tools/build_sqe1_issue_atlas.py | 과목별 쟁점 지도 생성기 |

---

## 교재 제작 정책

요청 중 "불법을 가리지 않고 유료 교재/문제집을 가공"하는 방식은 사용하지 않는다.

대신 다음 원칙으로 교재를 만든다.

- SQE/SRA 공식 specification, assessment topics, Standards and Regulations를 기준 범위로 삼는다.
- legislation.gov.uk, BAILII 등 공개 법령·판례 출처를 보조한다.
- 설명, 예시, 문제는 직접 작성한다.
- 유료 교재나 문제은행의 표현, 구성, 해설, 문제를 복제하지 않는다.
- 시험 변경 가능성이 있는 부분은 examinable law and practice cut-off와 공식 업데이트로 검증한다.

현재 PDF v0.4는 전체 과목 지도, SBA 시간전략, 과목별 공개 법령·판례 앵커, 권위자료 브리핑, rule sheet, 선택지 제거법, 자체 제작 original drill pack, mini MCQ bank, 긴 사실관계 세미나를 포함한다. 최종판까지는 과목별 세부 조문·판례 설명, 더 깊은 fact pattern 문제, full mock을 계속 추가한다.

별도 문제집 v0.2는 612개 original 문항, 과목별 answer key, FLK1/FLK2 각 180문항 full timed mock set을 포함한다. 공식 sample question이나 유료 문제은행 문항을 복제하지 않는다.

쟁점 지도 v0.1은 14개 과목 final rule grid, trigger map, Korean-law pitfalls, source anchors, last-day checklist, 84개 issue card를 포함한다. 브라우저 PDF 변환 권한 제한이 있을 때도 생성되도록 순수 Python PDF 백업 경로를 포함한다.

---

## 웹 기록

개인 Notion 또는 다른 웹 기록 도구를 별도로 연결한다. 공개 GitHub에는 개인 데이터베이스 링크를 넣지 않는다.

기록 항목:

- Date
- Study Hours
- FLK
- Subject
- Theory
- Question Count
- Accuracy
- Error Theme
- Tomorrow Recall
- Condition
- Status

---

## 알림/모니터링

사용자가 예약 작업을 삭제했으므로 현재는 교재 제작에 집중한다. 일정 확인은 필요할 때 공식 사이트로 직접 검증한다.

---

## 이번 주 할 일

1. Day 1 진단수업 완료.
2. 공식 SQE1 sample questions 최소 15문제 풀이.
3. 오답을 R/F/E/P/ETH 코드로 분류.
4. 교재 구매는 7일 진단 후 결정.
5. SQE2 exemption용 영문 자격/경력 증명 발급처 확인.

---

## 출처

- SQE dates and booking windows: https://sqe.sra.org.uk/booking/assessment-dates-locations/booking-windows
- SQE assessment topics: https://sqe.sra.org.uk/about/sqe-assessment-topics
- SQE1 single best answer questions: https://sqe.sra.org.uk/assessments/sqe1-assessments/sqe1-single-best-answer
- SQE1 sample questions: https://sqe.sra.org.uk/assessments/sqe1-assessments/sqe1-sample-questions
- SQE reports: https://sqe.sra.org.uk/sqe-results/reports
- SQE fees: https://sqe.sra.org.uk/about/cost
- SRA SQE exemptions: https://www.sra.org.uk/become-solicitor/qualified-lawyers/sqe-exemptions/
- SRA training/course finder: https://www.sra.org.uk/become-solicitor/sqe/sqe-training-options/sqe-training-course-finder/
