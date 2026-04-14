# 시나리오 스키마 (Scenario Schema)

## 목적
시뮬레이션 상황에서 리스크 요인(Risk Factor)에 가할 구체적인 충격치(Shock)와 조건을 정의합니다.

---

## 개념
**Scenario**는 가상의 상황이며, 하나 이상의 **Risk Factor**에 대한 변동 폭(Delta)의 집합입니다. 엔진은 이 스키마의 데이터를 읽어 `Base Value`에 적용합니다.

---

## 테이블 구조

| 컬럼명 | 설명 | 비고 |
|--------|------|------|
| **scenario_id** | PK (Primary Key) | 시나리오 식별자 |
| **factor_id** | FK (Risk Factor ID) | 대상 리스크 요인 |
| **scenario_name** | 시나리오 명칭 | 예: 경기침체 (Severe Recession) |
| **shock_value** | 충격치 (Shock) | 변동량 또는 변동률 |
| **shock_unit** | 충격 단위 | PERCENT, BP, ABSOLUTE 등 |
| **shock_direction** | 충격 방향 | INCREASE, DECREASE |
| **probability** | 시나리오 발생 확률 | 스트레스 시나리오별 가중치 |
| **is_regulatory** | 감독당국 표준 여부 | 바젤 III 표준 시나리오 등 여부 |

---

## 설계 원칙
- **매개변수 주입**: 시나리오는 데이터 자체가 아닌 '계산 매개변수'로서 동작합니다.
- **다대다 매핑**: 한 시나리오(예: 금융위기)는 여러 리스크 요인(금리 상승, 주가 하락)을 동시에 포함할 수 있습니다.

---

## 연결
→ [시나리오 모델 (Scenario Model)](../03_Behavior/Scenario_Model.md)  
→ [리스크 요인 스키마 (Risk Factor Schema)](./Risk_Factor_Schema.md)  
→ [현금흐름과 손실 (Cashflow to Loss)](../02_Logic/Cashflow_to_Loss_Logic.md)
