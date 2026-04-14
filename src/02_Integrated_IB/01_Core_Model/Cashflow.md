# 현금흐름 (Cashflow)

## 🔥 목적

딜(Deal)과 포지션(Position)에서 발생하는 실제 자금의 유효한 유입과 유출을 의미합니다.  
IB 리스크 관리의 가장 근본적인 관측 데이터입니다.

### ─────────────

## 📌 개념

- **Inflow (유입)**: 원금 상환, 이자 수익, 분양 대금, 배당금 등  
- **Outflow (유출)**: 대출 실행(Drawdown), 투자 집행, 운영 비용 등  

### ─────────────

## 🧠 리스크와의 관계

모든 리스크는 **현금흐름의 부족 (Shortfall)**에서 시작됩니다.

### 리스크 발생의 매커니즘
Expected Cashflow  
→ Actual Cashflow  
→ Shortfall  
→ Recovery  
→ Loss  

### ─────────────

## 📊 주요 지표

- **Expected Cashflow**: 계약 및 사업 계획상 예정된 현금흐름  
- **Actual Cashflow**: 실제로 발생한 현금흐름  
- **Net Cashflow**: 특정 시점의 순 현금 유입액 (Inflow - Outflow)  

### ─────────────

## ⚙️ Exposure / EAD와의 관계

Cashflow는 노출액 변동의 원인입니다.

### 변동 요인 분석
- Drawdown (자금 인출) → Exposure 증가 → EAD 증가  
- Repayment (상환) → Exposure 감소 → EAD 감소  
- Interest Accrual (이자 누적) → EAD 증가  

👉 즉, Cashflow는 Exposure와 EAD를 변화시키는 핵심 요인입니다.

### ─────────────

## ⚖️ 자산별 해석

### PF (Project Financing)
- 분양대금 및 사업 Cashflow가 상환 재원

### ABS (Asset-Backed Securities)
- 기초자산 Pool Cashflow가 투자 수익의 원천

### NPL (Non-Performing Loan)
- 담보 회수 및 배당 Cashflow

### Equity (지분 투자)
- Dividend 및 Exit Cashflow  
- 단, 리스크는 Market Value 변동으로 추가 반영

### ─────────────

## 🔗 연결

- [포지션 (Position)](./Position.md)
- [노출액 (Exposure)](./Exposure.md)
- [부도시노출액 (EAD)](./EAD.md)
- [손실률 (LGD)](./LGD.md)
- [현금흐름 스키마 (Cashflow Schema)](../05_Data_Model/01_Schemas/Cashflow_Schema.md)
- [손실 발생 구조 (Logic)](../05_Data_Model/02_Logic/Cashflow_to_Loss_Logic.md)

### ─────────────

*최종 업데이트: 2026-04-14*