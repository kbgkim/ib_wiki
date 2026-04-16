# IB Wiki Determinism Validation Runner Specification (Patched Final)

---

## 0. MISSION

본 문서는 동일한 입력과 상태에 대해 시스템이 항상 동일한 결과를 도출하는지 검증하는
**Determinism Validation Runner**의 실행 규약을 정의한다.

> **"Determinism must be proven through repeated identical execution."**

---

## 1. Determinism Definition

다음 식이 항상 성립해야 한다:

**(Input, Initial State) → Identical Output**

Output은 다음 3가지의 결합으로 정의된다:

* **Action**
* **State**
* **Trace**

---

## 2. Execution Unit

* **Input Pair**: `(Event_Payload, Initial_State)`
* **Execution Run**: 동일 입력을 독립된 환경에서 반복 실행

### STRICT RULE

* 최소 실행 횟수: **N ≥ 10,000**
* 2회 비교만으로 PASS 판정 금지
* 모든 실행은 동일 초기 상태에서 시작해야 한다

---

## 3. Execution Environment Control

Determinism 보장을 위해 실행 환경을 고정한다.

### REQUIRED

* 동일 DB Snapshot
* 동일 Event Store 상태
* 동일 Config
* 동일 코드 버전

### FORBIDDEN

* 외부 API 상태 의존
* 시스템 시간 기반 분기
* 랜덤 값 사용

---

## 4. Execution Pipeline

```
1. Environment Reset
2. Input Injection
3. Event Processing
4. Result Collection
5. Output Normalization
6. Hash Generation
7. Result Comparison
```

---

## 5. Result Collection

각 실행에서 다음을 수집한다:

### 5.1 Action

* PROCESS / REJECT / RETRY / DLQ / IGNORE

### 5.2 State

* Entity Snapshot (최종 상태)
* State Delta (변경 내용)

### 5.3 Trace

* event_id chain
* causation graph
* correlation grouping

---

## 6. Output Normalization

비교 가능성을 위해 모든 출력은 정규화되어야 한다.

### RULE

* JSON deterministic serialization
* key ordering 고정
* timestamp 제거 또는 고정값 치환
* null/empty 표준화

---

## 7. Output Hash Definition

```
OUTPUT_HASH = HASH(
    Action +
    Normalized State +
    Normalized Trace
)
```

### RULE

* 동일 입력 → 동일 Hash
* Hash mismatch → FAIL

---

## 8. Determinism Comparison

### Algorithm

```
baseline = first_run_hash

FOR i in N:
    run(input)
    current_hash = hash(output)

    IF current_hash != baseline:
        → NON-DETERMINISM
        → HARD FAIL
```

---

## 9. Trace Determinism Validation

Trace 구조 자체도 동일해야 한다.

### VALIDATION

* 동일 event_id chain
* 동일 causation_id 연결
* 동일 correlation_id grouping

### VIOLATION

* 구조 불일치 → FAIL

---

## 10. Concurrency Determinism

동시성 상황에서도 동일 결과를 보장해야 한다.

### TEST

* 동일 이벤트 동시 실행
* race condition 유도

### EXPECTED

* 동일 Action
* 동일 State
* 동일 Trace

---

## 11. Failure Classification Determinism

모든 실행 결과는 반드시 다음 중 하나로 수렴해야 한다:

* PROCESS
* REJECT
* RETRY
* DLQ
* IGNORE

### RULE

* 다중 결과 금지
* ambiguous 결과 → FAIL

---

## 12. Non-Determinism Detection

다음 발생 시 즉시 실패:

* Hash mismatch
* State mismatch
* Trace mismatch
* Action mismatch

---

## 13. Reporting

Runner는 다음 정보를 출력해야 한다:

* Total Runs
* Pass Count
* Fail Count
* First Failure Iteration
* Diff Analysis:

  * Action Diff
  * State Diff
  * Trace Diff

---

## 14. Final Verdict

### PASS

* 모든 실행 결과 Hash 동일

### FAIL

* 단 하나라도 불일치 발생

---

## 15. Final Statement

> **"Determinism is proven only when identical execution produces identical results without exception."**

---
