# SQE1 Dispute Resolution — 시험 대비 완성 이론서

Version: v1.0  
작성 기준일: 2026-07-11  
적용 출제범위: 2026-09-01 이후 시행되는 SRA FLK1 specification  
법령 업데이트 기준: 2026-07-11 현재 공표·시행된 법령과 CPR. 2027년 1월 시험의 법령 기준일(2026-09-11)에 맞추어 9월에 CPR 개정 여부를 최종 재점검할 것.

> 이 교재는 ‘규칙 암기’가 아니라 **사건의 현재 단계 → 다음 절차 → 기한 → 제재 → 최선의 답** 순서로 문제를 푸는 데 목적이 있다. 조문 번호는 출발점이고, 실제 시험에서는 조문의 효과를 의뢰인 사실에 적용해야 한다.

## 0. 출제범위와 공부법

### 0.1 SRA 범위 체크

이 교재는 다음 영역을 모두 다룬다.

1. litigation·arbitration·mediation의 선택
2. 당사자·청구원인·시효·pre-action conduct·준거법·웨일스어
3. High Court/County Court 및 전문법원의 관할
4. claim form 발행·송달·당사자 변경·국외송달
5. admission·acknowledgment·defence·counterclaim·관할 다툼·default judgment·중단·화해
6. statements of case·Part 18·amendment
7. applications·strike out·summary judgment·interim payment·injunction
8. overriding objective·track·directions·sanctions·relief·CCMC
9. 사실·전문가·전문증거·hearsay·입증책임
10. disclosure·inspection·privilege·without prejudice·waiver
11. trial 준비·진행·판결의 효과
12. costs·budgeting·Part 36·security·fixed costs
13. appeals
14. money judgment enforcement와 judgment debtor 정보취득

### 0.2 1.7분 SBA 풀이 알고리즘

문제를 읽으면서 다음 다섯 칸만 채운다.

| 칸 | 질문 |
|---|---|
| Stage | 아직 pre-action인가, 발행·송달·방어·case management·trial·enforcement 중 어디인가? |
| Clock | 어느 문서의 **송달일 또는 deemed service date**부터 며칠인가? |
| Test | permission, real prospect, good reason, just and convenient 등 적용 문턱은 무엇인가? |
| Consequence | 자동 제재인가, 법원 재량인가, 비용 제재인가? |
| Best step | 법률적으로 가능한 여러 조치 중 지금 가장 먼저 할 조치는 무엇인가? |

함정은 대체로 네 종류다.

- 옳은 법리를 **잘못된 단계**에 적용한다.
- issue date와 service date를 혼동한다.
- ‘할 수 있다’와 ‘반드시 해야 한다’를 바꾼다.
- 본안 승소 가능성만 보고 절차상 제재·비용·ADR를 무시한다.

---

## 1. 분쟁해결수단 선택

### 1.1 Litigation

공개된 국가법원이 강제력 있는 판결을 내리고 항소 체계가 존재한다. 다수 당사자, 긴급 injunction, 제3자 강제, 판례 형성, 광범위한 disclosure가 필요할 때 유리하다. 반면 공개성, 시간, 비용, 관계 악화가 단점이다.

### 1.2 Arbitration

당사자 합의에 기초한 사적 재판이다. 국제집행(New York Convention), 중립적 forum, 전문 arbitrator, 절차 유연성, 상대적 비공개성이 장점이다. 항소는 제한되고 중재인·기관비용이 추가되며, 다수 당사자 병합과 제3자에 대한 강제력이 소송보다 약할 수 있다.

핵심 법원칙은 Arbitration Act 1996(Arbitration Act 2025로 개정)이다.

- 유효한 arbitration agreement가 있고 그 범위에 속하는 소송이면 피고는 원칙적으로 법원절차의 stay를 신청한다(s 9).
- tribunal은 자신의 substantive jurisdiction을 판단할 수 있다(s 30; kompetenz-kompetenz).
- award는 당사자를 구속하고, 법원의 허가로 판결처럼 집행할 수 있다(s 66).
- serious irregularity challenge(s 68)와 point of law appeal(s 69)은 좁다.
- 2025 개정은 arbitration agreement의 준거법, arbitrator disclosure, summary disposal, emergency arbitrator 및 s 67 challenge 절차 등을 현대화했다. 시험에서는 세부 문언보다 ‘중재는 합의·제한된 법원개입·국제집행에 강점’이라는 선택 논리가 우선이다.

### 1.3 Mediation과 court-ordered ADR

중립적 mediator가 합의를 돕지만 결정을 강제하지 않는다. 합의되면 계약 또는 Tomlin order로 강제력을 확보한다. 비밀성, 속도, 창의적 구제, 거래관계 보존이 장점이다.

`Churchill v Merthyr Tydfil CBC [2023] EWCA Civ 1416`에 따라 법원은 당사자의 재판접근권의 본질을 침해하지 않고 비례적이며 정당한 목적을 달성하는 경우 비법원적 분쟁해결을 명하거나 절차를 stay할 수 있다. `Halsey v Milton Keynes General NHS Trust [2004] EWCA Civ 576`의 ‘강제 mediation 불가’라는 절대적 해석은 더 이상 안전하지 않다. `Dunnett v Railtrack plc [2002] EWCA Civ 303`은 불합리한 ADR 거절이 승소자의 비용 회수에도 불리할 수 있음을 보여준다.

**SBA trap:** mediation을 거절했다고 자동 패소하지는 않는다. 보통 핵심은 case management order, stay, 또는 costs consequence다.

### 1.4 선택표

| 사실 신호 | 우선 고려 |
|---|---|
| 해외 집행, 전문기술, 비공개 | arbitration |
| 지속적 거래관계, 다면적 해결책 | mediation |
| 긴급 freezing/search injunction, 제3자 명령 | litigation |
| 법적 선례 또는 공개 판단 필요 | litigation |
| 작은 가치·단순 사실·비용 민감 | negotiation/mediation, small claims process |

---

## 2. 소송 전 점검

### 2.1 올바른 당사자와 cause of action

법인격, 계약 당사자, 양도, subrogation, 대리, 사망, 파산·청산 여부를 먼저 확인한다. claimant는 실체법상 권리를 가진 자여야 하고 defendant는 의무자여야 한다.

- child 또는 protected party는 litigation friend를 통해 소송한다(CPR Part 21).
- 사망자의 estate는 personal representative가 대표한다.
- company는 별도 법인격을 가진다. director나 shareholder를 회사 채무의 당사자로 자동 추가하지 않는다.
- 이름의 오기(misnomer)와 잘못된 법적 실체를 상대로 한 경우를 구별한다.

### 2.2 시효: Limitation Act 1980

| 청구 | 기본기간 | 기산점/핵심 |
|---|---:|---|
| simple contract | 6년 | cause of action 발생일(s 5). 통상 breach 때 발생하며 손해 인지는 불필요 |
| tort 일반 | 6년 | cause of action 발생일(s 2). negligence는 통상 실제 손해 발생 필요 |
| personal injury | 3년 | cause of action 발생일 또는 date of knowledge 중 늦은 날(s 11, s 14) |
| latent damage negligence (PI 제외) | 6년 또는 지식 후 3년 | s 14A. long-stop은 행위·부작위 후 15년(s 14B) |
| deed/specialty | 12년 | s 8 |
| contribution | 2년 | 관련 판결·award·합의 등 기준(Civil Liability (Contribution) Act 1978) |

연장·정지 포인트:

- disability가 시효 발생 시 존재하면 s 28을 검토한다. 성년 후 생긴 장애는 원칙적으로 시계를 되돌리지 않는다.
- fraud, deliberate concealment, mistake는 s 32에 따라 발견 또는 합리적으로 발견 가능할 때까지 연기될 수 있다.
- PI는 s 33에 따라 형평상 재량 배제가 가능하지만 자동이 아니다.
- limitation defence는 피고가 plead해야 하는 defence다.
- claim form은 limitation 만료 전 법원에 전달되어 issue되어야 한다. 그러나 발행만 하고 송달을 놓치면 별도 문제가 생긴다.

**핵심 판례:** `Pirelli General Cable Works Ltd v Oscar Faber [1983] 2 AC 1`(재산상 손해 발생과 negligence accrual), `Haward v Fawcetts [2006] UKHL 9`(s 14A knowledge), `A v Hoare [2008] UKHL 6`(PI 재량의 접근).

### 2.3 Pre-Action Protocol/PD–Pre-Action Conduct

목적은 쟁점 이해, 정보·문서 교환, settlement/ADR, 효율적 case management와 비례적 비용이다. 특정 protocol이 있으면 그것을 따르고, 없으면 Practice Direction – Pre-Action Conduct and Protocols를 따른다.

일반 흐름:

1. concise letter of claim: 사실, 법적 근거, 손해, 원하는 구제, 핵심 문서
2. defendant acknowledgment/response
3. 핵심 문서 교환과 expert 필요성 검토
4. ADR 검토
5. limitation이 임박하면 protectively issue하고 stay를 구하는 방안 검토

불이행 효과는 자동 각하가 아니라 보통 directions, stay, costs, interest다. 악의적·중대한 불이행은 더 무거운 제재를 부를 수 있다.

### 2.4 준거법

영국의 retained rules를 중심으로 계약은 Rome I, 비계약은 Rome II 체계를 사용한다.

- 계약: 명시적 choice가 우선. 없으면 계약유형별 default와 가장 밀접한 관련을 본다. overriding mandatory rules와 public policy 예외를 구별한다.
- tort: 통상 damage가 발생한 국가의 법. 공통 habitual residence 또는 manifestly closer connection 예외를 검토한다.
- 준거법(applicable law)과 관할(jurisdiction), 송달(service)은 서로 다른 질문이다.

### 2.5 웨일스어

웨일스의 civil proceedings에서는 Welsh language 사용이 불이익을 초래해서는 안 된다. 초기 단계에서 언어 사용·번역·통역·hearing 관리 필요를 court에 알려 directions를 받아야 한다. 이것은 merits가 아니라 절차적 접근성과 case management 문제다.

---

## 3. 어디에서 시작할 것인가

### 3.1 County Court와 High Court

대부분의 민사금전청구는 County Court에서 시작한다. High Court는 가치·복잡성·공적 중요성·전문성 때문에 적합한 사건에 사용한다. 일반 money claim이 £100,000 미만이면 원칙적으로 High Court에서 시작하지 않으며, PI money claim의 High Court 기준은 일반적으로 £50,000이다. 단, 금액만이 아니라 복잡성·중요성이 함께 작용하고 court는 transfer할 수 있다.

High Court 주요 division/list:

- King’s Bench Division: 일반 contract/tort, Media and Communications, Administrative Court 등
- Business and Property Courts: Commercial Court, Technology and Construction Court, Insolvency and Companies List, Intellectual Property 등
- Chancery Division: trusts, estates, land, companies, insolvency, equitable relief

### 3.2 전문법원 선택 함정

건설·엔지니어링과 복잡한 professional negligence는 TCC, 국제상거래·선박·보험은 Commercial Court 성격이 강하다. 그러나 단지 계약이라고 모두 Commercial Court가 되는 것은 아니다.

### 3.3 관할과 forum

국외 요소가 있으면 다음 순서를 지킨다.

1. exclusive jurisdiction/arbitration clause가 있는가?
2. defendant가 England and Wales에 domiciled/present한가?
3. CPR PD 6B gateway가 있는가?
4. claim이 reasonable prospect를 가지는가?
5. England and Wales가 proper place인가(forum conveniens)?
6. permission이 필요한가, Hague Service Convention 등 어떤 송달수단인가?

---

## 4. 발행과 송달

### 4.1 Part 7와 Part 8

- Part 7: substantial dispute of fact가 예상되는 일반 청구.
- Part 8: 사실 다툼이 크지 않고 statute/rule이 허용하거나 법률판단·문서해석 중심인 청구. defence 대신 acknowledgment와 written evidence 구조가 중심이다.

### 4.2 Claim form과 particulars

claim form에는 parties, concise nature of claim, remedy, value statement 등이 들어간다. particulars of claim은 claim form에 포함·동봉·별도 송달할 수 있다. 별도면 claim form 송달 후 14일 이내이면서 claim form 자체의 최종 송달기한을 넘기면 안 된다(CPR 7.4).

statement of truth가 필요한 문서에 허위 진술을 하면 contempt consequences가 생길 수 있다.

### 4.3 국내 송달의 핵심 시계

- claim form은 관할 내 송달이면 issue 후 **4 calendar months** 내 CPR 7.5의 relevant step을 완료한다.
- 국외 송달이면 원칙적으로 **6 calendar months**다.
- CPR 6.14상 claim form은 관련 송달단계를 완료한 뒤 두 번째 business day에 deemed served되는 것이 원칙이다.
- 문서별 method와 address rule을 따로 확인한다. 개인, 회사, solicitor 수령주소가 다르다.
- email service는 상대방이 사전에 그 주소로 송달을 수락했음을 표시하는 등 PD 6A 요건을 충족해야 한다. 단순히 평소 email을 주고받았다는 이유만으로 안전하지 않다.

`Barton v Wright Hassall LLP [2018] UKSC 12`은 litigant in person도 송달 규칙을 지켜야 하며, email 송달 동의와 retrospective validation을 쉽게 가정할 수 없음을 보여준다. `Abela v Baadarani [2013] UKSC 44`는 alternative service/validation에서 문서를 피고에게 알리는 송달 목적을 강조하지만, 규칙 위반을 자동 치유하지는 않는다. `Vinos v Marks & Spencer plc [2001] 3 All ER 784`는 기간 만료 후 claim form 송달 연장의 엄격성을 보여준다.

### 4.4 Alternative service와 연장

good reason이 있으면 CPR 6.15에 따라 alternative method/place를 허가하거나 이미 취한 단계가 good service였다고 명할 수 있다. claim form 송달기간 연장은 만료 전 신청과 만료 후 신청의 문턱이 다르며, 만료 후에는 모든 합리적 송달조치를 취했으나 실패했고 신속히 신청한 경우 등 CPR 7.6의 엄격 요건을 본다.

### 4.5 국외 송달

permission 필요 여부를 먼저 확인한다. permission이 필요하면 PD 6B gateway, reasonable prospect, proper forum을 입증해야 한다. 그 다음 Hague Service Convention, 외국법상 방식, foreign government/judicial authority 등 허용 수단을 선택한다. 외국의 sovereignty와 해당국 reservation을 무시한 private service는 무효 위험이 있다.

### 4.6 당사자 추가·대체

CPR Part 19를 적용한다. limitation 전에는 통상 case resolution에 desirable한지 본다. limitation 후에는 s 35 Limitation Act 1980/CPR 19.6의 좁은 예외—잘못된 party name 교정, 기존 party의 사망·파산에 따른 대체, original action에서 필요한 claim 등—를 엄격히 적용한다.

**SBA trap:** ‘관련된 사람이니 추가 가능’이 아니라 limitation 후 추가인지, 새로운 cause of action인지, mistake가 단순 명칭오류인지 확인한다.

---

## 5. 피고의 대응과 조기 종결

### 5.1 응답 기한

기산점은 보통 **particulars of claim의 deemed service**다.

| 대응 | 통상 기한 |
|---|---:|
| acknowledgment of service | 14일 |
| defence(acknowledgment 없음) | 14일 |
| defence(적시에 acknowledgment) | 28일 |
| 합의에 의한 defence 연장 | 추가 최대 28일, court에 서면 통지(CPR 15.5) |
| jurisdiction challenge | acknowledgment로 의사 표시 후, acknowledgment filing 후 14일 내 application(CPR 11) |

### 5.2 Admission

전부 또는 일부 admission을 할 수 있다(CPR Part 14). monetary admission에는 payment proposal이 붙을 수 있다. admission 철회에는 상대 동의 또는 court permission이 필요하고, 당사자의 conduct·시기·prejudice·merits 등을 본다.

### 5.3 Defence와 counterclaim

defence는 각 allegation에 admit, deny(with reasons), 또는 unable to admit/deny and require proof로 답한다. bare denial은 위험하다. limitation, exclusion, contributory negligence, set-off 등 affirmative defence는 명시한다.

counterclaim은 일반적으로 Part 20 claim이다. defence와 함께 제기하면 permission 없이 가능한 경우가 보통이나, 이후에는 permission이 필요할 수 있다. contribution/indemnity against another defendant와 new party claim의 절차를 구별한다.

### 5.4 Default judgment

피고가 acknowledgment/defence를 제때 하지 않았고 다른 제한이 없으면 claimant는 CPR Part 12 default judgment를 구할 수 있다. 그러나 acknowledgment/defence가 늦었더라도 default judgment가 **입력되기 전** 접수되었다면 통상 default를 입력할 수 없다.

Set aside:

- wrongly entered라면 court는 반드시 set aside(CPR 13.2).
- correctly entered라면 real prospect of successfully defending 또는 some other good reason, promptness와 전체 사정을 본다(CPR 13.3).
- `FXF v English Karate Federation Ltd [2023] EWCA Civ 891`에 따라 제재구제 성격이 있으면 `Denton` 분석도 중요하다.

### 5.5 Discontinuance와 settlement

claimant는 CPR Part 38에 따라 notice로 전부·일부 중단할 수 있다. 원칙적으로 discontinuing claimant가 그때까지 defendant costs를 부담한다. 같은 사실에 기초한 재소는 permission 문제가 생길 수 있다.

settlement 형식:

- consent order: court order 자체에 조건을 표시
- Tomlin order: proceedings를 stay하고 비공개 schedule에 넓은 상업조건을 둘 수 있음. 강제하려면 보통 order 조항에 따라 다시 신청
- dismissal는 claim을 끝내므로 단순 stay보다 재소 방지 효과가 강하다

---

## 6. Statements of Case

### 6.1 기능

statement of case는 증거 전체가 아니라 각 당사자의 material facts와 법적 쟁점의 경계를 정한다. surprise를 막고 disclosure·evidence·trial 범위를 형성한다.

### 6.2 Claim/Defence/Reply/Part 20

- particulars: duty/contract, breach, causation, loss, interest, aggravated/exemplary damages 등 필요한 사실을 particularise.
- defence: allegation별 응답과 positive case.
- reply: defence에 답할 필요가 있을 때만. defence의 단순 부인을 반복하지 않는다.
- Part 20: counterclaim 또는 contribution/indemnity/additional claim.

### 6.3 Part 18 further information

쟁점을 명확히 하고 추가정보를 얻기 위한 request다. 목적은 evidence fishing이 아니다. 먼저 합리적 서면 request를 하고, 불응하면 court order를 신청한다. small claims에서는 Part 18이 원칙적으로 적용되지 않지만 court가 명할 수 있다.

### 6.4 Amendment

상대에게 송달 전에는 자유로운 편이나 송달 후에는 상대의 written consent 또는 court permission이 필요하다(CPR 17). limitation 후 new claim은 same or substantially same facts, correction of party name 등 statutory/rule exception을 충족해야 한다.

### 6.5 Strike out와 차이

CPR 3.4 strike out:

- no reasonable grounds
- abuse of process 또는 just disposal 방해
- rule/practice direction/court order 불이행

Summary judgment와 달리 strike out은 pleading의 결함·abuse·non-compliance에 초점이 있다. `Summers v Fairclough Homes Ltd [2012] UKSC 26`은 dishonest exaggeration이 있어도 전체 PI claim strike out은 비례성과 재판권을 고려해 예외적으로만 사용함을 보여준다.

---

## 7. Interim Applications

### 7.1 일반 절차(CPR Part 23)

application notice에 order와 이유를 명시하고 evidence를 붙여 file·serve한다. 일반적으로 hearing 최소 3일 전 송달하지만 특정 rule과 order가 우선한다. without notice는 긴급성, 목적 좌절 위험 또는 규칙상 허용이 있어야 하고, 신청인은 full and frank disclosure 의무를 진다.

### 7.2 Summary judgment(CPR Part 24)

test:

1. 상대가 claim/defence/issue에서 성공할 **real prospect가 없고**, 그리고
2. trial로 처리할 other compelling reason이 없다.

‘가능성이 낮다’가 아니라 현실적인 가능성이 없는지를 본다. mini-trial을 하지 않지만 단순히 fanciful한 defence는 제거한다. `Swain v Hillman [2001] 1 All ER 91`과 `Easyair Ltd v Opal Telecom Ltd [2009] EWHC 339 (Ch)`가 대표적이다.

### 7.3 Interim payment(CPR Part 25)

주요 gateway:

- defendant가 liability를 admit
- claimant가 substantial damages를 받을 judgment를 이미 확보했으나 금액 평가가 남음
- trial에서 substantial sum judgment가 예상됨

amount는 final judgment의 reasonable proportion을 넘지 않아야 하고 contributory negligence, set-off, counterclaim을 고려한다.

### 7.4 Interim injunction

`American Cyanamid Co v Ethicon Ltd [1975] AC 396` framework:

1. serious question to be tried인가?
2. damages가 claimant에게 adequate remedy인가?
3. injunction이 잘못 내려졌을 때 cross-undertaking in damages가 defendant를 적절히 보호하는가?
4. balance of convenience와 status quo

mandatory injunction, freedom of expression 등은 더 높은 주의가 필요할 수 있다.

### 7.5 Freezing injunction

자산을 보전하지만 security를 주거나 우선권을 만드는 것이 아니다. good arguable case, assets, unjustified dissipation의 real risk, just and convenient를 입증한다. 보통 without notice이므로 full and frank disclosure, cross-undertaking, return date가 핵심이다. `Mareva Compania Naviera SA v International Bulkcarriers SA [1975] 2 Lloyd’s Rep 509`, `Brink’s-MAT Ltd v Elcombe [1988] 1 WLR 1350`.

### 7.6 Search order

증거 파괴의 실제 위험이 있는 매우 예외적 구제다. extremely strong prima facie case, serious damage, incriminating material과 destruction risk가 필요하다. 독립 supervising solicitor 등 safeguards가 따른다(`Anton Piller KG v Manufacturing Processes Ltd [1976] Ch 55`).

---

## 8. Case Management

### 8.1 Overriding objective

CPR 1.1의 핵심은 cases를 justly and at proportionate cost로 처리하는 것이다. 당사자는 court가 목적을 달성하도록 돕고 orders를 준수해야 한다. active case management에는 issues identification, ADR, timetable, summary disposal, technology와 vulnerable party participation 등이 포함된다.

### 8.2 Track allocation

| Track | 정상 기준 |
|---|---|
| small claims | 보통 £10,000 이하. PI·housing 등 별도 sub-limit/예외 존재 |
| fast track | 보통 £25,000 이하, trial 1일 이하, expert evidence 제한 |
| intermediate | 보통 £100,000 이하, trial 3일 이하, expert·당사자 수 제한, 비례적 관리 가능 |
| multi-track | 그 밖의 복잡·고가·특정 제외 사건 |

금액만으로 자동 배정하지 않는다. remedy, complexity, parties, evidence, importance, parties’ circumstances를 본다(CPR 26.13). fast/intermediate에는 complexity band 1–4가 fixed recoverable costs에 영향을 준다.

### 8.3 Directions와 DQ

directions questionnaire에는 settlement/mediation, witnesses, experts, track, venue, unavailable dates, costs/complexity band 의견 등을 기재한다. failure to file하면 unless order 또는 strike out 위험이 있다.

Fast/intermediate/multi track에서는 disclosure, witness statements, expert reports, pre-trial checklist, trial window를 순서대로 관리한다. 비용이 드는 신청 전에 상대와 협의하고 proportionate alternative를 검토한다.

### 8.4 Sanctions와 relief: Denton 3단계

`Denton v TH White Ltd [2014] EWCA Civ 906`:

1. breach가 serious or significant한가?
2. why default occurred—good reason이 있는가?
3. all the circumstances, 특히 litigation의 효율·비례적 수행과 rule/order 준수 필요성

`Mitchell v News Group Newspapers Ltd [2013] EWCA Civ 1537`의 엄격성을 Denton이 구조화했다. 신청은 prompt해야 한다. 상대방은 사소한 위반을 기회주의적으로 이용하지 말아야 하며 unreasonable opposition은 costs 불이익을 받을 수 있다.

**SBA trap:** merits가 좋다는 사실만으로 relief가 주어지지 않는다. 반대로 trivial breach를 자동 치명적이라고 보아도 틀린다.

### 8.5 Costs and Case Management Conference

CCMC에서 court는 issues, directions, experts, timetable과 costs budget을 함께 관리한다. approved/agreed budget은 이후 recoverable costs의 기준점이 되고, 벗어나려면 good reason이 필요할 수 있다.

---

## 9. Evidence

### 9.1 Burden와 standard

민사사건은 주장하는 자가 balance of probabilities로 입증한다. 중대한 allegation도 별도의 형사기준으로 바뀌지 않지만, 본질적으로 가능성이 낮은 사실은 이를 입증할 더 강한 증거가 필요할 수 있다(`Re B (Children) [2008] UKHL 35`).

### 9.2 Relevance와 admissibility

relevant evidence라도 privilege, public policy, rule, case management에 의해 제한될 수 있다. 법원은 weight와 admissibility를 구별한다.

### 9.3 Hearsay

Civil Evidence Act 1995에 따라 civil proceedings에서 hearsay는 원칙적으로 admissible하지만 notice와 weight 문제가 남는다. maker를 부르지 않는 이유, contemporaneity, multiple hearsay, motive, editing 등을 평가한다. 상대는 maker의 cross-examination을 요구하거나 credibility를 공격할 수 있다(CPR Part 33).

**SBA trap:** hearsay이므로 자동 배제된다는 답은 대개 틀리다.

### 9.4 Witness statements

사실증인의 statement는 본인이 알 수 있는 사실, 정보·belief의 출처, chronological clarity, statement of truth를 갖춘다. 통상 trial에서 evidence-in-chief가 된다. 기한 내 serve하지 않으면 permission 없이는 witness를 부르지 못하거나 statement에 의존하지 못할 수 있다(CPR 32.10).

cross-examination은 보통 leading questions가 가능하다. examination-in-chief는 원칙적으로 non-leading이다. re-examination은 cross에서 나온 사항을 명확히 한다.

### 9.5 Affidavit

일부 injunction, contempt, statute/rule이 요구하는 상황에서 sworn/affirmed evidence를 사용한다. 모든 application evidence가 affidavit일 필요는 없고 witness statement가 일반적이다.

### 9.6 Expert evidence(CPR Part 35)

- court permission 없이는 expert evidence에 의존하거나 expert를 부를 수 없다.
- expert의 overriding duty는 instructing party가 아니라 court에 있다.
- report는 qualifications, instructions의 substance, materials, range of opinion, conclusions, statement of duty/understanding과 truth를 포함한다.
- court는 single joint expert를 명할 수 있다.
- 상대 expert에게 written questions는 원칙적으로 한 번, report clarification 목적, 보통 28일 내 제기한다.
- experts’ discussion은 쟁점 합의·불일치와 이유를 정리하며 당사자의 타협 협상이 아니다.

`The Ikarian Reefer [1993] 2 Lloyd’s Rep 68`은 독립성·객관성의 고전적 기준이고, `Jones v Kaney [2011] UKSC 13`은 expert witness의 의뢰인에 대한 negligence 면책을 폐지했다.

---

## 10. Disclosure, Inspection, Privilege

### 10.1 Standard disclosure(CPR 31.6)

당사자는 다음 documents를 disclose한다.

1. 자신이 rely하는 documents
2. 자신의 case에 adverse한 documents
3. 상대 case에 adverse한 documents
4. 상대 case를 support하는 documents
5. relevant practice direction이 요구하는 documents

document는 전자자료·metadata·녹음 등 정보를 기록한 모든 매체를 포함한다. control은 possession만이 아니라 document를 얻을 현재의 권리도 포함할 수 있다. disclosure duty는 proceedings 동안 계속된다.

### 10.2 List와 inspection

list에는 documents와 더 이상 control하지 않는 문서, inspection을 거부하는 문서 및 이유를 표시한다. 상대의 written notice 후 보통 7일 내 inspection/copy를 허용한다(CPR 31.15). disclosure와 inspection은 다르다: privileged document도 존재를 disclose하되 inspection을 거부할 수 있다.

### 10.3 Specific, pre-action, non-party disclosure

- specific disclosure: search, 특정 문서/범주 disclosure, 적절한 추가 단계 명령(CPR 31.12)
- pre-action disclosure: likely parties, 해당 문서가 standard disclosure 범위에 들고, 공정한 disposal·조기 해결·비용절감에 desirable(CPR 31.16)
- non-party disclosure: issues에 관련되고 adversely affect/support하며 공정한 disposal 또는 비용절감에 necessary(CPR 31.17)

### 10.4 Legal advice privilege

client와 lawyer 사이의 confidential communication이 legal advice를 주고받기 위한 것이어야 한다. ‘client’의 범위가 법인에서는 제한될 수 있다(`Three Rivers DC v Bank of England (No 5) [2003] EWCA Civ 474`). 단순 상업·행정 communication은 보호되지 않는다.

### 10.5 Litigation privilege

communication이 다음을 충족해야 한다.

1. litigation이 진행 중이거나 reasonably in contemplation
2. adversarial litigation
3. dominant purpose가 litigation을 위한 evidence/advice의 취득

lawyer-client뿐 아니라 third party communication도 가능하다. `Waugh v British Railways Board [1980] AC 521`(dominant purpose), `SFO v Eurasian Natural Resources Corp Ltd [2018] EWCA Civ 2006`(litigation contemplation/purpose)이 핵심이다.

### 10.6 Without prejudice와 offers

진정한 settlement negotiation은 without prejudice rule로 보호된다. 표제 유무가 결정적이지 않고 substance를 본다. ‘without prejudice save as to costs’는 merits 판단 전에는 보이지 않되 costs 단계에서 사용할 수 있다. 인정된 채무의 단순 지급협상은 보호되지 않을 수 있다.

### 10.7 Waiver와 inadvertent disclosure

client가 privilege를 보유한다. 문서 일부를 의도적으로 이용하면 fairness상 관련 subject matter까지 collateral waiver가 확장될 수 있다. 명백한 실수로 privileged document를 열람한 solicitor는 이용 가능성을 독단적으로 판단하지 말고 상대에게 알리고 court direction을 구해야 한다.

---

## 11. Trial과 Judgment

### 11.1 준비

- pre-trial checklist/listing questionnaire: directions 준수, witnesses/experts, estimate, special measures, settlement, timetable 확인
- trial bundle: court order/PD에 맞춰 indexed, paginated, 핵심 최신본만 포함
- witness summons(CPR 34): 출석 또는 document 제출을 강제. 충분한 notice와 conduct money 필요
- skeleton/authorities/chronology: court order와 court guide에 따라 제출

### 11.2 통상 순서

claimant opening → claimant witnesses(cross/re-exam) → defendant opening/ evidence → closing submissions → judgment → consequential orders/costs. 실제 순서는 judge의 case management에 따라 달라질 수 있다.

### 11.3 Judgment의 효과

판결은 선언·금전·injunction·specific performance·costs 등을 포함할 수 있다. 이유를 포함한 final order가 appeal과 enforcement의 출발점이다.

재소 제한:

- cause of action estoppel: 동일 cause를 다시 다투지 못함
- issue estoppel: 이전에 필수적으로 확정된 동일 issue를 같은 parties/privies가 다시 다투지 못함
- Henderson abuse: 이전 절차에서 제기했어야 할 주장을 뒤늦게 제기하는 것이 abuse인지 전체 사정을 봄

`Virgin Atlantic Airways Ltd v Zodiac Seats UK Ltd [2013] UKSC 46`은 res judicata의 범주를 설명한다. 판결 이유의 모든 말이 issue estoppel이 되는 것은 아니고, 판결에 necessary였는지 본다.

---

## 12. Costs와 Settlement Offers

### 12.1 기본 원칙

court는 costs에 폭넓은 재량을 가진다(CPR 44.2). 일반 출발점은 unsuccessful party pays successful party’s costs이나 conduct, partial success, admissible offers를 고려한다.

- standard basis: 의심은 paying party에게 유리; proportionate costs만 허용
- indemnity basis: 의심은 receiving party에게 유리; 별도 proportionality 제한 방식이 다르며 비정상적 conduct 등이 근거가 될 수 있음
- summary assessment: 보통 짧은 hearing/trial 종료 시 즉시
- detailed assessment: costs officer가 별도 절차로 평가
- small claims: 제한된 court fees, witness expenses, unreasonable conduct costs 등만 통상 회수
- fast/intermediate: 많은 사건에 fixed recoverable costs와 complexity band 적용

### 12.2 Costs budgeting

multi-track 등 적용사건에서 parties는 Precedent H를 제출하고 court는 costs management order를 할 수 있다. 예산 불제출은 통상 court fees만의 budget으로 취급되는 강한 제재 위험이 있다. 승인 예산은 costs를 보장하지 않지만 이후 assessment의 중요한 기준이다.

### 12.3 Part 36 형식

유효한 offer는:

- written
- Part 36에 따른 것임을 명시
- whole/part/issue와 counterclaim 반영 여부 표시
- 통상 최소 21일 relevant period

offer는 pre-action에도 가능하고 service될 때 made된다. trial judge는 merits를 결정할 때 offer 내용을 보지 않는다.

### 12.4 Part 36 결과표

| 상황 | 통상 결과(불공정하지 않은 한) |
|---|---|
| relevant period 내 수락 | claimant가 acceptance 시까지 costs를 받는 구조가 일반적 |
| defendant offer를 늦게 수락 | claimant는 period 만료까지 costs, 그 후 defendant costs를 부담하는 것이 일반적 |
| claimant가 trial에서 defendant offer를 이기지 못함 | period 만료 후 defendant costs + 그 costs에 대한 interest |
| claimant가 자신의 offer와 같거나 더 유리한 judgment | 만료 후 indemnity costs, damages interest(기준금리 + 최대 10%), costs interest, additional amount(최대 £75,000) |

claimant의 additional amount는 award의 첫 £500,000에 10%, 그 초과분에 5%, 총 £75,000 cap 구조다.

`Gibbon v Manchester City Council [2010] EWCA Civ 726`은 Part 36이 common-law offer와 다른 self-contained code임을 강조한다.

### 12.5 Security for costs(CPR 25.12–25.13)

defendant가 신청하며, statutory condition 중 하나와 all circumstances상 just함을 입증해야 한다. 예: claimant가 jurisdiction 밖에 거주(규정상 범위), impecunious company로 costs 지급 곤란, address 변경/미제공, assets를 옮겨 집행 곤란. genuine claim을 stifle하지 않도록 접근권과 enforcement risk를 균형한다.

### 12.6 Non-party costs

exceptional이지만 litigation을 실질적으로 통제·자금지원하고 이익을 얻으려 한 자에게 costs order가 가능할 수 있다. 해당 non-party에게 공정한 notice와 hearing 기회를 주어야 한다.

---

## 13. Appeals

### 13.1 Permission

appeal은 재심이 아니라 review가 원칙이다. permission은:

- real prospect of success, 또는
- some other compelling reason

lower court 또는 appeal court에 신청한다. 일반 appellant’s notice 기한은 decision 후 21일이지만 lower court가 달리 정할 수 있다. sealed notice service 등 세부기한은 최신 CPR 52/order를 확인한다.

### 13.2 Grounds

decision이 wrong이거나 serious procedural/other irregularity 때문에 unjust해야 한다. 단순히 appeal judge가 다른 결론을 선호할 수 있다는 것만으로 부족하다.

### 13.3 Destination과 second appeal

appeal route는 decision-maker와 court level에 따라 정해진다. leapfrog를 가정하지 않는다. second appeal은 important point of principle or practice 또는 다른 compelling reason이라는 더 높은 문턱을 가진다.

### 13.4 Appeal의 효과

appeal 제기 자체가 원판결 집행을 자동 stay하지 않는다. 필요하면 stay를 신청한다. fresh evidence는 제한적으로만 허용된다(`Ladd v Marshall [1954] 1 WLR 1489`: 합리적 노력에도 이전에 확보 불가, 중요한 영향, 신빙성).

---

## 14. Money Judgment Enforcement

### 14.1 먼저 자산을 찾는다

CPR Part 71의 order to obtain information from judgment debtor를 사용하면 debtor가 oath 아래 employment, bank accounts, property, liabilities 등에 답하고 documents를 제시하게 할 수 있다. 2026-09 SRA 명칭은 과거 ‘oral examination’ 대신 이 표현을 사용한다.

### 14.2 수단 선택

| 알려진 자산/상황 | 적합한 수단 |
|---|---|
| goods | writ/warrant of control |
| bank account 또는 제3자가 debtor에게 지급할 채무 | third party debt order |
| land·securities | charging order, 필요 시 order for sale |
| salary | attachment of earnings(주로 County Court) |
| debtor가 자산정보를 숨김 | Part 71 information order |
| 지급불능이 명확하고 threshold 충족 | bankruptcy/winding-up은 collective insolvency 수단; 단순 압박용 남용 금지 |

Enforcement는 자동이 아니다. judgment creditor가 방법을 선택하고 비용·우선순위·담보권·공동소유·면제재산을 고려한다.

---

## 15. Ethics and Professional Conduct

Dispute Resolution에서 ethics는 별도 장이 아니라 모든 단계에 침투한다.

### 15.1 Court와 상대방

- court를 오도하지 않는다. client가 거짓 evidence를 고집하면 confidentiality와 duty to court를 함께 처리하며 계속 acting 가능성을 검토한다.
- 상대·witness가 solicitor를 두었으면 부당하게 직접 접촉하지 않는다.
- documents를 파기·은닉하도록 돕지 않는다. litigation hold와 disclosure duty를 설명한다.
- without notice application에서는 client에게 불리한 material도 full and frank disclosure한다.

### 15.2 Client

- merits, procedure, costs, enforcement risk, ADR를 균형 있게 설명한다.
- litigation funding와 costs exposure를 명확히 한다.
- settlement authority를 확인한다. solicitor가 임의로 client claim을 화해하지 않는다.
- own-interest conflict, client conflict, confidentiality/disclosure 충돌을 조기에 점검한다.

### 15.3 Witness와 expert

- witness를 준비할 수 있으나 답을 coaching하거나 허위 기억을 만들면 안 된다.
- expert에게 원하는 결론을 요구하지 않는다. expert duty is to the court.
- privileged/inadvertently disclosed material을 악용하지 않는다.

---

## 16. 핵심 판례·조문 압축표

### 16.1 반드시 이름과 기능을 연결할 판례

| 판례 | 시험용 한 줄 rule |
|---|---|
| Churchill v Merthyr Tydfil CBC [2023] | 비례적이고 재판접근권 본질을 해치지 않으면 court-ordered ADR/stay 가능 |
| Halsey v Milton Keynes [2004] | ADR 거부의 합리성과 비용; 강제 ADR에 관한 과거 제한은 Churchill과 함께 읽음 |
| Dunnett v Railtrack [2002] | 승소자도 불합리한 ADR 거절로 costs 불이익 가능 |
| Pirelli v Oscar Faber [1983] | negligence property damage의 accrual은 damage 발생과 연결 |
| Haward v Fawcetts [2006] | latent damage의 knowledge는 손해의 본질적 사실에 관한 지식 |
| Barton v Wright Hassall [2018] | email/claim form 송달 규칙과 LiP에 대한 엄격 적용 |
| Abela v Baadarani [2013] | alternative service에서 service 목적과 good reason |
| Vinos v M&S [2001] | 만료 후 claim form 송달 연장은 엄격 |
| Swain v Hillman [2001] | summary judgment: real, not fanciful prospect |
| American Cyanamid [1975] | interim injunction: serious issue, adequacy of damages, balance |
| Brink’s-MAT v Elcombe [1988] | without notice full and frank disclosure |
| Denton v TH White [2014] | relief from sanctions 3단계 |
| Mitchell v NGN [2013] | rule compliance와 costs budget 제재의 엄격성 |
| FXF v English Karate [2023] | discretionary default set-aside와 Denton relevance |
| Re B (Children) [2008] | 민사 standard는 하나: balance of probabilities |
| The Ikarian Reefer [1993] | expert 독립성과 court duty |
| Jones v Kaney [2011] | expert의 client에 대한 negligence immunity 폐지 |
| Three Rivers (No 5) [2003] | corporate client와 legal advice privilege 범위 |
| Waugh v British Railways [1980] | litigation privilege dominant purpose |
| SFO v ENRC [2018] | contemplated litigation과 investigation documents |
| Summers v Fairclough [2012] | dishonest claim strike-out은 예외·비례성 필요 |
| Gibbon v Manchester CC [2010] | Part 36은 독자적 procedural code |
| Virgin Atlantic v Zodiac [2013] | res judicata/estoppel 범주 |
| Ladd v Marshall [1954] | appeal에서 fresh evidence 기준 |

### 16.2 조문 지도

| Source | 핵심 |
|---|---|
| Limitation Act 1980 ss 2, 5, 8, 11, 14, 14A, 14B, 28, 32, 33, 35 | tort/contract/deed/PI/latent damage/disability/fraud·mistake/discretion/new claims |
| Civil Evidence Act 1995 | civil hearsay admissibility와 weight |
| Arbitration Act 1996, as amended by Arbitration Act 2025 | stay, tribunal jurisdiction, award, challenge/enforcement |
| CPR Parts 1, 3 | overriding objective, case management, sanctions |
| CPR Parts 6, 7 | service, issue, particulars |
| CPR Parts 10–16 | acknowledgment, jurisdiction, default, admission, defence, statements |
| CPR Parts 17–20 | amendments, further information, parties, additional claims |
| CPR Parts 23–25 | applications, summary judgment, interim remedies |
| CPR Parts 26–29 | allocation, tracks, trial management |
| CPR Parts 31–35 | disclosure, evidence, hearsay, witnesses, experts |
| CPR Parts 36, 38, 40 | offers, discontinuance, judgments/orders |
| CPR Parts 44–47 | costs principles, fixed costs, special cases, assessment |
| CPR Part 52 | appeals |
| CPR Parts 70–73 | enforcement, information, control of goods, third-party debt, charging orders |

---

## 17. Time-limit sheet

아래는 closed-book용 핵심값이다. 문제에서 court order가 다른 날짜를 정하면 order가 우선한다.

| Event | 핵심 기한 |
|---|---:|
| claim form service within jurisdiction | issue 후 4 calendar months |
| claim form service out of jurisdiction | issue 후 6 calendar months |
| separate particulars | claim form service 후 14일 이내 + claim form 최종기한 전 |
| acknowledgment | particulars deemed service 후 14일 |
| defence without AoS | 14일 |
| defence with AoS | 28일 |
| agreed defence extension | 추가 최대 28일 |
| jurisdiction application | AoS filing 후 14일 |
| general application notice | 통상 hearing 최소 3일 전 |
| Part 36 relevant period | 최소 21일 |
| expert written questions | 통상 report service 후 28일, 한 번 |
| appellant’s notice | 통상 decision 후 21일(다른 order 없을 때) |

---

## 18. 최종 문제풀이 문장은행

- “The limitation period runs from ___, not from the claimant’s later discovery, unless ___ applies.”
- “The claimant must distinguish issue from valid service; the latter requires compliance with CPR 6 and 7.”
- “The defendant should file an acknowledgment of service and make the jurisdiction application within the CPR 11 timetable.”
- “Strike out addresses a defective or abusive statement of case; summary judgment asks whether there is a real prospect of success and a compelling reason for trial.”
- “Hearsay is not automatically inadmissible in civil proceedings; notice and weight remain material.”
- “Disclosure does not equal inspection: privileged documents are listed but inspection may be withheld.”
- “The expert’s overriding duty is to the court, not to the party paying the fee.”
- “A Part 36 offer is a self-contained procedural offer and its consequences depend on timing and the judgment obtained.”
- “An appeal does not automatically stay enforcement.”
- “Before choosing enforcement, identify the debtor’s asset: goods, bank debt, land, earnings, or insolvency.”

## 19. 10개 자가점검

1. breach 사실은 7년 전, claimant가 1년 전에 알았다. simple contract의 기본답은?  
   **답:** 지식과 무관하게 breach에서 6년이므로 prima facie time-barred.
2. claim form을 마지막 날 issue했지만 5개월 뒤 국내 송달했다.  
   **답:** limitation issue와 별도로 CPR 7.5/7.6 service failure 검토.
3. defendant가 particulars 후 12일째 AoS. defence 기한은?  
   **답:** 통상 particulars deemed service 후 28일.
4. defence는 사실상 약하지만 witness credibility가 핵심이다. summary judgment?  
   **답:** real prospect/compelling reason를 보며 credibility trial 필요성이 반대요소.
5. 독립 회계사가 litigation을 위해 작성한 report.  
   **답:** dominant purpose와 reasonable contemplation 충족 시 litigation privilege 가능.
6. hearsay이므로 배제 신청만 하면 되는가?  
   **답:** 아니다. admissible할 수 있으며 notice, cross-examination, weight 공격.
7. £80,000, 2일 trial, parties 1:1, experts 제한.  
   **답:** intermediate track 정상 후보.
8. defendant Part 36 offer를 claimant가 이기지 못했다.  
   **답:** relevant period 후 defendant costs 등 CPR 36.17 결과 검토.
9. appeal filed. judgment enforcement가 자동 중지되는가?  
   **답:** 아니다. stay 신청 필요.
10. debtor의 은행계좌가 확인됐다.  
    **답:** third party debt order가 직접적 후보.

---

## 20. 공식 출처

- SRA, SQE1 FLK1 specification applicable from 1 September 2026: https://sqe.sra.org.uk/docs/default-source/pdfs/sqe1-flk1-%28from-1-september-2026%29.pdf
- Civil Procedure Rules and Practice Directions: https://www.justice.gov.uk/courts/procedure-rules/civil
- Limitation Act 1980: https://www.legislation.gov.uk/ukpga/1980/58
- Civil Evidence Act 1995: https://www.legislation.gov.uk/ukpga/1995/38
- Arbitration Act 1996: https://www.legislation.gov.uk/ukpga/1996/23
- Arbitration Act 2025: https://www.legislation.gov.uk/ukpga/2025/4

이 자료는 학습용이다. 실제 사건의 advice에는 최신 CPR, Practice Direction, court guide, order와 commencement/transitional provisions를 별도로 확인해야 한다.
