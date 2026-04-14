# NPL 리스크 매핑 가이드 (NPL Risk Mapping Guide)

## 1. Position Mapping
부실채권(NPL) 자산은 원인 채권(대출) 및 담보권 단위의 **Position**으로 관리됩니다.

- **포지션 구분**: 이미 부도난 개별 채권 및 그에 부수하는 담보권 기반의 독립적 리스크 단위.
- **표준화**: 매입한 모든 NPL 채권은 [Core_Definitions](../../00_Standard_Layer/Core_Definitions.md#1-position-포지션)상 포지션으로 변환됩니다.

### ─────────────

## 2. PD Definition
NPL의 부도 확률(Probability of Default)은 이미 부실화된 상태를 전제로 합니다.

- **정의**: [Core_Definitions PD Section](../../00_Standard_Layer/Core_Definitions.md#3-pd-probability-of-default) 및 [Risk_Model_Rule NPL Exception](../../00_Standard_Layer/Risk_Model_Rule.md#4-npl-exception-rule)에 따라 **100% 고정**으로 정의.
- **특징**: 추가적인 부도 발생 여부가 아닌, 회수(Recovery)의 질적 관리에 집중.

### ─────────────

## 3. EAD Definition
부도 시 노출 금액(Exposure at Default)은 매입 시점의 권리 금액 및 미상환 원금을 의미합니다.

- **정의**: [Core_Definitions EAD Section](../../00_Standard_Layer/Core_Definitions.md#5-ead-exposure-at-default)을 준수.
- **산출**: 미상환 원금 잔액(OPB) + 확정된 미수이자.

### ─────────────

## 4. LGD Definition
부도 시 손실률(Loss Given Default)은 매입가 대비 최종 회수 가능액의 차이로 결정됩니다.

- **회수 기반**: [Mapping_Rule NPL Section](../../00_Standard_Layer/Mapping_Rule.md#3-npl)에 따라 정규화.
- **LGD 산출**: 1 - (예상 회수액 / EAD). 담보 낙찰가 및 경매 비용을 반영하여 산정.

### ─────────────

## 5. Cashflow Structure
NPL 리스크의 본질은 회수 현금흐름(Recovery Cashflow)의 성과에 있습니다.

- **Expected Cashflow**: 담보 처분 시나리오 및 배당 계획에 따른 예상 회수액.
- **Actual Cashflow**: 법원 경매 또는 론세일(Loan Sale)을 통해 실제 유입된 자금.
- **Shortfall**: 예상 회수 시점의 지연 또는 회수액 부족 발생. [Cashflow Rule](../../00_Standard_Layer/Cashflow_Rule.md)을 따름.

### ─────────────

## 6. Risk Drivers
NPL 현금흐름에 영향을 미치는 핵심 리스크 동인입니다.

- **담보 가치 하락**: 부동산 경기 침체로 인한 낙찰가율 저하.
- **회수 지연**: 유치권 분쟁, 경매 유찰 등 법적/절차적 원인에 의한 회수 기간 장기화.
- **비용 증대**: 법적 절차 및 자산 관리 비용의 과다 집행.

### ─────────────

## 7. Expected Loss (EL) Impact
NPL의 최종 기대 손실은 PD 100%를 전제로 산출됩니다.

- **공식**: $EL = LGD \times EAD$ (단, $PD = 100\%$이므로 $PD \times LGD \times EAD$와 동일 결과)
- **관리**: [Risk_Model_Rule](../../00_Standard_Layer/Risk_Model_Rule.md)에 따라 포지션별 EL 상시 모니터링.

### ─────────────

## Standard Reference
- [Core_Definitions](../../00_Standard_Layer/Core_Definitions.md)
- [Position](../../../01_Core_Model/Position.md)
- [Cashflow Model](../../../01_Core_Model/Cashflow.md)
- [Asset Mapping Rule](../../00_Standard_Layer/Mapping_Rule.md)

### ─────────────

*최종 업데이트: 2026-04-14*