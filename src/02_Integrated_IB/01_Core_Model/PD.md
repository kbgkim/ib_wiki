# 부도 확률 (Probability of Default, PD)

차주 또는 대상 자산이 약속된 시점에 의무를 이행하지 못할(부도) 가능성을 나타내는 지표입니다.

---

## 정의

- 특정 관측 기간(일반적으로 1년) 내 부도 발생 확률
- 리스크 측정의 핵심 입력 변수

---

## 개념적 의미

PD는 “Cashflow 실패 이벤트의 발생 확률”입니다.

즉,

정상 Cashflow 발생  
→ 부도 없음  

Cashflow 미이행 (Shortfall 발생)  
→ 부도 발생  

---

## 리스크 구조 내 역할

PD는 다음 구조에서 시작점 역할을 합니다:

PD  
→ Default 발생 여부  
→ EAD 확정  
→ LGD 적용  
→ EL 산출  

---

## Cashflow 관점

PD는 Expected Cashflow가 실제로 실현되지 못할 확률입니다.

Expected Cashflow  
→ 미이행 가능성 (PD)  
→ Shortfall 발생  
→ Loss 발생  

---

## 자산별 특성

### PF (Project Financing)
- 시행사/시공사 신용도 + 사업성 기반 산출

---

### ABS (Asset-Backed Securities)
- 기초자산 Pool의 평균 부도율 기반

---

### NPL (Non-Performing Loan)
- 이미 부도 상태  
→ PD = 100% 적용  

---

### Equity (지분 투자)
- 명확한 PD 개념 적용 어려움  
- 기업 실패 확률로 간접 사용 가능  
- 실무에서는 Market Risk 중심으로 관리

---

## 특징

- 시간 기반 확률 (Time horizon 의존)
- 경기 및 산업 환경에 민감
- 포트폴리오 리스크 집계 시 핵심 변수

---

## 연결

→ [부도시노출액 (EAD)](./EAD.md)  
→ [손실률 (LGD)](./LGD.md)  
→ [기대손실 (Expected Loss)](./Expected_Loss.md)  
→ [현금흐름 (Cashflow)](./Cashflow.md)