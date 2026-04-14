# Equity 매핑 (Equity Mapping)

지분/주식 투자를 Position 기반 리스크 모델로 변환합니다.

---

## 포지션 (Position)

- 투자 건별 단위  
- 개별 기업 또는 펀드 지분 투자 단위  

---

## 부도 확률 (PD)

- 기업의 파산 확률 또는 사업 실패 가능성  
- 단, Equity에서는 보조적 지표로 활용  

---

## 노출액 (Exposure)

- 투자 원금 (Cost)  
- 또는 현재 시장 가치 (Market Value) 기준  

---

# ⚖️ 리스크 산출 방식 (Dual Structure)

Equity 리스크는 두 가지 관점으로 관리됩니다.

---

## 1. 신용 방식 (Credit Method) - 보조 모델

시스템 통합 또는 초기 리스크 통합 목적에서 사용됩니다.

- **EAD**: 투자 원금 (Cost) 기준  
- **PD**: 기업 파산 확률  
- **LGD**: 100% 가정  

→ Equity를 Credit Risk 형태로 단순화한 모델

> ❗ 실제 리스크 측정의 주 모델은 아님

---

## 2. 시장 방식 (Market Method) - 핵심 모델 (권장)

Equity의 본질적인 리스크 모델입니다.

- **Market Value**: 공정 가치 (Fair Value)  
- **Shock**: 시장 변동성 기반 가격 충격  

Loss = Market Value × Shock  

---

## 📊 Cashflow 관점

Equity 리스크는 두 가지 흐름으로 발생합니다:

---

### 1. Cashflow Risk

- Dividend (배당)
- Exit (지분 매각)

Expected Cashflow  
→ Actual Cashflow  
→ Shortfall  
→ Loss

---

### 2. Valuation Risk (핵심)

- 시장 가치 하락
- Exit 시점 평가 손실

Market Value  
→ Shock  
→ Loss  

---

## 핵심 리스크 요인

- 기업가치 하락 (실적 부진 / 시장 악화)
- Exit 실패 (IPO / M&A 지연)
- 유동성 부족 (비상장 특성)

---

## 구조적 특징

- Credit Risk 모델과 구조는 유사하지만 본질은 Market Risk
- Cashflow 기반 + Market Value 기반 이중 구조
- 실질 손실은 대부분 Valuation Risk에서 발생

---

## 연결

→ [포지션 (Position)](../01_Core_Model/Position.md)  
→ [시장가치 (Market Value)](../01_Core_Model/Market_Value.md)  
→ [지분 리스크 (Equity Risk)](../03_Risk_Calculation/Equity_Risk.md)  
→ [현금흐름 (Cashflow)](../01_Core_Model/Cashflow.md)