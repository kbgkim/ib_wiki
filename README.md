# 🏛️ IB Integrated Wiki (투자은행 통합 지식 라이브러리)

> **"자산이 아닌 리스크를 통합한다 (Integrate the Risk, not the Asset)"**

본 프로젝트는 투자은행(IB) 실무에서 다루는 4대 핵심 자산군(**PF, ABS, NPL, Equity**)의 지식을 체계적으로 구조화하고, 이를 **Asset → Position → Cashflow → Risk**라는 단일 온톨로지로 통합 관리하는 프로덕션급 지식 위키입니다.

---

## 🌟 프로젝트 아키텍처 (Layered Architecture)

본 위키는 지식의 엄격한 분리와 위계를 위해 다음과 같은 **6단계 레이어**를 따릅니다.

1.  ⚖️ **[00_Standard_Layer](src/00_Standard_Layer/Core_Definitions.md)**: 리스크 관리 헌법 및 핵심 정의
2.  🧩 **[01_Core_Model](src/01_Core_Model/Position.md)**: 포지션, 현금흐름, 리스크 변수(PD/LGD/EAD) 표준 모델
3.  🔄 **[02_Integrated_IB](src/02_Integrated_IB/Synthesis_Map.md)**: 자산 간 시너지 맵 및 통합 뷰
4.  🏗️ **[03_Assets_Verticals](src/03_Assets_Verticals/PF/PF_Mapping.md)**: 자산별 특화 매핑 및 도메인 지식
5.  ⚙️ **[04_Risk_Calculation](src/04_Risk_Calculation/EL_Calculation.md)**: 기대손실(EL) 및 리스크 산출 엔진 로직
6.  📊 **[05_Data_Model](src/05_Data_Model/01_Schemas/Position_Schema.md)**: 물리적 데이터 스키마 및 이벤트 모델

---

## 🧬 도메인 아키텍처 (Domain Architecture)

본 위키는 지표의 정적 정의와 동적 변화를 동시에 관리하기 위해 **Event-driven Domain Structure**를 채택하고 있습니다.

### 1. 3-Layer 원칙
- **Core Domain**: 자산의 본질적 금융 구조 및 온톨로지 고정.
- **Extension Layer**: ESG, STO, Syndication 등 구조적 확장 요소 선별 적용.
- **Scenario Layer**: 거시 리스크 전파 및 시나리오 모델링.

### 2. 동적 라이프사이클 모델
- **Event Catalog**: 리스크($PD/LGD$)와 가치($Cashflow$)를 변화시키는 핵심 트리거 정의.
- **State Machine**: 딜의 생애주기에 따른 상태 전이 모델(State Machine) 구축.

---

## 🛠️ 활용 방법 (How to Use)

- **지식 탐색**: [핵심 정의(Core Definitions)](src/00_Standard_Layer/Core_Definitions.md)에서 공통 언어와 **이벤트/상태** 개념을 먼저 익히십시오.
- **도메인 명세**: 자산별 라이프사이클 시각화 자료 확인 ([PF](src/03_Assets_Verticals/PF/Basics.md) / [ABS](src/03_Assets_Verticals/ABS/Basics.md) / [NPL](src/03_Assets_Verticals/NPL/Basics.md) / [Equity](src/03_Assets_Verticals/Equity/Basics.md))
- **인과 관계**: [통합 리스크 전파 명세](src/02_Integrated_IB/Synthesis_Map.md)에서 도메인 간 리스크 전이 경로를 추적하세요.

---

## 📜 수정 이력 (Modification History)

| 날짜 | 주요 변경 사항 | 비고 |
| :--- | :--- | :--- |
| **2026-04-10** | 프로젝트 초기화 및 6단계 계층형 아키텍처 스캐폴딩 | Initial Commit |
| **2026-04-14** | 자산군별 온톨로지 정렬 및 전면 리팩토링 실시 | Ontology Refactoring |
| **2026-04-16** | **이벤트 기반 도메인 아키텍처 및 통합 리스크 명세 전환** | **Current Version** |

---

## 👨‍💻 관리 및 기여

- **원격 저장소**: [https://github.com/kbgkim/ib_wiki](https://github.com/kbgkim/ib_wiki)
- **최종 보강**: 통합 리스크 시스템 명세 정렬 및 인과관계 명세화 완료

---

*Created by [Antigravity](https://github.com/kbgkim)*
