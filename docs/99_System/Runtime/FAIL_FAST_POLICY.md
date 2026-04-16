# IB Wiki Fail-Fast Policy

## 0. OBJECTIVE

본 문서는 시스템이 오류를 감지하는 즉시 실행을 중단하여 비정상 상태 확산을 방지하는 Fail-Fast 전략을 정의한다.

> "Fail early, fail clearly, fail deterministically."

---

## 1. Fail-Fast Principle

- 오류는 가능한 한 가장 빠른 단계에서 탐지되어야 한다.
- 오류를 허용하고 진행하는 것은 **FORBIDDEN**이다.
- 모든 실패 분류는 [SYSTEM_CONTRACT.md](../Contract/SYSTEM_CONTRACT.md)의 규격을 따른다.

---

## 2. Fail Stages

### 2.1 Input Stage
- 필수 필드 누락
- invalid domain

→ 즉시 REJECT

---

### 2.2 Pre-Processing Stage
- duplicate event_id

→ IGNORE

---

### 2.3 Processing Stage
- trace chain 단절
- causation_id 오류

→ HARD FAIL (즉시 중단)

---

### 2.4 State Transition Stage
- version mismatch
- sequence violation

→ REJECT

---

### 2.5 Post-Processing Stage
- side effect 실패

→ RETRY 또는 DLQ

---

## 3. Fail Priority

1. Input Error
2. Trace Error
3. Concurrency Error
4. Business Rule Error

---

## 4. No Recovery Rule

- REJECT된 이벤트는 복구되지 않는다
- Retry는 transient failure에만 허용

---

## 5. Error Isolation

- 하나의 이벤트 실패는 다른 이벤트에 영향 주지 않는다
- 글로벌 상태 오염 금지

---

## 6. Logging Rule

- 모든 실패는 반드시 event_id 기반 기록
- 실패 원인 명확히 남길 것
- 추적 연쇄(Trace Chain) 무결성은 [TRACEABILITY_SPEC.md](../Trace/TRACEABILITY_SPEC.md)에 의거하여 검증한다.

---

## 7. Deterministic Failure Rule

- 동일 오류 → 동일 실패 결과
- 실패 또한 결정론적이어야 한다

---

## 8. Final Statement

> "A system that does not fail fast cannot be trusted."