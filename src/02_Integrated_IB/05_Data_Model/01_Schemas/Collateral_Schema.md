# 담보 스키마 (Collateral Schema)

## 목적
딜의 안정성을 확보하기 위해 제공된 담보물 및 보증 자산의 상세 정보를 정의합니다.

---

## 개념
**Collateral**은 리스크 산출 시 **LGD(손실률)**를 결정하는 결정적인 요소입니다. 담보 가치가 높을수록 회수율(Recovery Rate)이 증가하며 실질 손실이 감소합니다.

---

## 테이블 구조

| 컬럼명 | 설명 | 비고 |
|--------|------|------|
| **collateral_id** | PK (Primary Key) | 담보 식별자 |
| **position_id** | 포지션 식별자 | 해당 담보가 보호하는 포지션 |
| **collateral_type** | 담보 유형 | 부동산, 상장주식, 예금, 질권 등 |
| **val_amount** | 감정가/평가액 | 최근 평가액 |
| **val_date** | 평가일 | |
| **senior_amount** | 선순위 채권액 | 본 포지션보다 우선하는 타 채권액 |
| **net_val_amount** | 실질 담보 가치 | 감정가 - 선순위 채권액 |
| **ltv** | 담보 인정 비율 | 노출액 / 감정가 |
| **status** | 담보 상태 | 설정 완료, 해지 등 |

---

## 설계 원칙
- **LGD 연동**: `net_val_amount`는 엔진 내에서 회수 예상액(Recovery)으로 변환되어 LGD 산출에 반영됩니다.
- **주기적 갱신**: 매 분기 또는 반기별로 `val_amount` 스냅샷을 관리하여 시가 변동을 반영합니다.

---

## 연결
→ [손실률 (LGD)](../../01_Core_Model/LGD.md)  
→ [포지션 스키마 (Position Schema)](./Position_Schema.md)
