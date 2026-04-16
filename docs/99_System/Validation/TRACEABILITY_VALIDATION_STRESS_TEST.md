# IB Wiki TRACEABILITY VALIDATION STRESS TEST

## 1. Validation Objective

본 문 문서는 [`TRACEABILITY_SPEC.md`](../Trace/TRACEABILITY_SPEC.md)가 [`SYSTEM_CONTRACT.md`](../Contract/SYSTEM_CONTRACT.md)와 충돌 없이 동작하며, 모든 상태 변화가 반드시 추적 가능함을 검증한다.

---

## 2. Core Principle

- **Trace Chain Integrity 유지**: 모든 비즈니스 흐름은 단절 없는 인과 체인을 형성해야 한다.
- **System Contract Decision Tree 준수**: 추적성 검증 결과는 시스템 계약의 결정 트리와 동기화되어야 한다.
- **Deterministic Outcome 보장**: 동일 입력에 대해 상시 동일한 Trace Graph와 행동 결과를 보장한다.

👉 **단 하나라도 위반 시 HARD FAIL로 처리한다.**

---

## 3. Test Layers

### Layer 1: Trace Field Integrity
필수 Trace 필드(`event_id`, `correlation_id`, `causation_id`, `entity_id` 등)의 존재 및 유효성 검증.

### Layer 2: Trace Chain Integrity
`causation` 필드와 `correlation` 구조를 통한 부모-자식 관계 및 흐름의 완결성 검증.

### Layer 3: Trace vs Contract Interaction
멱등성(Idempotency), 순서(Ordering) 규칙과 추적성 규칙이 충돌하는 상황에서의 처리 정합성 검증.

### Layer 4: Failure Trace Continuity
Retry, DLQ, Reject 상황에서 원본 인과 관계가 소실되지 않고 유지되는지 검증.

### Layer 5: Cross-Domain Isolation
도메인 간 Trace 공유 시에도 상태 격리 원칙이 훼손되지 않는지 검증.

---

## 4. Deterministic Test Cases

### TC-T01: Missing Trace Field
- **Input**: `correlation_id = NULL`
- **Expected Result**:
  - **Action**: **REJECT**
  - **Reason**: Mandatory Trace Field Missing (Violation of Rule 3)

---

### TC-T02: Invalid causation_id
- **Input**: 해당 시스템에 존재하지 않는 `causation_id` 참조.
- **Expected Result**:
  - **Action**: **HARD FAIL**
  - **Reason**: Trace Chain Break (Violation of Rule 7)

---

### TC-T03: Orphan Event
- **Input**: `causation_id = NULL`이나 기존 `correlation_id`가 존재하는 흐름의 중간 이벤트.
- **Expected Result**:
  - **Action**: **REJECT**
  - **Reason**: Root Rule Violation (Violation of Rule 4.4)

---

### TC-T04: Duplicate Event
- **Input**: 이미 처리된 기존 `event_id` 재전송.
- **Expected Result**:
  - **Action**: **IGNORE**
  - **Trace Status**: 기존 Trace 유지 (Duplicate Entry Logged)
  - **State Change**: NO-OP

---

### TC-T05: Retry with New event_id
- **Input**: 재시도(Retry) 요청이나 새로운 `event_id`를 생성하여 전송.
- **Expected Result**:
  - **Action**: **REJECT**
  - **Reason**: Retry Rule Violation (Violation of Rule 6.1)

---

### TC-T06: Side Effect without Trace
- **Execution**: `event_id`와 연결되지 않은 직접적인 DB 수정 또는 외부 API 호출 시도.
- **Expected Result**:
  - **Action**: **HARD FAIL**
  - **Reason**: Untraceable State Change (Violation of Rule 0)

---

### TC-T07: Cross-Domain Causation
- **Input**: 다른 도메인의 이벤트를 부모(`causation_id`)로 참조하는 비정상적 시도.
- **Expected Result**:
  - **Action**: **REJECT** (Domain Boundary Violation)

---

### TC-T08: Cycle Creation
- **Execution**: `A → B → C → A` 형태의 인과 순환 참조 구성 시도.
- **Expected Result**:
  - **Action**: **HARD FAIL**
  - **Reason**: Cycle Detected (Violation of Rule 4.3)

---

### TC-T09: Timestamp Ordering Attack
- **Execution**: 현재 시점보다 미래 또는 과거의 `timestamp`를 가진 이벤트의 역전 주입.
- **Expected Result**:
  - **Action**: **PROCESS**
  - **Reason**: `timestamp`는 참조용이며, 순서(Ordering)는 `sequence_number`로만 결정함 (Violation of Rule 3.2 아님)

---

### TC-T10: DLQ Re-injection
- **Input**: `causation_id` 정보가 유실되었거나 손상된 DLQ 이벤트의 재주입.
- **Expected Result**:
  - **Action**: **DLQ** (수동 조치 전까지 격리 유지)

---

### TC-T11: Multi Conflict
- **Input**: `duplicate` + `invalid causation_id` + `domain mismatch`가 병발한 이벤트.
- **Expected Result**:
  - **Action**: **REJECT** (Decision Tree 계층 우선순위에 따른 거절)

---

### TC-T12: Full Trace Reconstruction
- **Execution**: 정상적인 Root-Child 인과 관계 시퀀스 주입.
- **Expected Result**:
  - **Forward Trace**: 모든 자식 이벤트 도달 가능.
  - **Backward Trace**: Root 이벤트까지 역추적 성공.
  - **Full Flow Reconstruction**: 단일 `correlation_id`로 전체 그래프 복원 성공.

---

## 5. Cross-Layer Conflict Priority

규칙 간 상충 발생 시 승리 규칙(Winner) 매트릭스입니다.

| Conflict | Winner | Reason |
| :--- | :--- | :--- |
| **Invalid Input vs Trace** | **Input Guard** | 입항 규약 검증이 추적성 체인 검증보다 선행함 |
| **Trace Break vs Retry** | **Trace Guard** | 추적성 단절은 일시적 장애가 아니므로 HARD FAIL 처리 |
| **Duplicate vs Ordering** | **Idempotency** | 중복 체크가 순서 검증보다 우선하여 IGNORE 처리 |
| **Domain vs Trace** | **Domain Guard** | 도메인 경계 위반 차단이 추적성 유지보다 우선함 |

---

## 6. Determinism Rule

- 모든 입력은 결정론적 추적 그래프(Deterministic Trace Graph)를 생성한다.
- 추적 기록 행위 자체가 시스템 상태에 비결정론적 영향을 주어서는 안 된다.

---

## 7. Final Verdict

다음 중 하나라도 발생 시 **FAIL**로 판정한다:

- Trace Chain의 논리적 단절.
- `event_id` 없는 Side Effect 발생.
- `causation_id` 참조의 불일치.
- 동일 입력에 대한 비결정적 결과 발생.

---

## 8. Final Statement

**"A system that cannot prove its causality cannot guarantee its correctness."**
