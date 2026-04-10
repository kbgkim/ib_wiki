# 리스크 엔진 기술 사양 (Risk Engine Technical Specification)

본 문서는 통합 리스크 모델을 실제로 시스템에서 구현하기 위한 수학적 정규화 알고리즘과 가중치 집계 로직을 기술합니다.

## 1. 리스크 정규화 및 집계 (Normalization & Aggregation)

### 1.1 4대 분석 범주 (Risk Categories)
시스템은 다차원 리스크 분석을 위해 다음 4가지 범주를 정규화하여 관리합니다.

- **Financial (재무)**: 인수 가액, 배당 수익률 등을 기반으로 한 경제적 리스크.
- **Legal (법무)**: 계약 위반, 소송 가능성 및 규제 준수 여부.
- **Operational (운영)**: 자산 관리 실무, 설비 노후도 및 운영 효율성.
- **Security (보안/VDR)**: 데이터룸 접근 로그 분석 기반의 내부 통제 리스크. (현업: **VDR 실사 리스크**)

### 1.2 수학적 정규화 알고리즘
서로 다른 입력값(통화, 비율, 빈도 등)을 0(Safe)에서 100(High Risk) 사이의 점수로 정규화하여 비교 가능하도록 만듭니다.

- **산식**: `Total_Risk_Score = sum(Category_Score[i] * Weight[i]) / 100`

### 1.3 등급 맵핑 (Risk Grading Scale)
산출된 점수는 다음 금융권 등급 체계에 따라 맵핑됩니다.

| 점수 범위 | 등급 (Grade) | 상태 (Status) |
| :--- | :--- | :--- |
| **0 - 20** | **AAA ~ AA** | **안전 (Safe)** |
| **21 - 40** | **A ~ BBB** | **주의 (Warning)** |
| **41 - 60** | **BB ~ B** | **경고 (Caution)** |
| **61 - 100** | **CCC ~ D** | **위험 (High Risk)** |

## 2. 데이터 모델 및 엔지니어링

### 2.1 리스크 데이터 파이프라인
데이터는 실시간으로 수집되어 다음 단계를 거쳐 DW(Data Warehouse)로 적재됩니다.
`Kafka (수집) → Spark (처리) → Risk Calculation (계산) → DW (저장)`

### 2.2 핵심 데이터 모델
- **Asset**: 자산 식별자, 유형, 노출액(Exposure).
- **RiskFactor**: 자산별 PD, LGD, 시나리오 가중치.
- **Cashflow**: 기대 현금흐름 및 스트레스 테스트 현금흐름.

## 3. UI/UX 연동 로직
- **Risk Radar Chart**: 4각 레이더 차트를 통해 리스크 불균형 시각화.
- **Dynamic Waterfall**: 각 리스크 요인이 최종 평가 가치(NPV)를 삭감(**Erosion**)하는 과정을 동적으로 표시.

---
*최종 수정일: 2026-04-10*
*참조: ib-mna-engine/Phase 4*
