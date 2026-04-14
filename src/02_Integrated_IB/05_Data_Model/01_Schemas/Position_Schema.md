# 포지션 스키마 (Position Schema)

## 🔥 목적

모든 IB 자산(PF, NPL, ABS, Equity)의 **리스크 계산 및 현금흐름 관리 기준 단위**인 Position을 정의합니다.

---

# 📌 개념

Position은 단순 데이터가 아니라 다음 3가지 역할을 수행합니다:

- Risk Calculation Unit
- Cashflow Generation Unit
- Exposure Tracking Unit

---

# 🧠 구조 관계

Deal  
→ Position (1:N)  
→ Cashflow  
→ Risk

---

# 📊 테이블 구조

| 컬럼명 | 설명 |
|--------|------|
| position_id | PK |
| deal_id | Deal FK |
| asset_type | PF / NPL / ABS / Equity |
| position_status | ACTIVE / CLOSED / DEFAULT / WRITTEN_OFF |
| exposure | 현재 노출 금액 |
| market_value | 평가 금액 (Equity 중심) |
| as_of_date | Snapshot 기준일 |

---

# ⚙️ 핵심 설계 원칙

## 1️⃣ Position = Risk Engine Input Unit

모든 리스크 계산은 Position 단위로 수행됩니다.

---

## 2️⃣ Asset Type = Risk Engine Routing Key

| asset_type | Risk Model |
|------------|------------|
| PF | Cashflow Risk |
| NPL | Recovery Risk |
| ABS | Structured Credit Risk |
| Equity | Market Risk |

---

## 3️⃣ EAD / LGD 구조 (Derived Fields)

다음 값은 저장값이 아니라 **파생 계산값**입니다:

- EAD = Exposure + Future Drawdown
- LGD = Loss / EAD

---

## 4️⃣ Lifecycle 관리

Position 상태는 리스크 이벤트와 직접 연결됩니다:

- ACTIVE → 정상
- CLOSED → 종료
- DEFAULT → 부도 발생
- WRITTEN_OFF → 손실 확정

---

## 📈 시간 구조 (Critical)

- as_of_date = Snapshot Key
- 모든 리스크 계산 기준 시점

---

# 🔥 리스크 엔진 역할

Position은 다음 입력을 제공합니다:

Position  
→ Cashflow  
→ Risk Engine  
→ EL / Loss

---

# 🔗 연결

→ [딜 스키마 (Deal Schema)](./Deal_Schema.md)  
→ [현금흐름 (Cashflow)](../../01_Core_Model/Cashflow.md)  
→ [리스크 결과 스키마 (Risk Result Schema)](./Risk_Result_Schema.md)