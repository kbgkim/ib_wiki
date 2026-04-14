# 손실률 (LGD; Loss Given Default)

## 🔥 목적
**LGD**는 부도가 발생했을 때, 채권자나 투자자가 회수하지 못하고 실제로 잃게 되는 금액의 비율을 의미합니다. 자산의 담보 가치와 우선순위(Waterfall)에 의해 결정됩니다.

- **표준 정의**: [Core_Definitions LGD Section](../../00_Standard_Layer/Core_Definitions.md#4-lgd-loss-given-default)

### ─────────────

## 📌 개념
LGD는 1에서 회수율(Recovery Rate)을 뺀 값과 같습니다.

👉 **LGD = 1 - Recovery Rate**

IB 리스크에서 LGD는 단순히 고정된 수치가 아니라, 부도 시점의 담보 처분 가치나 현금흐름 재구조화 결과에 따라 변동됩니다.

### ─────────────

## ⚙️ 자산별 특성 (LGD Mapping)
자산군별 LGD 산출 방식은 [Mapping_Rule](../../00_Standard_Layer/Mapping_Rule.md)을 따릅니다.

- **PF**: 담보 LTV 및 시공사 신용보강 반영.
- **ABS**: 트랜치 순위 및 워터폴(Waterfall) 구조 반영.
- **NPL**: 담보 낙찰가율 및 회수 비용 반영.
- **Equity**: 지분 자본의 후순위성으로 인해 **100% 원칙**.

### ─────────────

## Standard Reference
- [Core_Definitions](../../00_Standard_Layer/Core_Definitions.md)
- [Mapping_Rule](../../00_Standard_Layer/Mapping_Rule.md)
- [Risk_Model_Rule](../../00_Standard_Layer/Risk_Model_Rule.md)
- [Position](./Position.md)

### ─────────────

*최종 업데이트: 2026-04-14*