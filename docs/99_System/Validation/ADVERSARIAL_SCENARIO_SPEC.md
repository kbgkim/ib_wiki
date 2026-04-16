# IB Wiki Adversarial Scenario Specification

## 0. OBJECTIVE

본 문서는 시스템 계약의 **적대적 환경에서의 복원력(Resilience)**을 검증하기 위한 비정상 입력 생성 규칙을 정의한다.

> **"If a system survives adversarial input, it is truly deterministic."**

---

## 1. Adversarial Strategy

모든 테스트 시나리오 생성은 다음 원칙을 엄격하게 따른다:

- **최대 충돌 유도**: 시스템 가드(Guard) 간의 판단 우선순위를 테스트하기 위해 보완적인 충돌 상황을 유도한다.
- **다중 규칙 위반 동시 발생**: 단일 위반이 아닌 다중 레이어 위반을 동시에 주입한다.
- **비정형 조합 생성**: 정해진 경로 외의 랜덤하고 비정상적인 필드 조합을 생성한다.

---

## 2. Mutation Rules

이벤트 페이로드 변조를 위한 핵심 규칙입니다.

### 2.1 Field Mutation
- **NULL injection**: 필수 필드(`event_id`, `correlation_id` 등)에 의도적으로 NULL 주입.
- **Invalid enum**: 도메인 규약에 없는 유효하지 않은 문자열 주입.
- **Random UUID collision**: 기존 처리된 `event_id`와 동일한 UUID를 고의로 생성하여 주입.

### 2.2 Logical Mutation
- **Invalid causation_id**: 존재하지 않거나 현재 흐름과 무관한 인과 관계 식별자 주입.
- **Mismatched domain**: 엔티티의 실제 소속과 다른 도메인 이벤트 전송.
- **Stale version**: 현재 엔티티 버전보다 낮은 구버전 정보 주입.

---

## 3. Conflict Injection Rules

시스템 레이어 간의 충돌을 명시적으로 유도하는 조합 규칙입니다.

- **Duplicate + Invalid Input**: 이미 처리된 ID를 사용하면서 내의 필드는 규약을 위반하도록 변조.
- **Retry + DLQ condition**: 일시적 복구 가능 장애 상황에서 데이터 자체가 파손된 페이로드를 주입.
- **Ordering violation + Concurrency violation**: 이전 시퀀스 번호를 사용하면서 동시에 엔티티 버전도 과거 시점으로 조작.
- **Cross-domain + Trace break**: 도메인 경계를 위반하면서 인과 체인(`causation_id`)도 고의로 누락시킴.

---

## 4. Composite Scenario Generator

복합 시나리오 생성 모델의 예시입니다.

### Example Scenario A:
- **Input**:
    - `event_id`: duplicate (이미 처리됨)
    - `entity_version`: stale (구버전)
    - `domain`: mismatch (도메인 불일치)
    - `sequence_number`: out-of-order (순서 붕괴)
- **Expected Outcome**:
    - **Action**: **REJECT** (Input/Domain violation 우선순위가 Idempotency/Concurrency보다 선행함)

---

## 5. Worst Case Scenario

시스템이 맞닥뜨릴 수 있는 극한의 위반 상황 정의입니다.

- **Conditions**:
    - `invalid input` (필드 파손)
    - `duplicate` (중복 수신)
    - `stale version` (버전 불일치)
    - `broken trace` (인과 관계 단절)
    - `ordering gap` (순서 공백)
- **Expected Outcome**:
    - **Action**: **REJECT** (Step 1 Guard Layer에 의해 즉시 거절)

---

## 6. Randomized Edge Generator

결정론적 결과를 유지하면서 무작위성을 부여하는 원칙입니다.

- 랜덤하게 선택된 필수 필드 제거 시도.
- 랜덤한 식별자 충돌 상황 생성.
- 랜덤한 순서 붕괴 주입.
- **STRICT RULE**: 어떠한 랜덤 조합이 생성되더라도, 시스템의 판단 결과는 항상 단 하나의 결정론적 Action으로 수합되어야 한다.

---

## 7. Validation Rule

모든 적대적 입력(Adversarial Input)은 반드시 다음을 만족해야 한다.

- 시스템의 어떠한 비정상적인 상태 전이도 유발해서는 안 된다.
- 무단 사이드 이펙트(Side Effect) 발생을 100% 차단해야 한다.
- **결과**: 반드시 단 하나의 명시적인 **Action**으로 수렴해야 한다.

---

## 8. Failure Classification Enforcement

적대적 검증의 결과는 어떠한 모호성 없이 반드시 다음 4대 범주 중 하나로만 분류되어야 한다.

1.  **RETRY**: 일시적 지연으로 위장한 적대적 상황.
2.  **REJECT**: 명백한 규약 위반 상황 (가장 선호되는 적대적 거절).
3.  **DLQ**: 복구가 불가능한 고의적 데이터 파손 상황.
4.  **IGNORE**: 이미 처리된 정보를 이용한 적대적 재전송 상황.

---

## 9. Final Statement

> **"Adversarial validation proves system resilience under undefined and hostile conditions."**

---

## 10. Adversarial Execution Loop

Adversarial Scenario는 단일 실행이 아닌 반복 실행을 통해 검증되어야 한다.

### Execution Model

- Iteration Count: N (최소 10,000 이상 권장)
- Input Generation: 매 Iteration마다 Mutation + Conflict 조합 생성
- Evaluation: 각 실행 결과를 즉시 판정

### RULE

- 단일 실행 기반 검증은 INVALID
- 반복 실행 중 단 하나라도 비결정적 결과 발생 시 FAIL

---

## 11. Deterministic Assertion Rules

각 실행 결과는 반드시 다음 조건을 만족해야 한다:

- 동일 조건 → 동일 Action
- 동일 조건 → 동일 State
- 동일 조건 → 동일 Trace

### VIOLATION

- 결과 불일치 발생 → NON-DETERMINISM → HARD FAIL

---

## 12. Stress Level Definition

Adversarial 테스트는 3단계로 구분된다:

### Level 1: Basic Conflict
- 단일 규칙 위반

### Level 2: Multi Conflict
- 2~3개 규칙 동시 위반

### Level 3: Chaos Level
- 모든 규칙 위반 + 랜덤 조합

### RULE

- Level 3까지 통과하지 못하면 시스템은 Production Ready가 아니다

--

## 13. Coverage Guarantee Rule

Adversarial Generator는 다음을 보장해야 한다:

- 모든 필드에 대해 최소 1회 이상 Mutation 수행
- 모든 Guard 조합에 대해 최소 1회 Conflict 발생
- 모든 Failure Type(RETRY/REJECT/DLQ/IGNORE) 최소 1회 유도

### RULE

- 커버되지 않은 영역 존재 → VALIDATION INCOMPLETE

--- 

*최종 업데이트: 2026-04-16 (Resilience Mastery Defined)*
