# IB 리스크 데이터 모델 (IB Risk Data Model)

## 목적
IB 전 자산(PF, NPL, ABS, Equity)을 단일 리스크 구조로 통합하여 관리합니다.

---

## 핵심 구조
**Deal** → **Position** → **Cashflow** → **Risk**

---

## 정의

### 딜 (Deal)
금융 거래의 최상위 단위로서 자산 유동화 또는 구조화의 기초가 됩니다.

---

### 포지션 (Position)
딜 내 자금 단위로서 리스크 계산의 최소 기준입니다.
> 모든 리스크는 **Position** 단위에서 계산됩니다.

---

### 현금흐름 (Cashflow)
실제적인 자금의 유입과 유출을 의미합니다.
> 모든 손실은 **현금흐름 부족 (Shortfall)**에서 발생합니다.

---

## 현금흐름 기반 리스크 구조 (Cashflow-centric)

**Position**  
 → **Expected Cashflow** (예상)  
 → **Actual Cashflow** (실적)  
 → **Shortfall** (부족액)  
 → **Loss** (손실)  
 → **Risk** (계산 결과)

**정의:**
- **Expected Cashflow**: 계약 및 사업 계획상의 예정 유입액
- **Actual Cashflow**: 실제 회수 및 집행 금액
- **Shortfall**: 예상 대비 부족 금액 ($Expected - Actual$)
- **Loss**: 실제 확정된 손실

---

## 1. 신용 리스크 (Credit Risk)
대출 및 채권 기반 자산 (**PF, NPL, ABS** 등)

**$$EL = PD \times LGD \times EAD$$**

- **PD (부도 확률)**: 차주/사업장의 부도 가능성
- **EAD (부도시 노출액)**: 위기 시점의 노활 총액
- **LGD (손실률)**: 부도 시 실제 손실 비중

---

## 2. 지분 리스크 (Equity Risk)
지분 투자 자산 (**비상장주식, 상장주식** 등)

**$$Loss = Market Value \times Shock$$**

- **Market Value**: 현재 시점의 공정 가치 (MTM)
- **Shock**: 가격 변동 충격 시나리오 비율

---

## 통합 리스크 산출 요약

**$$Total Risk = \sum Credit Risk + \sum Equity Risk$$**

---

## 자산별 리스크 해석 (Cashflow Perspective)

- **PF**: **분양대금** 유입 부족 → **미분양** 리스크 실현
- **ABS**: 기초자산 **Pool Cashflow** 회수 저조 → **트랜치(Tranche)** 손실 전이
- **NPL**: 담보 **Recovery** 부족 → **LGD** 직접 상승
- **Equity**: **배당(Dividend)** 및 **회수(Exit)** 흐름 지연/감소 → **평가손실** 발생

---

## 설계 및 운영 원칙

- **포지션 기준**: 모든 자산은 포지션 단위로 분해하여 관리합니다.
- **구조적 통일**: Credit과 Equity는 로직은 다르나 포지션 기반의 데이터 모델을 공유합니다.
- **현금흐름 중심**: 리스크 측정의 근거는 항상 실제 현금흐름 데이터에 둡니다.
- **시간 축 관리**: 모든 데이터는 **기준일(as_of_date)** 별로 스냅샷을 관리합니다.

---

## 상세 데이터 모델 (Schema)

### 1. 마스터 데이터 (Master Data)
→ [딜 스키마 (Deal Schema)](../05_Data_Model/01_Schemas/Deal_Schema.md)  
→ [거래 상대방 스키마 (Counterparty Schema)](../05_Data_Model/01_Schemas/Counterparty_Schema.md)  
→ [담보 스키마 (Collateral Schema)](../05_Data_Model/01_Schemas/Collateral_Schema.md)

### 2. 리스크 엔진 입력/결과 (Engine Data)
→ [포지션 스키마 (Position Schema)](../05_Data_Model/01_Schemas/Position_Schema.md)  
→ [현금흐름 스키마 (Cashflow Schema)](../05_Data_Model/01_Schemas/Cashflow_Schema.md)  
→ [리스크 결과 스키마 (Risk Result Schema)](../05_Data_Model/01_Schemas/Risk_Result_Schema.md)  
→ [현금흐름과 손실 (Cashflow to Loss Logic)](../05_Data_Model/02_Logic/Cashflow_to_Loss_Logic.md)

### 3. 시나리오 분석 (Scenario Data)
→ [리스크 요인 스키마 (Risk Factor Schema)](../05_Data_Model/01_Schemas/Risk_Factor_Schema.md)  
→ [시나리오 스키마 (Scenario Schema)](../05_Data_Model/01_Schemas/Scenario_Schema.md)

---

## 핵심 요약
- **Risk**는 결과 (Result)
- **Cashflow**는 원인 (Cause)
- **Position**은 기준 (Basis)