# IB Wiki Specification Consistency Matrix

## 0. OBJECTIVE

본 문서는 시스템 내 모든 Spec 간의 충돌 가능성을 제거하고, 단일한 지배 규칙(Dominant Rule)을 정의한다.

> "No two specs may produce conflicting outcomes."

---

## 1. Consistency Principle

- 모든 Spec은 상호 배타적이지 않아야 한다.
- 동일 입력에 대해 다중 Action이 발생하는 상황은 **FORBIDDEN**이다.
- 충돌 발생 시 반드시 우선순위에 의해 단일 결과로 수렴해야 한다.

---

## 2. Dominant Rule Hierarchy

우선순위는 다음과 같다:

1. **RULE ZERO** ([SYSTEM_CONTRACT.md](../Contract/SYSTEM_CONTRACT.md))
2. **SYSTEM CONTRACT** ([SYSTEM_CONTRACT.md](../Contract/SYSTEM_CONTRACT.md))
3. **TRACEABILITY SPEC** ([TRACEABILITY_SPEC.md](../Trace/TRACEABILITY_SPEC.md))
4. **RUNTIME ENFORCEMENT** ([FAIL_FAST_POLICY.md](../Runtime/FAIL_FAST_POLICY.md))
5. **EXECUTION VALIDATION** ([INTEGRATED_VALIDATION_RUN.md](../Validation/INTEGRATED_VALIDATION_RUN.md))
6. **DOMAIN RULES** (Lifecycle Specifications)

---

## 3. Conflict Resolution Matrix

| Conflict Case | Dominant Rule | Result |
|--------------|--------------|--------|
| Invalid Input vs Duplicate | Input Validation | REJECT |
| Duplicate vs Ordering | Idempotency | IGNORE |
| Ordering vs Concurrency | Concurrency | REJECT |
| Trace Missing vs Processing | Traceability | HARD FAIL |
| Runtime vs Validation | Runtime Enforcement | Runtime Decision |
| Domain Rule vs System Contract | System Contract | Contract Decision |

---

## 4. Trace vs Reject Rule

- REJECT된 이벤트라도 반드시 Trace는 기록되어야 한다.
- 상태 변화는 없지만, Trace는 존재해야 한다.

---

## 5. DLQ vs Retry Conflict

- Recoverable → RETRY
- Non-recoverable → DLQ
- 동시에 만족할 경우 → DLQ 우선

---

## 6. Ambiguity Elimination Rule

- 하나의 입력은 반드시 하나의 Action으로 귀결된다.
- 다중 Action 가능성 발견 시 → SPEC ERROR → 즉시 수정 필요

---

## 7. Cross-Spec Integrity Rule

- 모든 Spec은 이 Matrix를 기준으로 재검증되어야 한다.
- Matrix와 불일치하는 Spec 존재 시 → HARD FAIL

---

## 8. Final Statement

> "Consistency across specs guarantees a single deterministic system behavior."