# IB Wiki Adversarial Stress Test Report (2026-04-16)

본 보고서는 IB Wiki의 이벤트 기반 시스템 설계가 비정상적인 입력, 동시성 충돌, 데이터 오염 등의 적대적 상황(Adversarial Cases)에서 어떻게 붕괴되는지 탐지한 '파괴 중심'의 스트레스 테스트 결과입니다.

## 1. Overall Robustness Score: 45 / 100
- **판정**: **BROKEN (System Collapse Likely)**
- **요약**: 정상 흐름(Golden Path)에 대해서는 완벽히 작동하나, 분산 시스템의 고질적 문제인 중복 발생, 순서 역전, 동시성 충돌에 대한 방어 기제(Guard)가 전무하여 실제 운영 환경에서는 시스템 붕괴 위험이 매우 높음.

---

## 2. Scenario Breakdown Results

### (1) Out-of-Order Delivery (순서 역전)
- **상태**: **FRAGILE**
- **현상**: `LOAN_DEFAULT`가 `PROJECT_FAILURE`보다 먼저 수신될 경우, `ACTIVE` 상태 가드만 통과하면 부실 전처리(`DELINQUENT` 핸들러 로직)를 건너뛰고 상환 불능 처리됨.
- **결과**: 워터폴(Waterfall) 중단 등 선행 리스크 관리 로직이 실행되지 않은 채 상태가 전이됨.

### (2) Duplicate Event Injection (중복 주입)
- **상태**: **BROKEN**
- **현상**: 동일 `event_id`로 동일 이벤트가 2회 주입될 경우, 핸들러가 이를 중복 실행함 (Idempotency 부재).
- **결과**: `Next Event`가 중복 트리거되거나, 리스크 지표가 이중으로 감액/증액되는 데이터 오염 발생.

### (3) Missing Event Collapse (이벤트 누락)
- **상태**: **ROBUST**
- **현상**: `LOAN_APPROVED` 없이 `FUNDING_EXECUTED` 발생 시도.
- **결과**: **SUCCESS (Rejected)**. `Lifecycle.md`의 Pre-condition 가드(`Approved` 상태 체크)가 정상 작동하여 비정상 실행을 차단함.

### (4) Concurrent Event Collision (동시성 충돌)
- **상태**: **BROKEN**
- **현상**: 동일 딜에 대해 `CASH_TRAP_TRIGGER`와 `INTEREST_RATE_UP`이 동시에 Risk Level을 업데이트하려고 시도함.
- **결과**: **Race Condition 발생**. 낙관적 잠금(Optimistic Locking)이나 버전 관리 필드가 없어 '마지막에 쓴 데이터'가 이전 업데이트를 덮어씀 (Lost Update).

### (5) Cross-Domain Contamination (도메인 오염)
- **상태**: **FRAGILE**
- **현상**: PF 도메인이 이미 NPL로 전이되었음에도 불구하고, 지연된 PF 이벤트(`PRE_SALE_SHORTFALL`)가 수신됨.
- **결과**: `domain` 필드 검증 로직이 핸들러에 명시되지 않아, NPL 상태인 개체의 PF 지표가 오염될 가능성 존재.

---

## 3. Critical Break Points
- **Idempotency (멱등성) 부재**: `event_id`를 통한 중복 처리 방지 로직이 설계 명세에 누락됨.
- **Concurrency Control 부재**: 전 비즈니스 개체에 대해 `version` 필드가 페이로드와 핸들러 로직에서 정의되지 않음.

---

## 4. Race Condition Findings
- **발견 사항**: `Risk_Level` 및 `Cash_Reserve` 업데이트 핸들러. 다수의 시나리오가 동시에 발생할 경우 실제 현금 흐름 잔액과 시스템상 데이터 간의 불일치(Inconsistency)가 발생할 수 있는 치명적 지점임.

---

## 5. Idempotency Failures
- `EVENT_HANDLER_SPEC.md`의 공통 로직에서 `event_id` 로깅만 수행할 뿐, 중복 여부 확인 및 거절(Reject) 프로세스가 정의되지 않음.

---

## 6. Cross-Domain Violations
- 시나리오 `S1`에서 거시 리스크가 전 자산군으로 퍼질 때, 공통 `correlation_id`를 통해 서로 다른 도메인의 핸들러가 상충하는 업데이트를 수행할 우려가 있음 (Isolation Guard 부재).

---

## 7. Missing Guards (누락된 보호 장치)
- **Reject Logic**: Validation 실패 시 시스템이 어떤 Fallback을 취해야 하는지(Ignore / Dead Letter Queue / Retry) 정의되지 않음.
- **Ordering Guard**: 이벤트 선후 관계를 보장하기 위한 `sequence_number` 또는 `logical_clock` 부재.

---

## 8. Final Verdict (BROKEN)

> [!CAUTION]
> **검증 판정: BROKEN**
> 본 시스템 설계는 정밀한 논리 설계는 훌륭하나, **'분산 환경의 불확실성'**에 대한 내성이 전혀 없음. 메시지 중복 및 순서 붕괴 상황에서 데이터 정합성을 유지할 수 없으므로, 운영 환경 적용 전 **멱등성(Idempotency) 및 동시성 제어(Concurrency Control)** 섹션의 추가가 필수적임.
