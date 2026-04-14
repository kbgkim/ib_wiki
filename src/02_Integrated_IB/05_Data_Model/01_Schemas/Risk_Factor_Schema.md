# 리스크 요인 스키마 (Risk Factor Schema)

## 목적
현금흐름 변동을 유발하는 외부 시장 지표(Risk Driver)의 실측 데이터를 정의합니다.

---

## 개념
**Risk Factor**는 관측 가능한 시장 데이터이며, 리스크 엔진에서 시나리오별 충격(Shock)을 가하기 전의 **기초값(Base Value)** 역할을 합니다.

---

## 테이블 구조

| 컬럼명 | 설명 | 비고 |
|--------|------|------|
| **factor_id** | PK (Primary Key) | 요인 식별 코드 |
| **factor_name** | 요인 명칭 | 예: 국고채 3년, KOSPI 200, 환율 등 |
| **factor_type** | 요인 유형 | INTEREST_RATE, STOCK_INDEX, FX, COMMODITY 등 |
| **base_value** | 현재 시장가/지표값 | 특정 시점의 실측값 |
| **volatility** | 역사적 변동성 (Std Dev) | 리스크 시뮬레이션의 기초 |
| **source** | 데이터 출처 | Bloomberg, 한국은행, 연합인포맥스 등 |
| **as_of_date** | 데이터 생성 기준일 | |

---

## 설계 원칙
- **객관적 실측치**: 실제 시장에서 관측된 데이터만을 저장하며 가공된 시나리오는 포함하지 않습니다.
- **기준일 관리**: 시계열 분석을 위해 일자별로 데이터를 스냅샷 관리합니다.

---

## 연결
→ [시나리오 모델 (Scenario Model)](../03_Behavior/Scenario_Model.md)  
→ [시나리오 스키마 (Scenario Schema)](./Scenario_Schema.md)  
→ [변동성 (Volatility)](../../01_Core_Model/Volatility.md)
