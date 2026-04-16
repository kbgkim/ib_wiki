# ABS 라이프사이클 및 이벤트 모델 명세

## 1. 개요 (Overview)
본 문서는 ABS(자산유동화) 딜의 생애주기를 상태 전이(State Transition)와 비즈니스 이벤트(Event) 관점에서 정의합니다. 모든 이벤트는 **정량적 트리거**와 **정합성 검증 레이어**를 통해 실행 가능한 시스템 사양으로 명세화되었습니다.

---

## 2. State Machine (상태 전이 모델)

ABS 딜의 상태는 자산 풀링과 유동화 증권 발행 단계에 따라 다음과 같이 전이됩니다.

```mermaid
stateDiagram-v2
    [*] --> SOURCING: 유동화 대상 자산 선별
    SOURCING --> POOLING: 자산 풀(Pool) 구성
    POOLING --> STRUCTURING: 트랜치 설계 및 SPV 설립
    STRUCTURING --> ISSUANCE: 신용평가 및 증권 발행
    
    state ISSUANCE {
        [*] --> ACTIVE: 정상 상환 및 관리
        ACTIVE --> CASH_TRAP: 트리거 발생 (Trap)
        CASH_TRAP --> ACTIVE: 리워크/정상화 (Release)
        ACTIVE --> AMORTIZATION: 순차 상환 진행
        AMORTIZATION --> "DEFAULT": 상환 불능 (Default)
    }
    
    ISSUANCE --> CLOSED: 법인 청산/상환 완료
    "DEFAULT" --> NPL_TRANSFER: 부실 자산 매각
    
    %% Invalid Transitions
    SOURCING --> ISSUANCE: [Error] 구조화 없이 발행 불가
    ACTIVE --> POOLING: [Error] 발행 후 자산 풀 변경 금지
```

---

## 3. Full Event Catalog & Validation Layer

| Event Name | Pre-condition (필수 상태/데이터) | Trigger Condition (정량적/결정적) | Post-state | Invalid Transition |
| :--- | :--- | :--- | :--- | :--- |
| **POOL_FINALIZED** | `SOURCING` / `Asset_List` | 대상 자산군 확정 및 실사 완료 | `POOLING` | `ISSUANCE`로 직전이 |
| **TRUE_SALE_SIGNED** | `POOLING` / `Legal_Opinion` | 자산 양도 계약 체결 | `STRUCTURING` | `SOURCING` 상태 |
| **SECURITIES_ISSUED** | `STRUCTURING` / `Credit_Rating` | 유동화증권 발행 및 매각 완료 | `ACTIVE` | `POOLING` 상태 |
| **CASH_TRAP_TRIGGER** | `ACTIVE` / `DSCR` | **DSCR < 1.05** 또는 연체율 > 5.0% | `CASH_TRAP` | `CLOSED` 상태 |
| **CASH_TRAP_RELEASE** | `CASH_TRAP` / `Reserve_Balance`| **DSCR > 1.15** 및 리저브 충족 | `ACTIVE` | `SOURCING` 상태 |
| **DEFAULT_DECLARED** | `ACTIVE` or `AMORTIZATION` | **선순위 이자 미지급 > 5영업일** | `"DEFAULT"` | `POOLING` 상태 |
| **REDEMPTION_FINAL** | `AMORTIZATION` / `Zero_Balance` | 최종 트랜치 원리금 상환 완료 | `CLOSED` | `POOLING` 상태 |

---

## 4. 리스크 전이 논리 (Event Logic)

### 가. 정합성 검증 규칙 (Validation Rules)
1. **정량적 트리거 우선**: `CASH_TRAP` 진입과 해제는 계량 지표(DSCR 등)에 의해 자동 판정됨.
2. **트리거 배타성**: `CASH_TRAP` 상태에서는 `AMORTIZATION` 이벤트 스케줄링이 자동 일시 중단됨.
3. **법적 절연 필수**: `SECURITIES_ISSUED`는 반드시 `TRUE_SALE_SIGNED` 로그가 존재해야 트리거 가능.

---

## 🔗 연결
- [이벤트 핸들러 실행 명세](../../06_Execution_Flow/EVENT_HANDLER_SPEC.md)
- [ABS 도메인 기초 및 명세](./Basics.md)

### ─────────────

*최종 업데이트: 2026-04-16 (Audit 결함 해결 및 트리거 정량화)*
