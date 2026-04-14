# 딜 이벤트 모델 (Deal Event Model)

## 목적
딜(Deal) 상태 변화가 리스크에 미치는 동적 영향도를 정의합니다.

---

## 개념

**Event**는 포지션(Position)과 현금흐름(Cashflow)을 변화시키며, 결과적으로 리스크 산출 결과 값을 변동시킵니다.

---

## 구조

**Deal Event**  
 → **Position** 상태 변화  
 → **Cashflow** 스케줄/실적 변화  
 → **Risk** 값 재산출  

---

## 주요 이벤트 (Core Events)

- **Drawdown** (대출 실행): Exposure 및 EAD 증가
- **Repayment** (상환): Exposure 감소
- **Delinquency** (연체): Cashflow Shortfall 발생 → LGD 할증 고려
- **Default** (부도): PD 100% 적용 및 회수(Recovery) 프로세스 진입
- **Prepayment** (조기상환): 미래 현금흐름의 소멸 및 재투자 리스크 발생

---

## 설계 원칙

- **이벤트 기반 추적**: 데이터의 모든 변화는 명시적인 Event로 기록되어야 합니다.
- **실시간 반영**: Event 발생 → 물리적 데이터 변경 → 리스크 엔진 재작동 순으로 연동됩니다.

---

## 연결

→ [포지션 (Position)](../../01_Core_Model/Position.md)  
→ [현금흐름 (Cashflow)](../../01_Core_Model/Cashflow.md)  
→ [포지션 스키마 (Position Schema)](../01_Schemas/Position_Schema.md)