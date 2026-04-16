# 지분 투자 (Equity Investment) 도메인 명세

## 1. 개요 (Overview)
본 문서는 지분 투자(Equity)의 핵심 도메인 구조를 정의합니다. 지분 투자는 기업의 소유권을 취득하여 자본 가치 상승(Capital Gain) 및 배당(Dividend)을 추구하며, 리스크 체인의 최하단(Subordination)에서 가치 변동에 직접 노출되는 도메인입니다.

---

## 2. Core Domain Layer (도메인 핵심)

### 📌 핵심 구조: 후순위성 (Subordination) 및 잔여 청구권
- **리스크 최하단**: 파산 시 모든 채무(Senior/Mezzanine) 상환 후 잔여 재산에 대해서만 권리를 가집니다.
- **Market Value 중심**: PD/LGD 프레임워크를 기반으로 하되, 실질적으로는 시장 가치 하락(Mark-to-Market)에 따른 손실 변동성이 핵심입니다.

### ⚙️ 가치 평가 모델 (Valuation)
- **DCF & Multiples**: 미래 현금흐름 할인 또는 비교 기업 배수를 통한 가치 산정.
- **Shock Mechanism**: 시장 변동성 또는 실적 악화 이벤트 발생 시 가치 잠식(Loss) 트리거.

---

## 3. Extension Layer (구조 확장 요소)

핵심 모델에 주입되는 확장 속성입니다.

### 🤝 Private Debt 시너지 (하이브리드 구조)
- **구조적 영향**: 단순 지분 투자가 아닌 대출(Senior/Mezzanine)과 결합된 인수 금융 구조인 경우, 상환 우선순위 및 담보권 이벤트가 복합적으로 작용합니다.

### 🚪 Exit Strategy (엑시트 경로)
- **구조적 영향**: IPO(상장)와 Trade Sale(매각) 중 어느 경로를 선택하느냐에 따라 최종 가치 실현의 시점과 가치 평가 방식이 변경됩니다.

---

## 4. Risk / Value Impact Factor

| 구분 | Impact Factor | 리스크 지표 전이 (Direction) | 민감도 유형 (Type) |
| :--- | :--- | :--- | :--- |
| **Risk** | **상장 주식 Volatility** | 시장 변동성 상승 시 MTM 손실 증가 | **Linear** (Beta 계수와 비례) |
| **Risk** | **실적 성장성 (EBITDA)** | 실적 악화 시 Valuation Multiples 하락 | **Piecewise** (BEP 하차 시 가치 급감) |
| **Value** | **경영권 프리미엄** | 전략적 매수자(SI) 등장 시 가치 상승 | **Threshold** (매각 딜 클로징 시점) |

---

## 5. Scenario Impact (통합 시나리오 영향)

거시 경제 시나리오가 Equity 도메인 내 이벤트를 트리거하는 경로입니다.

| 시나리오 | 트리거 이벤트 (Trigger Event) | 구조적 영향 (Impact) |
| :--- | :--- | :--- |
| **S1: Interest Rate Shock** | `MARK_TO_MARKET_UPDATE` | 할인율(WACC) 상승에 따른 DCF 가치의 급격한 하락 및 평가 손실 발생 |
| **S2: Real Estate Crash** | `VALUATION_SHOCK` | 부동산 관련 포트폴리오 기업의 실적 악화 및 배수(Multiples) 하락 |
| **S3: Liquidity Crunch** | `EXIT_DELAYED` | IPO 시장 위축 및 M&A 구매력 저하로 인한 회수 시점 무기한 연기 |

---

## 🔗 연결
- [지분 투자 라이프사이클 및 이벤트 모델](./Unlisted_Deal_Lifecycle.md)
- [지분 리스크 매핑 가이드](./Equity_Mapping.md)

### ─────────────

*최종 업데이트: 2026-04-16 (아키텍처 재설계 반영)*
