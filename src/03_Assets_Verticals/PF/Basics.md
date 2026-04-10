# 프로젝트 파이낸싱 (Project Finance, PF) 기초

프로젝트 파이낸싱(PF)은 특정 프로젝트(인프라, 산업 단지, 발전소 등)의 사업성을 기반으로 자금을 조달하는 금융 기법입니다. 기업의 전반적인 신용이나 담보보다는 프로젝트 자체의 미래 현금흐름을 상환 재원으로 삼는 것이 특징입니다.

## 1. PF의 구조적 특징
- **특수목적법인 (Special Purpose Vehicle, SPV)**: 프로젝트 수행을 위해 별도의 독립된 법인을 설립.
- **부외금융 (Off-Balance Sheet)**: 프로젝트의 부채가 사업주의 재무제표에 직접 계상되지 않음.
- **비소구 / 제한적 소구 (Non-Recourse / Limited Recourse)**: 프로젝트 부실 시 대주(Lenders)가 사업주의 다른 자산에 대해 청구권을 갖지 않거나 매우 제한적으로 가짐 (현업 핵심).

## 2. 주요 리스크 관리 (Risk Management)
- **건설 리스크 (Construction Risk)**: 준공 지연이나 공사비 초과 발생 (E-PC 계약 및 책임준공 확약으로 완화).
- **운영 리스크 (Operation Risk)**: 준공 후 운영 효율성 저하나 기술적 결함.
- **수요 리스크 (Market/Demand Risk)**: 예상보다 낮은 매출 (수익형 민자사업 등에서 핵심).
- **금융 리스크 (Financial Risk)**: 금리 변동 및 환율 위험.

## 3. 현금흐름 모델링 및 지표
- **부채상환계수 (Debt Service Coverage Ratio, DSCR)**: 원리금 상환 능력을 나타내는 핵심 지표 (현업 목표 1.2배 이상).
- **차입금상환계수 (Loan Life Coverage Ratio, LLCR)**: 전체 대출 기간 동안의 현금흐름 안정성 평가.
- **현금흐름 폭포 (Cash Flow Waterfall)**: 
    1. 운영비용 (OpEx) 지불.
    2. 선순위 원리금 상환.
    3. 예비비 적립.
    4. 후순위 및 자본금 배당.

## 4. 통합 리스크 프로필 (Unified Risk Profile)
PF 자산은 프로젝트의 단계별 성공 확률을 기반으로 리스크가 측정됩니다.

- **부도 확률 (PD)**: **프로젝트 실패 확률** (준공 전: 건설 지연 리스크 / 준공 후: 운영 현금흐름 리스크)
- **부도 시 손실률 (LGD)**: **담보 살리기 가치** (부지 가치 및 기투자 자산의 청산 가치)
- **부도 시 노출액 (EAD)**: **대출 실행 잔액** 및 향후 투입 예정 금액

> [!NOTE]
> PF 리스크는 특정 임계점(Threshold) 통과 시 전이 속도가 빨라지므로 [리스크 전파 매커니즘](file:///home/kbgkim/antigravity/projects/ib_wiki/src/02_Integrated_IB/03_Risk_Propagation_Mechanics.md) 연구가 필수적입니다.

## 5. 관련 문서 (Related Documents)
- **통합 리스크 프레임워크**: [01_Unified_Risk_Framework.md](file:///home/kbgkim/antigravity/projects/ib_wiki/src/02_Integrated_IB/01_Unified_Risk_Framework.md) - PD/LGD/EAD 매핑 이론.
- **통합 시너지 맵**: [Synthesis_Map.md](file:///home/kbgkim/antigravity/projects/ib_wiki/src/02_Integrated_IB/Synthesis_Map.md) - 자산 간 연계 구조.
- **리스크 전파 매커니즘**: [03_Risk_Propagation_Mechanics.md](file:///home/kbgkim/antigravity/projects/ib_wiki/src/02_Integrated_IB/03_Risk_Propagation_Mechanics.md) - 비선형 충격 전이 모델.

---
*최종 수정일: 2026-04-11*
