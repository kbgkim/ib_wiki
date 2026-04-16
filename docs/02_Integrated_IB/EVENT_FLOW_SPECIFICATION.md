# IB 동적 이벤트 흐름 시스템 명세 (Event Flow Specification)

## 1. 개요 (Execution Flow Overview)

본 명세서는 IB Wiki의 정적 지식을 '실행 가능한 시스템 흐름'으로 전환하기 위한 동적 모델을 정의합니다. Audit 결과를 반영하여 **표준 페이로드 규격**과 **정량화된 트리거 로직**을 강제 적용함으로써 엔진 구현의 결정성(Determinism)을 확보합니다.

### 🔄 실행 아키텍처 (The Flow Loop)
`Scenario Trigger` → `Event Entry(Standard Payload)` → `Handler Execution(Logic Spec)` → `State Change` → `Next Trigger Validation` → `Sequence Continue`

---

## 2. Global Event Payload Standard

모든 시스템 이벤트는 **[글로벌 이벤트 페이로드 표준](../06_Execution_Flow/EVENT_PAYLOAD_STANDARD.md)**을 반드시 준수해야 합니다.

```json
{
  "event_id": "UUID-12345",
  "event_type": "FUNDING_EXECUTED",
  "domain": "PF",
  "entity_id": "DEAL-PF-001",
  "timestamp": "2026-04-16T14:30:00Z",
  "correlation_id": "CORR-999",
  "payload": {
    "amount": 100000000,
    "pre_sale_rate": 0.45
  }
}
```

---

## 3. Scenario-based Event Flow Sequences

시나리오 발생 시 각 자산군을 관통하는 이벤트의 선후 관계를 정의합니다.

### S1: Interest Rate Shock (금리 쇼크 시나리오)
1. **[Global]** `INTEREST_RATE_UP` (Macro Trigger: Benchmark Rate +100bp)
2. **[Equity]** `MTM_SHOCK_EVENT` (Valuation < 50% of Book Value)
3. **[ABS]** `CASH_TRAP_TRIGGER` (DSCR < 1.05)
4. **[PF]** `PRE_SALE_SHORTFALL` (Presale Rate < 30%)
5. **[PF]** `PROJECT_FAILURE` (Transition to DELINQUENT)
6. **[NPL]** `RECOVERY_INITIATED` (Transfer to NPL Domain)

---

## 4. Event Handler Definitions (상세 로직)

모든 이벤트의 실행 로직은 **[이벤트 핸들러 실행 명세](../06_Execution_Flow/EVENT_HANDLER_SPEC.md)**에 통합 관리됩니다. 각 핸들러는 다음을 수행합니다.
- 포지션 및 딜 상태 변경 (State Update)
- 리스크 지표(PD, LGD)의 방향성 조정
- 후행 이벤트 트리거 검증

---

## 5. Event Trigger Rules (Next Event Logic)

이벤트 간의 결정적(Deterministic) 전이 조건입니다.

| Source Event | Next Event | Trigger Condition (Quantitative Threshold) |
| :--- | :--- | :--- |
| `PRE_SALE_SHORTFALL` | `PROJECT_FAILURE` | `Presale_Rate < 30%` |
| `PROJECT_FAILURE` | `RECOVERY_INITIATED` | `Default_Event = TRUE` (이자 유예 종료 시) |
| `RECOVERY_INITIATED` | `PORTFOLIO_ACQUIRED` (NPL) | `Asset_Seizure_Confirmed = TRUE` |
| `CASH_TRAP_TRIGGER` | `CASH_TRAP_RELEASE` | `DSCR > 1.15` (연속 2회 충족 시) |
| `MTM_SHOCK_EVENT` | `INVESTMENT_WRITE_OFF` | `Solvency_Check = FAIL` (Residual Value < Debt) |

---

## 🔗 연결
- [통합 리스크 전파 명세](./Synthesis_Map.md)
- [표준 온톨로지 정의](../00_Standard_Layer/Core_Definitions.md)

### ─────────────

*최종 업데이트: 2026-04-16 (Audit 결함 해결 및 표준 통합)*
