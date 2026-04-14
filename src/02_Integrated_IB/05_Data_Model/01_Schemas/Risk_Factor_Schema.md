# 리스크 요인 스키마 (Risk Factor Schema)

## 🔥 목적

시장 및 거시경제 데이터를 기반으로  
리스크 시나리오 충격(Shock)을 생성하는 **기초 입력 데이터**를 정의합니다.

---

# 📌 개념

Risk Factor는 다음 역할을 수행합니다:

👉 Market Observation Layer  
👉 Shock Generator Input  
👉 Scenario Engine Base Data

---

# 🧠 구조 역할

Risk Factor  
→ Shock  
→ Scenario  
→ Risk Engine  
→ Cashflow / Loss

---

# 📊 테이블 구조

| 컬럼명 | 설명 |
|--------|------|
| factor_id | PK |
| factor_name | 시장 지표명 |
| factor_type | INTEREST_RATE / FX / INDEX / COMMODITY |
| base_value | 현재 시장 가격 (Spot Value) |
| historical_volatility | 과거 변동성 |
| stress_volatility | 스트레스 변동성 |
| source | 데이터 출처 |
| as_of_date | Snapshot 기준일 |

---

# ⚙️ 핵심 설계 원칙

## 1️⃣ Market Observation Layer

Risk Factor는 실제 관측값입니다:

```text id="obs"
Market Data → Risk Factor