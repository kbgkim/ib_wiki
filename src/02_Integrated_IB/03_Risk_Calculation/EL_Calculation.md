# 기대손실 계산 (Expected Loss Calculation)

## 공식
**$$EL = PD \times LGD \times EAD$$**

- **PD**: 부도 확률 (Probability of Default)
- **LGD**: 부도 시 손실률 (Loss Given Default)
- **EAD**: 부도 시 익스포저 (Exposure at Default)

> [!NOTE]
> **NPL(부실채권) 특이사항**
> NPL은 이미 부도 상태($PD=100\%$)이므로 실질적인 계산은 **$EL = EAD \times LGD$**로 수행됩니다.

## 계산 흐름 (Pipeline)
1. **[포지션 (Position)](../01_Core_Model/Position.md)**: 기초 데이터 로드 및 단위 확정
2. **[노출액 (Exposure)](../01_Core_Model/Exposure.md) & [PD](../01_Core_Model/PD.md)**: 현재 노출액 및 부도 확률 산출
3. **[부도시노출액 (EAD)](../01_Core_Model/EAD.md)**: 부도 시점의 총 위험액 산정
4. **[손실률 (LGD)](../01_Core_Model/LGD.md)**: 담보 가치 기반 손실 비중 결정
5. **기대손실 (EL)**: 최종 리스크 값 산정

## 연결
→ [포지션 (Position)](../01_Core_Model/Position.md)  
→ [부도시노출액 (EAD)](../01_Core_Model/EAD.md)  
→ [손실률 (LGD)](../01_Core_Model/LGD.md)