# 개발 문서 지도

필요한 분야만 선택해서 읽는다. 이 문서들은 새 Flutter 프로젝트에 적용할 개발·운영 정책이다. 앱 코드·플랫폼 디렉터리·도구 명령은 대상 프로젝트의 구성이고, 이 자료 저장소의 앱 구현을 뜻하지 않는다.

## 빠른 시작

[작업 규칙](../AGENTS.md) → [프로젝트 정의](../PROJECT.md) → [세션 복구](agent/CONTEXT_RECOVERY.md) → 관련 분야 문서 → [실행 계획](exec-plans/TEMPLATE.md) → 검증·인계 순으로 진행한다.

[공식 출처](SOURCES.md)에서 버전·정책 확인 날짜를 확인한다. 템플릿 예시를 대상 앱의 확정된 설계·지원·성능 수치로 간주하지 않는다.

## adr

- [설계 결정 템플릿](adr/ADR_TEMPLATE.md)
- [설계 결정 기록](adr/README.md)

## agent

- [AI 작업 보안](agent/AGENT_SECURITY.md)
- [자율 실행 범위](agent/AUTONOMY_POLICY.md)
- [문맥 관리](agent/CONTEXT_MANAGEMENT.md)
- [문맥 복구](agent/CONTEXT_RECOVERY.md)
- [문서 갱신 정책](agent/DOCUMENTATION_UPDATE_POLICY.md)
- [작업 실패 복구](agent/FAILURE_RECOVERY.md)
- [작업 인계](agent/HANDOFF_PROTOCOL.md)
- [AI 운영 모델](agent/OPERATING_MODEL.md)
- [AI 작업 안내](agent/README.md)
- [세션 시작](agent/SESSION_BOOTSTRAP.md)
- [작업 실행 규약](agent/TASK_EXECUTION_PROTOCOL.md)
- [도구 사용 정책](agent/TOOL_POLICY.md)
- [AI 검증 규약](agent/VERIFICATION_PROTOCOL.md)

## analytics

- [분석 전략](analytics/ANALYTICS_STRATEGY.md)
- [충돌 보고](analytics/CRASH_REPORTING.md)
- [이벤트 스키마](analytics/EVENT_SCHEMA.md)
- [운영 성능 지표](analytics/PERFORMANCE_METRICS.md)
- [개인정보를 최소화한 분석](analytics/PRIVACY_SAFE_ANALYTICS.md)

## architecture

- [Flutter 앱 구조](architecture/APP_ARCHITECTURE.md)
- [캐시 전략](architecture/CACHE_STRATEGY.md)
- [데이터 흐름](architecture/DATA_FLOW.md)
- [의존성 주입](architecture/DEPENDENCY_INJECTION.md)
- [의존성 규칙](architecture/DEPENDENCY_RULES.md)
- [도메인 계층](architecture/DOMAIN_LAYER.md)
- [오류 처리 구조](architecture/ERROR_HANDLING.md)
- [기능 플래그](architecture/FEATURE_FLAGS.md)
- [로컬 저장소](architecture/LOCAL_STORAGE.md)
- [모듈 구조](architecture/MODULE_STRUCTURE.md)
- [네이티브 연동](architecture/NATIVE_INTEGRATION.md)
- [내비게이션과 라우팅](architecture/NAVIGATION_ROUTING.md)
- [네트워크 계층](architecture/NETWORKING.md)
- [관측 가능한 아키텍처](architecture/OBSERVABILITY.md)
- [오프라인 전략](architecture/OFFLINE_STRATEGY.md)
- [아키텍처 개요](architecture/OVERVIEW.md)
- [플랫폼 추상화](architecture/PLATFORM_ABSTRACTION.md)
- [저장소 패턴](architecture/REPOSITORY_PATTERN.md)
- [상태 관리](architecture/STATE_MANAGEMENT.md)
- [웹 아키텍처](architecture/WEB_ARCHITECTURE.md)

## design

- [접근성 기준](design/ACCESSIBILITY.md)
- [애니메이션과 모션](design/ANIMATION_MOTION.md)
- [화면 분기 기준](design/BREAKPOINTS.md)
- [컴포넌트 설계](design/COMPONENT_GUIDELINES.md)
- [다크 모드](design/DARK_MODE.md)
- [디자인 시스템](design/DESIGN_SYSTEM.md)
- [디자인 토큰](design/DESIGN_TOKENS.md)
- [입력 방식 지원](design/KEYBOARD_MOUSE_TOUCH.md)
- [국제화·현지화](design/LOCALIZATION.md)
- [반응형·적응형 UI](design/RESPONSIVE_ADAPTIVE.md)
- [테마 설계](design/THEMING.md)
- [화면 구성 원칙](design/UI_GUIDELINES.md)
- [사용 경험 원칙](design/UX_GUIDELINES.md)

## engineering

- [비동기와 동시성](engineering/ASYNC_CONCURRENCY.md)
- [읽기 쉬운 코드](engineering/CLEAN_CODE.md)
- [Dart·Flutter 스타일](engineering/DART_FLUTTER_STYLE.md)
- [사용 중단 정책](engineering/DEPRECATION_POLICY.md)
- [개발 원칙](engineering/DEVELOPMENT_PRINCIPLES.md)
- [엔지니어링 오류 정책](engineering/ERROR_POLICY.md)
- [불변성과 소유권](engineering/IMMUTABILITY.md)
- [격리 실행](engineering/ISOLATES.md)
- [로그 작성](engineering/LOGGING.md)
- [널 안전성](engineering/NULL_SAFETY.md)
- [패키지 도입 정책](engineering/PACKAGE_POLICY.md)

## exec-plans

- [실행 계획](exec-plans/README.md)
- [실행 계획 템플릿](exec-plans/TEMPLATE.md)

## monetization

- [광고 배치 정책](monetization/AD_PLACEMENT_POLICY.md)
- [광고 개인정보 동의](monetization/AD_PRIVACY_CONSENT.md)
- [광고 연동](monetization/ADS.md)
- [사용 권리](monetization/ENTITLEMENTS.md)
- [수익화 아키텍처](monetization/MONETIZATION_ARCHITECTURE.md)
- [수익화 검증 표](monetization/MONETIZATION_TEST_MATRIX.md)
- [결제 보안](monetization/PAYMENT_SECURITY.md)
- [결제 연동](monetization/PAYMENTS.md)
- [구매 복원](monetization/PURCHASE_RESTORATION.md)
- [거래 검증](monetization/RECEIPT_VERIFICATION.md)
- [스토어 정책 확인](monetization/STORE_POLICY.md)
- [구독 상태 관리](monetization/SUBSCRIPTIONS.md)

## operations

- [백업과 복원](operations/BACKUP_RECOVERY.md)
- [CI와 출시 자동화](operations/CI_CD.md)
- [설정 관리](operations/CONFIGURATION.md)
- [재해 복구](operations/DISASTER_RECOVERY.md)
- [환경 분리](operations/ENVIRONMENTS.md)
- [운영 관측](operations/OBSERVABILITY.md)

## performance

- [빌드 크기 예산](performance/BUILD_SIZE_BUDGET.md)
- [이미지와 자산 최적화](performance/IMAGE_ASSET_OPTIMIZATION.md)
- [메모리 관리](performance/MEMORY_GUIDE.md)
- [네트워크 성능](performance/NETWORK_PERFORMANCE.md)
- [성능 예산](performance/PERFORMANCE_BUDGET.md)
- [성능 개선 절차](performance/PERFORMANCE_GUIDE.md)
- [성능 분석 가이드](performance/PROFILING_GUIDE.md)
- [위젯 재빌드 개선](performance/REBUILD_OPTIMIZATION.md)
- [렌더링 성능](performance/RENDERING_PERFORMANCE.md)
- [앱 시작 성능](performance/STARTUP_PERFORMANCE.md)
- [Wasm 선택 전략](performance/WASM_STRATEGY.md)
- [웹 성능](performance/WEB_PERFORMANCE.md)

## privacy

- [개인정보·정책 점검](privacy/COMPLIANCE_CHECKLIST.md)
- [동의 관리](privacy/CONSENT_MANAGEMENT.md)
- [데이터 목록](privacy/DATA_INVENTORY.md)
- [보관과 삭제](privacy/DATA_RETENTION.md)
- [개인정보 아키텍처](privacy/PRIVACY_ARCHITECTURE.md)
- [추적 정책](privacy/TRACKING_POLICY.md)

## product

- [기능 목록과 상태](product/FEATURE_CATALOG.md)
- [비기능 요구사항](product/NON_FUNCTIONAL_REQUIREMENTS.md)
- [제품 비전](product/PRODUCT_VISION.md)
- [요구사항 관리](product/REQUIREMENTS.md)
- [성공 지표](product/SUCCESS_METRICS.md)
- [사용자 여정](product/USER_JOURNEYS.md)
- [사용자 유형](product/USER_PERSONAS.md)

## release

- [Android 출시](release/ANDROID_RELEASE.md)
- [iOS 출시](release/IOS_RELEASE.md)
- [출시 후 점검](release/POST_RELEASE_CHECKLIST.md)
- [출시 체크리스트](release/RELEASE_CHECKLIST.md)
- [스토어 제출](release/STORE_SUBMISSION.md)
- [웹 출시](release/WEB_RELEASE.md)

## security

- [인증](security/AUTHENTICATION.md)
- [권한 부여](security/AUTHORIZATION.md)
- [암호 기술 사용](security/CRYPTOGRAPHY.md)
- [데이터 분류](security/DATA_CLASSIFICATION.md)
- [데이터 보호](security/DATA_PROTECTION.md)
- [의존성 보안](security/DEPENDENCY_SECURITY.md)
- [보안 사고 대응](security/INCIDENT_RESPONSE.md)
- [모바일 보안](security/MOBILE_SECURITY.md)
- [통신 보안](security/NETWORK_SECURITY.md)
- [플랫폼 저장소 보안](security/PLATFORM_STORAGE_SECURITY.md)
- [비밀 관리](security/SECRET_MANAGEMENT.md)
- [안전한 코드 작성](security/SECURE_CODING.md)
- [보안 아키텍처](security/SECURITY_ARCHITECTURE.md)
- [보안 검증 체계](security/SECURITY_TESTING.md)
- [세션 관리](security/SESSION_MANAGEMENT.md)
- [공급망 보안](security/SUPPLY_CHAIN_SECURITY.md)
- [위협 모델](security/THREAT_MODEL.md)
- [웹 보안](security/WEB_SECURITY.md)

## testing

- [접근성 검증](testing/ACCESSIBILITY_TESTING.md)
- [광고 테스트](testing/AD_TESTING.md)
- [플랫폼 검증 표](testing/CROSS_PLATFORM_MATRIX.md)
- [전체 흐름 테스트](testing/E2E_TESTING.md)
- [시각 회귀 테스트](testing/GOLDEN_TESTING.md)
- [통합 테스트](testing/INTEGRATION_TESTING.md)
- [결제 테스트](testing/PAYMENT_TESTING.md)
- [성능 테스트](testing/PERFORMANCE_TESTING.md)
- [병합 품질 기준](testing/QUALITY_GATES.md)
- [기능별 보안 테스트](testing/SECURITY_TESTING.md)
- [테스트 데이터 정책](testing/TEST_DATA_POLICY.md)
- [테스트 계층](testing/TEST_PYRAMID.md)
- [테스트 전략](testing/TEST_STRATEGY.md)
- [단위 테스트](testing/UNIT_TESTING.md)
- [위젯 테스트](testing/WIDGET_TESTING.md)

## workflow

- [브랜치 전략](workflow/BRANCHING_STRATEGY.md)
- [코드 리뷰](workflow/CODE_REVIEW.md)
- [커밋 규칙](workflow/COMMIT_CONVENTION.md)
- [완료 기준](workflow/DEFINITION_OF_DONE.md)
- [착수 기준](workflow/DEFINITION_OF_READY.md)
- [개발 전체 절차](workflow/DEVELOPMENT_WORKFLOW.md)
- [Git 작업 절차](workflow/GIT_WORKFLOW.md)
- [긴급 수정 절차](workflow/HOTFIX_WORKFLOW.md)
- [이슈 관리](workflow/ISSUE_WORKFLOW.md)
- [PR 절차](workflow/PULL_REQUEST_WORKFLOW.md)
- [릴리스 절차](workflow/RELEASE_WORKFLOW.md)
- [되돌림 절차](workflow/ROLLBACK_WORKFLOW.md)
- [버전 관리](workflow/VERSIONING.md)
