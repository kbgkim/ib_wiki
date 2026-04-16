# 리스크 결과 스키마 (Risk_Result_Schema)

## 🔥 목적

리스크 엔진의 최종 연산 결과(EL, Loss 등)를 포지션별, 시나리오별로 저장하는 물리 데이터 구조를 정의합니다.

### ─────────────

## 📊 테이블 구조 (Table Detail)

### RISK_RESULT_DETAIL

| 컬럼명 | 타입 | 설명 |
| :--- | :--- | :--- |
| **result_id** | VARCHAR | PK (고유 식별자) |
| **position_id** | VARCHAR | FK (포지션 ID) |
| **scenario_id** | VARCHAR | FK (적용 시나리오 ID) |
| **pd** | DECIMAL | 반영된 부도 확률 (PD) |
| **ead** | DECIMAL | 반영된 부도 시 노출액 (EAD) |
| **lgd** | DECIMAL | 반영된 손실률 (LGD) |
| **expected_loss** | DECIMAL | 최종 기대손실 (EL) |
| **market_value** | DECIMAL | 평가 금액 (Equity용 마크-투-마켓) |
| **shock** | DECIMAL | 적용된 가격 충격 비율 |
| **loss** | DECIMAL | 최종 산출 손실액 (Scenario Loss) |
| **as_of_date** | DATE | 산출 기준일 |

### ─────────────

## ⚙️ 설계 원칙 (Design Principles)

### 1. 연산 이력 저장
- 계산 시점의 변수들(PD, LGD 등)을 결과와 함께 저장하여 사후 원인 추적이 가능하도록 설계합니다.

### 2. 재계산 지원
- 외부 환경 변동 시 동일 시점 데이터를 바탕으로 리스크를 재계산할 수 있는 멱등성을 보장하기 위한 구조를 유지합니다.

### 3. 부하 분리 저장
- 원천 트랜잭션 데이터(Cashflow)와 연산 결과(Risk Result)를 분리하여 시스템 성능을 최적화합니다.

### ─────────────

## 🔗 연결

- [포지션 스키마 (Position Schema)](./Position_Schema.md)
- [기대손실 계산 (EL Calculation)](../../04_Risk_Calculation/EL_Calculation.md)
- [지분 리스크 계산 (Equity Risk Calculation)](../../04_Risk_Calculation/Equity_Risk.md)

### ─────────────

*최종 업데이트: 2026-04-14*