# IB Wiki Determinism Proof Specification

## 0. OBJECTIVE

본 문서는 시스템이 **완전한 결정론적 행동을 수행함을 증명**하기 위한 논리 구조를 정의한다.

> **"Determinism must be proven, not assumed."**

---

## 1. Determinism Definition

본 시스템에서 결정론(Determinism)은 다음 수식으로 상시 성립되어야 한다.

**동일 입력 (Input) + 동일 상태 (State) → 동일 결과 (Output)**

---

## 2. Decision Tree Mapping

모든 입력은 반드시 다음의 결정론적 트리를 통과하며, 중첩되거나 누락된 경로 없이 하나의 행동으로 수렴한다.

1.  **Invalid Input Detection**: 규약 위반 입력 시 즉각 **REJECT**.
2.  **Duplicate Check**: 처리 이력 존재 시 즉각 **IGNORE**.
3.  **Transient Failure Check**: 일시적 장애 감지 시 **RETRY**.
4.  **Unrecoverable Detection**: 복구 불가 논리 오류 시 **DLQ**.
5.  **Else**: 모든 가드를 통과한 경우에만 **PROCESS**.

---

## 3. Uniqueness Proof

각 입력은 시스템 내에서 **단 하나의 실행 경로**만을 선택할 수 있다.

- 시스템은 병렬 가드(Guard)가 아닌 **직렬 가드 파이프라인**을 사용한다.
- 각 단계는 배타적(Exclusive)이며, 하나의 결과가 도출되는 즉시 하위 단계 실행을 중단한다.
- 결과적으로 동일 이벤트에 대해 다중 경로 선택(Ambiguity)은 물리적으로 불가능하다.

---

## 4. Rule Priority Proof

결정론적 일관성을 확보하기 위해 다음의 우선순위를 엄격히 준수한다.

1.  **Input Validation**: 데이터의 원천 규약 적합성을 우선 검증한다.
2.  **Idempotency (Duplicate)**: 동일 작업의 중복 수행을 차단한다.
3.  **Failure Classification**: 장애 유형을 선분류하여 실행 지속 여부를 결정한다.
4.  **Processing**: 모든 안전 장치가 통과된 상태에서만 비즈니스 로직을 실행한다.

---

## 5. Conflict Resolution Proof

보완적 또는 상충적 규칙 결합 시 다음의 해결 원칙을 따른다.

- **Input > Duplicate**: 입력 규약 위반이 중복 체크보다 우선하여 오염된 데이터의 입항을 차단한다.
- **Duplicate > Ordering**: 중복 수신된 이벤트는 순서 검증 절차 이전에 무시된다.
- **Concurrency > Ordering**: 엔티티 버전 정합성 검증이 비즈니스 순서 검증보다 우선하여 데이터의 물리적 손상을 방지한다.

---

## 6. Non-Determinism Elimination

결과를 예측 불가능하게 만드는 모든 요소를 규약 차원에서 원천 배제한다.

- **시간 기반 로직 금지**: `timestamp`를 분기나 순서의 결정 로직으로 사용하지 않는다 (오직 `sequence_number`만 허용).
- **랜덤 처리 금지**: 모든 비즈니스 수식 및 분기에는 랜덤 변수를 개입시키지 않는다.
- **외부 상태 의존 금지**: 특정 시점의 외부 시스템 API 상태나 비영속화된 전역 변수에 의존하는 분기를 금지한다.

---

## 7. State Consistency Proof

시스템의 모든 상태 변화는 다음을 통해 무결성을 증명한다.

- **Event-driven**: 모든 상태 변화는 반드시 기록된 이벤트를 원인으로 한다.
- **Trace-driven**: 인과 식별자(`causation_id`)가 없는 상태 변화를 원천 차단한다.
- **Versioned Content**: 엔티티 버전 검증을 통과한 경우에만 최종 커밋(Commit)이 허용된다.

---

## 8. Trace Determinism

**동일 입력 → 동일 Trace Chain 생성**

- 추적 데이터 생성 로직은 시스템 클록이나 인프라 ID에 의존하지 않으며, 입력 데이터의 식별자를 기반으로 결정론적으로 그래프를 구성한다.

---

## 9. Side Effect Determinism

- 모든 사이드 이펙트(외부 시스템 통지 등)는 상태 커밋(State Commit)이 성공한 이후에만 실행된다.
- 사이드 이펙트 실행 로직은 반드시 **멱등(Idempotent)**이어야 하며, 시스템 재시도 시에도 중복 부작용을 유발하지 않아야 한다.

---

## 10. Proof Conclusion

IB Wiki 시스템에 입력되는 모든 이벤트는 논리적 설계에 의해 다음을 보장받는다.

- **하나의 Action** (유일한 실행 결과)
- **하나의 State** (예측 가능한 데이터 변화)
- **하나의 Trace** (증명 가능한 원인 분석)

---

## 11. Final Statement

> **"This proof confirms that the system produces a single deterministic outcome for every valid and invalid input."**

---

*최종 업데이트: 2026-04-16 (Determinism Fully Proven)*
