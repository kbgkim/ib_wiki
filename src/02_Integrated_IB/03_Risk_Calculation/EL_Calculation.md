# 기대손실 계산 (Expected Loss Calculation)

## 🔥 개념 정의

Expected Loss (EL)은  
IB 리스크 모델에서 **최종 산출 결과값 (Result Layer)** 입니다.

즉,

👉 EL = Position 기반 모든 리스크 계산의 최종 출력값

---

## 📌 공식

$$EL = PD \times LGD \times EAD$$

- **PD**: 부도 확률 (Probability of Default)
- **LGD**: 부도 시 손실률 (Loss Given Default)
- **EAD**: 부도 시 익스포저 (Exposure at Default)

---

## ⚠️ NPL 특수 처리

NPL은 이미 부도 상태이므로:

PD = 100%

따라서:

EL = EAD × LGD

👉 이 경우 EL은 “회수 실패 결과”로 해석됨

---

# 🔄 계산 구조 (Execution Flow)

EL 계산은 단순 공식이 아니라  
**Position 기반 데이터 파이프라인**으로 수행됩니다.

---

## 1️⃣ Position Layer (기준 단위)

- 모든 리스크 계산의 시작점
- 자산 분해 단위

→ [Position](../01_Core_Model/Position.md)

---

## 2️⃣ Exposure / PD Layer

- 현재 노출액 산정
- 부도 확률 계산

→ Credit Risk 입력 단계

---

## 3️⃣ EAD Layer

- 부도 시점 노출액
- 미래 확장 Exposure 포함

→ [EAD](../01_Core_Model/EAD.md)

---

## 4️⃣ LGD Layer

- 담보 / 회수 기반 손실률 결정
- 자산별 구조 반영

→ [LGD](../01_Core_Model/LGD.md)

---

## 5️⃣ Result Layer (EL)

최종 산출:

EL = PD × LGD × EAD

---

# 🧠 자산별 EL 구조

## PF
- Cashflow 부족 → EL 증가

## ABS
- Waterfall 실패 → 트랜치 손실 → EL 증가

## NPL
- Recovery 실패 → LGD 변동 → EL 결정

## Equity
- Market Value × Shock → EL 대신 Loss 구조

---

# 📊 핵심 구조 요약

EL은 단독 계산이 아니라:

Position  
→ Risk Factors (PD / LGD / EAD)  
→ Aggregation  
→ Result (EL)

---

# 🔗 연결

→ [포지션 (Position)](../01_Core_Model/Position.md)  
→ [부도 확률 (PD)](../01_Core_Model/PD.md)  
→ [부도시노출액 (EAD)](../01_Core_Model/EAD.md)  
→ [손실률 (LGD)](../01_Core_Model/LGD.md)