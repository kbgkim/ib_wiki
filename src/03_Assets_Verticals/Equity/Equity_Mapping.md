# Equity 리스크 매핑 가이드 (Equity Risk Mapping Guide)

## 1. Position Mapping
Equity(자본/지분) 자산은 발행 기업의 소유권 단위인 **Position**으로 관리됩니다.

- **포지션 구분**: 상장/비상장 주식 및 지분형 투자 단위.
- **표준화**: 보유한 모든 지분 자산은 [Core_Definitions](../../00_Standard_Layer/Core_Definitions.md#1-position-포지션)상 포지션으로 변환됩니다.

### ─────────────

## 2. PD Definition
Equity의 부도 확률(Probability of Default)은 발행 기업의 파산 또는 회생 절차 진입 확률을 의미합니다.

- **정의**: [Core_Definitions PD Section](../../00_Standard_Layer/Core_Definitions.md#3-pd-probability-of-default)에 따라 '기업 Failure 확률'로 정의.
- **특징**: 지분 투자자는 채권자보다 후순위이므로 기업 부도 시 즉각적인 가치 소멸로 이어짐.

### ─────────────

## 3. EAD Definition
부도 시 노출 금액(Exposure at Default)은 해당 지분의 현재 공정 가치(Fair Value)를 의미합니다.

- **정의**: [Core_Definitions EAD Section](../../00_Standard_Layer/Core_Definitions.md#5-ead-exposure-at-default)을 준수.
- **산출**: 현재 시장 가치 (Market Value).

### ─────────────

## 4. LGD Definition
Equity의 부도 시 손실률(Loss Given Default)은 지분의 후순위성으로 인해 매우 높게 설정됩니다.

- **손실 전환**: [Mapping_Rule Equity Section](../../00_Standard_Layer/Mapping_Rule.md#4-equity)에 따라 보통주 기준 **100%**를 기본 원칙으로 함.
- **특이사항**: 청산 시 잔여 재산 분배 가능성이 극히 낮아 Recovery를 0으로 간주.

### ─────────────

## 5. Cashflow Structure
Equity 리스크는 배당(Dividend)과 매각(Exit) 현금흐름의 불확실성에 기인합니다.

- **Expected Cashflow**: 예정된 배당금 유입액 및 투자 회수(Exit) 시점의 예상 가액.
- **Actual Cashflow**: 실제 수취한 배당금 및 자산 매각으로 유입된 현금.
- **Shortfall**: 배당 컷(Cut) 또는 엑시트 실패로 인한 현금 유입 부족. [Cashflow Rule](../../00_Standard_Layer/Cashflow_Rule.md)을 따름.

### ─────────────

## 6. Risk Drivers
Equity 현금흐름 및 가치에 영향을 미치는 핵심 리스크 동인입니다.

- **시장 변동성 (Market Volatility)**: 시장 가격의 급격한 변동에 따른 평가 손익 발생.
- **배당 리스크 (Dividend Risk)**: 기업 이익 하락으로 인한 배당 중단.
- **유동성 리스크 (Exit Risk)**: 시장 상황 악화로 인한 적기 매각 실패 및 가치 하락.

### ─────────────

## 7. Expected Loss (EL) Impact
Equity의 최종 리스크는 신용 모델(EL)과 시장 모델(Shock)을 병행하여 관리합니다.

- **신용 관점**: $EL = PD \times 100\% \times Market Value$
- **시장 관점**: [Risk_Model_Rule Market Model](../../00_Standard_Layer/Risk_Model_Rule.md#2-market-model-equity-only)에 따라 **Volatility Shock** 기반 손실액 산출.

### ─────────────

## Standard Reference
- [Core_Definitions](../../00_Standard_Layer/Core_Definitions.md)
- [Position](../../../01_Core_Model/Position.md)
- [Cashflow Model](../../../01_Core_Model/Cashflow.md)
- [Asset Mapping Rule](../../00_Standard_Layer/Mapping_Rule.md)

### ─────────────

*최종 업데이트: 2026-04-14*