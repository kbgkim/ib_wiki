# IB Wiki Architectural Refactoring Log

본 문서는 IB Wiki의 아키텍처 재설계 계획과 그 실행 결과를 기록하는 공식 로그입니다.

---

## [Log 2026-04-16 #3] 통합 리스크 시스템 명세 정렬 (Integrated Risk Specification)

### 📋 계획 (Plan)
- **목표**: 개별 자산 중심 모델을 넘어 거시 시나리오 기반의 통합 리스크 전파 모델 구축.
- **핵심 요소**:
    - Scenario Layer 정의 (S1: 금리, S2: 부동산, S3: 유동성).
    - 도메인 간 이벤트 인과관계(Event Causality) 명세화.
- **범위 제한**: DB 매핑, 세부 회계 알고리즘 등 물리적 구현 요소 배제.

### ✅ 실행 결과 (Results)
- **Scenario Impact**: 4대 자산 도메인 기초 문서에 거시 시나리오 영향도 섹션 통합 완료.
- **Causality Graph**: `Synthesis_Map.md`를 [통합 리스크 전파 명세](../02_Integrated_IB/Synthesis_Map.md)로 업그레이드 완료 (Mermaid 및 Data Transfer Point 정의).
- **검증**: `verify_links.py` 실행 결과, 전체 58개 문서에 대해 Broken Link 0건 확인.

---

## [Log 2026-04-16 #2] 전 자산군 이벤트 기반 도메인 재설계 (Multi-Asset Refactoring)

### 📋 계획 (Plan)
- **목표**: PF/ABS/NPL/Equity 전 도메인을 3계층 아키텍처(Core/Extension/Execution)로 재구조화.
- **핵심 요소**: Event Catalog 및 State Machine 구축.

### ✅ 실행 결과 (Results)
- **PF/ABS/NPL/Equity**: 각 기초 문서와 라이프사이클 문서를 이벤트 모델 기반으로 정렬 완료.
- **Standardization**: `Core_Definitions.md`에 Event/State 개념을 기저 온톨로지로 공식 편입.

---

## [Log 2026-04-16 #1] 3계층 아키텍처 파일럿 (PF Pilot)

### 📋 계획 (Plan)
- **목표**: 프로젝트 파이낸싱(PF) 도메인을 대상으로 새로운 아키텍처 표준 정립 및 파일럿 적용.

### ✅ 실행 결과 (Results)
- PF 도메인 문서에 대해 Core/Extension 분리 및 Risk/Value Impact Factor 도출 완료.
- 성공적인 파일럿 결과를 바탕으로 전 도메인 확산 결정.

---

*최종 업데이트: 2026-04-16 (Antigravity AI)*
