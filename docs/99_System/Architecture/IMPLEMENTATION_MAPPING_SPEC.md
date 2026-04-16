# IB Wiki Implementation Mapping Specification

## 0. OBJECTIVE

본 문서는 모든 Spec을 실제 시스템 구현 컴포넌트로 매핑하여, 설계와 구현 간의 단절을 제거한다.

> "A spec not mapped to implementation is not real."

---

## 1. Mapping Principle

- 모든 규칙은 반드시 하나 이상의 구현 위치를 가져야 한다.
- 하나의 규칙이 여러 레이어에 분산 구현되는 것을 금지한다.
- 상세 실행 규약은 [SYSTEM_CONTRACT.md](../Contract/SYSTEM_CONTRACT.md)를 준수한다.

---

## 2. Core Mapping Table

| Spec Rule | Implementation Layer | Component |
|----------|--------------------|----------|
| Input Validation | API Layer | Request Validator |
| Idempotency | Persistence Layer | Inbox Table / Dedup Store |
| Ordering | Domain Layer | Aggregate Sequence Check |
| Concurrency | Domain Layer | Version Check |
| Traceability | Event Layer | Event Envelope |
| Causation Chain | Event Layer | Event Metadata |
| Determinism | Handler Layer | Pure Function Handler |
| Side Effect | Infra Layer | Outbox Pattern |
| Retry | Messaging Layer | Retry Queue |
| DLQ | Messaging Layer | Dead Letter Queue |

---

## 3. Layer Definition

### 3.1 API Layer
- 입력 검증 수행
- invalid request 차단

### 3.2 Event Layer
- Trace metadata 생성
- event_id / correlation_id 관리

### 3.3 Domain Layer
- 상태 전이 수행
- version / sequence 검증

### 3.4 Persistence Layer
- 상태 저장
- idempotency 보장

### 3.5 Messaging Layer
- Retry / DLQ 처리

### 3.6 Infra Layer
- 외부 시스템 연동
- Side Effect 실행

---

## 4. Deterministic Handler Rule

- 모든 Handler는 Pure Function 형태여야 한다:
  
  Input + State → Output

- 외부 의존성 직접 호출 금지

---

## 5. Outbox Enforcement

- Side Effect는 반드시 Outbox를 통해 수행
- State Commit 이후에만 실행

---

## 6. Anti-Pattern (FORBIDDEN)

- Handler 내부 DB 직접 업데이트
- Event 없이 상태 변경
- 외부 API 결과로 분기 결정

---

## 7. Trace Mapping Rule

- 모든 로그는 event_id 기반으로 기록
- Trace와 로그 불일치 금지
- 문서 작성 및 명명 규칙은 [STYLE_GUIDE.md](../STYLE_GUIDE.md)를 따른다.

---

## 8. Final Statement

> "Implementation must be a direct projection of specification."