# 현금흐름 스키마 (Cashflow_Schema)

## 🔥 목적

딜과 포지션에서 발생하는 실제/예정 자금 흐름을 기록하는 이벤트 기반 물리 데이터 구조를 정의합니다. 
IB 리스크 관리의 가장 핵심적인 관측 데이터 스키마입니다.

### ─────────────

## 📊 테이블 구조 (Table Detail)

### CASHFLOW_EVENT

| 컬럼명 | 타입 | 설명 |
| :--- | :--- | :--- |
| **cashflow_id** | VARCHAR | PK (고유 식별자) |
| **position_id** | VARCHAR | FK (소속 포지션 ID) |
| **cashflow_date** | DATE | 자금 발생 예정일 또는 실제일 |
| **cashflow_type** | ENUM | PRINCIPAL / INTEREST / FEE / RECOVERY / DIVIDEND / EXIT |
| **expected_amount** | DECIMAL | 계약상 예정 금액 |
| **actual_amount** | DECIMAL | 실제로 발생/회수된 금액 |
| **event_status** | VARCHAR | PLANNED / CONFIRMED / SETTLED |
| **as_of_date** | DATE | Snapshot 기준일 |

### ─────────────

## 🧠 리스크 매핑 키 (Risk Mapping Key)

각 `cashflow_type`은 리스크 변수에 다음과 같이 매핑됩니다.

### 타입별 리스크 영향
- **PRINCIPAL**: EAD(익스포저) 잔액 변동 직접 영향  
- **INTEREST**: PF/NPL 프로젝트 수익성 및 상환 능력 지표  
- **RECOVERY**: 부도 시 회수(Recovery) 데이터로서 LGD 결정 요인  
- **DIVIDEND / EXIT**: Equity 포지션의 수익 실현 및 Valuation Risk 요인  

### ─────────────

## ⚙️ 설계 특징
- **Append-only**: 과거 현금흐름 이력은 변경하지 않고 추가적인 조정(Adjustment) 이벤트를 통해 수정합니다.
- **Time-series**: 시간 기반 리스크 시뮬레이션의 기초 시퀀스 데이터를 형성합니다.

### ─────────────

## 🔗 연결

- [현금흐름 (Cashflow)](../../../01_Core_Model/Cashflow.md)
- [포지션 스키마 (Position Schema)](./Position_Schema.md)
- [손실 발생 로직 (Logic)](../02_Logic/Cashflow_to_Loss_Logic.md)

### ─────────────

*최종 업데이트: 2026-04-14*