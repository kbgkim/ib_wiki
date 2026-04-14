# Equity 매핑 (Equity Mapping)

지분/주식 투자를 Positioning 기반 리스크 모델로 변환합니다.

## 포지션 (Position)
- **투자 건별 단위**: 개별 포트폴리오사 또는 펀드 참여 지분

## 부도 확률 (PD)
- 기업의 파산 확률이나 비즈니스 모델 실패 가능성을 의미합니다.

## 노출액 (Exposure)
- **투자 원금 (Cost)** 또는 현재의 **시장 가치 (Market Value)**를 기준으로 합니다.

## 리스크 산출 방식 (Dual Approach)

### 1. 신용 방식 (Credit Method)
간이 시뮬레이션 시 사용합니다.
- **EAD**: 투자 원금
- **PD**: 기업 파산 확률
- **LGD**: **100% 가정** (지분가치 희석 및 변제 후순위성 반영)

### 2. 시장 방식 (Market Method) - 권장
- **시장 가치 (Market Value)** 기준
- **변동성 (Shock)** 기반 가격 하락 리스크 산출

## 핵심 리스크 요인
- **기업가치 하락**: 실적 부진 및 시장 저평가
- **엑시트 (Exit) 실패**: IPO 지연 또는 매각처 확보 곤란

## 연결
→ [포지션 (Position)](../01_Core_Model/Position.md)  
→ [시장가치 (Market Value)](../01_Core_Model/Market_Value.md)  
→ [지분 리스크 (Equity Risk)](../03_Risk_Calculation/Equity_Risk.md)