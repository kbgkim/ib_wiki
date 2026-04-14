# 담보 스키마 (Collateral_Schema)

## 🔥 목적

포지션의 손실 완화 수단인 담보(Collateral) 및 신용보강 정보를 정의합니다. 
부도 시 회수 가치를 결정하며, 최종적으로 LGD 산정의 핵심 근거가 됩니다.

### ─────────────

## 📊 테이블 구조 (Table Detail)

### COLLATERAL_MASTER

| 컬럼명 | 타입 | 설명 |
| :--- | :--- | :--- |
| **collateral_id** | VARCHAR | PK (고유 식별자) |
| **position_id** | VARCHAR | FK (연결된 포지션 ID) |
| **collateral_type** | ENUM | REAL_ESTATE / STOCK / GUARANTEE / CASH |
| **valuation_amount** | DECIMAL | 현재 평가액 |
| **valuation_date** | DATE | 최근 평가 시점 |
| **loan_to_value** | DECIMAL | 적용 LTV (채권액 / 담보가치) |
| **seniority_rank** | INT | 담보권 순위 (1순위, 2순위 등) |
| **as_of_date** | DATE | Snapshot 기준일 |

### ─────────────

## 🧠 구조 역할

### LGD 산정의 핵심 데이터
- 담보의 유형과 평가 가치는 **회수율(Recovery Rate)**을 결정합니다.
- 부동산 담보의 경우 위치, 용도 정보가 추가적으로 연결되어 시나리오별 가격 하락폭을 결정합니다.

### ─────────────

## 🔗 연결

- [손실률 (LGD)](../../../01_Core_Model/LGD.md)
- [포지션 스키마 (Position Schema)](./Position_Schema.md)

### ─────────────

*최종 업데이트: 2026-04-14*