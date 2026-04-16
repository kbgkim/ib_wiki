# 딜 스키마 (Deal Schema)

## 🔥 목적

IB 리스크 관리의 최상위 통제 단위인 딜(Deal)에 대한 물리적 마스터 테이블 구조를 정의합니다. 
하나의 딜은 여러 포지션(Position)을 포함하는 컨테이너 역할을 수행합니다.

### ─────────────

## 📊 테이블 구조 (Table Detail)

### DEAL_MASTER

| 컬럼명 | 타입 | 설명 |
| :--- | :--- | :--- |
| **deal_id** | VARCHAR | PK (고유 식별자) |
| **deal_name** | VARCHAR | 딜 명칭 (건물명, 프로젝트명 등) |
| **asset_class** | ENUM | PF / NPL / ABS / EQUITY |
| **status** | VARCHAR | ACTIVE / CLOSED / DEFAULT |
| **total_commitment** | DECIMAL | 전체 약정 금액 |
| **currency** | CHAR(3) | 통화 코드 |
| **manager_id** | VARCHAR | 담당 운용역 ID |
| **as_of_date** | DATE | Snapshot 기준일 |

### ─────────────

## 🧠 구조 역할

### 최상위 엔티티
- 시스템에서 리스크를 집계하는 가장 큰 단위입니다.
- 개별 포지션의 집합체로서 비즈니스 시나리오가 적용되는 지점입니다.

### ─────────────

## 🔗 연결

- [통합 리스크 데이터 모델](../../02_Integrated_IB/IB_Risk_Data_Model.md)
- [포지션 스키마 (Position Schema)](./Position_Schema.md)

### ─────────────

*최종 업데이트: 2026-04-14*