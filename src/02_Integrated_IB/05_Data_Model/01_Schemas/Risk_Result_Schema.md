# 리스크 결과 스키마 (Risk Result Schema)

## 목적
리스크 계산 결과를 저장하고 재활용하기 위한 데이터 구조를 정의합니다.

---

## 개념

**Risk Result**는 Position 단위로 계산된 최종 리스크(EL, Loss 등) 결과를 저장하는 스냅샷 데이터입니다.

---

## 테이블 구조

| 컬럼명 | 설명 |
|--------|------|
| **risk_id** | PK (Primary Key) |
| **position_id** | Position 식별자 |
| **risk_type** | 리스크 유형 (CREDIT / EQUITY) |
| **pd** | 반영된 부도 확률 |
| **ead** | 반영된 부도 시 노출액 |
| **lgd** | 반영된 손실률 |
| **expected_loss** | 최종 기대손실 (EL) |
| **market_value** | 평가 금액 (Equity용) |
| **shock** | 적용된 가격 충격 비율 |
| **loss** | 최종 산출 손실액 |
| **as_of_date** | 산출 기준일 |

---

## 설계 원칙

- **이력 저장**: 계산 시점의 변수들과 결과를 함께 저장하여 원인 추적이 가능하도록 합니다.
- **재계산 지원**: 언제든 동일한 시점의 데이터를 바탕으로 리스크를 재계산할 수 있는 구조를 유지합니다.
- **분리 저장**: 원천 데이터(Cashflow)와 계산 결과(Risk)를 분리하여 시스템 부하를 관리합니다.

---

## 연결

→ [포지션 스키마 (Position Schema)](./Position_Schema.md)  
→ [현금흐름 (Cashflow)](../../01_Core_Model/Cashflow.md)  
→ [기대손실 계산 (EL Calculation)](../../03_Risk_Calculation/EL_Calculation.md)