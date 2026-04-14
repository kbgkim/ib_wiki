# 딜 스키마 (Deal Schema)

## 🔥 목적

IB 금융 거래의 최상위 객체인 **딜(Deal)**의 마스터 및 리스크 기준 단위를 정의합니다.

---

## 📌 개념

**Deal**은 다음 구조의 최상위 레벨입니다:

Deal  
→ Position  
→ Cashflow  
→ Risk

👉 모든 리스크 계산은 Deal 단위 집계로 종료됩니다.

---

# 🧠 역할 정의

- Deal = Business Contract Unit
- Position = Risk Calculation Unit
- Cashflow = Financial Movement Unit

---

# 📊 테이블 구조

| 컬럼명 | 설명 | 비고 |
|--------|------|------|
| deal_id | PK | 딜 고유 식별자 |
| deal_name | 딜 명칭 | 국문/영문 |
| industry_code | 자산군/산업 분류 | PF / NPL / ABS / Equity |
| currency | 통화 | KRW, USD 등 |
| total_commitment | 총 약정액 | Deal 규모 |
| start_date | 실행일 | 최초 실행 |
| end_date | 만기일 | 종료 예정 |
| status | 라이프사이클 상태 | ACTIVE / MATURED / DEFAULT / WRITTEN_OFF |
| dept_code | 담당 부서 | RM / 심사 / 운용 |
| as_of_date | 기준일 (Snapshot Key) | ⚠ 핵심 키 |

---

# 🔥 Deal Lifecycle (중요)

Deal 상태는 단순 상태값이 아니라  
**리스크 이벤트 트리거 기준**입니다.

- ACTIVE → 정상 운영
- MATURED → 만기 종료
- DEFAULT → 부도 발생
- WRITTEN_OFF → 손실 확정
- RESTRUCTURED → 구조조정

---

# 🔗 구조적 관계

## 1:N 관계

Deal  
→ Position (1:N)

👉 하나의 Deal은 여러 Position으로 분해됨

---

# ⚙️ Data Mart 설계 핵심

## as_of_date 역할

- 모든 데이터의 Snapshot 기준
- Risk Engine 실행 기준 시점
- Time-series 분석 Key

---

# 📈 Risk Model 연결

Deal은 직접 리스크를 계산하지 않고:

Deal  
→ Position  
→ Risk Engine  
→ EL / Loss

---

# 🔗 연결

→ [포지션 스키마 (Position Schema)](./Position_Schema.md)  
→ [현금흐름 (Cashflow)](../../01_Core_Model/Cashflow.md)