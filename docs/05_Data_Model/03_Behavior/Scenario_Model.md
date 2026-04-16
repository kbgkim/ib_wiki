# 시나리오 모델 (Scenario_Model)

## 🔥 목적

리스크 요인(Risk Factor)의 변동이 어떻게 전체 포트폴리오의 **시나리오적 충격(Shock)**으로 변환되고 전파되는지에 대한 논리적 모델을 정의합니다.

### ─────────────

## 📌 개념

시나리오는 특정 경제 상황을 시스템이 해석할 수 있는 '충격 계수(Shock Multiplier)'의 집합으로 치환하는 과정입니다.

👉 **Scenario = {Factor_A: Shock_X, Factor_B: Shock_Y, ...}**

### ─────────────

## 🧠 충격 전파 구조 (Progression Logic)

### 단계별 전파
1. **Scenario Definition**: 상황 설정 (예: 금리 급등 섹터 위기)  
2. **Shock Generation**: 리스크 요인별 충격치 산출  
3. **Transmission**: 개별 포지션의 현금흐름 파라미터(PD/LGD)에 충격 투영  
4. **Outcome**: 최종 손실액 및 가치 하락 산출  

### ─────────────

## ⚙️ 주요 시나리오 유형

### Base Case (기준 상황)
- 예상된 현금흐름이 정상적으로 발생하는 상황

### Stress Case (위기 상황)
- 주요 거시 경제 지표에 유의미한 충격(1~2 Standard Deviation)이 가해진 상황

### Worst Case (최악 상황)
- 극단적인 시장 붕괴나 개별 자산의 완전 손실을 가정한 시나리오

### ─────────────

## 🔗 연결

- [시나리오 스키마 (Scenario Schema)](../01_Schemas/Scenario_Schema.md)
- [리스크 요인 스키마 (Risk Factor Schema)](../01_Schemas/Risk_Factor_Schema.md)

### ─────────────

*최종 업데이트: 2026-04-14*