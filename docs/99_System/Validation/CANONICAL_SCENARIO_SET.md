# IB Wiki Canonical Scenario Set

## 0. OBJECTIVE

본 문서는 시스템 검증의 기준이 되는 **표준 시나리오 집합**을 정의한다.

> "Random tests find bugs. Canonical tests prove correctness."

---

## 1. Scenario Categories

### 1.1 Normal Flow
- 정상 이벤트 처리
- 상태 변화 발생
- Trace chain 생성

### 1.2 Boundary Condition
- 최소/최대 값 테스트
- edge case 처리

### 1.3 Failure Flow
- invalid input
- domain violation
- ordering failure

### 1.4 Recovery Flow
- retry → success
- retry → DLQ

---

## 2. Scenario Requirements

각 시나리오는 반드시 포함:

- Input Payload
- Initial State
- Expected Action
- Expected State
- Expected Trace

---

## 3. Determinism Baseline

- 모든 Canonical Scenario는 Determinism 검증 기준으로 사용
- Hash 결과는 항상 동일해야 한다

---

## 4. Coverage Rule

- 모든 Guard 최소 1회 이상 포함
- 모든 Failure Type 최소 1회 포함

---

## 5. Regression Rule

- 변경 이후 모든 Scenario 재실행 필수
- 기존 결과와 불일치 시 FAIL

---

## 6. Versioning

- Scenario도 Version 관리 대상
- 변경 시 Validation 필요

---

## 7. Final Statement

> "Canonical scenarios define the ground truth of system behavior."