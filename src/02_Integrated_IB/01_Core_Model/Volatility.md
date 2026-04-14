# 변동성 (Volatility)

가격 변동의 폭과 리스크 수준을 나타내는 시장 기반 위험 지표입니다.

---

## 의미

- **시장 리스크 (Market Risk)**: 가격 불확실성을 수치화한 값  
- **변동 범위**: 자산 가격이 일정 기간 동안 움직일 수 있는 폭  
- **리스크 민감도**: 가격 충격(Shock)의 입력 변수  

---

## 리스크 모델 내 역할

Volatility는 Equity 리스크에서 다음 구조의 핵심 입력값입니다:

Market Value  
→ Volatility (변동성)  
→ Shock (가격 충격)  
→ Loss  

즉, Volatility는 Shock를 결정하는 핵심 파라미터입니다.

---

## 활용

### 1. 스트레스 테스트 (Stress Test)
- 극단적인 시장 상황 가정
- 가격 하락률 확대 적용
- Loss 극대화 시나리오 분석

---

### 2. 시나리오 분석 (Scenario Analysis)
- 다양한 시장 조건에서 자산 가치 변화 분석
- 금리, 경기, 유동성 환경 반영

---

### 3. 리스크 산출 (Equity Risk)
- 변동성이 높을수록 Shock 증가
- Loss 증가 → Equity Risk 증가

---

## 자산별 적용

### 상장 주식
- 역사적 변동성 (Historical Volatility)
- 시장 기반 실시간 반영

---

### 비상장 주식
- 유사 기업 비교 또는 모델 기반 추정 변동성

---

## 관계 구조

Volatility는 다음 구조에서 Shock를 결정합니다:

Volatility  
→ Shock  
→ Market Value × Shock = Loss  

---

## 연결

→ [시장가치 (Market Value)](./Market_Value.md)  
→ [지분 리스크 (Equity Risk)](../03_Risk_Calculation/Equity_Risk.md)