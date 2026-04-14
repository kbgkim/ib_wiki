# ABS 리스크 매핑 가이드 (ABS Risk Mapping Guide)

## 1. Position Mapping
자산유동화(ABS) 자산은 유동화 구조 내의 특정 **Tranche(트랜치)** 단위의 **Position**으로 관리됩니다.

- **포지션 구분**: Senior, Mezzanine, Equity 등 상환 우선순위에 따른 독립적 리스크 단위.
- **표준화**: 투자된 모든 유동화 증권은 [Core_Definitions](../../00_Standard_Layer/Core_Definitions.md#1-position-포지션)상 포지션으로 변환됩니다.

### ─────────────

## 2. PD Definition
ABS의 부도 확률(Probability of Default)은 기초자산 풀(Pool)의 건전성과 직결됩니다.

- **정의**: [Core_Definitions PD Section](../../00_Standard_Layer/Core_Definitions.md#3-pd-probability-of-default)에 따라 '기초자산의 Default 확률'로 정의.
- **매핑 요인**: 기초자산 채무자의 연체율, 부도 이력, 거시 경제 변수.

### ─────────────

## 3. EAD Definition
부도 시 노출 금액(Exposure at Default)은 투자한 ABS 증권의 가치를 의미합니다.

- **정의**: [Core_Definitions EAD Section](../../00_Standard_Layer/Core_Definitions.md#5-ead-exposure-at-default)을 준수.
- **산출**: 유동화 증권의 액면가 및 미수이자 포함 잔액.

### ─────────────

## 4. LGD Definition
부도 시 손실률(Loss Given Default)은 워터폴(Waterfall) 구조 내에서 해당 트랜치가 가진 신용보강 수준에 따라 결정됩니다.

- **구조적 보호**: 선순위 트랜치는 하위 트랜치의 신용보강(Subordination)에 의해 보호됨.
- **손실 전이**: 기초자산 손실이 신용보강 한도를 초과할 때 실질적인 LGD가 발생.

### ─────────────

## 5. Cashflow Structure
ABS 리스크의 본질은 워터폴에 따른 현금 배분 성공 여부에 있습니다.

- **Expected Cashflow**: 기초자산 풀로부터 유입되어 워터폴에 따라 배분될 예정 유입액.
- **Actual Cashflow**: 자산보유자 및 수탁기관을 통해 실제 트랜치로 지급된 현금흐름.
- **Shortfall**: 하위 트랜치의 부실로 인해 상위 트랜치 배분액이 부족해지는 현상. [Cashflow Rule](../../00_Standard_Layer/Cashflow_Rule.md)을 따름.

### ─────────────

## 6. Risk Drivers
ABS 현금흐름에 영향을 미치는 핵심 리스크 동인입니다.

- **신용보강 부족**: 기초자산 손실이 Over-collateralization(OC) 비율을 초과할 리스크.
- **조기상환 리스크**: 기초자산의 급격한 조기상환으로 인한 재투자 리스크 및 수익성 하락.
- **운용사 리스크**: 유동화 자산 관리자(Servicer)의 역량 및 도덕적 해이.

### ─────────────

## 7. Expected Loss (EL) Impact
최종 기대 손실은 표준 엔진 규칙에 따라 산출됩니다.

- **공식**: $EL = PD \times LGD \times EAD$
- **관리**: [Risk_Model_Rule](../../00_Standard_Layer/Risk_Model_Rule.md)에 따라 트랜치별 EL 산출.

### ─────────────

## Standard Reference
- [Core_Definitions](../../00_Standard_Layer/Core_Definitions.md)
- [Position](../../../01_Core_Model/Position.md)
- [Cashflow Model](../../../01_Core_Model/Cashflow.md)
- [Asset Mapping Rule](../../00_Standard_Layer/Mapping_Rule.md)

### ─────────────

*최종 업데이트: 2026-04-14*