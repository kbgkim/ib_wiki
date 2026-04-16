# IB Wiki Architectural Refactoring Log

본 문서는 IB Wiki의 아키텍처 재설계 계획과 그 실행 결과를 기록하는 공식 로그입니다.

---

## [Log 2026-04-16 #6] 리포지토리 대규모 구조 개편 (Repository Restructuring: src -> docs)

### 📋 계획 (Plan)
- **목표**: 위키의 표준성 및 범용성을 높이기 위해 소스 코드 성격의 `src/` 디렉토리를 문서 중심의 `docs/` 디렉토리로 전환.
- **핵심 요소**:
    - `src/` -> `docs/` 이름 변경 및 전체 내부 링크(상대 경로) 무결성 확보.
    - `README.md` 및 `DASHBOARD.md` 등 최상위 문서의 진입점 경로 업데이트.

### ✅ 실행 결과 (Results)
- **Restructuring**: `src/` 하위의 모든 계층(00~99)이 `docs/`로 성공적으로 이관됨.
- **Link Integrity**: `verify_links.py` 스캔 결과, 전체 84개 파일에 대해 Broken Link 0건 확인.
- **System Hardening**: 지식 위키로서의 정체성을 강화하고 GitHub Pages 등 외부 렌더링 도구와의 호환성 확보.

---

## [Log 2026-04-16 #5] 동적 이벤트 흐름 시스템 전환 (Dynamic Event Flow System)

### 📋 계획 (Plan)
- **목표**: 정적 이벤트 카탈로그를 실행 가능한 시간 순서 기반의 동적 시스템으로 전환.
- **핵심 요소**:
    - **Scenario Sequence**: S1, S2 시나리오의 타임라인별 이벤트 흐름 정의.
    - **Logic Handler**: 이벤트 수신 시 시스템의 논리적 행동 지침(State/Risk Update) 명세.
    - **Canonical Payload**: 모든 이벤트가 공유하는 표준 데이터 규격(JSON) 수립.
- **범위 제한**: 구현 단계의 기술 스택(Kafka 등) 및 수식 정의 배제.

### ✅ 실행 결과 (Results)
- [동적 이벤트 흐름 명세서](../02_Integrated_IB/EVENT_FLOW_SPECIFICATION.md) 생성 및 통합 리스크 전파 명세와 연결 완료.
- 리스크 엔진이 해석 가능한 수준의 리거 필드(Payload) 및 트리거 규칙(Trigger Rule) 확립.

---

## [Log 2026-04-16 #4] 논리 정합성 강화 (Logical Integrity Enhancement)

### 📋 계획 (Plan)
- **목표**: 모든 비즈니스 이벤트에 대해 정합성 검증 레이어(Validation Layer)를 적용하여 논리적 결함 차단.
- **핵심 요소**: Pre-condition, Post-state, Invalid Transition 정의.

### ✅ 실행 결과 (Results)
- PF/ABS/NPL/Equity 전 도메인의 라이프사이클 문서에 이벤트 정합성 테이블 및 명시적 전이 금지 규칙 반영 완료.
- `Core_Definitions.md`에 Validation Layer 표준 규격 공식화.

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
