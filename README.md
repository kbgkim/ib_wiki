# 🏛️ IB Integrated Wiki (투자은행 통합 지식 라이브러리)

> **"자산이 아닌 리스크를 통합한다 (Integrate the Risk, not the Asset)"**

본 프로젝트는 투자은행(IB) 실무에서 다루는 4대 핵심 자산군(**PF, ABS, NPL, Equity**)의 지식을 체계적으로 구조화하고, 이를 **Asset → Position → Cashflow → Risk**라는 단일 온톨로지로 통합 관리하는 프로덕션급 지식 위키입니다.

### ─────────────

## 🌟 프로젝트 아키텍처 (Layered Architecture)

본 위키는 지식의 엄격한 분리와 위계를 위해 다음과 같은 **6단계 레이어**를 따릅니다.

1.  ⚖️ **[00_Standard_Layer](src/00_Standard_Layer/Core_Definitions.md)**: 리스크 관리 헌법 및 핵심 정의
2.  🧩 **[01_Core_Model](src/01_Core_Model/Position.md)**: 포지션, 현금흐름, 리스크 변수(PD/LGD/EAD) 표준 모델
3.  🔄 **[02_Integrated_IB](src/02_Integrated_IB/Synthesis_Map.md)**: 자산 간 시너지 맵 및 통합 뷰
4.  🏗️ **[03_Assets_Verticals](src/03_Assets_Verticals/PF/PF_Mapping.md)**: 자산별 특화 매핑 및 도메인 지식
5.  ⚙️ **[04_Risk_Calculation](src/04_Risk_Calculation/EL_Calculation.md)**: 기대손실(EL) 및 리스크 산출 엔진 로직
6.  📊 **[05_Data_Model](src/05_Data_Model/01_Schemas/Position_Schema.md)**: 물리적 데이터 스키마 및 이벤트 모델

### ─────────────

## 🧬 통합 온톨로지 (Unified Ontology)

모든 자산은 형식을 불문하고 아래의 공통 흐름으로 환원되어 관리됩니다.

**Asset** (특정 자산 도메인)
→ **Position** (모든 리스크의 최소 단위)
→ **Cashflow** (리스크를 유발하는 현금흐름 데이터)
→ **Risk** (분석된 최종 위험 지표)

### ─────────────

## 🛠️ 활용 방법 (How to Use)

- **지식 탐색**: [핵심 정의(Core Definitions)](src/00_Standard_Layer/Core_Definitions.md)에서 공통 언어를 먼저 익히시는 것을 권장합니다.
- **리스크 분석**: [자산별 매핑 가이드](src/03_Assets_Verticals/)를 통해 각 도메인이 어떻게 공통 모델로 변환되는지 확인하세요.
- **데이터 구조**: 시스템 구현이 목적이라면 [데이터 모델](src/05_Data_Model/) 레이어를 참조하십시오.

### ─────────────

## 👨‍💻 관리 및 기여

- **원격 저장소**: [https://github.com/kbgkim/ib_wiki](https://github.com/kbgkim/ib_wiki)
- **최종 업데이트**: 2026-04-14 (Ontological Refactoring 완료)

### ─────────────

*Created by [Antigravity](https://github.com/kbgkim)*
