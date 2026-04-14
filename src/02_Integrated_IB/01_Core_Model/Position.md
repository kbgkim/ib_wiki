# 포지션 (Position)

딜 내에서 내가 보유한 자금의 최소 관리 단위입니다.

## 특징
- **리스크 계산 최소 단위**: 모든 리스크 엔진은 포지션 단위로 데이터를 집계합니다.
- **현금흐름 발생 기준**: 투자금의 유입과 유출이 일어나는 물리적/논리적 단위입니다.
- **Exposure 산출 기준**: 개별 포지션의 성격에 따라 노출액 산정 방식이 달라집니다.

## 예시
- **PF**: 선순위 대출 / 후순위 투자
- **NPL**: 개별 담보 채권
- **ABS**: 트랜치 (선/중/후순위)

## 연결
→ [딜 (Deal)](../00_Root_Model/IB_Risk_Data_Model.md)  
→ [노출액 (Exposure)](./Exposure.md)  
→ [현금흐름 (Cashflow)](../../DASHBOARD.md)  
→ [리스크 (Risk)](../00_Root_Model/IB_Risk_Data_Model.md)