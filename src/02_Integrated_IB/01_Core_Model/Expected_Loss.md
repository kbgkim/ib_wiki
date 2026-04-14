# 기대손실 (Expected Loss, EL)

예상 손실 금액으로서 리스크 관리의 핵심 지표입니다.

---

## 공식

EL = PD × LGD × EAD  

- **PD (부도 확률)**: 차주 또는 프로젝트의 부도 가능성  
- **LGD (손실률)**: 부도 시 회수되지 못하는 비율  
- **EAD (부도시노출액)**: 부도 시점 기준 노출 금액  

---

## 개념 설명

EL은 “확률적으로 예상되는 평균 손실”을 의미합니다.

- 실제 발생 손실이 아닌 기대값
- 개별 포지션보다 포트폴리오에서 의미가 큼

---

## Cashflow 관점

EL은 현금흐름 부족 가능성을 확률적으로 표현한 값입니다.

Expected Cashflow 감소 가능성  
→ Shortfall 발생 가능성  
→ Recovery 감소  
→ Loss 기대값 = EL  

즉, EL은 미래 Cashflow 리스크를 정량화한 결과입니다.

---

## 자산별 적용

### PF / ABS / NPL
- Credit Risk 기반 EL 적용

---

### NPL (부실채권)
- PD = 100% 적용  
→ EL = LGD × EAD  

---

### Equity (지분 투자)
- EL 개념을 직접 사용하지 않음  
- 대신 Market Value 기반 손실 사용  

Loss = Market Value × Shock  

---

## 의미

- **충당금 기준**: 회계 및 규제 목적 손실 예상치  
- **리스크 지표**: 포트폴리오 위험 수준 평가  
- **의사결정 기준**: 투자 및 한도 설정 기준  

---

## 연결

→ [부도 확률 (PD)](./PD.md)  
→ [부도시노출액 (EAD)](./EAD.md)  
→ [손실률 (LGD)](./LGD.md)  
→ [현금흐름 (Cashflow)](./Cashflow.md)