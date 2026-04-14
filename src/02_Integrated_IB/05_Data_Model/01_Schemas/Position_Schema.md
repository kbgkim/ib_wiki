# 포지션 스키마 (Position_Schema)

## 🔥 목적

리스크 산출 및 관리의 최소 기본 단위인 포지션(Position)의 물리적 데이터 구조를 정의합니다. 
모든 리스크 지표(PD, LGD, EAD)는 본 포지션 테이블에 연결됩니다.

### ─────────────

## 📊 테이블 구조 (Table Detail)

### POSITION_MASTER

| 컬럼명 | 타입 | 설명 |
| :--- | :--- | :--- |
| **position_id** | VARCHAR | PK (고유 식별자) |
| **deal_id** | VARCHAR | FK (소속 딜 ID) |
| **asset_type** | ENUM | EQUITY / SENIOR_LOAN / MEZZANINE / BOND |
| **seniority_rank** | INT | Waterfall 상의 우선순위 (낮을수록 우선) |
| **ccf_rate** | DECIMAL | 적용 CCF (EAD 산출용) |
| **as_of_date** | DATE | Snapshot 기준일 |

### ─────────────

## 🧠 구조 역할

### 리스크 노드의 핵심
- 포지션은 개별 투자 단위의 경제적 성격을 규정합니다.
- 현금흐름(Cashflow)이 모여드는 바스켓이자, 리스크 엔진의 핵심 입력 대상입니다.

### ─────────────

## 🔗 연결

- [딜 스키마 (Deal Schema)](./Deal_Schema.md)
- [현금흐름 (Cashflow)](../../01_Core_Model/Cashflow.md)
- [리스크 결과 스키마 (Risk Result Schema)](./Risk_Result_Schema.md)

### ─────────────

*최종 업데이트: 2026-04-14*