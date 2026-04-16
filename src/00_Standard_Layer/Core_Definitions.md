# Core Definitions (IB Standard Layer)

## 1. Position (포지션)
모든 리스크 계산의 최소 단위

- PF / ABS / NPL / Equity 모두 Position으로 환원
- 모든 Exposure / EAD 기준 단위

---

## 2. Cashflow (현금흐름)
리스크의 원인 데이터

- Expected Cashflow
- Actual Cashflow
- Shortfall = Expected - Actual
- Loss = max(Shortfall, 0)

---

## 3. PD (Probability of Default)
부도 확률

- PF: 사업 실패 확률
- ABS: 기초자산 default
- NPL: 100% 고정
- Equity: 기업 failure probability

---

## 4. LGD (Loss Given Default)
부도 시 손실 전환 비율

- Recovery 기반
- 구조 (ABS waterfall / PF collateral / NPL auction)

---

## 5. EAD (Exposure at Default)
부도 시 노출 금액

- 현재 Exposure + 미래 drawdown
- credit stress 반영

---

## 6. Event (이벤트)
금융 개체의 상태 변화를 유발하는 비즈니스 사건

- **Risk Trigger**: PD, LGD 등 리스크 지표를 변화시키는 사건
- **Value Trigger**: 현금흐름(Cashflow)의 양과 시점을 변화시키는 사건

---

## 7. State (상태)
이벤트에 의해 결정되는 개체의 특정 시점 상황

- **Lifecycle State**: 딜의 생애주기 단계 (Proposed, Active, Closed 등)
- **Quality State**: 자산의 건전성 상태 (Normal, Delinquent, Default 등)

---

## 8. Core Identity Rule

All Risk = Function(Position, Cashflow, **Event**)
- 리스크는 포지션(대상)과 현금흐름(원천)에 이벤트(변화 동력)가 결합되어 결정됩니다.