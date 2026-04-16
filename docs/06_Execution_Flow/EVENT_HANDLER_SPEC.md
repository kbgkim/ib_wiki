# 이벤트 핸들러 실행 명세 (Event Handler Specification)

## 1. 개요 (Overview)
본 문서는 각 비즈니스 이벤트가 수신되었을 때 리스크 엔진이 수행해야 하는 논리적 행동 지침(Handler Logic)을 정의합니다. 모든 핸들러는 **상태 변경, 데이터 업데이트, 후행 이벤트 트리거**의 3단계를 수행합니다.

---

## 2. 공통 핸들러 로직 (Common Handler Logic)

모든 핸들러는 비즈니스 로직 실행 전 반드시 다음의 **4대 안정성 가드(Safety Guards)**를 순차적으로 통과해야 합니다.

1.  **Guard 1: Idempotency (멱등성 검증)**
    - `event_id`가 `Processed_Event_Store`에 존재하는지 확인.
    - 존재 시: **Ignore & Return Success (NO-OP)**.
2.  **Guard 2: Concurrency Control (동시성 제어)**
    - `Payload.entity_version`과 현재 시스템의 `Entity.version` 비교.
    - `Mismatch` 시: **Reject (Stale Update)** 및 Error 큐 전송.
3.  **Guard 3: Ordering Validation (순서 검증)**
    - `Payload.sequence_number`가 기대되는 차기 순번인지 확인.
    - `Out-of-Order` 시: 정책(`Buffer` 또는 `Discard`)에 따라 처리.
4.  **Guard 4: Failure & Recovery (실패 처리)**
    - 로직 실행 중 예외 발생 시 `Retry_Policy` 적용.
    - 최종 실패 시 원본 페이로드를 `Dead_Letter_Queue(DLQ)`로 전송.
5.  **Finalization**: `Audit Logging` 및 `Entity.version + 1` 업데이트.

---

## 3. 도메인별 핵심 핸들러 상세 (Domain Handlers)

### [PF] Project Financing
| Event | Handler Logic |
| :--- | :--- |
| **LOAN_APPROVED** | 1. `Deal_State` -> `Approved`<br>2. `Exposure_Limit` 활성화<br>3. `NextTrigger`: `FUNDING_EXECUTED` (자금 인출 조건 대기) |
| **FUNDING_EXECUTED**| 1. `Deal_State` -> `ACTIVE:CONSTRUCTION`<br>2. 원리금 상환 스케줄 생성<br>3. `NextTrigger`: 정기 `MONITORING` 이벤트 생성 |
| **PRE_SALE_SHORTFALL**| 1. `Risk_Level` 상향 (PD 증가)<br>2. `Cash_Waterfall` 루틴 점검<br>3. **Condition**: 분양률 < 30% 시 `PROJECT_FAILURE` 트리거 |
| **PROJECT_FAILURE** | 1. `Deal_State` -> `DELINQUENT`<br>2. 모든 `Inflow` Suspended 전환<br>3. `NextTrigger`: `LOAN_DEFAULT` 전이 체크 |
| **WORKOUT_END** | 1. `Deal_State` -> `CLOSED` (Restured)<br>2. 리스트럭처링 결과 반영 |

---

### [ABS] Asset-Backed Securities
| Event | Handler Logic |
| :--- | :--- |
| **SECURITIES_ISSUED**| 1. `Deal_State` -> `ACTIVE`<br>2. 트랜치별 원리금 상환 장부 생성<br>3. `True_Sale` 확정 로그 기록 |
| **CASH_TRAP_TRIGGER**| 1. 매점(Trap) 엔진 활성화<br>2. 후순위 배당 즉시 중단<br>3. `Reserve_Balance` 적립 로직 실행 |
| **CASH_TRAP_RELEASE**| 1. 매점(Trap) 엔진 비활성화<br>2. 정상 Waterfall 상환 체계 복구<br>3. `Deal_State` -> `ACTIVE` 복귀 |
| **REDEMPTION_FINAL** | 1. SPV 청산 상태 변경<br>2. 잔여 현금 정산 및 딜 종료 |

---

### [NPL] Non-Performing Loan
| Event | Handler Logic |
| :--- | :--- |
| **PORTFOLIO_ACQUIRED**| 1. 매입 원가(`OPB`) 및 취득가 장부 등록<br>2. `PD` 100% 고정<br>3. `NextTrigger`: `ASSET_VALUED` (실사 일정 예약) |
| **AUCTION_SUCCESSFUL**| 1. 배당금 유입 처리<br>2. 해당 담보 포지션 소멸<br>3. `Deal_State` -> `CLOSED` (Recovered) |
| **RESOLUTION_PATH_SET**| 1. 담보 LTV에 따른 회수 경로 확정 (`LIQUIDATION` vs `WORKOUT`) |

---

### [Equity] Unlisted Investment
| Event | Handler Logic |
| :--- | :--- |
| **MTM_SHOCK_EVENT** | 1. 공정가치 재평가 (Valuation Down)<br>2. `Valuation_Multiple` 하향 조정<br>3. **Condition**: 가치 손상 50% 이상 시 `IMPAIRMENT_FIXED` 트리거 |
| **EXIT_SUCCESS** | 1. 지분 매수자 확정 로직 실행<br>2. 투자 원금 및 자본이득(Gain) 정산<br>3. `Deal_State` -> `CLOSED` |

---

## 4. 트리거 규칙 요약 (Next Event Triggers)

모든 핸들러는 성공적인 상태 변경 후 다음의 규칙에 따라 후행 이벤트를 스케줄링합니다.
- `Event(Source) + Threshold(Logic) = Event(Destination)`
- 상세 규칙은 각 자산별 `Lifecycle.md` 문서의 트리거 섹션을 참조하십시오.

---

## 🔗 연결
- [글로벌 이벤트 페이로드 표준](./EVENT_PAYLOAD_STANDARD.md)
- [통합 리스크 전파 명세](../02_Integrated_IB/Synthesis_Map.md)
