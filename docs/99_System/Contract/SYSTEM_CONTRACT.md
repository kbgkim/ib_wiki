# IB Wiki System Contract (Final Freeze)

## 0. RULE ZERO (최상위 절대 규칙)

본 규칙은 시스템 내의 다른 어떤 규칙보다 우선(Override)하며, 시스템의 모든 행동의 준거가 된다.

> **"If a behavior is not explicitly defined → it is forbidden."**

- 시스템 내에서 정의되지 않은 모든 모호함은 유효하지 않은 상태(Invalid System State)로 간주한다.
- 어떤 암시적 행동(Implicit Behavior)도 허용되지 않으며, 모든 결과는 본 계약에 명시된 규칙에 의해서만 결정되어야 한다.
- 모든 Edge Case는 반드시 본 계약 내에 명시적으로 정의된 규칙에 의해 단 하나의 결정론적 결과로 수렴되어야 한다.

---

## 1. Contract Overview (계약 개요)
본 문서는 IB Wiki 이벤트 기반 시스템의 모든 동작 규칙을 원자적이고 변경 불가능하도록 고정하는 **최종 실행 규약(System Contract)**이다. 본 계약은 시스템의 입행, 상태 전이, 안정성 보장 및 실패 대응에 관한 최고 수준의 법(Law)으로 기능한다.

- **적용 대상**: IB Wiki 핵심 이벤트 처리 엔진 및 리스크 분석 시스템.
- **시스템 경계**: 외부 데이터 소스로부터 이벤트를 수신하는 입항(Ingestion) 레이어부터 상태가 영속화(Persistence)되는 전 단계까지를 포함한다.

---

## 2. Core System Principles (최상위 시스템 원칙)
- **Determinism is mandatory**: 동일한 입력과 상태에 대해 시스템은 항상 동일한 결과를 도출해야 한다.
- **Ambiguity is invalid state**: 시스템은 선택지가 존재하거나 결과가 불확실한 상태를 유지할 수 없다.
- **Explicit rule only**: 시스템의 모든 행동은 반드시 명문화된 규칙에 근거한다.

---

## 3. Event Input Contract (이벤트 입력 규약)
- **event_id**: 전역적으로 유일(Globally Unique)해야 하며, UUID 형식을 준수해야 한다.
- **entity_id**: 필수 필드이며 Null을 허용하지 않는다.
- **domain**: 반드시 `{PF, ABS, NPL, Equity}` 중 하나의 값을 가져야 한다.
- **invalid input**: 상기 제약 조건 중 하나라도 위반하는 입력은 즉시 **REJECT** 처리한다.

---

## 4. Event Processing Contract (이벤트 처리 규약)
- **Exactly-once processing**: 모든 이벤트는 정확히 1회만 비즈니스 로직에 반영되어야 한다.
- **Idempotent ignore**: 중복된 `event_id` 수신 시 시스템은 즉시 **IGNORE** 처리하며, 기존 처리 결과에 영향을 주지 않는다.
- **Deterministic handler**: 핸들러의 실행 논리는 외부 변수(현재 시간 등)에 의존하지 않고 오직 페이로드와 현재 상태에 의해서만 결정되어야 한다.
- **Side-effect control**: 핸들러 실행 중 발생하는 모든 부수 효과는 상태 전이가 확정된 후에만 실행되어야 한다.

---

## 5. Failure Handling Contract (실패 처리 규약 - STRICT)

모든 실패 상황은 예외 없이 아래의 4가지 분류 중 **정치 단 하나(Exactly One)**로만 분류되어야 하며, 중복 분류는 엄격히 금지된다.

1.  **RETRY**: 일시적이고 자동 복구가 가능한 실패 (예: 네트워크 타임아웃, DB 락 경합).
2.  **REJECT**: 입력 규약 위반, 권한 부재, 유효하지 않은 상태 전이 시도 (예: Domain mismatch).
3.  **DLQ (Dead Letter Queue)**: 논리적으로 처리가 불가능하거나 데이터가 손상되어 수동 분석이 필요한 실패.
4.  **IGNORE**: 이미 성공적으로 처리된 중복 이벤트 또는 결정론적으로 영향이 없는 재현 요청.

---

## 6. Concurrency Contract (동시성 규약)
- **entity_version**: 모든 엔티티는 버전 정보를 포함해야 하며, 모든 업데이트 페이로드는 `entity_version`을 필수 포함해야 한다.
- **Stale update**: 페이로드의 버전이 현재 시스템 상태의 버전과 일치하지 않을 경우 시스템은 반드시 **REJECT** 처리한다.
- **Deterministic resolution**: 동시 업데이트 시 먼저 도착하여 성공한 이벤트를 승인하며, 이후 도착 건은 버전 불일치로 자동 거절된다.

---

## 7. Ordering Contract (순서 보장 규약)
- **Ordering Base**: 시스템은 `sequence_number`를 기준으로 메시지의 논리적 순서를 검증한다.
- **Selection Rule (MANDATORY)**:
    - **BUFFER**: 지연된 이벤트가 유효 범위(Threshold) 내에 있고 선행 이벤트가 없는 경우 대기.
    - **REJECT**: 이벤트 시퀀스에 수용 불가능한 공백(Gap)이 있거나 이미 더 높은 시퀀스가 처리된 경우.
    - **DISCARD**: 복구가 불가능한 순서 손실이 발생하여 시퀀스의 완결성을 보장할 수 없는 경우.

---

## 8. Cross-Domain Contract (도메인 격리 규약)
- **Isolation**: `{PF, ABS, NPL, Equity}`는 상호 독립적인 상태 머신을 유지해야 한다.
- **Domain mismatch**: 페이로드의 `domain` 필드와 대상 엔티티의 실제 도메인이 불치할 경우 시스템은 반드시 **REJECT** 처리한다.
- **Correlation_id**: 상관 식별자는 추적(Tracing) 목적으로만 사용되며, 도메인 간의 직접적인 상태 변경 트리거로 직접 사용될 수 없다.

---

## 9. Idempotency Contract (멱등성 규약)
- **Deduplication mandatory**: 모든 핸들러 입항 단계에서 `event_id` 기반 중복 체크를 반드시 수행한다.
- **Ignore-only**: 중복된 이벤트에 대해 시스템은 성공 응답을 반환하되, 실제 상태 변경이나 부수 효과는 발생시키지 않는 **NO-OP**를 유지한다.
- **Retry context**: 재시도(Retry)는 실패한 건에 대한 재실행이나, 중복(Duplicate)은 성공한 건에 대한 재입력으로 엄격히 구분한다.

---

## 10. State Transition Contract (상태 전이 규약)
- **Explicit trigger**: 엔티티의 상태 변경은 오직 비즈니스 이벤트에 의해서만 발생할 수 있다.
- **No direct mutation**: DB 직접 수정 등 이벤트를 거치지 않는 모든 상태 변경은 금지된다.
- **Invalid transition**: 정의된 상태 전이 모델(Lifecycle)을 벗어나는 모든 전이 시도는 **REJECT** 처리한다.

---

## 11. Violation Rules (위기 관리 규칙)

### [HARD FAIL]
- 데이터 손상(Corruption) 발견 시.
- 교차 도메인 오염(Cross-domain contamination) 발생 시.
- 상태 불비(State inconsistency) 감지 시.
- **Then**: 시스템 정지 및 즉시 경보 발생.

### [SOFT FAIL]
- **When**: 일시적 오류(Transient error) 발생 시 → **RETRY**.
- **When**: 제어된 실패(Controlled failure / Logical error) 발생 시 → **DLQ**.

### [IGNORE]
- **When**: 멱등성 중복 이벤트 수신 시 → **IGNORE (NO-OP)**.
- **When**: 안전한 재현(Safe replay) 요청 시 → **IGNORE (Success status only)**.

---

### Decision Rule (절대 결정 트리)
1. 입력 규약을 위반했는가? (Invalid input) → **REJECT**
2. 이미 처리된 중복인가? (Duplicate) → **IGNORE**
3. 시스템 장애 등 일시적 실패인가? (Transient failure) → **RETRY**
4. 논리적 오류로 복구가 불가능한가? (Unrecoverable) → **DLQ**
5. **그 외(Else)** → **PROCESS**

---

## 12. Final Enforcement Statement (최종 선언)

본 계약에 정의되지 않은 모든 행동은 엄격히 금지된다.

> **"Any behavior not explicitly defined in this Contract is strictly forbidden."**

---

## 🔗 Rule Hierarchy (규칙 계층 구조)
1. **RULE ZERO** (Highest Absolute Priority)
2. **System Contract** (본 문서)
3. **TRACEABILITY SPEC** ([`TRACEABILITY_SPEC.md`](../Trace/TRACEABILITY_SPEC.md))
4. **Safety Layer Rules** ([`EXECUTION_FIX_PLAN.md`](../../06_Execution_Flow/EXECUTION_FIX_PLAN.md))
5. **Domain Rules** (Lifecycle Specifications)
6. **Scenario Rules** ([`EVENT_FLOW_SPECIFICATION.md`](../../02_Integrated_IB/EVENT_FLOW_SPECIFICATION.md))

---

*최종 봉인 시각: 2026-04-16 (Final Freeze)*
