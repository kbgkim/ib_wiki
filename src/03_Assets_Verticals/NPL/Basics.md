# 부실채권 (Non-Performing Loan, NPL) 도메인 명세

## 1. 개요 (Overview)
본 문서는 부실채권(NPL)의 핵심 도메인 구조를 정의합니다. NPL은 이미 부도가 발생한 채권(PD=100%)을 저가에 매입하여, 담보권 행사나 채무 조정을 통해 회수 가치를 극대화하는 자산 관리 중심의 도메인입니다.

---

## 2. Core Domain Layer (도메인 핵심)

### 📌 핵심 구조: 회수 가치 (Recovery Value) 중심
- **PD = 100% 고정**: 리스크 관점이 '부도 여부'에서 '회수율(LGD) 변동성'으로 전이됩니다.
- **OPB vs 매입가**: 장부상 원금(Outstanding Principal Balance)과 실질 매입 가격의 차이가 주된 수익 원천입니다.

### ⚙️ 리스크 전이 모델 (NPL 특화)
- **EAD**: 투자 원금 + 사후 관리 비용(법무, 명도 등).
- **LGD**: $1 - (\text{실제 회수액} / \text{EAD})$. 경매 유찰 횟수가 늘어날수록 급격히 상승합니다.

---

## 3. Extension Layer (구조 확장 요소)

핵심 모델에 주입되는 확장 속성입니다.

### 🏢 AMC (자산관리회사) 구조
- **구조적 영향**: 전문 AMC 위탁 여부에 따라 관리 수수료(Service Fee) 이벤트가 발생하며, 회수 프로세스의 효율성(Time to Recovery)이 변동됩니다.

### 🛤️ Resolution Path (회수 경로 분기)
- **구조적 영향**: 경매(Liquidation)와 채무 조정(Workout) 중 어느 경로를 선택하느냐에 따라 현금흐름의 시점(Timing)과 확실성(Certainty)이 재정의됩니다.

---

## 4. Risk / Value Impact Factor

| 구분 | Impact Factor | 영향도 (Impact) |
| :--- | :--- | :--- |
| **Risk** | **경매 낙찰가율 (Auction Rate)** | LGD 및 최종 회수액에 직접적인 영향을 미치는 최대 리스크 인자 |
| **Risk** | **회수 기간 (Resolution Period)** | 기간의 장기화는 내부수익률(IRR) 및 가치 하락의 주범 |
| **Value** | **채무자 상환 의지 (Willingness)** | 담보 처분 외에 채무 조정을 통한 조기 상환 가능성 확대 |

---

## 5. Scenario Impact (통합 시나리오 영향)

거시 경제 시나리오가 NPL 도메인 내 이벤트를 트리거하는 경로입니다.

| 시나리오 | 트리거 이벤트 (Trigger Event) | 구조적 영향 (Impact) |
| :--- | :--- | :--- |
| **S1: Interest Rate Shock** | `WORKOUT_DELAY` | 채무자의 이자 부담 증가로 인한 조정 협의 지연 및 회수 기간 장기화 |
| **S2: Real Estate Crash** | `AUCTION_FAILURE` | 부동산 시장 경색에 따른 경매 유찰 및 LGD 급증 |
| **S3: Liquidity Crunch** | `COLLECTION_DIP` | 매수 주체 부재로 인한 채권 재매각(Re-sale) 지연 및 유동성 회수 저하 |

---

## 🔗 연결
- [NPL 딜 라이프사이클 및 이벤트 모델](./NPL_Deal_Lifecycle.md)
- [NPL 리스크 매핑 가이드](./NPL_Mapping.md)

### ─────────────

*최종 업데이트: 2026-04-16 (아키텍처 재설계 반영)*
