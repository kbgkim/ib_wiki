# 부도확률 (PD; Probability of Default)

## 🔥 목적
**PD**는 특정 관찰 기간 내에 차주 혹은 자산 포지션이 약속된 현금흐름을 지급하지 못할 확률을 의미합니다. 기대손실(Expected Loss) 산출의 핵심 확률 변수입니다.

- **표준 정의**: [Core_Definitions PD Section](../../00_Standard_Layer/Core_Definitions.md#3-pd-probability-of-default)

### ─────────────

## 📌 개념
부도의 정의는 단순히 파산뿐만 아니라, 약정된 지급 기일에서 일정 기간 이상 연체된 상태를 포함합니다.

👉 **Ontology Flow**: Asset → Position → Cashflow (Failure) → **Risk (PD)**

### ─────────────

## ⚙️ 자산별 특성 (PD Mapping)
자산군별 PD 산출 방식은 [Mapping_Rule](../../00_Standard_Layer/Mapping_Rule.md)을 따릅니다.

- **PF**: 사업 성공 가능성 기반 산정.
- **ABS**: 기초자산 풀의 Default 확률.
- **NPL**: 이미 부도 상태이므로 **100% 고정**.
- **Equity**: 기업 파산(Failure) 확률.

### ─────────────

## Standard Reference
- [Core_Definitions](../../00_Standard_Layer/Core_Definitions.md)
- [Mapping_Rule](../../00_Standard_Layer/Mapping_Rule.md)
- [Risk_Model_Rule](../../00_Standard_Layer/Risk_Model_Rule.md)
- [Position](./Position.md)

### ─────────────

*최종 업데이트: 2026-04-14*