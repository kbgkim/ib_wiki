# 담보 스키마 (Collateral Schema)

## 🔥 목적

딜의 회수 가능성(Recovery)을 결정하여  
**LGD(손실률)**를 산출하는 핵심 입력 데이터입니다.

---

# 📌 개념

Collateral은 단순 자산이 아니라:

👉 Recovery Engine Input Layer  
👉 LGD 결정 핵심 요소

---

# 🧠 구조 역할

Position  
→ Collateral  
→ Recovery  
→ LGD  
→ EL

---

# 📊 테이블 구조

| 컬럼명 | 설명 |
|--------|------|
| collateral_id | PK |
| position_id | FK |
| collateral_type | 담보 유형 (부동산, 주식, 예금 등) |
| val_amount | 평가액 (Market Value) |
| val_date | 평가 기준일 |
| senior_amount | 선순위 채권액 |
| status | 담보 상태 |
| as_of_date | Snapshot 기준일 |

---

# ⚙️ 핵심 설계 원칙

## 1️⃣ net value = Derived Field

```text id="net_value"
net_val_amount = val_amount - senior_amount