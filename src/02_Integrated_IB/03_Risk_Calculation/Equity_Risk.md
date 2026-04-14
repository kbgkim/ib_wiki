# 지분 리스크 (Equity Risk)

지분 투자(Equity) 기반 자산의 시장 가치 변동 리스크를 측정하는 모델입니다.

---

# 📊 기본 구조 (Market Risk Model - Primary)

Equity Risk의 핵심은 시장 가치 변동입니다.

Position  
→ Market Value  
→ Volatility  
→ Shock  
→ Loss  

$$Loss = Market Value \times Shock$$

---

## 🔥 핵심 정의

- **Market Value**: 현재 공정 가치 (Exposure 역할)
- **Volatility**: 시장 변동성 (Shock 입력값)
- **Shock**: 가격 충격률 (실제 손실 결정 변수)
- **Loss**: 최종 손실 금액

---

# ⚙️ Shock 생성 구조

Shock는 Volatility로부터 결정됩니다:

Volatility  
→ Shock  

즉,

👉 Volatility = Risk Driver  
👉 Shock = Loss Trigger

→ [Volatility](../01_Core_Model/Volatility.md)

---

# 🧠 통합 프레임워크 (Credit Mapping - Secondary)

Equity를 Credit Risk로 해석하는 경우의 보조 모델입니다.

- **PD (부도 확률)**  
  - 기업 파산 또는 사업 실패 확률

- **LGD (손실률)**  
  - 100% 가정 (지분 후순위 구조)

- **EAD (익스포저)**  
  - Market Value 또는 투자 원금

---

⚠️ 이 Credit 구조는
- 회계적 통합
- 리스크 집계 목적
에만 사용됩니다.

👉 실제 리스크 계산의 중심은 Market Model입니다.

---

# 📉 특징

- 시장 변동성 기반 리스크 (Market Driven)
- Cashflow보다 Valuation 중심
- 비유동성 리스크 존재
- 변동성이 손실의 핵심 원인

---

# 🔗 구조적 위치

Equity Risk는 IB 모델에서:

👉 **Market Risk Layer**

---

# 🔥 자산별 비교

| 자산 | 리스크 구조 |
|------|------------|
| PF | Cashflow Risk |
| ABS | Structured Credit |
| NPL | Recovery Risk |
| Equity | Market Risk |

---

# 🔗 연결

→ [시장가치 (Market Value)](../01_Core_Model/Market_Value.md)  
→ [변동성 (Volatility)](../01_Core_Model/Volatility.md)  
→ [포지션 (Position)](../01_Core_Model/Position.md)