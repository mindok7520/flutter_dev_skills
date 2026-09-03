# 공식 출처와 검증 범위

UI/UX·상태관리·아키텍처·성능·셰이더·애니메이션 지침의 후속 조사는 [저장소 조사와 적용 기록](REFERENCE_RESEARCH.md)에 있다. 확인한 실제 파일과 커밋, 적용한 개념 및 적용하지 않은 규칙을 구분한다.

확인일: **2026-09-03**. 아래 자료에서 기술 사실과 작업 설계의 근거를 확인했다. 문서의 기본 아키텍처·예산·브랜치 방식은 이 저장소가 선택한 권장안이며, 모든 공식 문서가 강제하는 규칙은 아니다.

## 버전 예시

| 항목 | 확인한 값 | 적용 범위와 근거 |
| --- | --- | --- |
| Flutter | 3.47.2 stable | [공식 SDK archive](https://docs.flutter.dev/install/archive), [Windows 배포 메타데이터](https://storage.googleapis.com/flutter_infra_release/releases/releases_windows.json) |
| Dart | 3.13.2 | 위 Flutter 배포 메타데이터에 포함된 SDK |
| flutter_lints | 6.0.0 | [공식 패키지 페이지](https://pub.dev/packages/flutter_lints), 대상 앱의 기존 버전 우선 |
| PyYAML | 6.0.3 | [패키지 메타데이터](https://pypi.org/pypi/PyYAML/json), 자료 검증용 requirements-dev에만 사용 |
| markdown-it-py / mdurl | 4.2.0 / 0.1.2 | [파서 메타데이터](https://pypi.org/pypi/markdown-it-py/json), [URL 처리 메타데이터](https://pypi.org/pypi/mdurl/json). 제목·참조형 링크를 정규식 대신 Markdown 문법대로 검증하기 위한 개발 의존성 |
| FVM 설정 | `.fvmrc`의 `flutter` 필드 | [공식 설정 문서](https://fvm.app/documentation/getting-started/configuration) |

이 저장소 루트에는 Flutter 매니페스트나 SDK 핀이 없다. 위 버전은 선택형 템플릿을 작성할 때 확인한 예시다. 대상 앱의 현재 매니페스트·잠금·도구 체인을 조사한 뒤 적용한다. 최신 버전과 사용 버전·지원 종료·보안 영향·이전 비용을 구분한다.

## AI 작업과 프롬프트

- [OpenAI Harness engineering](https://openai.com/index/harness-engineering/): 짧은 지침 지도와 저장소 안의 설계·계획·자동 검증을 결합하는 운영 사례를 참고했다. 해당 조직의 성과 수치를 이 베이스의 보장 성능으로 사용하지 않는다.
- [Codex 지침](https://developers.openai.com/codex/guides/agents-md): 저장소 지침의 역할을 참고했다. 작성 시 로컬 openai-docs 도구가 가져온 공식 Codex manual의 지침·스킬 섹션도 확인했다.
- [스킬 작성](https://developers.openai.com/plugins/build/skills): 작업 트리거·입력·절차·결과·도구 경계를 스킬 단위로 구분하는 데 사용했다.
- [Anthropic 장기 작업](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents): 새 세션에서 진행 파일·Git·검증으로 작업을 복구하는 방식을 참고했다.
- [Anthropic 프롬프트 지침](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices): 명확한 목표·문맥·제약·예시·출력 형식에 기반해 프롬프트를 구성했다. 원문을 복사한 프롬프트 모음은 아니다.
- [GitHub Copilot 지침](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions): 저장소와 경로별 지침의 구분을 참고했다. 실제 IDE·에이전트의 자동 인식 범위는 해당 버전에서 확인한다.

## Flutter·Dart 설계와 품질

- [앱 아키텍처](https://docs.flutter.dev/app-architecture/guide): UI·상태·데이터 책임 분리와 필요한 경우의 도메인 계층.
- [성능](https://docs.flutter.dev/perf/best-practices): 레이아웃·렌더링·지연 생성의 비용과 측정 필요성.
- [반응형·적응형 UI](https://docs.flutter.dev/ui/adaptive-responsive): 공간과 사용 맥락에 맞는 UI 구성.
- [테스트](https://docs.flutter.dev/testing/overview): 단위·위젯·통합 테스트의 역할과 한계.
- [Wasm](https://docs.flutter.dev/platform-integration/web/wasm): 컴파일·패키지 호환·브라우저 조건. 실제 앱의 채택 여부와 헤더 구성은 별도로 검증한다.
- [Dart isolate](https://dart.dev/language/isolates): 실행·메모리 격리와 메시지 통신.
- [널 안전성](https://dart.dev/null-safety): 타입에서 값 부재를 표현하는 원칙.
- [pub outdated](https://dart.dev/tools/pub/cmd/pub-outdated): 버전 업데이트 조사이며 취약점 검사와 구분한다.

## 보안·접근성·수익화

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): 접근성 검토 기준. 자동 검사만으로 준수나 인증을 선언하지 않는다.
- [OWASP 모바일 보안](https://owasp.org/www-project-mobile-app-security/): 모바일 위협·검증 체계를 참고한다.
- [GitHub Actions 보안](https://docs.github.com/en/actions/reference/security/secure-use): 최소 권한·비신뢰 코드·액션 버전 고정 정책.
- [OSV](https://google.github.io/osv.dev/): 알려진 취약점 데이터 조회. 결과가 비어 있어도 안전의 완전한 증명은 아니다.
- [Apple 심사 지침](https://developer.apple.com/app-store/review/guidelines/): 실제 국가·상품·배포 경로별 결제·광고·개인정보 요구를 출시 직전에 확인한다.
- [Google Play 결제 정책](https://support.google.com/googleplay/android-developer/answer/10281818): 디지털·실물 상품과 정책 적용·예외 조건을 구분한다.
- [Play Billing 보안](https://developer.android.com/google/play/billing/security): 서버에서 구매를 검증하고 거래·권리를 보호하는 근거.
- [AdMob Flutter 동의](https://developers.google.com/admob/flutter/privacy): 동의 상태 확인과 광고 요청 가능 상태의 연결을 참고한다.

정책·법률·지원 상태는 변경될 수 있다. 관할과 제품이 정해지지 않은 이 자료 저장소에서는 특정 제품의 법적 준수·심사 통과를 확정하지 않는다. 도입 프로젝트는 확인 날짜·공식 링크·실제 적용 조건·검증 증거를 자체 기록한다.
