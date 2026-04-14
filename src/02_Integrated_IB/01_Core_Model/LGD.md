# 손실률 (LGD, Loss Given Default)

부도 발생 시 실제 손실로 확정되는 비율입니다.

---

## 통합 정의

LGD = 1 - (Recovery / EAD)

- **Recovery**: 부도 이후 회수된 금액
- **EAD (Exposure at Default)**: 부도 시점 기준 총 노출 금액

---

## 개념 설명

- LGD는 “얼마를 잃었는가”가 아니라  
  “얼마를 회수하지 못했는가”를 의미합니다.
- 즉, 회수율(Recovery Rate)의 보완 개념입니다.

---

## Cashflow 관점

LGD는 현금흐름(Cashflow) 부족의 결과로 발생합니다.

Expected Cashflow  
- Actual Cashflow  
= Shortfall  

Shortfall이 누적되면  
→ 최종적으로 Recovery 감소  
→ LGD 증가로 이어집니다.

---

## 자산별 해석

### PF (Project Financing)
- 분양 및 사업 Cashflow 기반 회수
- 미분양, 공사 지연 → Recovery 감소 → LGD 증가

---

### ABS (Asset-Backed Securities)
- 기초자산 Cashflow를 Waterfall 구조로 배분
- Cashflow 부족 → 트랜치별 손실 분배 → LGD 결정

---

### NPL (Non-Performing Loan)
- 담보 회수 기반
- 경매 낙찰가 및 회수금액이 Recovery를 결정
- LGD는 회수율에 직접적으로 의존

---

### Equity (지분 투자)
- LGD 개념을 직접 적용하지 않음
- 대신 Market Value 기반 손실로 측정

---

## 결정 요소

- **담보 가치**: 담보물의 경매/매각을 통한 회수 가능 금액
- **회수율**: 회수 비용을 제외한 순 회수 가능성
- **시장 상황**: 불황기 담보 가치 하락 등 거시 경제 요인

---

## 연결

→ [부도 확률 (PD)](./PD.md)  
→ [부도시노출액 (EAD)](./EAD.md)  
→ [기대손실 (Expected_Loss)](./Expected_Loss.md)  
→ [현금흐름 (Cashflow)](./Cashflow.md)