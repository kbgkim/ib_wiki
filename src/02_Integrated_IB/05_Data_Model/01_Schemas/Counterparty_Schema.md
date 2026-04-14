# 거래 상대방 스키마 (Counterparty Schema)

## 🔥 목적

딜(Deal)의 신용 리스크를 결정하는 핵심 주체인  
**거래 상대방(Counterparty)**의 신용 정보를 정의합니다.

---

# 📌 개념

Counterparty는 단순 법인이 아니라  
**PD(부도 확률)를 생성하는 Credit Driver Entity**입니다.

---

# 🧠 구조 역할

Counterparty  
→ PD Generation  
→ Deal Risk  
→ Portfolio Aggregation

---

# 📊 테이블 구조

| 컬럼명 | 설명 |
|--------|------|
| party_id | PK |
| party_name | 법인명 |
| reg_number | 사업자 등록번호 |
| internal_grade | 내부 신용등급 |
| external_grade | 외부 신용등급 |
| industry_type | 산업 분류 |
| financial_summary | 재무 요약 정보 |
| last_review_date | 신용 재평가일 |
| as_of_date | Snapshot 기준일 |

---

# ⚙️ 핵심 설계 원칙

## 1️⃣ PD 생성 엔진 입력값

Counterparty는 PD 계산의 입력 데이터입니다:

```text id="pd_input"
Counterparty → PD