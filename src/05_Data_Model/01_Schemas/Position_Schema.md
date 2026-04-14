# 포지션 스키마 (Position_Schema)

## 🔥 목적
리스크 산출 및 관리의 최소 기본 단위인 **Position**의 물리적 데이터 구조를 정의합니다.

- **표준 정의**: [Core_Definitions Position Section](../../../00_Standard_Layer/Core_Definitions.md#1-position-포지션)
- **온톨로지**: Asset → **Position** → Cashflow → Risk

### ─────────────

## 📊 테이블 구조 (Table Detail)

### POSITION_MASTER
| 컬럼명 | 타입 | 설명 | 표준 참조 |
| :--- | :--- | :--- | :--- |
| **position_id** | VARCHAR | PK (고유 식별자) | - |
| **deal_id** | VARCHAR | FK (소속 딜 ID) | - |
| **asset_type** | ENUM | PF / ABS / NPL / EQUITY | [Mapping_Rule](../../../00_Standard_Layer/Mapping_Rule.md) |
| **seniority_rank** | INT | Waterfall 상의 우선순위 | [Position](../../../../01_Core_Model/Position.md) |
| **ccf_rate** | DECIMAL | 적용 CCF (EAD 산출용) | [EAD](../../../../01_Core_Model/EAD.md) |

### ─────────────

## Standard Reference
- [Core_Definitions](../../../00_Standard_Layer/Core_Definitions.md)
- [Position Core Model](../../../../01_Core_Model/Position.md)
- [Deal Schema](./Deal_Schema.md)

### ─────────────

*최종 업데이트: 2026-04-14*