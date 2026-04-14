# ABS 매핑 (ABS Mapping)

자산유동화(ABS) 구조를 Position 기반 리스크 모델로 변환합니다.

---

## 포지션 (Position)

- **트랜치 (Tranching)**: 선순위 / 중순위 / 후순위로 구성된 구조화 투자 단위  
- 각 트랜치는 서로 다른 리스크와 수익을 가짐  

---

## 부도 확률 (PD)

- **기초자산 부도율**을 기반으로 산출  
- 유동화 포트폴리오 전체의 평균 부도 위험을 반영  

---

## 노출액 (Exposure)

- 현재 시점의 투자 원금  
- 트랜치별로 독립적으로 관리  

---

## 부도시노출액 (EAD)

- 잔존 투자금 + 미회수 가능 Cashflow  
- 트랜치 구조에 따라 다르게 산출  

---

## 손실률 (LGD)

LGD는 **Waterfall 구조에 의해 결정됩니다.**

- 선순위: 낮은 LGD  
- 중순위: 중간 LGD  
- 후순위: 높은 LGD  

---

# 💰 Cashflow 관점 (핵심 구조)

ABS의 리스크는 기초자산 Cashflow 실패에서 발생합니다.

---

## Cashflow 구조

- **Pool Cashflow**
  - 대출 상환
  - 매출채권 회수
  - 임대 수익

- **Expected Cashflow**
  - 구조 설계 시 가정된 유입

- **Actual Cashflow**
  - 실제 회수된 금액

---

## Loss 생성 구조

Expected Cashflow  
→ Actual Cashflow  
→ Shortfall  

---

## Waterfall 구조 (핵심)

Cashflow는 트랜치 우선순위에 따라 배분됩니다:

1. **선순위 트랜치**
2. **중순위 트랜치**
3. **후순위 트랜치**

---

## Loss 전달 구조 (Tranche Erosion)

Shortfall 발생 시:

후순위 → 먼저 손실 흡수  
중순위 → 다음 손실 흡수  
선순위 → 마지막 방어선  

---

## 리스크 전이 구조

Shortfall  
→ Waterfall 배분 실패  
→ Tranche LGD 증가  
→ Expected Loss 증가  

---

## 핵심 리스크 요인

- 기초자산 Cashflow 감소  
- 트랜치 손실 전이 (Subordination Failure)  
- 신용보강 약화 (OC / Guarantee)  
- 조기상환 / 연체 구조 붕괴  

---

## 구조적 위치 (모델 내 의미)

ABS는 다음 중간 구조를 가집니다:

- Credit Risk (PF/NPL) + Cashflow 기반
- Equity Risk (Market Loss) 구조 일부 포함

즉,

👉 **Credit + Structured Layer Hybrid Model**

---

## 연결

→ [포지션 (Position)](../01_Core_Model/Position.md)  
→ [현금흐름 (Cashflow)](../01_Core_Model/Cashflow.md)  
→ [부도시노출액 (EAD)](../01_Core_Model/EAD.md)  
→ [손실률 (LGD)](../01_Core_Model/LGD.md)