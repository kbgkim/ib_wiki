# IB 리스크 데이터 모델 (IB Risk Data Model)

## 목적
IB 전 자산(PF, NPL, ABS, Equity)을 단일 리스크 구조로 통합하여 관리합니다.

---

## 핵심 구조
**Deal** → **Position** → **Cashflow** → **Risk**

---

## 정의

### 딜 (Deal)
금융 거래의 최상위 단위 (구조화의 기초)

---

### 포지션 (Position)
딜 내 자금 단위로서 리스크 계산의 최소 기준입니다.

> 모든 리스크는 **Position** 단위에서 계산됩니다.

---

### 현금흐름 (Cashflow)
실제적인 자금의 유입과 유출을 의미합니다.

> 모든 손실은 **Cashflow**의 변형(미회수, 감소)에서 발생합니다.

---

### 리스크 (Risk)
포지션은 자산 특성에 따라 두 가지 리스크 모델로 확장됩니다.

---

## 1. 신용 리스크 (Credit Risk)
대출 및 채권 기반 자산 (**PF, NPL, ABS** 등)에 적용됩니다.

- **Position**
  - **Exposure**
    - **PD (부도 확률)**
    - **EAD (부도시노출액)**
    - **LGD (손실률)**
      - **Expected Loss (기대손실)**

### 핵심 변수 정의
- **Exposure**: 현재 시점의 노출 금액
- **PD (Probability of Default)**: 차주/사업장의 부도 확률
- **EAD (Exposure at Default)**: 부도 시점의 총 노출 예상액
- **LGD (Loss Given Default)**: 부도 발생 시 실제 손실 비중

---

## 2. 지분 리스크 (Equity Risk)
지분 투자 기반 자산 (**비상장주식, 상장주식** 등)에 적용됩니다.

- **Position**
  - **Market Value (시장 가치)**
    - **Shock (가격 하락 충격)**
      - **Loss (손실액)**

---

## 핵심 공식

### Credit Risk (신용 기반)
**$$EL = PD \times LGD \times EAD$$**
> [!NOTE]
> **NPL(부실채권)** 자산은 이미 부실화되었으므로 **$PD = 100\%$**를 적용하여 $EL = EAD \times LGD$로 계산합니다.

### Equity Risk (지분 기반)
**$$Loss = Market Value \times Shock$$**

---

## 설계 원칙
- **포지션 환원**: 모든 자산은 리스크 측정을 위해 포지션 단위로 분해합니다.
- **구조적 통일**: Credit과 Equity는 계산 로직은 다르나 포지션 기반의 동일한 데이터 구조를 공유합니다.
- **현금흐름 중심**: 현금흐름은 모든 리스크의 근원이며 측정 지표입니다.

---

## 연결
→ [포지션 (Position)](../01_Core_Model/Position.md)  
→ [노출액 (Exposure)](../01_Core_Model/Exposure.md)  
→ [부도시노출액 (EAD)](../01_Core_Model/EAD.md)  
→ [손실률 (LGD)](../01_Core_Model/LGD.md)  
→ [기대손실 (Expected Loss)](../01_Core_Model/Expected_Loss.md)  
→ [시장가치 (Market Value)](../01_Core_Model/Market_Value.md)  
→ [지분 리스크 (Equity Risk)](../03_Risk_Calculation/Equity_Risk.md)