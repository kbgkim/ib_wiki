# PF 매핑 (PF Mapping)

부동산 PF(Project Finance) 구조를 Position 기반 리스크 모델로 변환합니다.

---

## 🔥 PF의 본질

PF는 단순 대출이 아니라:

> ❗ **단일 프로젝트의 Cashflow 기반 구조화 신용 리스크 모델**

---

## 포지션 (Position) 구조

- **선순위 대출**
  - 담보권 우선
  - 안정적 회수 구조

- **후순위 투자**
  - 고수익 구조
  - 손실 흡수 역할 (Buffer Layer)

---

## 부도 확률 (PD)

PF에서 PD는 일반 Credit PD가 아니라:

👉 **Project Failure Probability**

구성 요소:
- 시행사 신용도
- 시공사 수행 능력
- 인허가 리스크
- 분양 성공 가능성

---

## 노출액 (Exposure)

- 대출 잔액
- 투자 집행 원금

---

## 부도시노출액 (EAD)

- 현재 인출 금액
- 미사용 한도 (Commitment)

---

## 손실률 (LGD)

LGD는 PF 구조에서 다음에 의해 결정됩니다:

- 담보 가치 (LTV)
- 분양률
- 프로젝트 종료 시점 회수 구조

---

# 💰 Cashflow 핵심 구조

PF 리스크의 본질은 Cashflow mismatch입니다.

---

## Cashflow 구조

- **Expected Cashflow**
  - 분양 대금
  - 임대 수익
  - 사업 수익

- **Actual Cashflow**
  - 실제 유입 자금

---

## Loss 생성 구조

Expected Cashflow  
→ Actual Cashflow  
→ Shortfall  

Shortfall = Cashflow 부족액

---

## Risk Transmission 구조

Cashflow 부족  
→ 회수율 감소  
→ LGD 증가  
→ EL 증가  

---

# 🏗 PF 핵심 특징

- 단일 프로젝트 기반 구조
- Cashflow 집중형 리스크
- 분양/공정률에 민감
- 시간 지연(Time Risk) 매우 중요

---

# ⚠️ 주요 리스크 요인

- 미분양 리스크 (Demand Failure)
- 공사 지연 (Construction Delay)
- 인허가 실패
- 금리 상승 (Financing Cost Increase)
- 분양률 하락

---

# 🔗 구조적 위치

PF는 다음 구조에 속합니다:

👉 **Cashflow-based Credit Risk Model**

---

# 🔗 ABS와의 차이

| 구분 | PF | ABS |
|------|----|-----|
| 구조 | 단일 프로젝트 | 자산 Pool |
| Cashflow | 직접 | 간접 |
| 구조화 | 낮음 | 높음 |
| 리스크 | 사업 실패 | 트랜치 전이 |

---

## 연결

→ [포지션 (Position)](../01_Core_Model/Position.md)  
→ [현금흐름 (Cashflow)](../01_Core_Model/Cashflow.md)  
→ [노출액 (Exposure)](../01_Core_Model/Exposure.md)  
→ [손실률 (LGD)](../01_Core_Model/LGD.md)