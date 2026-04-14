# 현금흐름 (Cashflow)

딜(Deal)과 포지션(Position)에서 발생하는 실제 자금의 유효한 유입과 유출을 의미합니다. IB 리스크 관리의 가장 근본적인 관측 데이터입니다.

## 개념
- **Inflow (유입)**: 원금 상환, 이자 수익, 분양 대금, 배당금 등
- **Outflow (유출)**: 대출 실행(Drawdown), 투자 집행, 운영 비용 등

## 리스크와의 관계
모든 리스크는 **현금흐름의 부족 (Shortfall)**에서 시작됩니다.
- **Credit Risk**: 차주가 약속된 Cashflow를 제공하지 못할 때 발생 (부도)
- **Market Risk**: 자산의 가치 하락으로 인해 미래의 예상 Cashflow(Exit)가 감소할 때 발생

## 주요 지표
- **Expected Cashflow**: 계약 및 사업 계획상 예정된 현금흐름
- **Actual Cashflow**: 실제로 입금/출금된 현금흐름
- **Net Cashflow**: 특정 시점의 순 현금 유입액

## 연결
→ [포지션 (Position)](./Position.md)  
→ [현금흐름 스키마 (Cashflow Schema)](../05_Data_Model/01_Schemas/Cashflow_Schema.md)  
→ [손실 발생 구조 (Cashflow to Loss Logic)](../05_Data_Model/02_Logic/Cashflow_to_Loss_Logic.md)
