# 자산유동화증권 (Asset-Backed Securities, ABS) 기초

자산유동화증권(ABS)은 대출, 리스, 매출채권 등 다양한 형태의 자산을 한데 묶어(Pooling) 이를 담보로 발행하는 증권을 의미합니다.

## 1. 유동화 프로세스 (Securitization Process)
유동화는 다음과 같은 메커니즘으로 진행됩니다.
1. **자산보유자 (Originator)**: 자산을 원래 보유하고 있던 주체 (예: 은행, PF 대주).
2. **자산 양도 (Transfer)**: 자산을 **특수목적법인 (Special Purpose Vehicle, SPV)**에 양도하여 파산격리(Bankruptcy Remoteness)를 확보.
3. **트랜칭 (Tranching)**: SPV가 발행하는 증권을 위험도에 따라 선순위(Senior), 중순위(Mezzanine), 후순위(Junior/Equity)로 구분.
4. **신용보강 (Credit Enhancement)**: 상위 트랜치의 신용등급을 높이기 위해 활용되는 기법.

## 2. ABS의 핵심 구성 요소
- **현금흐름 폭포 (Cash Flow Waterfall)**: 기초자산에서 발생하는 현금흐름을 각 트랜치에 배분하는 우선순위 체계.
- **내부 신용보강 (Internal Enhancement)**: 초과 담보(Over-collateralization), 초과 스프레드, 예비 기금 적립.
- **외부 신용보강 (External Enhancement)**: 신용장(L/C), 금융 보증(보험), 자금 보충 약정 (현업).
- **자산관리자 (Servicer)**: 차주로부터 원리금을 수납하고 관리하는 주체.

## 3. 통합 IB 관점에서의 ABS
ABS는 다른 IB 도메인에 '유동성'을 공급하는 엔진 역할을 합니다.
- **NPL 유동화**: 부실채권 포트폴리오를 **NPL ABS**로 전환하여 은행의 비유동 자산을 현금화.
- **PF 유동화**: 인프라나 프로젝트 대출을 기초로 **CLO (Collateralized Loan Obligation)** 등을 발행하여 자금 순환.

## 4. 통합 리스크 프로필 (Unified Risk Profile)
ABS는 기초 자산의 리스크가 트랜치 구조를 통해 재구성된 형태입니다.

- **부도 확률 (PD)**: **기초 자산 부도율** (Underlying default rate)
- **부도 시 손실률 (LGD)**: **트랜치별 손실 흡수력** (선순위일수록 LGD가 낮게 조정됨)
- **부도 시 노출액 (EAD)**: **보유 증권의 평가 가치**

> [!NOTE]
> ABS의 현금흐름 안정성은 [리스크 엔진 기술 사양](file:///home/kbgkim/antigravity/projects/ib_wiki/src/02_Integrated_IB/02_Risk_Engine_Tech_Spec.md) 내 정규화 로직을 통해 상시 모니터링됩니다.

## 5. 관련 문서 (Related Documents)
- **통합 리스크 프레임워크**: [01_Unified_Risk_Framework.md](file:///home/kbgkim/antigravity/projects/ib_wiki/src/02_Integrated_IB/01_Unified_Risk_Framework.md) - PD/LGD/EAD 매핑 이론.
- **통합 시너지 맵**: [Synthesis_Map.md](file:///home/kbgkim/antigravity/projects/ib_wiki/src/02_Integrated_IB/Synthesis_Map.md) - 자산 간 연계 구조.
- **리스크 엔진 기술 사양**: [02_Risk_Engine_Tech_Spec.md](file:///home/kbgkim/antigravity/projects/ib_wiki/src/02_Integrated_IB/02_Risk_Engine_Tech_Spec.md) - 구조화 리스크 정규화 로직.

---
*최종 수정일: 2026-04-11*
