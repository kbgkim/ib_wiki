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
- **지식 고도화 (Deep-dive)**: ABS 및 NPL 가치평가/회수 전략 실무 지식 내재화 완료 (2026-04-11)

## 4. 자동화 및 워크플로우 (Automation)
- **문서 입수 스킬**: `ib-wiki-ingestion` 스킬을 사용하여 인박스 문서를 자동으로 처리합니다.
- **검증 및 정합성 스킬**: `ib-wiki-verification` 스킬을 통해 위키의 기술적 무결성과 논리적 정합성을 점검합니다.
- **인제션 로그**: 모든 문서 처리 내역은 [INGESTION_LOG.md](INGESTION_LOG.md)에 기록됩니다.
- **검증 보고서**: 정기 검증 결과는 [VERIFICATION_REPORT.md](VERIFICATION_REPORT.md)에 공시됩니다.

## 5. 향후 과제 (Next Steps)
- `src/00_Inbox`에 추가되는 기존 문서들의 분석 및 위키 편입
- 각 자산군(Verticals)별 상세 수익 모델 및 현금흐름 시뮬레이션 로직 정리
- 리스크 지표 간 상관관계(Correlation Matrix) 분석 심화

---
*Created: 2026-04-10*
