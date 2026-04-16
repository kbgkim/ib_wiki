# IB Wiki Traceability Specification (TRACEABILITY_SPEC.md)

## 0. TRACEABILITY RULE ZERO (ABSOLUTE TRACE GUARANTEE)

> **"Every state change MUST be fully traceable back to its originating event."**

- 시스템 내 모든 상태 변화(State Change)는 반드시 하나의 `event_id`에 의해 설명 가능해야 한다.
- 추적 불가능한 상태 변화(Untraceable Mutation)는 **INVALID SYSTEM STATE**로 간주한다.
- 모든 이벤트는 **End-to-End Trace Chain**을 형성해야 한다.
- Trace가 단절되는 순간 해당 흐름 전체는 **HARD VIOLATION**으로 간주한다.

---

## 1. Traceability Objective

본 문서는 IB Wiki 시스템에서 발생하는 모든 이벤트, 상태 변화, 실패 및 재시도를 **완전하게 추적 가능(Full Traceability)**하도록 하기 위한 규약을 정의한다.

**목표:**
- 모든 상태 변화의 원인(Event)을 역추적 가능하게 한다.
- 분산 환경에서도 이벤트 흐름을 단일 체인으로 재구성 가능하게 한다.
- 장애, DLQ, Retry 흐름까지 포함한 **전체 Lifecycle Trace**를 확보한다.

---

## 2. Core Trace Model

Trace는 다음 4개 식별자를 기반으로 구성된다.

### 2.1 event_id (Primary Trace Key)
- 모든 이벤트의 고유 식별자.
- 시스템 내 단일 실행 단위.

### 2.2 correlation_id (Flow Trace Key)
- 동일 비즈니스 흐름을 연결하는 상위 식별자.
- 여러 이벤트를 하나의 Flow로 묶는다.

### 2.3 causation_id (Parent Event Link)
- 현재 이벤트를 발생시킨 원인 이벤트.
- 이벤트 간 인과 관계를 구성한다.

### 2.4 entity_id (State Anchor)
- 상태 변화가 발생하는 대상 엔티티.
- Trace의 상태 기준점이 된다.

---

## 3. Mandatory Trace Fields (STRICT)

모든 이벤트는 아래 필드를 반드시 포함해야 한다.

- **event_id** (REQUIRED, UNIQUE)
- **correlation_id** (REQUIRED)
- **causation_id** (REQUIRED or NULL for root)
- **entity_id** (REQUIRED)
- **domain** (REQUIRED)
- **sequence_number** (REQUIRED)
- **entity_version** (REQUIRED)
- **timestamp** (REQUIRED)

### [RULE]
- 하나라도 누락 시 → **REJECT**.
- Trace 필드는 수정 불가능하며 불변(IMMUTABLE)이어야 한다.

## 3.1 State Change Definition (MANDATORY)

- State Change는 다음으로 정의된다:
  - Persistent Storage의 값이 변경되는 모든 행위
  - 시스템 외부로 Side-effect를 발생시키는 모든 행위

### RULE

- 위 조건 중 하나라도 만족하면 반드시 event 기반이어야 한다
- 정의되지 않은 상태 변화는 **FORBIDDEN**

## 3.2 Logical Time Rule (MANDATORY)

- timestamp는 참조용이며 ordering 기준이 아니다
- 모든 순서는 sequence_number로만 결정한다

### RULE

- timestamp 기반 ordering 금지
- timestamp는 Trace 기록 목적에 한정한다

---

## 4. Trace Chain Construction Rules

### 4.1 Root Event
- `causation_id = NULL`.
- 새로운 Flow를 시작하는 모든 이벤트는 Root가 된다.

### 4.2 Child Event
- `causation_id = parent.event_id`.
- 부모 이벤트와의 동일 `correlation_id`를 의무적으로 유지한다.

### 4.3 Chain Integrity
- 모든 이벤트는 단일 부모만 가져야 한다.
- 순환 참조(Cycle)는 엄격히 **금지(FORBIDDEN)**된다.
- 끊어진 Chain은 **INVALID**로 처리한다.

## 4.4 Chain Completeness Rule

- 모든 event는 반드시 하나의 trace chain에 속해야 한다
- orphan event는 허용되지 않는다

### VIOLATION

- chain에 연결되지 않은 event → HARD FAIL
---

## 5. End-to-End Trace Guarantees

시스템은 반드시 다음을 보장해야 한다.

- **Forward Trace**: 특정 이벤트로부터 이후 발생한 모든 파생 이벤트를 추적 가능해야 한다.
- **Backward Trace**: 특정 상태로부터 해당 상태를 유발한 원인 이벤트까지 역추적 가능해야 한다.
- **Full Flow Reconstruction**: 하나의 `correlation_id`를 조회하여 전체 비즈니스 흐름을 재구성할 수 있어야 한다.

---

## 6. Trace in Failure Scenarios

### 6.1 Retry
- 동일 `event_id`를 유지한다.
- `retry_count`만 증가시키며 기존 Trace Chain을 유지한다.

### 6.2 DLQ
- 원본 이벤트 페이로드를 그대로 보존한다.
- DLQ 이동 행위 자체는 새로운 이벤트 생성이 아닌, 상태 추적의 연장선으로 취급한다.

### 6.3 Reject
- 상태 변화는 없으나, 해당 이벤트가 수신되어 거절되었다는 Trace 기록은 반드시 남겨야 한다.

## 6.4 Side Effect Trace Rule

- 모든 Side Effect는 반드시 event_id와 연결되어야 한다
- Side Effect는 독립적으로 실행될 수 없다

### RULE

- Trace 없는 Side Effect → HARD VIOLATION
- 동일 event_id에 대한 Side Effect는 반드시 멱등이어야 한다

---

## 7. Trace Consistency Rules

- `event_id`는 시스템 내에서 절대 재사용할 수 없다.
- `correlation_id`는 전체 Flow 단위로 고정되어야 한다.
- `causation_id`는 반드시 시스템 내에 존재하는 `event_id` 중 하나여야 한다.

### [VIOLATION]
- 존재하지 않는 `causation_id` 참조 시 → **HARD FAIL**.
- 도메인 간 비정상적인 인과 관계 연결 시 → **REJECT**.

---

## 8. Cross-Domain Trace Rules

- `correlation_id`는 도메인(PF, ABS, NPL, Equity) 간 공유가 가능하다.
- 그러나 상태 변경(State Mutation)은 각 도메인의 격리된 영억 내에서만 수행되어야 한다.
- **RULE**: Trace는 공유 가능하지만, 상태 전이는 공유할 수 없다.

---

## 9. Observability Requirements

Trace는 단순 저장이 아니라 관찰 가능해야 하며, 시스템은 다음 뷰(View)를 지원해야 한다.

- **Event Timeline View**: 시간순 이벤트 발생 내역.
- **Entity State Evolution View**: 특정 엔티티의 상태 변화 이력.
- **Correlation Flow Graph**: 비즈니스 흐름의 시각적 인과 지도.

---

## 10. Trace Storage Contract

- 모든 Trace 데이터는 영속화(Persistence)되어야 한다.
- 데이터 삭제는 금지되며, 오직 추가만 가능한 **Append-only** 방식을 따른다.

### [Retention Rule]
- 최소 보관 기간 내에 데이터를 삭제하는 행위는 **HARD VIOLATION**으로 간주한다.

---

## 11. Violation Handling

- **HARD VIOLATION**: Trace Chain 단절, `causation_id` 불일치, Trace 없는 상태 변화.
    - **조치**: 시스템 신뢰성 붕괴로 간주하여 처리 중단.
- **SOFT VIOLATION**: timestamp 지연, 로그 누락(논리 체인은 유지됨).
    - **조치**: Audit 대상으로 표시하여 추후 보정.

---

## 12. Final Enforcement Statement

> **"If a state change cannot be traced, it must not exist."**

---

## 13. Integration with System Contract

Traceability는 [`SYSTEM_CONTRACT.md`](../Contract/SYSTEM_CONTRACT.md)의 하위가 아닌 **동등한 강제 계층(Parallel Enforcement Layer)**으로 작동한다.

### [Hierarchy]
1. RULE ZERO
2. [`SYSTEM_CONTRACT.md`](../Contract/SYSTEM_CONTRACT.md)
3. **TRACEABILITY SPEC**
4. SAFETY LAYER
5. DOMAIN RULES

---

## 14. Deterministic Trace Guarantee

- 동일한 입력에 대해서는 항상 동일한 Trace 구조가 생성되어야 한다.
- Trace 기록 행위 자체도 결정론적(Deterministic)이어야 한다.

---

## 15. Final Statement

> **"Trace is not logging. Trace is the proof of system truth."**
