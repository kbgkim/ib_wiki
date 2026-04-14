# 현금흐름-손실 전이 로직 (Cashflow_to_Loss_Logic)

## 🔥 목적

개체에서 발생한 현금흐름의 부족(Shortfall)이 어떻게 실제 손실(Loss)로 확정되는지에 대한 연산 논리를 정의합니다. 
이 로직은 리스크 엔진의 핵심 연산 엔진(Logic Engine)을 구성합니다.

### ─────────────

## 📌 개념

리스크는 단순히 '돈을 못 받는 것'이 아니라, '예정된 시점에 예정된 금액이 들어오지 않는 것'으로 정의됩니다.

👉 **Loss = f(Expected CF, Actual CF, Recovery Strategy)**

### ─────────────

## 🧠 리스크 전이 단계 (Logic Chain)

현금흐름의 부실은 다음 3단계를 거쳐 최종 손실로 확정됩니다.

### 1. Shortfall (부족분 산출)
- **수식**: `Shortfall = Expected_Amount - Actual_Amount`
- **시점**: 각 현금흐름 예정일(Payment Date) 기준

### 2. Recovery (회수 시도)
- **수식**: `Recovery = Collateral_Value × Liquidation_Ratio`
- **행위**: 담보 처분, 보증 채무 이행 청구 등

### 3. Final Loss (최종 손실 확정)
- **수식**: `Final_Loss = Shortfall - Recovery`
- **의의**: 해당 포지션에서 최종적으로 소멸된 자본 가치

### ─────────────

## ⚖️ 자산별 특수 로직

### PF / Loan 자산
- 원리금 상환 부족분이 그대로 Shortfall로 전이됩니다.

### Equity 자산
- 배당금 부족분은 경영권 리스크로, 매각 대금 부족분은 자본 손실로 직접 매핑됩니다.

### ─────────────

## 🔗 연결

- [현금흐름 스키마 (Cashflow Schema)](../01_Schemas/Cashflow_Schema.md)
- [기대손실 (Expected Loss)](../../../01_Core_Model/Expected_Loss.md)

### ─────────────

*최종 업데이트: 2026-04-14*