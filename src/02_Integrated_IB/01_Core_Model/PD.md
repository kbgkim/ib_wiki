# 부도확률 (PD; Probability of Default)

## 🔥 목적

부도확률(Probability of Default)은 특정 관찰 기간 내에 차주 혹은 자산 포지션이 약속된 현금흐름(이자, 원금 등)을 지급하지 못할 확률을 의미합니다. 
기대손실(Expected Loss) 산출의 가장 핵심적인 확률 변수입니다.

### ─────────────

## 📌 개념

부도의 정의는 단순히 파산뿐만 아니라, 약정된 지급 기일에서 일정 기간(예: 90일) 이상 연체된 상태를 모두 포함합니다.

👉 IB 리스크에서 PD는 **"현금흐름 창출 실패의 확률"**로 정의됩니다.

### ─────────────

## 🧠 구조 역할

### 리스크 체인에서의 위치
1. 리스크 요인(Risk Factor) 발생  
2. 현금흐름(Cashflow) 변동성 증대  
3. **부도 확률(PD) 상승**  
4. 손실(Loss) 발생 가능성 확대  
5. 기대손실(EL) 산출  

### ─────────────

## 💰 Cashflow 관점

PD는 Expected Cashflow가 실제로 실현되지 못할 확률입니다.

### 현금흐름 전이 구조
Expected Cashflow  
→ 미이행 가능성 (PD)  
→ Shortfall 발생  
→ Loss 발생  

### ─────────────

## ⚖️ 자산별 특성

### PF (Project Financing)
- 시행사/시공사 신용도 + 사업성 기반 산출

### ABS (Asset-Backed Securities)
- 기초자산 Pool의 평균 부도율 기반

### NPL (Non-Performing Loan)
- 이미 부도 상태  
👉 **PD = 100%** 적용  

### Equity (지분 투자)
- 명확한 PD 개념 적용 어려움  
- 기업 실패 확률로 간접 사용 가능  
- 실무에서는 Market Risk 중심으로 관리

### ─────────────

## 🔗 연결

- [부도시노출액 (EAD)](./EAD.md)
- [손실률 (LGD)](./LGD.md)
- [기대손실 (Expected Loss)](./Expected_Loss.md)
- [현금흐름 (Cashflow)](./Cashflow.md)

### ─────────────

*최종 업데이트: 2026-04-14*