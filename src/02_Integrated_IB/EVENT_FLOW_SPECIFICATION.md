# IB 동적 이벤트 흐름 시스템 명세 (Event Flow Specification)

## 1. 개요 (Execution Flow Overview)

본 명세서는 IB Wiki의 정적 지식을 '실행 가능한 시스템 흐름'으로 전환하기 위한 동적 모델을 정의합니다. 모든 비즈니스 사건은 독립적으로 존재하지 않으며, 특정 시나리오에 의해 트리거되어 일련의 **이벤트 시퀀스(Sequence)**를 형성하고, 각 노드에서 정의된 **핸들러(Handler)**를 통해 시스템의 상태를 변화시킵니다.

### 🔄 실행 아키텍처 (The Flow Loop)
`Scenario Trigger` → `Event Entry` → `Handler Logic` → `State Change` → `Next Trigger Validation` → `Sequence Continue`

---

## 2. Canonical Event Payload Schema

모든 시스템 이벤트는 도메인에 관계없이 다음의 표준 JSON 데이터 규격을 준수해야 합니다.

```json
{
  "header": {
    "event_id": "UUID-12345",
    "event_name": "FUNDING_EXECUTED",
    "timestamp": "2026-04-16T14:30:00Z",
    "priority": "HIGH",
    "source_system": "DEAL_ENGINE"
  },
  "context": {
    "deal_id": "DEAL-PF-001",
    "asset_type": "PF",
    "exposure_id": "EXP-99",
    "current_state": "UNDER_REVIEW"
  },
  "payload": {
    "amount": 100000000,
    "currency": "KRW",
    "ref_id": "LOAN-CONTRACT-SK-01",
    "specific_attributes": {
       "pre_sale_rate": 0.45,
       "completion_rate": 0.12
    }
  }
}
```

---

## 3. Scenario-based Event Flow Sequences

시나리오 발생 시 각 자산군을 관통하는 이벤트의 선후 관계를 정의합니다.

### S1: Interest Rate Shock (금리 쇼크 시나리오)
1. **[Global]** `INTEREST_RATE_UP` (Macro Trigger)
2. **[Equity]** `MARK_TO_MARKET_UPDATE` (WACC 상승으로 인한 가치 하락)
3. **[ABS]** `CASH_TRAP_TRIGGER` (조달 비용 상승으로 인한 배당 중단)
4. **[PF]** `FUNDING_FAILURE` (추가 조달 금리 급증으로 인한 브릿지론 연장 실패)
5. **[PF]** `PROJECT_FAILURE` (사업성 악화)
6. **[NPL]** `PORTFOLIO_CREATION` (PF 부실 채권 인수)

### S2: Real Estate Crash (부동산 경기 급락 시나리오)
1. **[PF]** `PRE_SALE_SHORTFALL` (분양률 임계치 미달)
2. **[PF]** `COMPLETION_RISK` (공정 지연 및 시공사 부실)
3. **[ABS]** `COLLATERAL_DEVALUED` (기초자산 부동산 가치 하락)
4. **[PF]** `LOAN_DEFAULT` (이자 보전 불능)
5. **[NPL]** `AUCTION_FAILURE` (부동산 경매 시장 마비로 인한 유찰)

---

## 4. Event Handler Definitions (논리 수준)

각 이벤트 수신 시 시스템이 수행해야 하는 논리적 행동 지침입니다.

### Event: PROJECT_FAILURE
- **Handler Logic**:
  1. `Deal_State`를 `DELINQUENT`로 변경.
  2. 해당 포지션의 `Risk_Grade`를 최하단(D)으로 강제 조정.
  3. 모든 예정된 `Cashflow_Inflow`를 `Suspended` 상태로 전환.
  4. **Next Trigger**: `LOAN_DEFAULT` 전이 조건 체크.

### Event: CASH_TRAP_TRIGGER
- **Handler Logic**:
  1. 워터폴(Waterfall) 엔진 중단 명령 전송.
  2. `Reserve_Account_Balance` 적립 모드로 전환.
  3. `Junior_Tranche_Yield`를 0으로 고정.

---

## 5. Event Trigger Rules (Next Event Logic)

이벤트 간의 전이 조건(Trigger Rule)입니다.

| Source Event | Next Event | Trigger Condition (Threshold) |
| :--- | :--- | :--- |
| `PRE_SALE_SHORTFALL` | `PROJECT_FAILURE` | `Cash_Reserve < Next_Interest_Payment` |
| `PROJECT_FAILURE` | `LOAN_DEFAULT` | `DSCR < 0.8` (연속 2회 미치지 못할 경우) |
| `LOAN_DEFAULT` | `PORTFOLIO_ACQUIRED` (NPL) | `Foreclosure_Action = TRUE` |
| `CASH_TRAP` | `ACTIVE` (Restore) | `DSCR > 1.2` 및 `Reserve_Target` 충족 시 |

---

## 🔗 연결
- [통합 리스크 전파 명세](./Synthesis_Map.md)
- [표준 온톨로지 정의](../00_Standard_Layer/Core_Definitions.md)

### ─────────────

*최종 업데이트: 2026-04-16 (동적 실행 흐름 명세화)*
