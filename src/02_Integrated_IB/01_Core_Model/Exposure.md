# 노출액 (Exposure)

현재 시점 기준 리스크 노출 금액입니다.

---

## 정의

- **대출 잔액**: 현재 인출된 원금 규모
- **투자 금액**: 실제 투입된 자본 총액
- **보증 금액**: 신용 보강 등을 위해 제공된 보증액

---

## 개념 설명

Exposure는 “현재 시점에서 실제로 위험에 노출된 금액”을 의미합니다.

- 이미 실행된 금액만 포함
- 미래 인출 예정 금액은 포함하지 않음

---

## EAD와의 관계

- **Exposure**: 현재 시점 기준 노출 금액  
- **EAD (Exposure at Default)**: 부도 시점 기준 예상 노출 금액  

일반적으로:

Exposure ≤ EAD  

---

## 자산별 해석

### PF (Project Financing)
- 현재 인출된 대출 잔액

---

### ABS (Asset-Backed Securities)
- 현재 투자된 트랜치별 투자 금액

---

### NPL (Non-Performing Loan)
- OPB (미상환 원금 잔액)

---

### Equity (지분 투자)
- 투자 원금 또는 현재 시장 가치 (Market Value 기준 선택 가능)

---

## Cashflow 관점

Exposure는 과거 Cashflow의 결과입니다.

- Drawdown (자금 인출)
→ Exposure 증가  

- Repayment (상환)
→ Exposure 감소  

즉, Exposure는 Cashflow 흐름의 누적 결과로 형성됩니다.

---

## 특징

- **현재 기준**: 미래 변동을 제외한 확정된 노출 금액
- **Position 단위**: 개별 포지션별로 산출
- **동적 변화**: Cashflow에 따라 지속적으로 변동

---

## 연결

→ [포지션 (Position)](./Position.md)  
→ [부도시노출액 (EAD)](./EAD.md)  
→ [현금흐름 (Cashflow)](./Cashflow.md)