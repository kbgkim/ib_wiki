# 지분 리스크 산출 (Equity Risk Calculation)

## 🔥 목적

지분(Equity) 포지션의 가치 변동 및 손실 가능성을 측정하는 논리적 모델을 정의합니다. 
지분 리스크는 시장 리스크(Market Risk)와 신용 리스크(Credit Risk)의 속성을 동시에 가집니다.

### ─────────────

## 📌 1. 시장 모델 기반 산출 (Market Model)

지분 리스크의 일차적 산출 기준이며, 자산 가치의 변동성(Volatility)을 핵심 변수로 사용합니다.

### 산출 프로세스
1. **Current Valuation**: 현재 시장 가치(Market Value) 측정  
2. **Shock Generation**: 변동성 데이터를 기반으로 시나리오별 하락폭(Shock) 산출  
3. **Loss Mapping**: `Market_Value × Shock`를 통해 예상 손실 산정  

### ─────────────

## 🧠 2. 신용 리스크적 접근 (Credit Approach)

회계적 통합 및 전사 리스크 집계를 위해 지분 자산을 PD, LGD, EAD 규격으로 강제 매핑합니다.

### 마스터 변수 매핑
- **PD (부도확률)**: 발행 기업의 파산 또는 사업 실패 확률  
- **LGD (손실률)**: 지분의 후순위 구조를 반영하여 **100%** 가정  
- **EAD (익스포저)**: 현재 Market Value 또는 투자 원금  

👉 **주의**: 본 Credit 구조는 시스템적 통합 목적으로만 사용되며, 실제 리스크 관리의 중심은 Market Model입니다.

### ─────────────

## ⚙️ 3. 핵심 리스크 요인

### 시장 및 실적 요인
- **Valuation Risk**: 기업실정 부진 또는 시장 악화에 따른 가치 하락
- **Exit Risk**: IPO/M&A 지연으로 인한 회수 시나리오 실패
- **Liquidity Risk**: 비상장 주식 특유의 환금성 제약

### ─────────────

## 📊 자산별 리스크 구조 비교

| 자산군 | 리스크 본질 (Core Risk) |
| :--- | :--- |
| **PF** | Cashflow Risk (준공/분양) |
| **ABS** | Structured Credit (워터폴) |
| **NPL** | Recovery Risk (담보 회수) |
| **Equity** | Market Risk (가치 변동) |

### ─────────────

## 🔗 연결

- [시장가치 (Market Value)](../../01_Core_Model/Market_Value.md)
- [변동성 (Volatility)](../../01_Core_Model/Volatility.md)
- [포지션 (Position)](../../01_Core_Model/Position.md)

### ─────────────

*최종 업데이트: 2026-04-14*