# 시나리오 모델 (Scenario Model)

## 목적
Stress Test 및 리스크 시뮬레이션을 위한 데이터 변동 구조를 정의합니다.

---

## 개념

**Scenario**는 거시 경제 변수나 사업장별 특수 변수 변화에 따른 현금흐름(Cashflow) 및 리스크(Risk)의 변동을 시뮬레이션합니다.

---

## 주요 변수 (Drivers)

- **금리 상승**: 금융 비용 증가 → Cashflow 악화
- **분양률 감소**: 분양 수입 감소 → Shortfall 발생 (PF)
- **회수율 하락**: LGD 상승 → 기대손실 증가 (NPL/ABS)
- **경기 침체**: 전반적인 PD 상승 요인

---

## 시뮬레이션 구조 (Workflow)

**Scenario**  
 → **Cashflow** 변동 (Shock 적용)  
 → **Shortfall** 규모 변화  
 → **Risk Result** 재산출  

---

## 활용 방안

- **Stress Test**: 극단적 상황에서의 자본 적정성 평가
- **민감도 분석**: 특정 변수 변화에 따른 리스크 민감도 측정
- **리스크 예측**: 미래 시점의 리스크 수준 시뮬레이션

---

## 설계 원칙

- **독립성**: Scenario는 실제 데이터에 영향을 주지 않는 독립적인 시뮬레이션 환경으로 관리합니다.
- **현금흐름 기반**: 모든 시장 충격은 현금흐름의 변화를 통해 리스크에 투영됩니다.

---

## 연결

→ [현금흐름 (Cashflow)](../../01_Core_Model/Cashflow.md)  
→ [리스크 결과 스키마 (Risk Result Schema)](../01_Schemas/Risk_Result_Schema.md)  
→ [변동성 (Volatility)](../../01_Core_Model/Volatility.md)