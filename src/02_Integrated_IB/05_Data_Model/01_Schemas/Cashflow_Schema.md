# 현금흐름 스키마 (Cashflow Schema)

## 🔥 목적

Position 단위의 모든 현금 흐름을 이벤트 기반으로 기록하고  
리스크 계산의 원천 데이터로 활용합니다.

---

# 📌 개념 (핵심)

Cashflow는 단순 금액 데이터가 아니라  
**금융 이벤트(Event Stream)** 입니다.

👉 모든 리스크는 Cashflow의 부족(Shortfall)에서 발생합니다.

---

# 🧠 구조 관계

Deal  
→ Position  
→ Cashflow (Event Stream)  
→ Risk Engine

---

# 📊 테이블 구조

| 컬럼명 | 설명 |
|--------|------|
| cashflow_id | PK |
| position_id | FK |
| deal_id | FK |
| cashflow_date | 실제/예정 발생일 |
| cashflow_type | 이벤트 유형 |
| expected_amount | 예상 금액 |
| actual_amount | 실제 금액 |
| currency | 통화 |
| event_status | PLANNED / CONFIRMED / SETTLED |
| as_of_date | Snapshot 기준일 |

---

# ⚙️ Cashflow = Event Model

Cashflow는 다음과 같은 특징을 가집니다:

- Append-only 구조
- 시간 기반 이벤트 로그
- Position 중심 집계

---

# 🔥 Cashflow Type (Risk Mapping Key)

| Type | 의미 | Risk 영향 |
|------|------|------------|
| PRINCIPAL | 원금 | EAD 직접 영향 |
| INTEREST | 이자 | PF / NPL Cashflow |
| FEE | 수수료 | 수익성 |
| RECOVERY | 회수 | LGD 결정 |
| DIVIDEND | 배당 | Equity Cashflow |
| EXIT | 회수 이벤트 | Equity Loss |

---

# 📉 리스크 생성 구조

## 1️⃣ Shortfall

Position 단위:

```text
Shortfall = Expected Cashflow - Actual Cashflow