# 포지션 (Position)

딜 내에서 내가 보유한 자금의 최소 관리 단위이며,  
모든 리스크를 계산하는 기준 단위입니다.

---

## 정의

Position은 하나의 딜(Deal)을 구성하는 개별 자금 단위입니다.

> 모든 리스크는 Position 단위에서 측정되고 집계됩니다.

---

## 역할

- **리스크 계산 기준**: 모든 Risk는 Position 단위에서 계산
- **Cashflow 귀속 단위**: 모든 자금 흐름이 연결되는 기준
- **노출 관리 단위**: Exposure 및 EAD 산출 기준

---

## 구조

Position은 다음 구조로 리스크에 연결됩니다:

Position  
→ Exposure (현재 노출)  
→ EAD (미래 노출)  
→ Cashflow (자금 흐름)  
→ LGD (손실률)  
→ EL (기대손실)  

---

## 구성 요소

- Deal ID
- Position Type (대출, 투자 등)
- Exposure
- EAD
- Cashflow
- Risk 결과 (EL / Loss)

---

## 자산별 예시

### PF (Project Financing)
- 선순위 대출
- 후순위 투자

---

### ABS (Asset-Backed Securities)
- 트랜치 (선순위 / 중순위 / 후순위)

---

### NPL (Non-Performing Loan)
- 개별 채권 또는 담보 단위

---

### Equity (지분 투자)
- 투자 건별 지분 (포트폴리오사 단위)

---

## 특징

- 모든 자산을 동일 구조로 표현 가능
- 포트폴리오 집계의 최소 단위
- Credit Risk / Equity Risk 모두 수용 가능

---

## 연결

→ [딜 (Deal)](../00_Root_Model/IB_Risk_Data_Model.md)  
→ [노출액 (Exposure)](./Exposure.md)  
→ [부도시노출액 (EAD)](./EAD.md)  
→ [현금흐름 (Cashflow)](./Cashflow.md)  
→ [손실률 (LGD)](./LGD.md)  
→ [기대손실 (Expected Loss)](./Expected_Loss.md)