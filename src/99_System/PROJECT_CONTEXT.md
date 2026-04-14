# IB Wiki Project Context Summary

이 문서는 Antigravity(AI)가 다음 세션에서도 프로젝트의 맥락을 즉시 파악할 수 있도록 돕기 위한 요약본입니다.

## 1. 프로젝트 개요 (Project Overview)
- **명칭**: IB 통합 위키 (Investment Banking Integrated Wiki)
- **핵심 도메인**: **NPL**, **PF**, **Equity**, **ABS** 통합 관리
- **목적**: 자산별 현금흐름(Cashflow)과 리스크를 통합하여 관리하는 개인용 지식 라이브러리

## 2. 문서 작성 가이드라인 (Style Guide)
- **기본 언어**: 한국어 (한글)
- **영문 병기**: 전문 용어는 `한글 (Full English Name, Abbreviation)` 형식 사용
- **현업 용어**: 금융 실무 용어는 **`용어`** (현업) 처럼 볼드체로 강조

## 3. 현재까지 진행 상황 (Current Progress)
- **기반 구축**: 프로젝트 폴더 구조 스캐폴딩 및 Git/GitHub 원격 저장소 동기화 완료
- **리스크 모델 통합**: 
  - 공통 기대 손실 (Expected Loss, EL) 프레임워크 구축 ($PD \times LGD \times EAD$)
  - 리스크 점수 정규화 엔진 및 비선형 리스크 전파 모델(Sigmoid) 기술 스펙 내재화
- **인박스(Inbox) 시스템**: 외부 문서 입수를 위한 `src/00_Inbox` 폴더 및 아카이브 시스템 구축
- **지식 고도화 (Deep-dive)**: 전 자산군(ABS/PF/NPL/Equity) 고도화 및 모든 자산군 딜 라이프사이클/북킹 실무 가이드 구축 완료
- **지능형 시각화 (Intelligence)**: 4대 자산의 리스크/수익 현황을 통합 관제하는 **통합 리스크 대시보드(DASHBOARD.md)** 구축 완료 (2026-04-11)

## 4. 자동화 및 워크플로우 (Automation)
- **문서 입수 스킬**: `ib-wiki-ingestion` 스킬을 사용하여 인박스 문서를 자동으로 처리합니다.
- **검증 및 정합성 스킬**: `ib-wiki-verification` 스킬을 통해 위키의 기술적 무결성과 논리적 정합성을 점검합니다.
- **인제션 로그**: 모든 문서 처리 내역은 [INGESTION_LOG.md](INGESTION_LOG.md)에 기록됩니다.
- **검증 보고서**: 정기 검증 결과는 [VERIFICATION_REPORT.md](VERIFICATION_REPORT.md)에 공시됩니다.

## 5. 향후 고도화 로드맵 (Evolution Roadmap)
- **실행 가능한 리스크 시뮬레이터 (Simulator)**: $EL = PD \times LGD \times EAD$ 산출 로직을 파이썬 코드로 구현하여 실제 데이터 계산 및 대시보드 연동 기능 추가.
- **통합 스트레스 테스트 (Stress Test)**: "건설사 부도 -> PF 부실 -> NPL 공급 확대"와 같은 자산 간 리스크 전이 시나리오 설계 및 시각화.
- **지능형 인박스 정교화 (Auto-Ingestion)**: 외부 리서치 리포트나 뉴스 분석을 통한 대시보드 지표 자동 업데이트 파이프라인 완성.

---
*Created: 2026-04-10*
