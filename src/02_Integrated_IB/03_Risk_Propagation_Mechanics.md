# 리스크 전파 및 네트워크 분석 (Risk Propagation Mechanics)

본 문서는 단일 자산의 리스크를 넘어, 글로벌 분산 자산 간의 상관관계와 리스크가 전파되는 **파급 효과 (Ripple Effect)** 분석 모델을 기술합니다.

## 1. 비선형 리스크 전파 모델 (Non-linear Propagation)

전통적인 선형 모델과 달리, 특정 임계점을 넘어서는 급격한 위기 전이(Contagion)를 설명하기 위해 **시그모이드 충격 모델 (Sigmoid Shock Model)**을 적용합니다.

### 1.1 전파 수식
$$Risk_{target} = Risk_{source} \times Weight \times Multiplier(Risk_{source})$$

여기서 증폭 계수($Multiplier$)는 소스 리스크가 특정 임계값(Threshold, 예: 70점)을 넘을 때 급격히 증가하도록 설계되었습니다.

### 1.2 Java 구현 예시 (Logic Snippet)
리스크가 70점을 초과할 경우 비선형적으로 증폭되는 로직입니다.

```java
double multiplier = 1.0;
if (shockAmount > 70) {
    // Sigmoid 함수를 활용한 지수적 증폭
    multiplier = 1.0 + (1.0 / (1.0 + Math.exp(-0.2 * (shockAmount - 85))));
}
```

## 2. 통합 도메인 내 리스크 연결성

IB 통합 도메인(NPL/PF/ABS/Equity)에서는 다음과 같은 경로로 리스크가 전파됩니다.

- **PF 부실 → NPL 전이**: 개발 프로젝트의 현금흐름 차단이 채권 부실로 이어지는 경로 (가중치 높음).
- **공급망 충격 → PF 지연**: 원자재 가격 상승이나 물류 차질이 PF 준공 리스크로 전이.
- **시장 금리 상승 → ABS 수익률 악화**: 조달 비용 상승이 유동화 증권의 스프레드 확대로 전동.

## 3. UI 시각화 및 관제 (Command Center)

- **충격파 효과 (Shockwave Effect)**: 리스크 발생 시 해당 노드에서 원형 충격파가 퍼져나가는 애니메이션을 통해 위기 전이를 묘사.
- **전파 체인 패널 (Propagation Chain)**: 리스크가 어떤 경로를 거쳐 최종 포트폴리오에 도달하는지 실시간 경로 분석 결과 제공.

---
*최종 수정일: 2026-04-10*
*참조: ib-pf-engine/Phase 15*
