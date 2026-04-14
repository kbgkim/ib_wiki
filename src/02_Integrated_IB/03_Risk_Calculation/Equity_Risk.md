# 지분 리스크 (Equity Risk)

지분 투자(Equity) 기반 자산의 리스크를 측정하는 모델입니다.

## 기본 구조 (Market Risk Approach)
주식 또는 지분의 가치 변동성을 기반으로 손실을 산정합니다.

- **[포지션 (Position)](../01_Core_Model/Position.md)**
  - **[시장가치 (Market Value)](../01_Core_Model/Market_Value.md)**
    - **[변동성 (Volatility)](../01_Core_Model/Volatility.md)** (Shock)
      - **Loss (손실액)**

**$$Loss = Market Value \times Shock$$**

---

## 통합 프레임워크 적용 (Credit Approach)
지분 자산을 부도 확률 기반의 Credit 모델로 해석할 경우 다음과 같이 매핑합니다.

- **PD (부도 확률)**: 기업의 파산 또는 가치 영구 훼손 확률
- **LGD (손실률)**: **100% 가정** (지분의 후순위성으로 인해 부도 시 전액 손실로 간주)
- **EAD (익스포저)**: 현재의 시장 가치 또는 투자 원금

---

## 특징
- **변동성 기반**: 주로 시장 가격의 하락 충격(Shock)을 통해 측정합니다.
- **후순위성**: 채권 대비 변제 순위가 낮아 리스크 가중치가 높습니다.

## 연결
→ [시장가치 (Market Value)](../01_Core_Model/Market_Value.md)  
→ [변동성 (Volatility)](../01_Core_Model/Volatility.md)