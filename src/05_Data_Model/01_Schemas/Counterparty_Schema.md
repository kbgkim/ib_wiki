# 거래상대방 스키마 (Counterparty_Schema)

## 🔥 목적

리스크 관리의 핵심 주체인 차주 및 거래상대방(Counterparty)의 신용 정보를 정의합니다. 
모든 딜(Deal)은 최소 하나의 거래상대방과 연결되며, 이는 PD 산정의 기초가 됩니다.

### ─────────────

## 📊 테이블 구조 (Table Detail)

### COUNTERPARTY_MASTER

| 컬럼명 | 타입 | 설명 |
| :--- | :--- | :--- |
| **cpty_id** | VARCHAR | PK (고유 식별자) |
| **cpty_name** | VARCHAR | 상대방 명칭 (법인명 등) |
| **cpty_type** | ENUM | CORPORATE / SPV / FINANCIAL_INST / GOV |
| **internal_rating** | VARCHAR | 내부 신용 등급 |
| **external_rating** | VARCHAR | 외부 신용 등급 (S&P, Moody's 등) |
| **industry_code** | VARCHAR | 산업 분류 코드 |
| **country_code** | CHAR(3) | 국가 코드 |
| **as_of_date** | DATE | Snapshot 기준일 |

### ─────────────

## 🧠 구조 역할

### PD 산정의 기초 데이터
- 거래상대방의 신용 등급 및 산업 정보는 개별 포지션의 **부도확률(PD)**을 결정하는 가장 중요한 입력값입니다.
- SPV(특수목적법인)의 경우, 실질적 신용보강 주체인 모기업의 정보와 연결될 수 있습니다.

### ─────────────

## 🔗 연결

- [부도확률 (PD)](../../../01_Core_Model/PD.md)
- [딜 스키마 (Deal Schema)](./Deal_Schema.md)

### ─────────────

*최종 업데이트: 2026-04-14*