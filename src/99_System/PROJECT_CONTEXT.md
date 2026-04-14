# IB Wiki Project Context Summary

이 문서는 Antigravity(AI)가 다음 세션에서도 프로젝트의 맥락을 즉시 파악할 수 있도록 돕기 위한 요약본입니다.

## 1. 프로젝트 개요 (Project Overview)
- **명칭**: IB 통합 위키 (Investment Banking Integrated Wiki)
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
- **온톨로지 리팩토링 (2026-04-14)**:
  - 전 자산군에 대한 7단계 표준 매핑 구조 적용 완료
  - 모든 정의를 Standard Layer(`Core_Definitions.md`)로 중앙화하여 정합성 확보
  - 6단계 계층형 아키텍처로 전체 저장소 재구조화 완료
- **리스크 모델 통합**: 공통 EL 프레임워크($PD \times LGD \times EAD$) 및 비선형 전파 모델 구축
- **지능형 시각화**: 4대 자산 통합 관제 **대시보드(DASHBOARD.md)** 구축 및 아키텍처 반영 완료

## 4. 자동화 및 워크플로우 (Automation)
- **문서 입수 스킬**: `ib-wiki-ingestion` 스킬을 사용하여 인박스 문서를 자동으로 처리합니다.
- **검증 및 정합성 스킬**: `ib-wiki-verification` 스킬을 통해 위키의 기술적 무결성과 논리적 정합성을 점검합니다.
- **인제션 로그**: 모든 문서 처리 내역은 [INGESTION_LOG.md](INGESTION_LOG.md)에 기록됩니다.
- **검증 보고서**: 정기 검증 결과는 [VERIFICATION_REPORT.md](VERIFICATION_REPORT.md)에 공시됩니다.

## 5. 향후 고도화 로드맵 (Evolution Roadmap)
- **실행 가능한 리스크 시뮬레이터 (Simulator)**: $EL = PD \times LGD \times EAD$ 산출 로직을 파이썬 코드로 구현하여 실제 데이터 계산 및 대시보드 연동 기능 추가.
- **통합 스트레스 테스트 (Stress Test)**: "건설사 부도 -> PF 부실 -> NPL 공급 확대"와 같은 자산 간 리스크 전이 시나리오 설계 및 시각화.
- **지능형 인박스 정교화 (Auto-Ingestion)**: 외부 리서치 리포트나 뉴스 분석을 통한 대시보드 지표 자동 업데이트 파이프라인 완성.

### ─────────────

*Created: 2026-04-10*
