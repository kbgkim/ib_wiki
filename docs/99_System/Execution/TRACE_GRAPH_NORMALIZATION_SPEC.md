# IB Wiki Trace Graph Normalization Specification (Patched Final)

---

## 0. MISSION

본 문서는 분산 환경에서 생성된 Trace Graph를
**완전히 결정론적인 Canonical Form으로 변환**하기 위한 규칙을 정의한다.

> **"Different executions must produce identical canonical traces if logically equivalent."**

---

## 1. Normalization Objective

다음 조건을 만족해야 한다:

* 실행 순서가 달라도 동일 결과
* UUID가 달라도 동일 결과
* 환경이 달라도 동일 결과

---

## 2. Canonical Graph Principle

정규화된 Trace는 다음 속성을 가져야 한다:

* 구조 동일성 → 동일 표현
* 순서 독립성 → deterministic ordering
* ID 독립성 → structure-based identity

---

## 3. ID Normalization (Structure-based)

### 3.1 Rule

모든 event_id는 **구조 기반 식별자**로 변환한다.

### 방식

각 이벤트의 Canonical ID는 다음으로 구성된다:

```id="c9q1he"
CANONICAL_ID = HASH(
    parent_canonical_id +
    event_type +
    domain +
    sequence_number
)
```

### RULE

* UUID 사용 금지
* 생성 순서 의존 금지
* 항상 동일 구조 → 동일 ID

---

## 4. Deterministic Ordering

### 4.1 Sorting Rule

Fork된 이벤트는 다음 기준으로 정렬한다:

1. domain (ASC)
2. event_type (ASC)
3. sequence_number (ASC)
4. canonical_id (ASC)

### RULE

* 정렬 기준은 완전 순서를 보장해야 한다
* tie 발생 금지

---

## 5. Variable Erasure

다음 필드는 제거 또는 상수화한다:

* timestamp → 제거 또는 0
* trace_id → 제거
* runtime metadata → 제거

### RULE

* 환경 의존 필드는 Hash 대상에서 제외

---

## 6. Graph Serialization (Critical)

정규화된 Graph는 반드시 Canonical JSON으로 변환된다.

### Format

```json
{
  "nodes": [
    {
      "id": "...",
      "domain": "...",
      "event_type": "...",
      "sequence": 1,
      "children": [...]
    }
  ]
}
```

### RULE

* key ordering 고정
* 배열 순서 = deterministic sorting 결과
* whitespace 제거

---

## 7. Structural Preservation

정규화 과정에서도 반드시 유지:

* causation 관계
* parent-child 구조
* domain 정보
* sequence_number

### FORBIDDEN

* 구조 변경
* 관계 손실

---

## 8. Graph Integrity Validation

정규화 전 반드시 검증:

* orphan node 없음
* cycle 없음
* 단일 root 존재

### VIOLATION

* 구조 이상 → HARD FAIL

---

## 9. Canonical Equality Definition

두 Trace가 동일하다는 의미:

```id="8zz1qp"
Canonical(Graph A) == Canonical(Graph B)
```

---

## 10. Usage

정규화된 Trace는 다음에 사용된다:

* OUTPUT_HASH_SPEC 입력값
* Determinism Validation Runner 비교 대상

---

## 11. Failure Handling

다음 발생 시 즉시 실패:

* 정규화 불가
* 정렬 불가능
* 구조 불일치

---

## 12. Final Statement

> **"Trace normalization guarantees that logical equivalence is preserved as deterministic identity."**

---
