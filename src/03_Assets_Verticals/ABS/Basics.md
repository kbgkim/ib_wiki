# 자산유동화 (Asset-Backed Securities, ABS) 도메인 명세

## 1. 개요 (Overview)
본 문서는 자산유동화(ABS)의 핵심 도메인 구조를 정의합니다. ABS는 기초자산(Underlying Asset)에서 발생하는 현금흐름을 법적으로 격리된 특수목적기구(SPV)를 통해 증권화하여 리스크와 가치를 재구성하는 구조금융입니다.

---

## 2. Core Domain Layer (도메인 핵심)

### 📌 핵심 구조: 트랜칭 (Tranching) 및 워터폴
- **트랜치 계층**: 선순위(Senior), 중순위(Mezzanine), 후순위(Junior/Equity)로 리스크를 분리.
- **현금흐름 우선순위**: 모든 유입 현금은 사전에 정의된 Waterfall 원칙에 따라 상단(Senior)부터 순차 상환됩니다.

### ⚙️ 리스크 차단 효과 (Bankruptcy Remoteness)
- **자산 보유자(Originator)**의 파산 리스크로부터 기초자산을 완전히 분리하여 투자자의 안정성을 확보합니다.

---

## 3. Extension Layer (구조 확장 요소)

핵심 모델에 동적으로 주입되는 확장 속성입니다.

### ⚖️ True Sale (진성 매각) 및 법률 구조
- **구조적 영향**: 자산 양도가 담보 대출이 아닌 실질적 매각으로 판정되는지 여부에 따라 SPV의 자산 보유 상태(State)가 확정됩니다.

### 🛡️ Credit Enhancement (신용 보강)
- **구조적 영향**: 외부 보증(Provider) 또는 내부 보강(Over-collateralization) 이벤트 발생 시 트랜치별 LGD가 동적으로 재계산됩니다.

### 🪙 STO Branch (토큰증권 확장)
- **구조적 영향**: 발행 증권의 형태가 전통적 채권이 아닌 분산 원장 기반의 토큰 형태인 경우, 소유권 이전 이벤트의 검증 방식이 변경됩니다.

---

## 4. Risk / Value Impact Factor

| 구분 | Impact Factor | 영향도 (Impact) |
| :--- | :--- | :--- |
| **Risk** | **트랜치 두께 (Tranche Thickness)** | 후순위 채권의 비중이 높을수록 선순위 PD/LGD가 기하급수적으로 감소 |
| **Risk** | **기초자산 상관관계 (Correlation)** | 자산 간 상관관계가 높을수록 시스템 리스크 시 선순위 보호 효과 약화 |
| **Value** | **Prepayment Rate (조기상환율)** | 예상보다 빠른 상환 시 재투자 리스크(Value 하락) 발생 |

---

## 5. Scenario Impact (통합 시나리오 영향)

거시 경제 시나리오가 ABS 도메인 내 이벤트를 트리거하는 경로입니다.

| 시나리오 | 트리거 이벤트 (Trigger Event) | 구조적 영향 (Impact) |
| :--- | :--- | :--- |
| **S1: Interest Rate Shock** | `CASH_TRAP` | 조달 금리 상승으로 인한 초과 스프레드 감소 및 현금 유보 트리거 작동 |
| **S2: Real Estate Crash** | `COLLATERAL_DEVALUED` | 기초자산(부동산) 가치 하락에 따른 LTV 악화 및 선순위 안정성 저하 |
| **S3: Liquidity Crunch** | `REFINANCING_FAILURE` | ABCP 등 단기 유동화 증권의 차환 실패 리스크 및 유동성 지원 이벤트 호출 |

---

## 🔗 연결
- [ABS 딜 라이프사이클 및 이벤트 모델](./ABS_Deal_Lifecycle.md)
- [ABS 리스크 매핑 가이드](./ABS_Mapping.md)

### ─────────────

*최종 업데이트: 2026-04-16 (아키텍처 재설계 반영)*
