# 시나리오 스키마 (Scenario_Schema)

## 🔥 목적

리스크 엔진이 수행할 시나리오의 성격과 각 리스크 요인(Risk Factor)에 적용될 충격(Shock)의 크기를 정의합니다.

### ─────────────

## 📌 개념

시나리오는 '만약 ~라면'에 대한 시스템적 답변입니다.

👉 **역할**
- Stress Scenario 관리 (위기 상황 정의)
- Sensitivity Analysis (민감도 분석 기준)
- Shock Propagation Base (충격 전파 기반 데이터)

### ─────────────

## 📊 테이블 구조 (Table Detail)

### SCENARIO_MASTER

| 컬럼명 | 타입 | 설명 |
| :--- | :--- | :--- |
| **scenario_id** | VARCHAR | PK (고유 식별자) |
| **scenario_name** | VARCHAR | 시나리오 명칭 (Base / Stress / Worst) |
| **factor_id** | VARCHAR | FK (적용 대상 리스크 요인 ID) |
| **shock_value** | DECIMAL | 적용할 충격 계수 (Multiplier) |
| **description** | TEXT | 시나리오 설명 (예: 금리 100bp 상승) |
| **as_of_date** | DATE | Snapshot 기준일 |

### ─────────────

## 🧠 리스크 산출 피드백 루프

### 산출 흐름
1. 시나리오 로드 (Scenario)  
2. 리스크 요인에 충격 투영 (Risk Factor × Shock)  
3. 포지션별 리스크 변수 재산정 (PD/LGD 변동)  
4. 결과 저장 (Risk Result)  

### ─────────────

## 🔗 연결

- [리스크 요인 스키마 (Risk Factor Schema)](./Risk_Factor_Schema.md)
- [리스크 결과 스키마 (Risk Result Schema)](./Risk_Result_Schema.md)

### ─────────────

*최종 업데이트: 2026-04-14*
