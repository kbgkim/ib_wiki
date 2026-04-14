# 시장가치 (Market Value)

## 🔥 목적

시장가치(Market Value)는 특정 시점에서 자산을 시장에 매각할 때 받을 수 있는 공정 가치를 의미하며, 특히 지분(Equity) 자산의 리스크 노출액을 정의하는 핵심 기준입니다.

### ─────────────

## 📌 개념

Market Value는 장부 가격(Book Value)과 달리 시장의 수평적 가격 형성을 반영합니다.

👉 **Equity Exposure = Market Value**

신용 자산(PF, NPL 등)과 달리 지분 자산은 원금보다는 **시장 가격의 변동** 자체가 리스크의 본질입니다.

### ─────────────

## 🧠 리스크 관계 (Market Value vs Loss)

지분 리스크는 시장 가치 하락(Shock)을 통해 산출됩니다.

### 손실 산정 구조
1. 현재 **Market Value** 측정  
2. 변동성(Volatility) 기반의 가격 하락 충격(Shock) 부여  
3. 예상 가치 하락분 = **Market Value × Shock**  
4. 이 가치 하락분이 지분 리스크의 EL 또는 VaR가 됨  

### ─────────────

## 💰 Cashflow 관점

Market Value는 미래에 발생할 기대 현금흐름(배당, 매각액)을 현재 가치로 할인한 값의 총합입니다.

### 가치 형성 매커니즘
미래 기대 현금흐름 (Expected Exit Cashflow)  
→ 할인율 (Discount Rate) 적용  
→ **현재 Markt Value 확정**  

👉 따라서 현금흐름의 불확실성이 커지면 Market Value가 하락하게 됩니다.

### ─────────────

## ⚖️ 자산별 적용

### Equity (지분 자본)
- 상장 주식 마크-투-마켓(Mark-to-Market) 가치
- 비상장 주식 공정가치 평가액

### NPL / PF (대출/채권 자본)
- 보통 **Exposure** 개념을 사용하나, 매각 시나리오 시에는 담보물의 **Market Value**를 기준으로 LGD를 산출함

### ─────────────

## 🔗 연결

- [변동성 (Volatility)](./Volatility.md)
- [노출액 (Exposure)](./Exposure.md)
- [지분 리스크 (Equity Risk)](../03_Risk_Calculation/Equity_Risk.md)

### ─────────────

*최종 업데이트: 2026-04-14*