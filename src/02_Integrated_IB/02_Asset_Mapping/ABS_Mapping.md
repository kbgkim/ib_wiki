# ABS 매핑 (ABS Mapping)

자산유동화(ABS) 구조를 Position 기반 리스크 모델로 변환합니다.

## 포지션 (Position)
- **트랜치 (Tranching)**: 선순위, 중순위, 후순위별 수익 구조 및 리스크 전이 단계

## 부도 확률 (PD)
- **기초자산 부도율**: 유동화의 원천이 되는 기초자산(매출채권, 부동산 등)의 부도 확률을 기반으로 합니다.

## 노출액 (Exposure)
- 현재 시점의 실제 투자 원금입니다.

## 부도시노출액 (EAD)
- 잔존 투자금 및 잔여 보유 기간 동안의 노출 예상액입니다.

## 손실률 (LGD)
- **워터폴 (Waterfall) 구조**: 현금흐름 배분 순서 및 신용보강(Over-collateralization 등) 수준에 의해 결정됩니다.

## 핵심 리스크 요인
- **현금흐름 부족**: 기초자산의 회수 실적 저조
- **트랜치 손실 전이**: 하부 트랜치 소진 후 상부 트랜치 침범 리스크

## 연결
→ [포지션 (Position)](../01_Core_Model/Position.md)  
→ [현금흐름 (Cashflow)](../../DASHBOARD.md)  
→ [부도시노출액 (EAD)](../01_Core_Model/EAD.md)  
→ [손실률 (LGD)](../01_Core_Model/LGD.md)