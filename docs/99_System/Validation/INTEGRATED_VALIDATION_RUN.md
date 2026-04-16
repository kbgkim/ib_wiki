# IB Wiki Integrated Validation Run Specification

## 0. OBJECTIVE

본 문서는 [`SYSTEM_CONTRACT.md`](../Contract/SYSTEM_CONTRACT.md), [`TRACEABILITY_SPEC.md`](../Trace/TRACEABILITY_SPEC.md), [`EXECUTION_VALIDATION_SPEC.md`](./EXECUTION_VALIDATION_SPEC.md)의 **전체 통합 동작을 단일 흐름으로 검증**하기 위한 실행 시나리오를 정의한다.

> **"Validation must prove system behavior across the full lifecycle, not in isolation."**

---

## 1. Validation Scope

검증 대상은 다음 전체 라이프사이클 흐름을 포함한다.

**Event Ingestion → Validation → Processing → State Transition → Side Effect → Trace → Failure Handling → Governance**

---

## 2. End-to-End Flow Scenario (Primary)

### Scenario: FULL LIFECYCLE EXECUTION

연속적인 5단계 실행을 통해 시스템의 모든 레이어가 모순 없이 작동함을 증명한다.

#### Step 1: Valid Event Injection
- **Input**: 모든 규약을 준수하는 정상 신규 이벤트.
- **Expected Result**:
  - **Action**: **PROCESS**
  - **State**: 데이터베이스 상태 변화(Entity Update) 발생.
  - **Trace**: 새로운 Root Trace Chain 생성 성공.

#### Step 2: Duplicate Replay
- **Input**: Step 1에서 사용된 동일한 `event_id` 재전송.
- **Expected Result**:
  - **Action**: **IGNORE** (Idempotency Guard 작동)
  - **State**: 추가적인 상태 변화 없음 (NO-OP).
  - **Trace**: 기존 Trace 기록 유지 및 중복 기록 로그 생성.

#### Step 3: Transient Failure Injection
- **Input**: 실행 중 일시적 DB Lock 또는 외부 API 타임아웃 발생 상황.
- **Expected Result**:
  - **Action**: **RETRY** (Failure Handling 1순위)
  - **State**: 상태 커밋 미수행.
  - **Trace**: Retry Context를 포함한 Trace continuity 유지.

#### Step 4: DLQ Scenario
- **Input**: 페이로드 파손(Corrupted Payload) 또는 논리적 회복 불가능 오류.
- **Expected Result**:
  - **Action**: **DLQ** (Failure Handling 3순위)
  - **State**: 상태 변화 없음.
  - **Trace**: DLQ 격리 상태를 포함한 Trace chain 보존.

#### Step 5: Cross-domain Violation
- **Input**: 엔티티 식별자와 도메인이 일치하지 않는 이벤트(`domain mismatch`).
- **Expected Result**:
  - **Action**: **REJECT** (Domain Boundary Guard 작동)
  - **State**: 상태 변화 절대 금지.
  - **Trace**: 위반 사유가 포함된 Reject Trace 생성.

---

## 3. Cross-Spec Interaction Validation

### Rule Interaction Matrix

사양 간 충돌 시 시스템이 선택하는 지배적 규칙(Dominant Rule) 정의입니다.

| Interaction | Expected Dominant Rule | Reason |
| :--- | :--- | :--- |
| **Input vs Idempotency** | **Input Validation** | 원천 규약 위반이 중복 체크보다 선행함 |
| **Idempotency vs Ordering** | **Idempotency** | 중복 이벤트는 순서 검증 대상을 탈락시킴 |
| **Concurrency vs Ordering** | **Concurrency** | 버전 정합성이 논리적 순서보다 데이터 보호에 우선함 |
| **Trace vs Processing** | **Traceability** | 추적성 확보 실패 시 모든 처리 행위는 즉시 중단됨 |

---

## 4. Trace Continuity Validation

모든 통합 시나리오 단계에서 다음 사항을 보조한다.

- **Causation_id chain**: 모든 자식 이벤트는 반드시 부모의 `event_id`를 참조하여 체인을 유지한다.
- **Correlation_id persistence**: 단일 비즈니스 플로우 내의 모든 이벤트는 동일한 상관 ID를 공유한다.
- **No orphan event**: 인과 체인에서 이탈된 고립 이벤트의 발생을 절대적으로 방지한다.

---

## 5. Deterministic Flow Verification

동일 시나리오를 N회 반복 실행했을 때 다음 결과가 100% 일치해야 한다.

- 동일한 **Action** (PROCESS/REJECT/RETRY/DLQ/IGNORE)
- 동일한 **State** 결과 (데이터 정합성)
- 동일한 **Trace** 구조 (인과 그래프의 동일성)

---

## 6. Failure Propagation Validation

시스템 내의 모든 예외 상황은 반드시 다음 4대 범주 중 하나로만 수렴되어야 한다.

1.  **RETRY**: 일시적 장애, 자동 회복 가능 상황.
2.  **REJECT**: 규약 위반, 논리적 불가 상황.
3.  **DLQ**: 데이터 파손, 수동 조치 필요 상황.
4.  **IGNORE**: 중복 처리, 이미 완료된 상황.

👉 **하나의 장애에 대해 다중 분류를 허용하지 않는다.**

---

## 7. Final Verdict Rule

- **PASS**: 모든 시나리오 단계에서 단 하나의 결정론적 결과가 산출됨.
- **FAIL**: 단 한 지점이라도 모호성(Ambiguity) 또는 비결정적 분기 발생.

---

## 8. Final Statement

> **"Integrated validation confirms the system behaves deterministically across full lifecycle execution."**

---

## 9. Validation Trigger Rules

다음 조건 발생 시 Integrated Validation Run은 반드시 자동 실행되어야 한다.

- [`SYSTEM_CONTRACT.md`](../Contract/SYSTEM_CONTRACT.md) 변경
- [`TRACEABILITY_SPEC.md`](../Trace/TRACEABILITY_SPEC.md) 변경
- [`EVENT_HANDLER_SPEC.md`](../../06_Execution_Flow/EVENT_HANDLER_SPEC.md) 변경
- 신규 도메인 추가
- 배포 전 Pre-release 단계

### RULE

- Trigger 발생 시 Validation 미실행 → HARD VIOLATION

---

## 10. Failure Handling Integration

Validation 실패 시 다음 규칙을 적용한다.

- 즉시 배포 중단 (Deployment Block)
- 현재 계약 상태 INVALID 선언
- 자동 Rollback Trigger (Governance Policy 연동)

### RULE

- FAIL 상태에서 시스템 실행 지속 → FORBIDDEN

---

## 11. Execution Model

Integrated Validation Run은 다음 단위로 실행된다.

- Execution Unit: Full Scenario Batch
- Isolation: 독립된 Validation Context에서 실행
- Data Scope: Production 데이터와 완전 분리

### RULE

- Validation 실행은 실제 운영 상태에 영향을 주어서는 안 된다

