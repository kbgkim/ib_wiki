# 포지션 (Position)

## 🔥 목적
**Position**은 리스크 산출 및 관리의 최소 기본 단위입니다. 모든 자산(Asset)은 하나 이상의 포지션으로 환원되며, 모든 리스크 변수와 현금흐름은 포지션 단위로 귀속됩니다.

- **표준 정의**: [Core_Definitions Position Section](../00_Standard_Layer/Core_Definitions.md#1-position-포지션)

### ─────────────

## 📌 개념
포지션은 투자 대상의 경제적 권리와 의무가 정의된 '계좌' 혹은 '슬롯'과 같습니다.

👉 **Ontology Flow**: Asset → **Position** → Cashflow → Risk

### ─────────────

## 🧠 구조 역할
포지션은 상위 딜(Deal)과 하위 현금흐름(Cashflow)을 연결하는 허부 역할을 합니다.

- **상위**: 딜(Deal) - 비즈니스 시나리오 및 통제 단위
- **하위**: 현금흐름(Cashflow) - 포지션에서 파생되는 실제 자본 흐름

### ─────────────

## 📊 구성 요소
| 항목 | 설명 | 표준 참조 |
| :--- | :--- | :--- |
| **Exposure** | 포지션의 현재 노출액 | [Exposure](./Exposure.md) |
| **Risk Metrics** | 포지션별 PD, LGD, EAD | [Core_Definitions](../00_Standard_Layer/Core_Definitions.md) |
| **Cashflow Link** | 포지션에 귀속된 현금흐름 | [Cashflow](./Cashflow.md) |

### ─────────────

## Standard Reference
- [Core_Definitions](../00_Standard_Layer/Core_Definitions.md)
- [Position Schema](../05_Data_Model/01_Schemas/Position_Schema.md)
- [Cashflow Model](./Cashflow.md)

### ─────────────

*최종 업데이트: 2026-04-14*