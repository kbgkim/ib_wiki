# 기대손실 산출 로직 (EL Calculation Logic)

## 🔥 목적
개별 포지션의 기초 데이터를 바탕으로 기대손실(Expected Loss)을 산출하는 엔진의 논리적 단계를 정의합니다.

- **표준 규칙**: [Risk_Model_Rule](../00_Standard_Layer/Risk_Model_Rule.md)
- **온톨로지**: Asset → Position → Cashflow → **Risk (EL)**

### ─────────────

## 📌 1. 산출 파이프라인 (Pipeline)

리스크 엔진은 [Core_Definitions](../00_Standard_Layer/Core_Definitions.md) 및 [Risk_Model_Rule](../00_Standard_Layer/Risk_Model_Rule.md)에 의거하여 연산을 수행합니다.

1. **Data Ingestion**: Deal/Position/Cashflow 데이터 로드
2. **Variable Mapping**: [Mapping_Rule](../00_Standard_Layer/Mapping_Rule.md)을 적용하여 PD, LGD, EAD 매핑
3. **Core Calculation**: `EL = PD × LGD × EAD` 연산 수행
4. **Result Storage**: 산출된 EL을 [Risk_Result_Schema](../05_Data_Model/01_Schemas/Risk_Result_Schema.md)에 저장

### ─────────────

## 🧠 2. 자산별 특화 로직
산출 엔진은 자산 수직 구조([Assets_Verticals](../03_Assets_Verticals/))에서 정의된 개별 매핑 로직을 호출합니다.

- **NPL**: [NPL_Mapping](../03_Assets_Verticals/NPL/NPL_Mapping.md)에 따라 PD=100% 강제 적용.
- **Equity**: [Equity_Mapping](../03_Assets_Verticals/Equity/Equity_Mapping.md)에 따라 Volatility Shock 모델 병행.

### ─────────────

## Standard Reference
- [Core_Definitions](../00_Standard_Layer/Core_Definitions.md)
- [Risk_Model_Rule](../00_Standard_Layer/Risk_Model_Rule.md)
- [Expected_Loss Model](../01_Core_Model/Expected_Loss.md)

### ─────────────

*최종 업데이트: 2026-04-14*