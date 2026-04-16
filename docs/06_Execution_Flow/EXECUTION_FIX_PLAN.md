# 분산 시스템 안정성 계층 상세 명세 (Execution Fix Plan)

## 1. 개요 (Overview)
본 문서는 IB Wiki의 이벤트 기반 아키텍처를 분산 환경에서도 안전하게 실행하기 위한 **4대 안정성 계층(Safety Layer)**의 운영 원칙을 정의합니다. 중복, 충돌, 순서 붕괴 상황으로부터 데이터 무결성을 보호하는 것이 목적입니다.

---

## 2. Layer 1: Idempotency Layer (멱등성)

모든 비즈니스 이벤트는 **1회만 의미 있게 처리**되어야 합니다.

- **Deduplication Key**: `event_id` (UUID)
- **Processed Event Store**: 정합성 보장을 위해 처리 완료된 `event_id`를 최소 24시간 동안 저장하는 저장소(Event Store/Cache)를 상정함.
- **Handling Logic**:
    - 수신된 `event_id`가 Store에 존재하면: **REJECT (Duplicate)** - 로그 후 즉시 종료 (NO-OP).
    - 존재하지 않으면: 실행 후 처리 완료 상태로 Store에 기록.

---

## 3. Layer 2: Concurrency Control Layer (동시성)

동일한 `entity_id`에 대해 여러 핸들러가 동시에 상태를 업데이트하려 할 때 데이터 유실을 방지합니다.

- **Optimistic Locking**: 페이로드의 `entity_version` 필드를 활용.
- **Validation Logic**:
    - `Payload.entity_version`과 현재 시스템의 `Current_Version`을 비교.
    - **Match**: 업데이트 수행 및 `Version + 1` 증가.
    - **Mismatch**: **REJECT (Stale Update Error)** - 현재 데이터가 페이로드보다 최신이거나 중복된 이전 버전임.

---

## 4. Layer 3: Ordering / Sequencing Layer (순서 보장)

분산 큐에서 순서가 뒤바뀌어 도착한 이벤트를 논리적 순서에 따라 처리합니다.

- **Ordering Metadata**: `sequence_number`.
- **Handling Policy**:
    - **Late Event (Lower Sequence)**: 이미 더 높은 시퀀스가 처리된 경우 해당 지연 이벤트는 **DISCARD (Late Event)** 처리. (단, 멱등성 계층에서 이미 필터링될 가능성이 높음)
    - **Gap Detection**: 누락된 시퀀스가 발견될 경우 현재 스텝을 **BUFFER**하고 선행 이벤트 수신을 대기하거나 DLQ로 전송.

---

## 5. Layer 4: Failure & Recovery Layer (오류 복구)

실행 중 발생하는 각종 예외 상황에 대한 표준 대응 절차입니다.

- **Retry Policy**:
    - **Retryable Errors**: 일시적 데이터베이스 락(Lock), 네트워크 타임아웃. (Exponential Backoff 적용)
    - **Non-Retryable Errors**: 로직 오류, 데이터 유효성 위반, 버전 비일관성. (즉시 중단 및 DLQ행)
- **Dead Letter Queue (DLQ)**: 처리 실패한 이벤트를 영구 격리하여 분석용으로 보관.
- **Compensation**: 복잡한 트랜잭션 실패 시 이전 상태로 되돌리는 보상 이벤트를 정의함.

---

## 🔗 연결
- [글로벌 이벤트 페이로드 표준](./EVENT_PAYLOAD_STANDARD.md)
- [이벤트 핸들러 실행 명세](./EVENT_HANDLER_SPEC.md)
