# 부실채권 (Non-Performing Loan, NPL) 기초

부실채권(NPL)은 차주가 원리금 지급 약정을 일정 기간(통상 90일 이상) 이행하지 못한 대출 채권을 의미합니다. IB 영역에서 NPL 관리는 자산의 가치평가, 인수, 그리고 회수 전략(Recovery)에 집중됩니다.

## 1. NPL 건전성 분류
- **요주의**: 연체 발생 우려가 있는 단계.
- **고정 (Sub-standard)**: 연체가 발생했으나 담보가 확실한 단계.
- **회수의문 (Doubtful)**: 담보가 부족하여 전액 회수가 불확실한 단계.
- **추정손실 (Loss)**: 회수 가능성이 거의 없는 단계.

## 2. 가치평가 방법론 (Evaluation)
- **현금흐름 할인법 (Discounted Cash Flow, DCF)**: 미래 회수 예상 금액과 시점을 추정하여 현재 가치로 환산.
- **담보 가치 평가 (Fair Market Value of Collateral)**: 부동산 등 담보물의 경매 낙찰가율 등을 고려한 가치 산정.
- **부도 시 손실률 (Loss Given Default, LGD)**: 부도 발생 시 실제 손실되는 비율 산출 (현업 용어).

## 3. 회수 전략 (Recovery Strategies)
1. **자율 정상화 (Workout)**: 채무자와 협상을 통해 상환 조건을 조정 (현업: 채무 조정).
2. **법적 절차 (Enforcement)**: 경매(Foreclosure), 공매 등을 통한 담보권 행사.
3. **출자 전환 (Debt-to-Equity Swap)**: 부채를 지분으로 전환하여 기업의 주인으로서 직접 경영권 행사 (Equity 영역과 연계).
4. **채권 매각 및 유동화**: 자산관리회사(AMC) 등에 매각하거나 **NPL ABS**를 발행하여 현금화 (ABS 영역과 연계).

## 4. 통합 리스크 프로필 (Unified Risk Profile)
본 자산은 **통합 리스크 관리 체계**에 따라 다음과 같이 정량화됩니다.

- **부도 확률 (PD)**: **100%** (이미 부채 상환 약정이 불이행된 상태로 간주)
- **부도 시 손실률 (LGD)**: **가변적** (담보물의 경매 낙찰률 및 회수 비용에 따라 결정)
- **부도 시 노출액 (EAD)**: **채권 잔액** (원금 + 연체 이자 총액)

> [!NOTE]
> 상세 계산 로직은 [통합 리스크 관리 체계](file:///home/kbgkim/antigravity/projects/ib_wiki/src/02_Integrated_IB/01_Unified_Risk_Framework.md)를 참조하십시오.

---
*최종 수정일: 2026-04-10*
