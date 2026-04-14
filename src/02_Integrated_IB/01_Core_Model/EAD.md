# 부도시노출액 (EAD, Exposure at Default)

부도 발생 시점에 예상되는 총 노출 금액입니다.

---

## 정의

EAD는 부도 시점 기준으로 실제 회수 대상이 되는 금액입니다.

---

## Exposure와의 관계

- **Exposure**: 현재 시점 기준 노출 금액  
- **EAD**: 미래 부도 시점 기준 노출 금액  

일반적으로:

Exposure ≤ EAD  

---

## 특징

- **미사용 한도 포함**: 향후 추가 인출이 예상되는 금액 반영  
- **이자 누적 반영**: 부도 시점까지 발생할 이자 및 비용 포함  
- **확장성**: 현재 Exposure보다 커질 수 있는 잠재적 노출  

---

## 구성 요소

- 현재 노출액 (Exposure)
- 미사용 약정 (Undrawn Commitment)
- 발생 예정 이자
- 기타 비용 (수수료, 법적 비용 등)

---

## Cashflow 관점

EAD는 미래 Cashflow를 반영한 값입니다.

- Drawdown (추가 인출)
→ EAD 증가  

- Interest Accrual (이자 누적)
→ EAD 증가  

- Repayment (상환)
→ EAD 감소  

즉, EAD는 미래 시점에서의 Cashflow 결과를 반영한 노출 금액입니다.

---

## 자산별 해석

### PF (Project Financing)
- 현재 인출액 + 향후 인출 예정액 (공사비 등)

---

### ABS (Asset-Backed Securities)
- 잔존 투자금 및 잔여 기간 동안의 노출

---

### NPL (Non-Performing Loan)
- OPB + 연체 이자 + 법적 비용

---

### Equity (지분 투자)
- EAD 개념을 직접 사용하지 않음

---

## 연결

→ [노출액 (Exposure)](./Exposure.md)  
→ [손실률 (LGD)](./LGD.md)  
→ [기대손실 (Expected Loss)](./Expected_Loss.md)