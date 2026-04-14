# 현금흐름 스키마 (Cashflow Schema)

## 목적
Position 단위의 현금흐름을 관리하고 리스크 계산의 기반을 제공합니다.

---

## 개념

**Cashflow**는 실제 자금의 유입과 유출이며, 모든 리스크는 **현금흐름 부족 (Shortfall)**에서 발생합니다.

---

## 테이블 구조

| 컬럼명 | 설명 |
|--------|------|
| **cashflow_id** | PK (Primary Key) |
| **position_id** | Position 식별자 |
| **deal_id** | Deal 식별자 |
| **cashflow_date** | 발생 예정일 또는 실제 발생일 |
| **cashflow_type** | 유입/유출 유형 |
| **expected_amount** | 계약상의 예상 금액 |
| **actual_amount** | 실제 회수/집행 금액 |
| **currency** | 통화 (USD, KRW 등) |
| **status** | 처리 상태 |
| **as_of_date** | 데이터 생성/관리 기준일 |

---

## Cashflow 유형

- **PRINCIPAL** (원금)
- **INTEREST** (이자)
- **FEE** (수수료)
- **RECOVERY** (회수금)
- **DIVIDEND** (배당)
- **EXIT** (투자 회수)

---

## 리스크 계산 구조

**Shortfall** = $Expected Cashflow - Actual Cashflow$  
**Loss** = $max(Shortfall, 0)$

---

## 설계 원칙

- **Position 중심**: 모든 현금흐름은 상위 Position에 종속되어 관리됩니다.
- **예상 vs 실적**: `Expected`와 `Actual`을 분리 저장하여 Shortfall을 실시간으로 산출합니다.
- **범용성**: 전 자산군(PF, NPL 등)에 동일한 구조를 적용합니다.

---

## 연결

→ [현금흐름 (Cashflow)](../../01_Core_Model/Cashflow.md)  
→ [포지션 스키마 (Position Schema)](./Position_Schema.md)  
→ [리스크 결과 스키마 (Risk Result Schema)](./Risk_Result_Schema.md)