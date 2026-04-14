# 딜 스키마 (Deal Schema)

## 목적
IB 금융 거래의 최상위 객체인 **딜(Deal)**의 기본 마스터 정보를 정의합니다.

---

## 개념
**Deal**은 리스크 관리 및 수익성 분석의 가장 큰 단위이며, 여러 개의 **Position**을 하위에 포함할 수 있습니다.

---

## 테이블 구조

| 컬럼명 | 설명 | 비고 |
|--------|------|------|
| **deal_id** | PK (Primary Key) | 딜 식별자 |
| **deal_name** | 딜 명칭 | 국문/영문 혼용 가능 |
| **industry_code** | 자산군/산업 분류 | 예: Real Estate, Energy 등 |
| **currency** | 기본 통화 | KRW, USD 등 |
| **total_commitment** | 총 약정액 | 딜의 전체 규모 |
| **start_date** | 딜 시작일 | 대출/투자 실행일 |
| **end_date** | 만기 예정일 | 상환 완료 예정일 |
| **status** | 딜 진행 상태 | ACTIVE, CLOSED, DEFAULT 등 |
| **dept_code** | 담당 부서 코드 | RM/심사 부서 등 |
| **as_of_date** | 데이터 생성 기준일 | |

---

## 설계 원칙
- **계층적 관리**: 모든 포지션은 반드시 하나의 `deal_id`에 종속되어야 합니다.
- **최종 상태 반영**: 데이터는 현재 시점의 가장 최신 딜 정보를 반영합니다.

---

## 연결
→ [포지션 스키마 (Position Schema)](./Position_Schema.md)  
→ [현금흐름 (Cashflow)](../../01_Core_Model/Cashflow.md)
