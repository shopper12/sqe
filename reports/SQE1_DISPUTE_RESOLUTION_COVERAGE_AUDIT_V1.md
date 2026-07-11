# SQE1 Dispute Resolution Coverage Audit

Date: 2026-07-11  
Target: SRA FLK1 specification applicable from 2026-09-01  
Files audited:

- `textbooks/SQE1_DISPUTE_RESOLUTION_TEXTBOOK_V1.md`
- `question_banks/SQE1_DISPUTE_RESOLUTION_SBA_V1.md`

## 1. 결론

기존 통합 이론서의 Dispute Resolution 부분은 절차 단계의 이름만 있는 개요였고, 실제 SBA를 풀기 위한 기한·test·consequence·오답제거 구조가 없었다. v1은 SRA 세부 bullet 전부를 장 단위로 연결하고, 30개 original SBA로 주요 적용 포인트를 검증한다.

## 2. 구조적 결함과 보완

| 기존 결함 | 시험상 위험 | v1 보완 |
|---|---|---|
| pre-action→enforcement를 한 문단에 압축 | 현재 procedural stage를 구분하지 못함 | 14개 사건 단계 + Stage/Clock/Test/Consequence/Best step 알고리즘 |
| time limits 없음 | service/defence/appeal 문항 대량 오답 | 4개월·6개월·14일·28일·21일 핵심표 |
| strike out/summary judgment 혼재 | test가 비슷한 선택지 구분 불가 | pleading defect와 merits threshold 별도 장·SBA |
| disclosure와 inspection 혼재 | privilege 문항 오답 | CPR 31.6/31.15 및 privilege 유형 분리 |
| hearsay를 형사법처럼 취급 | ‘자동 배제’ 함정 | Civil Evidence Act 1995상 admissibility/notice/weight 구조 |
| track가 small/fast/multi만 존재 | 2023 이후 intermediate track 누락 | £100,000·3일·complexity band 반영 |
| ADR가 자발성 설명에 그침 | Churchill 이후 court power 누락 | Churchill/Halsey/Dunnett 관계 정리 |
| arbitration이 구법 중심 | 2025 개정 누락 | Arbitration Act 2025 시행 및 핵심 변화 표시 |
| costs가 loser-pays 한 줄 | Part 36·FRC·budget 문제 대응 불가 | offer 결과표, complexity band, budget sanction |
| enforcement가 이름 나열 | 자산별 최적수단 선택 불가 | goods/bank/land/wages/information 매칭표 |
| 판례가 장식적으로 나열 | facts-trigger와 rule 연결 불가 | 각 판례를 procedural function 한 줄로 고정 |
| ethics 별도 단원으로 고립 | pervasive ethics 출제 대응 약함 | disclosure, without notice, witness, settlement에 반복 삽입 |

## 3. SRA 출제범위 매핑

| SRA 영역 | 이론서 장 | SBA |
|---|---:|---:|
| arbitration, mediation, litigation | 1 | Q1–2 |
| parties, causes, limitation | 2 | Q3–4 |
| pre-action protocols | 2 | Q5 |
| applicable law, Welsh language | 2 | 이론·자가점검 |
| High Court/County Court/specialist courts | 3 | Q6 |
| issue, Part 7/8, party changes | 4 | Q7, Q10 |
| domestic/foreign/alternative service | 4 | Q8–9 |
| admission, AoS, defence, jurisdiction | 5 | Q11–12 |
| default judgment, discontinuance, settlement | 5 | Q13–14 |
| statements, reply, Part 20, Part 18, amendment | 6 | Q15–16 |
| applications, summary judgment, interim payment, injunction | 7 | Q17–19 |
| overriding objective, tracks, directions, sanctions, CCMC | 8 | Q20–21 |
| relevance, hearsay, burden/standard, witnesses, affidavits, experts | 9 | Q22–24 |
| disclosure, inspection, electronic documents, privilege, waiver | 10 | Q25–27 |
| summons, checklist, bundle, trial, judgment | 11 | 이론·자가점검 |
| costs, Part 36, security, fixed/assessed/non-party costs | 12 | Q28 |
| appeal permission, destination, grounds | 13 | Q29 |
| obtaining debtor information, enforcement methods | 14 | Q30 |

## 4. 핵심 판례 보완 목록

다음 판례를 단순 이름이 아니라 시험 기능과 연결했다.

- ADR: `Churchill`, `Halsey`, `Dunnett`
- limitation: `Pirelli`, `Haward`, `A v Hoare`
- service: `Barton`, `Abela`, `Vinos`
- summary judgment/injunction: `Swain`, `Easyair`, `American Cyanamid`, `Mareva`, `Brink’s-MAT`, `Anton Piller`
- sanctions/default: `Denton`, `Mitchell`, `FXF`
- evidence/expert: `Re B`, `The Ikarian Reefer`, `Jones v Kaney`
- privilege: `Three Rivers (No 5)`, `Waugh`, `SFO v ENRC`
- abuse/judgment: `Summers`, `Virgin Atlantic`
- settlement/appeal: `Gibbon`, `Ladd v Marshall`

## 5. 핵심 조문·규칙 보완 목록

- Limitation Act 1980: ss 2, 5, 8, 11, 14, 14A, 14B, 28, 32, 33, 35
- Civil Evidence Act 1995
- Arbitration Act 1996 ss 9, 30, 66, 67–69, as amended by Arbitration Act 2025
- CPR Parts 1, 3, 6–20, 23–29, 31–36, 38, 40, 44–47, 52, 70–73
- PD 6A/6B, PD Pre-Action Conduct and relevant protocols

## 6. 2026년 9월 변경 반영

SRA가 2026-09-01부터 Dispute Resolution의 enforcement 표현을 `oral examination`에서 `obtaining information from judgment debtor`로 변경했다. 교재와 문제집은 CPR Part 71의 현재 표현으로 통일했다.

## 7. 남은 업데이트 게이트

현재 날짜가 시험 법령 기준일(2026-09-11) 이전이므로 다음은 9월에 한 차례만 재검증한다.

1. 2026-07-12부터 2026-09-11 사이 시행되는 CPR/PD update
2. court fee와 fixed recoverable costs 금액표의 변동
3. SRA clean specification 교체본과 change-marked PDF의 차이
4. 새 appellate decision 중 기존 leading test를 변경한 사건

이 게이트는 현재 교재가 불완전하다는 뜻이 아니라, 미래 cutoff를 현재 시점에 확정했다고 가장하지 않기 위한 version-control 절차다.

## 8. 품질 기준 결과

각 장은 최소 네 가지 이상의 요소(rule/source/trigger/trap/ethics/application/self-test/alternative elimination)를 포함한다. 문제집의 모든 문항은 원문형 English facts와 5개 선택지, 정답, 한국어 rule/application 또는 오답제거를 포함하며 SRA 공개문항을 복제하지 않았다.
