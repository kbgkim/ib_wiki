# Equity 매핑 (Equity Mapping)

지분/주식 투자를 Position 기반 리스크 모델로 변환합니다.

---

## 포지션 (Position)
- **투자 건별 단위**: 개별 포트폴리오사 또는 펀드 참여 지분

---

## 부도 확률 (PD)
- 기업의 파산 확률이나 비즈니스 모델 실패 가능성을 의미합니다.

---

## 노출액 (Exposure)
- **투자 원금 (Cost)** 또는 현재의 **시장 가치 (Market Value)**를 기준으로 합니다.

---

## 리스크 산출 방식 (Dual Approach)

### 1. 신용 방식 (Credit Method)
주로 시스템 초기 단계나 부도 확률 기반 통합 관리 시 사용합니다.

- **EAD**: **투자 원금 (Cost)** 기준 노출액  
- **PD**: 대상 기업의 **파산 확률** 또는 사업 실패 확률  
- **LGD**: **100% 가정** (지분 자산의 후순위성 및 회수 불산성 반영)

→ 실제 지분 리스크를 단순화하여 **신용 리스크** 형태로 투영시킨 모델입니다.

---

### 2. 시장 방식 (Market Method) - 권장
실질적인 지분 가치 변동 리스크를 측정합니다.

- **시장 가치 (Market Value)**: 공정 가치 평가액 기반  
- **Shock (가격 변동률)**: 시장 변동성 지표를 반영한 하락 폭  
  **$$Loss = Market Value \times Shock$$**

→ Equity의 본질적인 리스크는 부도가 아닌 **가치 변동 리스크 (Valuation Risk)**에 있음을 반영합니다.

---

## 현금흐름 (Cashflow) 관점

Equity의 리스크는 다음과 같은 현금흐름 발생 시점에 실현됩니다:

- **Dividend (배당)**: 운영 수익의 유입
- **Exit (회수)**: 지분 매각(IPO, M&A)을 통한 자본 이득

리스크 측정은 다음과 같이 이원화되어 관리됩니다:
1. **Cashflow 리스크**: 예정된 배당 및 중간 회수금의 부족 (**Shortfall**)
2. **Valuation 리스크**: 최종 Exit 시점의 **공정 가치 하락**에 따른 손실

---

## 핵심 리스크 요인

- **기업가치 하락**: 실적 부진, 거시 경제 악화에 따른 저평가
- **엑시트 (Exit) 실패**: 회수 시점의 시장 경색 또는 원매자 확보 곤란
- **유동성 부족**: 비상장 지분 특성상 즉각적인 현금화 어려움

---

## 연결

→ [포지션 (Position)](../01_Core_Model/Position.md)  
→ [시장가치 (Market Value)](../01_Core_Model/Market_Value.md)  
→ [지분 리스크 (Equity Risk)](../03_Risk_Calculation/Equity_Risk.md)  
→ [현금흐름 (Cashflow)](../01_Core_Model/Cashflow.md)