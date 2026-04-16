# 부도시노출액 (EAD; Exposure at Default)

## 🔥 목적
**EAD**는 부도가 발생하는 시점에 리스크에 노출되어 있을 것으로 예상되는 총 금액입니다. 현재 노출액(Exposure)에 미래 추가 인출 가능액을 더해 산출됩니다.

- **표준 정의**: [Core_Definitions EAD Section](../00_Standard_Layer/Core_Definitions.md#5-ead-exposure-at-default)

### ─────────────

## 📌 개념
EAD는 단순히 현재의 대출 잔액이 아니라, 부도 시점까지 늘어날 수 있는 잠재적 노출액까지 고려한 수치입니다.

👉 **EAD = Current Exposure + (Undrawn Limit × CCF)**
- *CCF (Credit Conversion Factor): 미인출 한도의 유동성 소진 계수*

### ─────────────

## ⚙️ Exposure와의 관계
EAD는 미래 부도 시점의 가상적 노출액을 측정하며, 현재 시점의 Exposure는 그 하한선 역할을 합니다.

- **기준 시점**: 미래 부도 시점
- **속성**: 추정 및 모델링 데이터
- **핵심 동인**: 미래 현금 유출(Drawdown) 시나리오

### ─────────────

## Standard Reference
- [Core_Definitions](../00_Standard_Layer/Core_Definitions.md)
- [Exposure Model](./Exposure.md)
- [Cashflow Model](./Cashflow.md)
- [Position](./Position.md)

### ─────────────

*최종 업데이트: 2026-04-14*