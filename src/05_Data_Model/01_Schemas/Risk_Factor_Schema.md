# 리스크 요인 스키마 (Risk_Factor_Schema)

## 🔥 목적

시장 및 거시경제 데이터를 기반으로 리스크 시나리오 충격(Shock)을 생성하는 **기초 입력 데이터**를 정의합니다.

### ─────────────

## 📌 개념

Risk Factor는 시장에서 관측 가능한 지표들을 시스템이 이해할 수 있는 규격으로 관리합니다.

👉 **역할**
- Market Observation Layer (시장 관측)
- Shock Generator Input (시나리오 생성 입력)
- Scenario Engine Base Data (엔진 기초 데이터)

### ─────────────

## 🧠 구조 역할

### 리스크 전이 경로
Risk Factor  
→ Shock (충격치)  
→ Scenario (시나리오)  
→ Risk Engine (산출 엔진)  
→ Cashflow / Loss (결과 산출)  

### ─────────────

## 📊 테이블 구조 (Table Detail)

### RISK_FACTOR_MASTER

| 컬럼명 | 타입 | 설명 |
| :--- | :--- | :--- |
| **factor_id** | VARCHAR | PK (고유 식별자) |
| **factor_name** | VARCHAR | 시장 지표명 |
| **factor_type** | ENUM | INTEREST_RATE / FX / INDEX / COMMODITY |
| **base_value** | DECIMAL | 현재 시장 가격 (Spot Value) |
| **historical_volatility** | DECIMAL | 과거 변동성 |
| **stress_volatility** | DECIMAL | 스트레스 변동성 |
| **source** | VARCHAR | 데이터 출처 |
| **as_of_date** | DATE | Snapshot 기준일 |

### ─────────────

## ⚙️ 핵심 설계 원칙

### Market Observation Layer
- Risk Factor는 실제 시장 관측값입니다.
- **Market Data → Risk Factor** 단계는 외부 연동 또는 수동 업로드로 관리됩니다.

### ─────────────

## 🔗 연결

- [변동성 (Volatility)](../../01_Core_Model/Volatility.md)
- [시나리오 스키마 (Scenario Schema)](./Scenario_Schema.md)

### ─────────────

*최종 업데이트: 2026-04-14*