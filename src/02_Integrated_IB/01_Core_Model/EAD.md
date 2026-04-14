# 부도시노출액 (EAD; Exposure at Default)

## 🔥 목적

부도시노출액(Exposure at Default)은 부도가 발생하는 시점에 리스크에 노출되어 있을 것으로 예상되는 총 금액입니다. 
현재 노출액(Exposure)에 미래 추가 인출 가능액을 더해 산출됩니다.

### ─────────────

## 📌 개념

EAD는 단순히 현재의 대출 잔액이 아니라, 부도 시점까지 늘어날 수 있는 잠재적 노출액까지 고려한 수치입니다.

👉 **EAD = Current Exposure + (Undrawn Limit × CCF)**
- *CCF (Credit Conversion Factor): 미인출 한도의 유동성 소진 계수*

### ─────────────

## 🧠 구조 역할

### 리스크 산출 프로세스
1. Exposure 확인 (현재 잔액)  
2. 미래 시나리오 기반 인출 가능성 검토  
3. **EAD 산정**  
4. PD, LGD와 결합하여 EL 산출  

### ─────────────

## 📊 Exposure와의 차이

| 항목 | Exposure (현재 노출액) | EAD (부도 시 노출액) |
| :--- | :--- | :--- |
| **기준 시점** | 현재 (As-of Date) | 미래 부도 시점 |
| **속성** | 확발된 실물 데이터 | 추정 및 모델링 데이터 |
| **크기** | 확정 잔액 | Exposure + 미래 추가 노출 |

👉 일반적으로: **Exposure ≤ EAD**

### ─────────────

## 💰 Cashflow 관점

EAD의 변동은 미래에 발생할 현금 유출(Drawdown) 시나리오에 의해 결정됩니다.

### 변동 메커니즘
- 한도 대출(Commitment) 보유  
- 위기 상황 발생  
- 차주의 현금 확보를 위한 Drawdown(인출)  
- **EAD 상승**  
- 리스크 노출 확대  

### ─────────────

## ⚖️ 자산별 해석

### PF (Project Financing)
- 기 인출 금원 + 향후 공사비 집행을 위한 미인출 한도액

### ABS (Asset-Backed Securities)
- 투자한 트랜치의 현재 익스포저 (보통 추가 인출 한도가 없어 Exposure와 일치)

### NPL (Non-Performing Loan)
- 이미 부실화된 시점의 원금 잔액 + 미수이자

### Equity (지분 투자)
- 현재 투자 원가 또는 공정 가치 (전액 손실 가능성 기반)

### ─────────────

## 🔗 연결

- [노출액 (Exposure)](./Exposure.md)
- [손실률 (LGD)](./LGD.md)
- [부도확률 (PD)](./PD.md)
- [현금흐름 (Cashflow)](./Cashflow.md)

### ─────────────

*최종 업데이트: 2026-04-14*