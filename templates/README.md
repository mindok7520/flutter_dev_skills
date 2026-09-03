# 템플릿 도입 안내

이 디렉터리에는 **대상 Flutter 프로젝트에 선택적으로 복사하거나 통합하는 설정과 개발 도구**가 있다. 앱 코드·플랫폼 프로젝트·완성된 배포 파이프라인을 포함하지 않는다. 기존 앱의 요구·도구 체인·설정이 우선이다.

## 도입 순서

1. 대상 SDK로 별도 Flutter 프로젝트를 만들거나 기존 프로젝트를 준비한다.
2. 루트의 `scripts/install.py --target 경로`로 기본 자료의 복사 예정 목록을 확인한다.
3. 충돌을 해결한 뒤 `--apply`로 적용한다. 기존 내용이 다른 파일을 강제 덮어쓰는 옵션은 제공하지 않는다.
4. 제품 정의·아키텍처 양식을 실제 조사 결과로 채운다.
5. 필요한 설정·개발 도구·CI만 아래 기준으로 통합하고 대상 프로젝트에서 검증한다.

## 파일별 적용 방법

| 파일 또는 경로 | 적용 방법 | 적용 전 확인 |
| --- | --- | --- |
| `project/PROJECT.md` | 대상 루트의 제품 정의 양식 | 현재 구현·플랫폼·목표·데이터·수익화 |
| `project/ARCHITECTURE.md` | 실제 코드의 설계 지도 작성 | 기존 상태관리·라우팅·서비스 경계 |
| `project/CONTRIBUTING.md`, `SECURITY.md` | 협업·보고 절차 | 저장소 보호·실제 담당자·연락 경로 |
| `project/.github/CODEOWNERS` | 대상 저장소의 소유자 규칙 작성 | 실제 계정과 저장소 접근 권한 |
| `flutter/pubspec.yaml` | 필요한 항목만 기존 파일에 병합 | 앱 이름·SDK·버전·현재 의존성 보존 |
| `flutter/.fvmrc` | 선택한 정확한 SDK 버전으로 작성 | 이 파일의 버전은 확인 당시 예시 |
| `flutter/analysis_options.yaml` | 기존 분석 규칙에 병합 | flutter_lints 버전·생성 코드 위치 |
| `flutter/l10n.yaml` | 국제화 도입 시 추가 | ARB 파일·지원 언어·생성 경로 먼저 준비 |
| `flutter/dart_test.yaml` | 테스트 환경에 맞게 조정 | CI 자원·테스트 태그·시간 제한 |
| `flutter/.env.example` | 공개 구성의 문서로 사용 | Flutter는 자동 로드하지 않음 |
| `flutter/.gitignore` | 기존 ignore에 항목 병합 | 비밀·생성물·증거 경로 |
| `flutter/tool/`, `flutter/scripts/` | 선택형 개발 도구 복사 | 실제 앱 루트에서만 실행 |
| `flutter/.github/workflows/` | 선택형 앱 CI 복사 | SDK 핀·도구·웹 대상·플랫폼 환경 |

## SDK와 의존성

예시는 2026-09-03 확인한 Flutter 3.47.2 / Dart 3.13.2 / flutter_lints 6.0.0을 기준으로 한다. 이를 모든 프로젝트의 최소 지원 버전으로 강제하지 않는다. 기존 매니페스트·잠금 파일·공식 변경 기록을 확인하고 갱신 여부를 결정한다.

국제화 샘플은 `flutter_localizations`와 `generate: true`를 포함한다. 실제 `lib/l10n/app_en.arb` 등 언어 파일은 제품 문구가 정해진 뒤 대상 앱에서 작성한다. 이 자료에는 가상의 제품 문구나 위젯을 넣지 않는다.

## 개발 도구

선택형 설치는 다음과 같이 미리 확인한다.

```sh
python scripts/install.py --target ../my_flutter_app --with-tooling
python scripts/install.py --target ../my_flutter_app --with-tooling --apply
```

복사한 대상 프로젝트에서 실행한다.

```sh
dart run tool/bootstrap.dart
dart run tool/check.dart
dart run tool/verify.dart
dart run tool/analyze_dependencies.dart --outdated --security
```

- `bootstrap.dart`: 기존 앱의 SDK를 확인하고 의존성을 가져온다. 국제화 설정이 있으면 생성기를 실행한다. 앱 생성·SDK 업그레이드는 하지 않는다. `pub get`은 잠금 파일·생성 메타데이터를 갱신할 수 있으므로 diff를 확인한다.
- `check.dart`: 앱 루트·지침·잠금 파일·SDK 일치·의존성 override 정책을 확인한다. 문서의 모든 내용이나 보안 취약점의 부재를 보증하지 않는다.
- `verify.dart`: 실제 존재하는 소스를 포맷 검사하고 정적 분석·단위/위젯 테스트·웹 release 빌드를 실행한다. 이 기본 검증을 채택하려면 대상 앱의 웹 플랫폼과 의미 있는 테스트가 필요하다. 웹을 지원하지 않는 제품은 품질 정책과 도구·CI를 함께 조정한다.
- `analyze_dependencies.dart`: 해석된 패키지 목록을 조사한다. `--outdated`는 업데이트 현황, `--security`는 공개 OSV 데이터베이스의 알려진 Pub 취약점을 조회한다. 공급망·라이선스·네이티브 SDK는 별도 검토한다. 내부 레지스트리의 패키지명 공개가 허용되지 않는 프로젝트는 공개 조회를 사용하지 않고 내부 검사를 연결한다.

도구는 추가 Dart 패키지 없이 SDK 표준 라이브러리만 사용한다. 새 도구가 정책을 과도하게 강제한다면 이유·대안·검증을 기록한 뒤 대상 프로젝트에서 조정한다. 단순히 실패를 무시하지 않는다.

## 성능 예산

`tool/performance_budget.json`은 초기 제안이다. 제품의 대표 기기·화면 주사율·데이터량·네트워크 조건으로 조정한다. 스크립트는 측정기를 대신하지 않는다.

```sh
dart run tool/performance_budget.dart --measurements artifacts/performance.json
```

측정 JSON은 다음 필드를 가진다. 실제 측정 전 숫자를 채워 성공시키지 않는다.

| 필드 | 요구 값 |
| --- | --- |
| `platform`, `device` | 실제 플랫폼·기기 또는 브라우저와 버전 |
| `mode` | `profile` 또는 `release` |
| `commit` | 측정한 코드의 40자리 Git SHA |
| `profile` | 예산의 `mobile-60hz` 또는 `web` |
| `sampleCount` | 예시 정책에서는 20회 이상 |
| `evidence` | 프로젝트 안의 실제 추적 파일 경로 |
| `metrics` | 예산과 같은 지표별 `value`와 `unit` 객체 |

모바일 예산은 `startupP95`, `frameP95`, `peakMemory`를, 웹 예산은 `startupP95`, `compressedTransfer`를 요구한다. 단위는 예산 JSON과 일치해야 한다. 원본 추적, 반복 조건, 요약 통계의 계산 방법을 실행 계획에 함께 기록한다.

## 출시 검증

```sh
dart run tool/release_check.dart --platform web --candidate
dart run tool/release_check.dart --platform web
```

`--candidate`는 후보의 SDK·플랫폼·버전만 확인한다. 서명·스토어·정책·실제 배포를 검증한 결과가 아니다. 기본 모드는 `tool/release_config.json`의 `productReady: false` 때문에 실패한다. 이것이 미설정 베이스의 의도된 동작이다.

제품 책임자가 실제 앱 식별자·준비 상태를 확정하고 `evidence`에 `quality`, `security`, `privacy`, `operations`, 선택한 플랫폼의 증거 JSON 경로를 설정한다. 증거는 각각 `commit`, `status`, `recordedAt`, `details`를 포함한다. `commit`은 현재 검사 커밋, `status`는 실제 성공 시 `passed`, `recordedAt`은 ISO 8601 시각, `details`는 검증 내용·보고서 또는 실행 링크다.

현재 커밋에서 생성한 증거는 아티팩트나 작업용 경로로 주입한다. 증거를 추가 커밋해서 검사 SHA가 달라지면 새 SHA에서 다시 검증해야 한다. 게이트는 증거의 형식을 확인할 뿐 내용의 진실을 보증하지 않는다. 서명과 수익화·정책의 실검증은 분야별 체크리스트와 책임자 검토를 따른다.

## CI 도입

```sh
python scripts/install.py --target ../my_flutter_app --with-tooling --with-ci
```

검토 후 `--apply`를 추가한다. 대상의 `.fvmrc`에 정확한 안정 SDK 버전이 있어야 한다. 이미 다른 CI가 있으면 파일을 비교해서 병합한다. source 저장소의 Python 자료 검증 CI는 대상 앱에 복사하지 않는다.

앱 CI는 품질·PR 규칙·의존성 점검·정기 점검을 제공한다. Android·iOS·웹 후보는 수동 실행하고 산출물만 보관한다. Android의 실제 서명 설정을 반드시 검토하며 Flutter 기본 생성기의 debug 서명을 그대로 출시용으로 사용하지 않는다. iOS 후보는 코드 서명이 없는 컴파일 결과다.

`release.yml`은 준비 증거를 검사하는 예시다. 제품에서는 승인된 실행의 증거 아티팩트를 검사 전에 내려받는 단계를 연결해야 한다. 이 자료는 배포 공급자·자격·스토어 업로드를 선택하거나 구성하지 않는다.

Actions는 확인한 커밋으로 고정했다. 주기적으로 공식 릴리스·보안 공지를 검토하고 업데이트한다. GitHub 보호 규칙과 운영 environment의 승인·비밀·브랜치 제한은 UI 또는 승인된 관리 도구에서 별도로 설정한다.
