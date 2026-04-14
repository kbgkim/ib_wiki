# 현금흐름 (Cashflow)

## 🔥 목적
**Cashflow**는 포지션(Position)에서 발생하는 실제 자금의 유효한 유입과 유출을 의미하며, 리스크 발생의 원인 데이터입니다.

- **표준 정의**: [Core_Definitions Cashflow Section](../../00_Standard_Layer/Core_Definitions.md#2-cashflow-현금흐름)
- **운영 규칙**: [Cashflow Rule](../../00_Standard_Layer/Cashflow_Rule.md)

### ─────────────

## 📌 개념
- **Inflow (유입)**: 원금 상환, 이자 수익, 분양 대금, 배당금 등
- **Outflow (유출)**: 대출 실행(Drawdown), 투자 집행, 운영 비용 등

👉 **Ontology Flow**: Asset → Position → **Cashflow** → Risk

### ─────────────

## 🧠 리스크 발생 매커니즘
모든 리스크는 현금흐름의 부족인 **Shortfall**에서 시작됩니다.

1. **Expected Cashflow**: 계약상 예정된 흐름
2. **Actual Cashflow**: 실제 발생한 흐름
3. **Shortfall**: Expected - Actual
4. **Loss**: Shortfall 기반 손실 확정

### ─────────────

## ⚙️ Exposure / EAD와의 관계
Cashflow는 포지션의 노출액(Exposure) 변동을 유발하는 동인입니다.

- **Inflow (상환)**: Exposure 감소 → EAD 감소
- **Outflow (인출)**: Exposure 증가 → EAD 증가

### ─────────────

## Standard Reference
- [Core_Definitions](../../00_Standard_Layer/Core_Definitions.md)
- [Cashflow Rule](../../00_Standard_Layer/Cashflow_Rule.md)
- [Cashflow Schema](../../05_Data_Model/01_Schemas/Cashflow_Schema.md)
- [Position](./Position.md)

### ─────────────

*최종 업데이트: 2026-04-14*