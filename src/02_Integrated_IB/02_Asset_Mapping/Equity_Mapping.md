# Equity 리스크 매핑 가이드 (Equity Risk Mapping Guide)

## 🔥 목적

자본/지분(Equity) 자산의 리스크 구조를 표준화된 PD, LGD, EAD 프레임워크로 변환하는 기준을 정의합니다. 
Equity는 채무 관계가 아닌 소유권 형태이므로 **'시장 및 가동 변동 기반의 시장 리스크'** 관점에서 주로 분석됩니다.

### ─────────────

## 📌 매핑 매커니즘 (Mapping Mechanism)

지분 리스크는 기업 가치의 변동성과 파산 가능성을 결합한 **Dual Approach**로 산출됩니다.

### 리스크 변수 매핑 테이블

| 구분 | Equity 리스크 요인 | 통합 모델 변수 (Standard) |
| :--- | :--- | :--- |
| **파산 확률** | 기업 신용도, 산업 업황 | **PD (부도확률)** |
| **가치 손실** | 지분 후순위성 (보통주 위주) | **LGD (100% 원칙)** |
| **시장 가치** | 현재 지분 공정 가치 (Market Value) | **EAD (익스포저)** |

### ─────────────

## 🧠 리스크 산출 듀얼 접근법

지분 포지션은 성격에 따라 두 가지 모델링 기법을 혼합하여 사용합니다.

### 1. 신용 리스크적 관점 (Credit Approach)
- 발행 기업의 부도 시 해당 지분이 휴지조각이 될 확률을 PD로 산출합니다.

### 2. 시장 리스크적 관점 (Market Approach)
- 시장 가격의 하락(Volatility 기반 Shock)이 지분 잔존 가치에 미치는 영향을 산출합니다.

### ─────────────

## 💰 Cashflow 관점

Equity 리스크는 배당 유입과 최종 매각 대금(Exit Value)의 불확실성을 측정하는 작업입니다.

### 현금흐름 리스크 요인
- **Dividend Risk**: 영업 이익 하락으로 인한 배당금 축소 또는 중단  
- **Exit Risk**: 시장 침체로 인한 IPO 지연 또는 매각 대금 하락  

### ─────────────

## ⚖️ Valuation Risk (핵심)

지분 리스크의 실질적 대부분은 시점별 평가 가치(Market Value)의 하락에서 발생합니다.

### 가치 하락 매커니즘
Market Value (현재가)  
→ Shock (변동성 충격)  
→ **Valuation Loss 확정**  

👉 지분 리스크 관리의 핵심은 '보수적인 Shock 산출'과 '정확한 Market Value 측정'에 있습니다.

### ─────────────

## 🔗 연결

- [통합 리스크 프레임워크](../01_Unified_Risk_Framework.md)
- [시장가치 (Market Value)](../01_Core_Model/Market_Value.md)
- [변동성 (Volatility)](../01_Core_Model/Volatility.md)
- [지분 리스크 (Equity Risk)](../03_Risk_Calculation/Equity_Risk.md)

### ─────────────

*최종 업데이트: 2026-04-14*