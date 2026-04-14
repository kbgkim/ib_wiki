# 거래 상대방 스키마 (Counterparty Schema)

## 목적
딜(Deal)과 관련된 모든 거래 주체(차주, 시행사, 시공사 등)의 정보 및 신용 등급을 정의합니다.

---

## 개념
**Counterparty**는 리스크 산출 시 **PD(부도 확률)**를 결정하는 핵심 주체입니다. 한 명의 Counterparty는 여러 딜에 참여할 수 있습니다.

---

## 테이블 구조

| 컬럼명 | 설명 | 비고 |
|--------|------|------|
| **party_id** | PK (Primary Key) | 상대방 식별자 |
| **party_name** | 법인명/주체명 | |
| **reg_number** | 사업자 등록 번호 | 중복 방지 식별자 |
| **internal_grade** | 내부 신용 등급 | PD 산출의 기초 |
| **external_grade** | 외부 신용 등급 | 나이스, 한신평 등 |
| **industry_type** | 산업 대분류 | 제조업, 건설업 등 |
| **financial_summary** | 주요 재무 지표 | 부채비율, 영업이익 등 |
| **last_review_date** | 최종 신용 등급 검토일 | |
| **as_of_date** | 데이터 생성 기준일 | |

---

## 설계 원칙
- **PD 도출의 근거**: `internal_grade`는 엔진 내에서 수치화된 PD로 변환되어야 합니다.
- **고유성 유지**: 사업자 등록 번호를 기준으로 동일 주체의 중복 생성을 방지합니다.

---

## 연결
→ [부도 확률 (PD)](../../01_Core_Model/PD.md)  
→ [딜 스키마 (Deal Schema)](./Deal_Schema.md)
