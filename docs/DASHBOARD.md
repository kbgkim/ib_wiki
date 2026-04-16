# IB 통합 리스크 & 퍼포먼스 대시보드 (IB Intelligence Dashboard)

본 대시보드는 4대 핵심 자산(PF, ABS, NPL, Equity)의 운용 현황과 리스크 지표를 실시간으로 통합 시각화합니다. 
*(데이터 기준일: 2026-04-14, Ontological Refactoring 완료)*

### ─────────────

## 🚩 레드 플래그 및 긴급 주의 (Red Flags)

### CAUTION
**주요 리스크 경보**
1. **PF 평가 등급 하락**: '부실우려' 등급 사업장 2건 발생 -> [PF 매핑 가이드](03_Assets_Verticals/PF/PF_Mapping.md) 참조
2. **ABS 차환 리스크**: 단기 ABCP 매입확약 300억 만기 도래
3. **NPL 회수 지연**: 유치권 분쟁으로 인한 경매 지연 사업장 발생

### ─────────────

## 1. 포트폴리오 총괄 (Global Executive View)

| 항목 | 현재 수치 | 리스크 레이어 | 상태 |
| :--- | :--- | :--- | :---: |
| **전체 AUM** | **1,250억 원** | [01_Core_Model](01_Core_Model/Position.md) | 🟢 |
| **기대 손실 (EL)** | **6.5억 원** | [04_Risk_Calculation](04_Risk_Calculation/EL_Calculation.md) | 🟠 |
| **표준 가이드라인** | **준수** | [00_Standard_Layer](00_Standard_Layer/Core_Definitions.md) | 🔵 |

### ─────────────

## 2. 자산별 심층 관제 (Asset Control Center)

### 부동산 PF 점검 현황
- **매핑 가이드**: [PF_Mapping.md](03_Assets_Verticals/PF/PF_Mapping.md)
- **라이프사이클**: [PF_Deal_Lifecycle.md](03_Assets_Verticals/PF/PF_Deal_Lifecycle.md)

### ABS 및 유동화 리스크
- **매핑 가이드**: [ABS_Mapping.md](03_Assets_Verticals/ABS/ABS_Mapping.md)
- **라이프사이클**: [ABS_Deal_Lifecycle.md](03_Assets_Verticals/ABS/ABS_Deal_Lifecycle.md)

### NPL 회수 성과 (Recovery)
- **매핑 가이드**: [NPL_Mapping.md](03_Assets_Verticals/NPL/NPL_Mapping.md)
- **라이프사이클**: [NPL_Deal_Lifecycle.md](03_Assets_Verticals/NPL/NPL_Deal_Lifecycle.md)

### Equity 평가 손익
- **매핑 가이드**: [Equity_Mapping.md](03_Assets_Verticals/Equity/Equity_Mapping.md)
- **라이프사이클**: [Unlisted_Deal_Lifecycle.md](03_Assets_Verticals/Equity/Unlisted_Deal_Lifecycle.md)

### ─────────────

## Standard Reference
- [Core_Definitions](00_Standard_Layer/Core_Definitions.md)
- [Synthesis Map](02_Integrated_IB/Synthesis_Map.md)
- [Data Model](05_Data_Model/01_Schemas/Position_Schema.md)

### ─────────────

## System Governance & Execution
- **Contract**: [SYSTEM_CONTRACT.md](99_System/Contract/SYSTEM_CONTRACT.md) / [GOVERNANCE](99_System/Contract/CONTRACT_GOVERNANCE.md)
- **Trace**: [TRACEABILITY_SPEC.md](99_System/Trace/TRACEABILITY_SPEC.md)
- **Validation**: [INTEGRATED_VALIDATION_RUN.md](99_System/Validation/INTEGRATED_VALIDATION_RUN.md)
- **Execution**: [OUTPUT_HASH_SPEC.md](99_System/Execution/OUTPUT_HASH_SPEC.md) / [NORMALIZATION](99_System/Execution/TRACE_GRAPH_NORMALIZATION_SPEC.md)
- **Status & Log**: [VERIFICATION_REPORT.md](99_System/VERIFICATION_REPORT.md) / [ARCHITECTURAL_LOG.md](99_System/ARCHITECTURAL_LOG.md)

### ─────────────

*최종 업데이트: 2026-04-14 (Risk Engine Layered Architecture 적용)*
