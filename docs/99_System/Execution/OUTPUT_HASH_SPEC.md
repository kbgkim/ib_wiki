# IB Wiki Output Hashing Specification

## 0. MISSION
시스템의 실행 결과가 결정론적임을 수학적으로 입증하기 위해, 실행 결과물의 **지문(Fingerprint)**을 생성하는 해싱 규약을 정의한다.

## 1. Hash Components
최종 해시(Unified Hash)는 다음 세 부분의 결합으로 생성된다.

### 1.1 State Delta Hash
- 실행 후 변경된 엔티티의 상태 값을 캐노니컬 JSON(Canonical JSON)으로 변환 후 해싱.
- 변경된 필드와 값의 정렬이 항상 일정해야 함.

### 1.2 Normalized Trace Hash
- [`TRACE_GRAPH_NORMALIZATION_SPEC.md`](./TRACE_GRAPH_NORMALIZATION_SPEC.md)에 의거하여 정규화된 트레이스 데이터를 해싱.
- 비결정론적 식별자가 제거된 순수 인과 구조를 반영.

### 1.3 Event Metadata Hash
- 입력된 원본 이벤트의 식별 정보를 포함.

## 2. Hashing Algorithm
- **Algorithm**: SHA-256
- **Format**: HEX String (Lowercase)

## 3. Strict Determinism
- 단 1비트의 차이라도 발생할 경우 시스템은 비결정적(Non-deterministic)으로 간주된다.
- 해시 불일치는 **ARCHITECTURE VIOLATION**으로 보고된다.
