# 손실률 (LGD; Loss Given Default)

## 🔥 목적

손실률(Loss Given Default)은 부도가 발생했을 때, 채권자나 투자자가 회수하지 못하고 실제로 잃게 되는 금액의 비율을 의미합니다. 
자산의 담보 가치와 우선순위(Waterfall)에 의해 결정됩니다.

### ─────────────

## 📌 개념

LGD는 1에서 회수율(Recovery Rate)을 뺀 값과 같습니다.

👉 **LGD = 1 - Recovery Rate**

IB 리스크에서 LGD는 단순히 고정된 수치가 아니라, 부도 시점의 담보 처분 가치나 현금흐름 재구조화 결과에 따라 변동됩니다.

### ─────────────

## 🧠 구조 역할

### 손실 산출 체인
1. 부도 확률(PD)로 부도 사건 발생  
2. 부도 시점의 총 노출액(EAD) 확정  
3. **LGD**를 적용하여 최종 손실 확정  
4. 기대손실(EL) = EAD × PD × LGD  

### ─────────────

## 💰 Cashflow 관점

LGD는 부도 이후 발생하는 회수 현금흐름(Recovery Cashflow)의 크기에 결정됩니다.

### 손실 전이 구조
부도 발생  
→ Cashflow 중단  
→ 담보 처분 또는 재구조화  
→ Recovery Cashflow 발생  
→ **미회수분(Shortfall) 발생**  
→ 최종 LGD 확정  

### ─────────────

## ⚖️ 자산별 해석

### PF (Project Financing)
- **주요 결정 요인**: LTV(담보인정비율), 시공사 책임 준공, 분양 대금 에스크로 구조

### ABS (Asset-Backed Securities)
- **주요 결정 요인**: 트랜치 순위(Senior/Mezzanine), 신용보강 규모, 워터폴(Waterfall) 구조

### NPL (Non-Performing Loan)
- **주요 결정 요인**: 담보물의 경·공매 낙찰가, 회수 예상 기간, 배당 순위

### Equity (지분 투자)
- **주요 결정 요인**: 원칙적으로 **LGD = 100%** (지분 자본의 후순위성)

### ─────────────

## 🔗 연결

- [부도확률 (PD)](./PD.md)
- [부도시노출액 (EAD)](./EAD.md)
- [기대손실 (Expected Loss)](./Expected_Loss.md)
- [현금흐름 (Cashflow)](./Cashflow.md)

### ─────────────

*최종 업데이트: 2026-04-14*