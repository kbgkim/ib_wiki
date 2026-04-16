# Global Event Payload 표준 (Event Payload Standard)

## 1. 개요 (Overview)
본 문서는 IB 리스크 엔진 및 분석 시스템에서 사용되는 모든 비즈니스 이벤트의 표준 데이터 규격을 정의합니다. 도메인 간의 일관된 데이터 전송과 인과관계(Correlation) 추적을 위해 모든 이벤트는 아래의 표준 규격을 반드시 준수해야 합니다.

---

## 2. 표준 JSON 스키마 (Canonical Schema)

모든 이벤트 메시지는 아래의 필드를 최상위 계층에 포함해야 하며, 개별 비즈니스 데이터는 `payload` 객체 내에 정의합니다.

```json
{
  "event_id": "UUID",
  "event_type": "string",
  "domain": "PF | ABS | NPL | Equity",
  "entity_id": "string",
  "entity_version": "integer",
  "sequence_number": "integer",
  "timestamp": "ISO8601",
  "correlation_id": "string",
  "source_event_id": "string (optional)",
  "payload": {
    "key": "value"
  }
}
```

---

## 3. 필드 정의 및 제약 조건

| 필드명 | 데이터 타입 | 설명 | 필수 여부 |
| :--- | :--- | :--- | :---: |
| **event_id** | String (UUID) | 각 이벤트 메시지의 유일 식별자 | **MUST** |
| **event_type** | String | 이벤트의 명칭 (예: `LOAN_DEFAULT`, `CASH_TRAP`) | **MUST** |
| **domain** | Enum | 해당 이벤트가 속한 자산 도메인 (PF, ABS, NPL, Equity) | **MUST** |
| **entity_id** | String | 대상 딜(Deal) 또는 포지션(Position)의 ID | **MUST** |
| **entity_version** | Integer | 대상 엔티티의 현재 버전 (동시성 제어용) | **MUST** |
| **sequence_number** | Integer | 시나리오 내에서의 이벤트 발생 순번 | **MUST** |
| **timestamp** | String | 이벤트 발생 시각 (UTC, ISO8601 포맷) | **MUST** |
| **correlation_id** | String | 시나리오 기반 이벤트 흐름 전체를 관통하는 상관 식별자 | **MUST** |
| **source_event_id** | String | 이 이벤트를 트리거한 선행 이벤트의 ID | Optional |
| **payload** | Object | 이벤트별 비즈니스 데이터를 담는 가변 구조체 | **MUST** |

---

## 4. 도메인별 Payload 확장 규격 (예시)

### PF (Project Financing)
```json
"payload": {
  "pre_sale_rate": 0.45,
  "completion_rate": 0.12,
  "developer_credit_grade": "BBB-"
}
```

### ABS (Asset-Backed Securities)
```json
"payload": {
  "tranche_id": "TR-SR-01",
  "dscr": 1.15,
  "collected_cash": 500000000
}
```

---

## 🔗 연결
- [이벤트 핸들러 실행 명세](./EVENT_HANDLER_SPEC.md)
- [표준 온톨로지 정의](../00_Standard_Layer/Core_Definitions.md)
