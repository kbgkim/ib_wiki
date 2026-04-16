# IB Wiki Project Milestones

본 문서는 IB Wiki 프로젝트의 주요 마일스톤 달성 기록 및 향후 로드맵을 관리합니다.

---

## 🏁 [M1] Spec Freeze v1.0 (2026-04-16)

### 📜 Spec Freeze Declaration
본 시스템 명세는 현재 시점에서 완전히 고정(Frozen)되었다.

- 거버넌스 프로세스 없이 시스템의 어떠한 동작 변경도 허용되지 않는다
- 모든 시스템 동작은 결정론적으로 정의되어 있으며 완전히 명세화되어 있다
- 향후 작업은 거버넌스 하의 구현 및 보강으로만 제한된다

**시각**: 2026-04-16  
**버전**: v1.0

### 🎯 달성 성과 (Achievements)
- **4대 자산 도메인 온톨로지 확립**: PF, ABS, NPL, Equity에 대해 Asset → Position → Cashflow → Risk 체계 정립.
- **이벤트 기반 명세화**: 각 자산별 State Machine 및 Event Catalog 정밀 명세 완료.
- **시스템 거버넌스 체계 구축**: `SYSTEM_CONTRACT`, `CONTRACT_GOVERNANCE`, `SPEC_CONSISTENCY_MATRIX` 등 최상위 규약 freeze.
- **디렉토리 구조 최적화**: `src/` -> `docs/` 전환 및 6단계 계층형 아키텍처 정착.

---

## 🗓️ 향후 로드맵 (Future Roadmap)

### [M2] Simulation Engine Prototype
- v1.0 명세를 기반으로 한 결정론적 리스크 산출 엔진(Python) 개발.
- 시나리오별 EL($PD \times LGD \times EAD$) 산출 기능 구현.

### [M3] Production Integration Readiness
- 고도화된 세부 요건 반영 및 실제 데이터 매핑 검증.
- 실시간 이벤트 로그 연동 및 대시보드 시각화 심화.

---
*Last Updated: 2026-04-16*
