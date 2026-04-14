# 현금흐름과 손실 (Cashflow to Loss Logic)

## 목적
현금흐름 기반으로 손실이 발생하는 구조를 정의합니다.

---

## 기본 구조

**Expected Cashflow**  
- **Actual Cashflow**  
= **Shortfall**  

**Shortfall** → **Loss** (실질 손실)

---

## 정의

- **Expected Cashflow**: 계약 및 사업 계획에 근거한 예상 자금 흐름
- **Actual Cashflow**: 회수 또는 집행된 실제 자금 흐름
- **Shortfall**: 예상 대비 부족한 금액
- **Loss**: 회수 불능으로 확정되어 리스크로 전이된 손실

---

## 리스크 지표와의 연결 (Logic Link)

Loss(현금흐름 손실)는 다음과 같이 신용 리스크 지표에 직접적인 영향을 미칩니다:

1. **상환 재원 부족 (Shortfall)** 발생
2. **회수율 (Recovery Rate)** 하락: $Recovery = EAD - Loss$
3. **손실률 (LGD)** 상승: $LGD = 1 - (Recovery / EAD)$
4. **기대손실 (Expected Loss)** 증가: $EL = PD \times LGD \times EAD$

---

## 설계 원칙

- **리스크의 기원**: 모든 리스크 지표는 사후적으로 계산되나, 그 근원은 현금흐름의 부족입니다.
- **EAD / LGD의 동적 관리**: 실제 발생한 Shortfall 데이터를 기반으로 LGD 실측치를 업데이트하여 모델의 정확도를 높입니다.

---

## 연결

→ [현금흐름 (Cashflow)](../../01_Core_Model/Cashflow.md)  
→ [기대손실 (Expected Loss)](../../01_Core_Model/Expected_Loss.md)  
→ [손실률 (LGD)](../../01_Core_Model/LGD.md)