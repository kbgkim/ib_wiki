# NPL 매핑 (NPL Mapping)

부실채권(NPL) 투자를 Position 기반 리스크 모델로 변환합니다.

---

## 포지션 (Position)

- **개별 채권**: 담보물별 또는 채무자별 개별 관리 단위  

---

## 부도 확률 (PD)

- **100% 고정**: NPL은 이미 부실화된 자산이므로 PD = 100%를 전제합니다.

---

## 노출액 (Exposure)

- **OPB (Outstanding Principal Balance)**: 채권의 미상환 원금 잔액  

---

## 부도시노출액 (EAD)

- 원금(OPB) + 회수 시점까지의 연체 이자 + 법적 비용 등을 포함한 총 회수 대상 금액  

---

## 손실률 (LGD)

- **담보 회수율 기반 산출**

LGD = 1 - (Recovery / EAD)

- Recovery는 다음 요소를 반영하여 산정합니다:
  - 경매 낙찰가
  - 수의매각 예상가
  - 회수 비용 차감

---

## Cashflow 관점

NPL 자산의 리스크는  
회수금(Recovery) 기준 Cashflow 부족으로 설명됩니다.

---

### 구조

- **Expected Recovery**
  - 담보 평가액 기준 예상 회수금

- **Actual Recovery**
  - 실제 회수된 금액 (경매, 매각, 배당 등)

---

### 손실 발생 구조

**Expected Recovery**  
- **Actual Recovery**  
= **Shortfall** (회수 부족액)

**Shortfall**이 발생하면  
→ 담보 처분을 통한 현금 유입이 계획보다 적음을 의미하며  
→ 이는 즉각적인 **손실(Loss)**로 인식됩니다.

---

### 리스크 지표 연결

**Recovery 부족**  
→ **손실률(LGD)** 상승: $LGD = 1 - (Actual Recovery / EAD)$  
→ **기대손실(Expected Loss)** 증가  

> **NPL과 PD**  
> NPL은 **PD = 100%**로 고정되어 있으므로, 리스크의 변동성은 오직 **LGD(회수율)**의 변화에 의해 결정됩니다.

---

## 핵심 리스크 요인

- **경매가 하락**: 부동산 경기 악화로 낙찰가 저하  
- **회수 기간 지연**: 법적 분쟁 및 절차 지연  
- **담보 가치 변동**: 시장 상황에 따른 회수율 변화  
- **추가 비용 발생**: 소송비, 관리비 등  

---

## 연결

→ [포지션 (Position)](../01_Core_Model/Position.md)  
→ [노출액 (Exposure)](../01_Core_Model/Exposure.md)  
→ [부도시노출액 (EAD)](../01_Core_Model/EAD.md)  
→ [손실률 (LGD)](../01_Core_Model/LGD.md)  
→ [현금흐름 (Cashflow)](../01_Core_Model/Cashflow.md)