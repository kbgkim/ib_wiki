# 기대손실 산출 로직 (EL Calculation Logic)

## 🔥 목적

개별 포지션의 기초 데이터를 바탕으로 기대손실(Expected Loss)을 산출하는 엔진의 논리적 단계를 정의합니다. 
이는 리스크 엔진의 **'Calculation Pipeline'**을 형성합니다.

### ─────────────

## 📌 1. 산출 파이프라인 (Pipeline)

기대손실 산출은 데이터 로드부터 최종 집계까지 4단계를 거칩니다.

### 산출 단계
1. **Data Ingestion**: Deal/Position/Cashflow 데이터 로드  
2. **Variable Mapping**: 자산군별 특성을 반영한 PD, LGD, EAD 매핑  
3. **Core Calculation**: `EL = PD × LGD × EAD` 연산 수행  
4. **Result Storage**: 산출된 EL 및 중간 변수를 리스크 결과 테이블에 저장  

### ─────────────

## 🧠 2. 자산별 산출 알고리즘

### PD (부도 확률) 연산
- **PF / ABS**: 내부 등급 모델 및 사업성 평가 점수에 따름
- **NPL**: 부실채권이므로 **100% 고정**

### LGD (손실률) 연산
- **PF / NPL**: 담보 가치(Collateral Value) 기반 회수 가능성 시뮬레이션
- **ABS**: 워터폴 순위에 따른 손실 흡수력(Subordination) 분석

### EAD (익스포저) 연산
- **공통**: 현재 잔액 + (미인출 한도 × CCF)

### ─────────────

## ⚙️ 3. 리스크 결과 집계 (Aggregation)

산출된 기대손실은 상위 계층으로 자동 집계됩니다.

### 집계 계층 구조
- **Level 1**: Position별 기대손실
- **Level 2**: Deal별 기대손실 (포지션 합계)
- **Level 3**: Portfolio/Sector별 기대손실

### ─────────────

## 🔗 연결

- [통합 리스크 프레임워크](../01_Unified_Risk_Framework.md)
- [기대손실 (Expected Loss)](../01_Core_Model/Expected_Loss.md)
- [리스크 결과 스키마](../05_Data_Model/01_Schemas/Risk_Result_Schema.md)

### ─────────────

*최종 업데이트: 2026-04-14*