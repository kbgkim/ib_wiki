# 통합 리스크 관리 체계 (Unified Risk Management Framework)

## 🔥 목적

본 문서는 **NPL, PF, Equity, ABS** 전 자산을 관통하는 통합 리스크 관리 이론과 프레임워크를 정의합니다.  
본 위키의 핵심 설계 철학인 **"자산이 아닌 리스크를 통합한다"**는 원칙에 따라 모든 자산 유형을 단일한 통제 환경으로 구축합니다.

---

## 📌 1. 전 자산 리스크 통합의 원칙

이론적으로 성격이 판이한 자산(예: 가격 변동이 핵심인 주식과 프로젝트 성공이 핵심인 PF)을 하나의 모델로 합치는 것은 논리적 모순에 직면할 수 있습니다.

👉 이를 해결하기 위해 우리는 모든 자산을 **"미래 현금흐름의 불확실성 (Uncertainty of Future Cashflows)"**이라는 단일 철학적 개념으로 환원합니다.

| 자산 유형 | 핵심 리스크 구조 | 통합 관점 (Cashflow) |
| :--- | :--- | :--- |
| **자본 (Equity)** | 가격 변동성 (Market Volatility) | 불확실한 배당 및 매각 대금 현금흐름 |
| **자산유동화 (ABS)** | 현금흐름 안정성 (Structure Stability) | 기초자산의 상환 유입 지속 여부 |
| **프로젝트 파이낸싱 (PF)** | 사업 성공 여부 (Project Success) | 준공 및 분양 기반의 미래 현금흐름 |
| **부실채권 (NPL)** | 회수 가능성 (Recovery) | 담보 가치 기반의 회수 현금흐름 |

---

## 🧠 2. 공통 언어: PD, LGD, EAD 프레임워크

이질적인 자산의 리스크 구조를 규격화하기 위해 다음의 3대 핵심 변수를 사용합니다.

$$EL (예상 손실) = PD \times LGD \times EAD$$

- **PD (Probability of Default, 부도 확률)**: 차주 또는 프로젝트가 약속된 현금흐름을 창출하지 못하거나 투자 대상이 실패할 확률.
- **LGD (Loss Given Default, 부도 시 손실률)**: 부도 발생 시 실제 손실로 확정되는 비중. 담보 또는 변제 우선순위(**Tranching**)에 따라 결정됨.
- **EAD (Exposure at Default, 부도 시 익스포저)**: 위기 발생 시점에 위험에 노출된 총 자본 총액 (투자금, 대출 잔액 등).

---

## ⚖️ 3. 실전 자산별 리스크 매핑 로직

| 자산군 | PD (부도 확률) 산정 | LGD (부도 시 손실률) 산정 | EAD (익스포저) 산정 |
| :--- | :--- | :--- | :--- |
| **NPL** | **100% 고정** (이미 부실화됨) | **예상 회수율 (Recovery Rate)** 기반 | 보유 **채권 잔액** |
| **ABS** | 기초자산(Underlying)의 부도율 | **트랜치 구조 및 워터폴** 반영 | 실제 **투자 금액** |
| **PF** | **프로젝트 실패 확률** (사업성 평가) | **담보 가치(LTV)** 및 신용보강 반영 | 실제 **대출 실행 규모** |
| **Equity** | **기업 실패 확률** (파산 확률) | **약 100%** (지본가치 후순위성 반영) | 실제 **투자 금액** |

---

## ⚙️ 4. 환경 변화와 리스크의 유동성

자산의 리스크는 고정된 값이 아니라 거시 경제 지표와 상관관계(Correlation) 및 시나리오에 의해 동적으로 변화합니다.

- **Base (정상)**: 안정적 시장 환경을 가정한 리스크 기준점.
- **Stress (위기)**: 유의미한 거시 충격 시의 리스크 변동성 확대 측정.
- **Worst (극단)**: 최악의 상황(Black Swan)에서의 생존 가능성 테스트.

---

## 🔗 연결

### 상위 거버넌스
- **리스크 관리 정책**: [Risk_Management_Policy.md](../01_Foundations/Risk_Management_Policy.md)
- **IB 기본 개요**: [IB_Overview.md](../01_Foundations/IB_Overview.md)
- **통합 시너지 맵**: [Synthesis_Map.md](Synthesis_Map.md)

### 상세 자산별 매핑 (Asset Verticals)
- **부실채권**: [NPL Mapping](./02_Asset_Mapping/NPL_Mapping.md)
- **프로젝트 파이낸싱**: [PF Mapping](./02_Asset_Mapping/PF_Mapping.md)
- **자산유동화**: [ABS Mapping](./02_Asset_Mapping/ABS_Mapping.md)
- **자본/지분**: [Equity Mapping](./02_Asset_Mapping/Equity_Mapping.md)

### 세부 리스크 데이터 모델 (Detailed Data Models)
- **[통합 리스크 데이터 모델 (Root Model)](00_Root_Model/IB_Risk_Data_Model.md)**: 전체 데이터 아키텍처 개요
- **[핵심 리스크 변수 (Core Model)](01_Core_Model/Position.md)**: PD, LGD, EAD, EL 등 핵심 변수 정의
- **[현금흐름 (Cashflow)](01_Core_Model/Cashflow.md)**: 리스크의 원천으로서의 현금흐름 개념
- **[리스크 데이터 스키마 (Schemas)](05_Data_Model/01_Schemas/Position_Schema.md)**: DB 설계를 위한 상세 테이블 구조
- **[리스크 산출 로직 (Calculation)](03_Risk_Calculation/EL_Calculation.md)**: EL 및 Equity Risk 산출 흐름

---
*최종 수정일: 2026-04-14*
