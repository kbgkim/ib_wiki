# PF 리스크 매핑 가이드 (PF Risk Mapping Guide)

## 1. Position Mapping
PF(프로젝트 파이낸싱) 자산은 개별 사업장 단위의 **Position**으로 관리됩니다.

- **포지션 구분**: 기초 자산(토지) 및 사업권 기반의 독립된 리스크 단위.
- **표준화**: 모든 PF 대출 및 투자는 [Core_Definitions](../../00_Standard_Layer/Core_Definitions.md#1-position-포지션)상 포지션으로 변환됩니다.

### ─────────────

## 2. PD Definition
PF의 부도 확률(Probability of Default)은 사업의 성공 가능성(분양 및 준공)과 직결됩니다.

- **정의**: [Core_Definitions PD Section](../../00_Standard_Layer/Core_Definitions.md#3-pd-probability-of-default)에 따라 '사업 실패 확률'로 정의.
- **매핑 요인**: 분양율, 공정률, 인허가 획득 여부.

### ─────────────

## 3. EAD Definition
부도 시 노출 금액(Exposure at Default)은 현재 익스포저와 미래 추가 자금 집행분을 포함합니다.

- **정의**: [Core_Definitions EAD Section](../../00_Standard_Layer/Core_Definitions.md#5-ead-exposure-at-default)을 준수.
- **산출**: 현재 대출 잔액 + 미인출 한도(Commitment).

### ─────────────

## 4. LGD Definition
부도 시 손실률(Loss Given Default)은 PF 특화 담보 구조에 따라 결정됩니다.

- **부동산 담보**: LTV(Loan to Value) 기반 실질 담보 가치 산정.
- **신용 보강**: 시공사 책임준공 확약, 신탁사 수익권 증서 등 PF 전유 구조 반영.

### ─────────────

## 5. Cashflow Structure
PF 리스크의 본질은 현금흐름의 실현 여부에 있습니다.

- **Expected Cashflow**: 분양 수입 및 상환 계획표상의 예정 유입액.
- **Actual Cashflow**: 실시간 분양 대금 및 이자 수취액.
- **Shortfall**: 예상 대비 실제 유입액 부족분. [Cashflow Rule](../../00_Standard_Layer/Cashflow_Rule.md)을 따름.

### ─────────────

## 6. Risk Drivers
PF 현금흐름에 영향을 미치는 핵심 리스크 동인입니다.

- **분양 리스크**: 분양 지연으로 인한 상환 재원 부족.
- **준공 리스크**: 시공사 부실로 인한 현금 유입 시점 미스매치.
- **금융 리스크**: 금리 상승에 따른 이자 비용(Outflow) 증대.

### ─────────────

## 7. Expected Loss (EL) Impact
최종 기대 손실은 표준 엔진 규칙에 따라 산출됩니다.

- **공식**: $EL = PD \times LGD \times EAD$
- **관리**: [Risk_Model_Rule](../../00_Standard_Layer/Risk_Model_Rule.md)에 따라 포지션별 EL 산출.

### ─────────────

## Standard Reference
- [Core_Definitions](../../00_Standard_Layer/Core_Definitions.md)
- [Position](../../../01_Core_Model/Position.md)
- [Cashflow Model](../../../01_Core_Model/Cashflow.md)
- [Asset Mapping Rule](../../00_Standard_Layer/Mapping_Rule.md)

### ─────────────

*최종 업데이트: 2026-04-14*