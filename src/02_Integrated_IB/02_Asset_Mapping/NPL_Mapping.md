# NPL 매핑 (NPL Mapping)

부실채권(NPL) 투자를 Position 기반 리스크 모델로 변환합니다.

---

## 포지션 (Position)

- 개별 채권 단위  
- 담보 또는 채무자 기준으로 분리 관리  

---

## 부도 확률 (PD)

- **100% 고정**
- 이미 부실화된 자산이므로 PD 변동 없음  

👉 NPL에서는 PD가 아니라 **회수율이 리스크를 결정**

---

## 노출액 (Exposure)

- **OPB (Outstanding Principal Balance)**  
- 미상환 원금 기준 금액  

---

## 부도시노출액 (EAD)

NPL에서 EAD는 일반 Credit과 다르게 정의됩니다.

👉 **EAD = Recovery 기준 Exposure**

구성:
- OPB
- 연체이자
- 법적 비용
- 기타 회수 대상 금액

---

## 손실률 (LGD)

LGD는 회수 결과에 의해 결정됩니다.

LGD = 1 - (Actual Recovery / EAD)

---

## 💰 Cashflow 관점 (핵심 구조)

NPL은 **Recovery 기반 Cashflow 모델**입니다.

---

### 구조

- **Expected Recovery**
  - 담보 평가 기반 예상 회수금

- **Actual Recovery**
  - 실제 회수 금액 (경매 / 매각 / 배당)

---

### Loss 생성 구조

Expected Recovery  
→ Actual Recovery  
→ Shortfall  

Shortfall = Expected - Actual  

---

### Risk Engine 흐름

Recovery 부족  
→ LGD 증가  
→ EL 증가  

---

## 🔥 핵심 구조 정의

👉 NPL은 “Default Model”이 아니라

> ❗ **Recovery Model (회수 기반 리스크 모델)**

---

## 특징

- PD = 100% 고정
- 리스크 변동 요인 = LGD (회수율)
- Cashflow = 회수 이벤트 중심
- 시장 영향 = 담보 가치 직접 반영

---

## 핵심 리스크 요인

- 경매가 하락 (부동산 경기 영향)
- 회수 지연 (법적 절차)
- 담보 가치 변동
- 추가 비용 발생 (소송 / 관리비)

---

## 구조적 위치

NPL은 다음 구조를 가집니다:

Credit Model의 특수형 + Recovery 중심 구조

---

## 연결

→ [포지션 (Position)](../01_Core_Model/Position.md)  
→ [노출액 (Exposure)](../01_Core_Model/Exposure.md)  
→ [부도시노출액 (EAD)](../01_Core_Model/EAD.md)  
→ [손실률 (LGD)](../01_Core_Model/LGD.md)  
→ [현금흐름 (Cashflow)](../01_Core_Model/Cashflow.md)