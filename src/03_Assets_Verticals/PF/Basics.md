# 프로젝트 파이낸싱 (Project Financing, PF) 도메인 명세

## 1. 개요 (Overview)
본 문서는 프로젝트 파이낸싱(PF)의 핵심 도메인 구조를 정의합니다. PF는 자산보유자의 신용이 아닌, 특정 프로젝트의 미래 사업성과 현금흐름을 기반으로 리스크와 가치를 산출하는 구조금융입니다.

---

## 2. Core Domain Layer (도메인 핵심)

### 📌 핵심 구조: 비소구 금융 (Non-recourse)
- **비소구/제한적 소구**: 사업 실패 시 대주단은 프로젝트 자산 내에서만 채권을 회수합니다.
- **현금흐름 격리**: 시행사(Owner)의 다른 자산과 프로젝트 자산을 법적으로 격리(SPC 활용)합니다.

### ⚙️ 주요 이해관계자 (Stakeholders)
- **시행사 (Developer)**: 사업 주체, 인허가 책임.
- **시공사 (Contractor)**: 건설 책임, **'책임준공 확약'** 제공.
- **대주단 (Lenders)**: 선/중/후순위 자금 공급.

---

## 3. Extension Layer (구조 확장 요소)

핵심 모델에 동적으로 주입되어 리스크 및 가치에 영향을 미치는 확장 요소입니다.

### 🌱 ESG Factor (환경/사회영역)
- **구조적 영향**: 친환경 인증 여부(LEED 등)에 따라 조달 금리(Spread)가 조정되거나, 특정 시나리오 발생 시 보조금 유입 이벤트가 트리거됩니다.

### 🤝 Syndication (MLA/LOM/MLM 구조)
- **구조적 영향**: 주관사(Mandated Lead Arranger)의 참여 여부에 따라 신디케이션 성공 확률 및 수수료(Fee) 구조가 변동됩니다.

---

## 4. Risk / Value Impact Factor

PF 도메인의 가치와 리스크에 직접적인 영향을 미치는 핵심 변수 정의입니다.

| 구분 | Impact Factor | 영향도 (Impact) |
| :--- | :--- | :--- |
| **Risk** | **분양률 (Pre-sale Rate)** | 신규 현금흐름 유입 속도와 PD(부도확률)에 결정적 영향 |
| **Risk** | **공정률 (Completion Rate)** | 준공 리스크 해소 단계별로 LGD(손실률) 감소 효과 |
| **Value** | **임대료 (Rent Revenue)** | 준공 후 운영 단계의 지속적 Cashflow 창출 동인 |

---

## 5. Scenario Impact (통합 시나리오 영향)

거시 경제 시나리오가 PF 도메인 내 이벤트를 트리거하는 경로입니다.

| 시나리오 | 트리거 이벤트 (Trigger Event) | 구조적 영향 (Impact) |
| :--- | :--- | :--- |
| **S1: Interest Rate Shock** | `FUNDING_FAILURE` | 대부 비용 상승에 따른 수지 악화 및 조달 실패 이벤트 발생 |
| **S2: Real Estate Crash** | `PRE_SALE_SHORTFALL` | 분양 수입금 유입 지연으로 인한 Waterfall 정지 및 PD 급증 |
| **S3: Liquidity Crunch** | `SYNDICATION_DELAY` | 신디케이션 미참여 발생 및 주관사 인수 리스크 전이 |

---

## 🔗 연결
- [PF 딜 라이프사이클 및 이벤트 모델](./PF_Deal_Lifecycle.md)
- [PF 리스크 매핑 가이드](./PF_Mapping.md)

### ─────────────

*최종 업데이트: 2026-04-16 (아키텍처 재설계 반영)*
