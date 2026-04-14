# 포지션 스키마 (Position Schema)

## 목적
모든 IB 자산(PF, NPL, ABS, Equity)의 리스크 계산 기준이 되는 **Position** 데이터를 정의합니다.

---

## 개념

**Position**은 딜(Deal)을 구성하는 자금 단위이며, 모든 리스크는 **Position** 기준으로 계산됩니다.

---

## 테이블 구조

| 컬럼명 | 설명 |
|--------|------|
| **position_id** | PK (Primary Key) |
| **deal_id** | Deal 식별자 |
| **asset_type** | 자산 유형 (PF, NPL, ABS, Equity) |
| **exposure** | 현재 노출 금액 |
| **ead** | 부도 시 노출 금액 |
| **lgd** | 손실률 |
| **market_value** | 평가 금액 (Equity) |
| **as_of_date** | 기준일 |

---

## 설계 원칙

- **포지션 환원**: 모든 자산은 Position 단위로 분해하여 관리합니다.
- **통합 구조**: Credit과 Equity 리스크 계산에 필요한 공통 필드를 유지합니다.
- **스냅샷 관리**: 시간 기준(`as_of_date`)을 필수로 포함하여 과거 이력을 관리합니다.

---

## 연결

→ [포지션 (Position)](../../01_Core_Model/Position.md)  
→ [현금흐름 (Cashflow)](../../01_Core_Model/Cashflow.md)  
→ [리스크 결과 스키마 (Risk Result Schema)](./Risk_Result_Schema.md)