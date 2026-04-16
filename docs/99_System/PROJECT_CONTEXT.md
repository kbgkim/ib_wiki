# IB Wiki Project Context Summary

이 문서는 Antigravity(AI)가 다음 세션에서도 프로젝트의 맥락을 즉시 파악할 수 있도록 돕기 위한 요약본입니다.

## 1. 프로젝트 개요 (Project Overview)
- **명칭**: IB 통합 위키 (Investment Banking Integrated Wiki)
- **버전**: **v1.0 (Spec Frozen)**
- **핵심 도메인**: **NPL**, **PF**, **Equity**, **ABS** 통합 관리
- **목적**: 자산별 현금흐름(Cashflow)과 리스크를 통합하여 관리하는 개인용 지식 라이브러리

## 2. 계층형 아키텍처 (Layered Architecture)
- **00_Standard_Layer**: 금융 온톨로지 정의 및 리스크 관리 헌법
- **01_Core_Model**: Canonical 모델 (Position, Cashflow, PD/LGD/EAD)
- **02_Integrated_IB**: 통합 뷰 및 자산 간 시너지 맵
- **03_Assets_Verticals**: 자산별 특화 매핑 가이드 (PF, ABS, NPL, Equity)
- **04_Risk_Calculation**: 리스크 산출 엔진 로직 및 기술 사양
- **05_Data_Model**: 물리적 데이터 스키마 및 이벤트 모델

## 3. 문서 작성 가이드라인 (Style Guide)
- **기본 언어**: 한국어 (한글)
- **영문 병기**: 전문 용어는 `한글 (Full English Name, Abbreviation)` 형식 사용
- **현업 용어**: 금융 실무 용어는 **`용어`** (현업) 처럼 볼드체로 강조
- **온톨로지**: 모든 자산 문서는 **Asset → Position → Cashflow → Risk** 흐름 준수

## 4. 현재까지 진행 상황 (Current Progress)
- **기반 구축**: 프로젝트 폴더 구조 스캐폴딩 및 GitHub 동기화 완료
- **이벤트 기반 도메인 재설계 (2026-04-16)**:
  - 단순 문서 집합에서 **Domain Specification + Event-based Architecture**로 대대적 전환 완료
  - **3계층 아키텍처** 확립: Core Domain(고정), Extension Layer(구조 확장), Execution Layer(제외)
  - 전 자산군(PF, ABS, NPL, Equity)에 대해 **Event Catalog** 및 **State Machine** 상세 명세 구축
  - 이벤트 트리거와 리스크 인자($PD, LGD, Cashflow$) 간의 논리적 결합 완료
- **리스크 모델 통합**: 공통 EL 프레임워크($PD \times LGD \times EAD$) 및 비선형 전파 모델 구축
- **시스템 거버넌스 및 실행 안정성 강화 (2026-04-16)**:
  - **Implementation Mapping**: 설계 규약과 실제 코드 컴포넌트 간의 매핑 명세 수립.
  - **Consistency Matrix**: 다중 명세 간 충돌 해소를 위한 지배 규칙(Dominant Rule) 체계 확립.
  - **Fail-Fast Policy**: 비정상 상태 확산 방지를 위한 즉각적 실행 중단 및 오류 차단 규약 정의.
- **Milestone M1 달성 (2026-04-16)**: [Spec Freeze v1.0](./MILESTONES.md#M1-spec-freeze-v10-2026-04-16) 선언 및 분석/설계 단계 공식 종료.
- **지능형 시각화**: 4대 자산 통합 관제 **대시보드(DASHBOARD.md)** 구축 및 아키텍처 반영 완료

## 4. 자동화 및 워크플로우 (Automation)
- **문서 입수 스킬**: `ib-wiki-ingestion` 스킬을 사용하여 인박스 문서를 자동으로 처리합니다.
- **검증 및 정합성 스킬**: `ib-wiki-verification` 스킬을 통해 위키의 기술적 무결성과 논리적 정합성을 점검합니다.
- **아키텍처 변경 로그**: 상세 계획 및 실행 결과는 [ARCHITECTURAL_LOG.md](ARCHITECTURAL_LOG.md)에 기록됩니다.
- **인제션 로그**: 모든 문서 처리 내역은 [INGESTION_LOG.md](INGESTION_LOG.md)에 기록됩니다.
- **검증 보고서**: 정기 검증 결과는 [VERIFICATION_REPORT.md](VERIFICATION_REPORT.md)에 공시됩니다.

## 5. 향후 고도화 로드맵 (Evolution Roadmap)
- **명세 기반 시스템 구현 (Simulator)**: [통합 리스크 전파 명세](../02_Integrated_IB/Synthesis_Map.md)를 바탕으로, 시나리오별 $PD \times LGD \times EAD$를 산출하는 Python 프로토타입 개발. (현재 구현 대기 중)
- **지능형 대시보드 정교화**: 실시간 이벤트 로그를 시뮬레이터와 연동하여 리스크 가시성 확보.

### ─────────────

*Created: 2026-04-10*
