# Flutter AI Development Base

새 Flutter 프로젝트에 **필요한 파일을 가져다 넣고 개발을 시작하기 위한 자료 저장소**다. 실행 앱이나 제품 예제는 포함하지 않는다. AI 지침, 분야별 문서, 작업 프롬프트 62개, 스킬 29개, 협업 양식과 선택적으로 도입할 설정·CI·개발 도구 템플릿을 제공한다.

## 빠른 시작: 클론부터 첫 AI 작업까지

Python 3.11 이상과 대상 앱에 사용할 Flutter SDK를 준비한다. 명령은 PowerShell·터미널에서 실행할 수 있다. macOS·Linux에서 `python` 명령이 없다면 `python3`로 바꾼다. 이 자료 저장소만 읽거나 수동 복사할 때는 Flutter 설치가 필요하지 않다.

### 1. 개발 자료 저장소 클론

```sh
git clone https://github.com/mindok7520/flutter_dev_skills.git
cd flutter_dev_skills
```

이 폴더는 자료 원본으로 유지한다. 실제 앱은 이 안에 만들지 않는다.

### 2. 옆 디렉터리에 새 Flutter 앱 생성

```sh
python --version
flutter --version
flutter create ../my_flutter_app
```

`my_flutter_app`은 예시 이름이다. 원하는 앱 이름으로 바꾸되 이후 명령의 경로도 동일하게 바꾼다. 기존 Flutter 앱이 있다면 생성 단계는 건너뛰고 그 경로를 사용한다. 기본 생성기의 `com.example` 앱 식별자는 출시 전에 제품의 실제 값으로 바꾼다.

```text
parent-directory/
  flutter_dev_skills/  Development materials
  my_flutter_app/      Actual Flutter project
```

### 3. 복사 예정 사항 확인 후 적용

현재 위치는 여전히 `flutter_dev_skills`다.

```sh
python scripts/install.py --target ../my_flutter_app
python scripts/install.py --target ../my_flutter_app --apply
```

첫 명령은 미리보기, 두 번째는 실제 복사다. 상세 파일 목록은 `--list`로 확인한다. 경로에 공백이 있으면 `--target "../My Flutter App"`처럼 따옴표로 감싼다.

대상에 이미 같은 내용의 파일이 있으면 그대로 유지한다. 내용이 다른 파일이 있으면 **복사 전에 전체 작업을 중단**하고 충돌 목록을 보여준다. 기존 지침·문서가 중요한 프로젝트는 목록을 비교해 필요한 자료만 수동 통합한다. 강제 덮어쓰기는 하지 않는다.

### 4. 대상 프로젝트의 제품 정의 작성

대상 앱의 `PROJECT.md`에 만들 제품·사용자·플랫폼·핵심 기능·제외 범위를 기록한다. `ARCHITECTURE.md`에는 실제 코드 구조와 기술 결정을 적는다. 이 두 파일은 제품별로 채우는 양식이며 자료 설치만으로 기능이 구현된 것은 아니다.

직접 양식을 채우기 어렵다면 대상 앱 폴더를 AI 도구에서 열고 다음 요청을 보낸다. 대괄호 안을 자신의 아이디어로 바꾸고, AI의 질문에 답하면 된다.

```text
AGENTS.md와 PROJECT.md를 읽고 02-requirements-analysis를 적용해 줘.
만들고 싶은 앱은 [누가 어떤 문제를 해결하려고 사용하는 앱인지]야.
첫 버전에 꼭 필요한 기능은 [핵심 기능]이고, 지원 플랫폼은 [플랫폼]이야.
부족한 제품 결정을 쉽게 질문하고 내 답변으로 PROJECT.md를 작성해 줘.
확정한 내용과 미정인 내용을 구분하고 첫 개발 작업을 제안해 줘.
UI는 54-design-brief로 필요한 취향과 제약을 먼저 확인해 줘.
```

막연한 아이디어부터 설명해도 된다. 정하지 않은 서버·상태관리·디자인을 AI가 확정 사실로 기록하게 하지 말고, 제안의 이유를 듣고 결정한다.

새 앱의 초기 상태를 확인한다.

```sh
cd ../my_flutter_app
flutter analyze
flutter test
```

### 5. 대상 앱 폴더를 AI 도구에서 열고 첫 작업 요청

AI 도구의 작업 폴더를 **my_flutter_app**으로 지정한다. 다음처럼 요청한다.

> AGENTS.md와 PROJECT.md를 읽고 00-session-bootstrap 프롬프트를 적용해 줘. 현재 코드와 도구 체인을 조사하고, PROJECT.md의 제품 목표를 구현할 개발 순서와 첫 이슈의 수락 기준을 정리해 줘. 기존 파일과 설정은 보존하고, 여러 세션이 필요한 작업은 docs/exec-plans/active/에 기록해 줘.

대상 앱용 GitHub 저장소를 연결한 뒤 작업별 이슈와 브랜치를 사용한다. 예를 들어 이슈 #142라면 `develop`에서 `feature/142-add-settings` 또는 `codex/142-add-settings`를 만들고 PR로 통합한다. 빈 저장소의 최초 초기화 예외와 `master` 운영은 [브랜치 정책](docs/workflow/BRANCHING_STRATEGY.md)을 따른다. 이 자료 저장소의 원격 저장소를 새 앱의 원격으로 사용하지 않는다.

대화가 끊기면 `52-session-handoff`로 남긴 기록과 `00-session-bootstrap` 또는 문맥 복구 지침으로 이어서 작업한다.

자동 도입 대상은 `AGENTS.md`, 에이전트 어댑터, `docs/`, `prompts/`, `.agents/skills/`, `.cursor/rules/`, GitHub 지침·이슈/PR 양식과 프로젝트 정의 양식이다. 이 저장소의 초기화 이력·README·LICENSE·검증용 Python 코드는 대상 앱에 복사하지 않는다.

## 설정·도구·CI는 선택해서 도입

[templates/README.md](templates/README.md)에 파일별 적용 방법이 있다. `templates/flutter/`의 `pubspec.yaml`, 분석·국제화·테스트·SDK 설정은 **대상 프로젝트의 기존 파일에 필요한 항목만 통합**한다. 앱 이름·SDK·의존성을 일괄 교체하지 않는다.

`--with-tooling`은 Dart 개발 도구와 셸 래퍼를, `--with-ci`는 대상 Flutter 앱용 CI를 추가한다. CI는 개발 도구가 필요하므로 두 옵션을 함께 사용한다. 먼저 대상 앱의 `.fvmrc`에 실제로 선택한 정확한 Flutter 버전을 기록한다. 이때도 기존 파일 충돌을 먼저 검사한다.

```sh
python scripts/install.py --target ../my_flutter_app --with-tooling --with-ci
```

위 명령은 자료 원본인 `flutter_dev_skills` 디렉터리에서 실행한다. 빠른 시작을 따라 대상 앱으로 이동했다면 먼저 `cd ../flutter_dev_skills`로 돌아온다. 검토 후 같은 명령에 `--apply`를 추가한다. 앱 코드·플랫폼 파일·광고·결제 SDK를 생성하거나 설치하지 않는다. 서명·운영 배포·GitHub 보호 설정도 자동 변경하지 않는다.

## AI에게 첫 작업 전달하기

대상 프로젝트의 `PROJECT.md`에 제품 목표·플랫폼·데이터·출시 범위를 채운다. `AGENTS.md`와 [세션 시작 프롬프트](prompts/00-session-bootstrap.md)를 읽게 하고 실제 이슈·수락 기준·허용 범위를 전달한다. 대화가 끊기면 Git 상태와 `docs/exec-plans/active/`의 실행 계획으로 재개한다.

도구별 자동 인식 범위는 다를 수 있다. 첫 세션에서 실제로 읽은 지침 경로를 확인하고, 자동 인식하지 않는 도구에는 해당 파일을 직접 제공한다. 프롬프트와 스킬을 모두 한 번에 읽게 하지 않는다.

## 디자인은 사용자 질문부터 시작

새 화면·디자인 개편·탐색 방식·모션·셰이더 효과는 [디자인 작업 절차](docs/design/DESIGN_WORKFLOW.md)를 따른다. AI가 기존 자료를 읽고 **사용자 목표·취향·제약 중 미정인 내용을 질문한 뒤 응답을 기다리도록** 구성했다. 한 번에 한 가지 질문을 우선하며 관련 질문은 최대 세 개까지 묶는다.

**54 요구 질문 → 55 방향 비교와 선택 → 56 합의된 UI 구현 → 57 실행 화면 검수** 순서다. 이미 완성된 디자인과 구현 범위를 승인했거나 선택을 위임했다면 그 답변을 재사용한다. 같은 작업의 로컬 구현과 검증을 매번 다시 승인받지는 않는다. 범위가 명확한 검토나 승인된 화면의 버그 수정은 그 범위에 맞게 진행한다.

대상 앱에서 다음 요청으로 시작한다.

```text
AGENTS.md와 PROJECT.md를 읽고 54-design-brief를 적용해 줘.
사용자, 주요 화면, 원하는 느낌과 제약 중 부족한 내용을 먼저 질문해 줘.
내 답변을 디자인 요구 문서에 반영하고 대표 화면의 방향을 비교해 줘.
내가 선택한 방향으로 구현하고 실제 화면과 사용자 흐름을 검증해 줘.
```

이미 디자인을 정했다면 다음처럼 승인한 범위를 명시한다.

```text
첨부한 디자인과 PROJECT.md의 요구사항으로 설정 화면을 구현해 줘.
이 디자인과 범위는 승인한 상태이므로 56-implement-ui를 적용해 줘.
모호한 제품 결정만 질문하고 구현·테스트·57-visual-review까지 진행해 줘.
이미지나 실제 실행 화면을 확인하지 못했다면 미검증으로 표시해 줘.
```

## 어떤 내용을 어디에서 찾는가

“프롬프트”는 개별 작업 요청문, “스킬”은 반복 작업의 진입점이며 분야별 문서는 판단 기준과 상세 절차다. AI 도구가 링크를 자동으로 읽지 않으면 해당 파일을 직접 제공한다. 같은 정책을 어댑터마다 복제하지 않고 원본에 연결한다.

| 작업 | 선택할 프롬프트 | 상세 기준과 양식 |
| --- | --- | --- |
| 아이디어를 제품 정의로 정리 | [02 요구 분석](prompts/02-requirements-analysis.md) | [제품 정의 양식](templates/project/PROJECT.md) |
| 새 디자인 전에 사용자에게 질문 | [54 디자인 요구](prompts/54-design-brief.md) | [사용자 확인 절차](docs/design/DESIGN_WORKFLOW.md), [디자인 요구 양식](docs/design/PRODUCT_DESIGN_BRIEF.md) |
| 대표 화면의 방향 비교·선택 | [55 디자인 방향](prompts/55-visual-direction.md) | [공통 디자인 체계](docs/design/DESIGN_SYSTEM.md), [색·글꼴·간격](docs/design/DESIGN_TOKENS.md) |
| 합의한 UI와 상태 구현 | [56 UI 구현](prompts/56-implement-ui.md) | [화면 명세](docs/design/SCREEN_SPEC_TEMPLATE.md), [컴포넌트 계약](docs/design/COMPONENT_GUIDELINES.md) |
| 실제 화면의 차이 수정 | [57 실행 화면 검수](prompts/57-visual-review.md) | [시각 검수](docs/design/VISUAL_REVIEW.md), [이미지 회귀 검사](docs/testing/GOLDEN_TESTING.md) |
| 정보 계층·문구·사용 흐름 | [17 UI](prompts/17-ui-review.md), [18 UX](prompts/18-ux-review.md) | [UI 기본 규칙](docs/design/UI_GUIDELINES.md), [사용 경험](docs/design/UX_GUIDELINES.md) |
| 화면 크기·입력·접근성 | [19 적응형](prompts/19-responsive-review.md), [20 접근성](prompts/20-accessibility-review.md), [42 국제화](prompts/42-localization-review.md) | [적응형 설계](docs/design/RESPONSIVE_ADAPTIVE.md), [접근성](docs/design/ACCESSIBILITY.md), [국제화](docs/design/LOCALIZATION.md) |
| 상태관리 방식과 수명 | [58 상태관리](prompts/58-state-management-decision.md) | [기존 방식·로컬 상태·ChangeNotifier·Riverpod·Bloc 비교](docs/architecture/STATE_MANAGEMENT.md) |
| 아키텍처·책임·의존성 | [05 설계](prompts/05-architecture-design.md), [06 검토](prompts/06-architecture-review.md) | [앱 구조](docs/architecture/APP_ARCHITECTURE.md), [의존성](docs/architecture/DEPENDENCY_RULES.md), [데이터 흐름](docs/architecture/DATA_FLOW.md) |
| 성능·메모리·렌더링·동시성 | [13 성능](prompts/13-performance-audit.md), [14 메모리](prompts/14-memory-audit.md), [15 렌더링](prompts/15-rendering-audit.md), [16 동시성](prompts/16-concurrency-review.md), [30 측정](prompts/30-performance-test.md) | [측정 절차](docs/performance/PROFILING_GUIDE.md), [재빌드](docs/performance/REBUILD_OPTIMIZATION.md), [비동기 수명](docs/engineering/ASYNC_CONCURRENCY.md) |
| 애니메이션 목적·구현·검증 | [59 애니메이션](prompts/59-animation-design.md) | [기본 애니메이션·flutter_animate·Rive 선택 조건](docs/design/ANIMATION_MOTION.md) |
| 셰이더 효과의 지원·비용 | [60 셰이더](prompts/60-shader-review.md) | [입력 계약·좌표·수명·대체 화면·실측](docs/performance/SHADER_GUIDE.md) |
| 공통 위젯의 상태별 예제 | [61 컴포넌트 카탈로그](prompts/61-component-catalog.md) | [실제 위젯 예제와 검증](docs/design/COMPONENT_GUIDELINES.md) |
| 보안·결제·출시·운영 등 | [전체 62개 프롬프트](prompts/README.md) | [전체 문서 지도](docs/README.md) |

새 스킬은 `$ui-design`, `$visual-review`, `$state-management`, `$animation`, `$shaders`다. 기존 `$architecture`, `$performance`, `$responsive-ui` 등도 새 공통 지침에 연결했다. 스킬을 인식하지 않는 AI에는 표의 프롬프트를 직접 제공하면 된다.

## 영어 본문과 한국어 안내

개정한 **프롬프트 34개와 스킬 21개**의 실행 본문은 영어다. 나머지 기존 분야의 한국어 본문은 유지했고 [전체 지도](prompts/README.md)에 프롬프트별 언어를 표시했다. 사용자 질문·판단 설명·최종 답변·README는 한국어이며, 제품 화면의 문구는 제품의 지원 언어를 따른다.

영어가 모든 AI 모델에서 더 좋은 결과를 낸다고 검증한 것은 아니다. 기술 용어와 원본 대조를 일관되게 하고 중복 번역으로 생기는 정책 차이를 줄이기 위한 구성이다. 명확한 입력, 사용자와 합의한 범위, 실제 실행 증거를 우선한다.

## 참고한 저장소와 적용 범위

Superpowers, Anthropic 디자인 스킬, Vercel 검토 지침, UI UX Pro Max, shadcn/ui, Flutter samples·DevTools, Riverpod, Bloc, Wonderous, flutter_animate, Rive, flutter_shaders, Widgetbook 등 **15개 저장소**의 실제 파일을 확인했다. [조사 및 적용 기록](docs/REFERENCE_RESEARCH.md)에 커밋·확인 날짜·파일 링크·채택한 개념·그대로 도입하지 않은 규칙을 정리했다.

참고 저장소를 설치하거나 그 앱을 복사하는 구성은 아니다. 대상 프로젝트의 기존 상태관리와 아키텍처를 우선하고, 새로운 도구·셰이더·애니메이션은 목적·호환성·수명·성능 비용을 검토한 뒤 선택한다.

## 이 자료 저장소 자체의 검증

Python 3.11 이상을 사용한다. 이 저장소를 관리하는 데 Flutter 설치는 필요하지 않다.

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests -v
```

검증은 요구 파일 목록·문서 링크·스킬 메타데이터·프롬프트·YAML·CI 고정 버전·복사 충돌 방지를 확인한다. 앱 분석·위젯 테스트·기기 빌드와 실제 배포 검증은 복사한 대상 프로젝트에서 수행한다.

[문서 지도](docs/README.md), [프로젝트 범위](PROJECT.md), [기여 방법](CONTRIBUTING.md), [템플릿 안내](templates/README.md)를 함께 참고한다.

## 출처와 권리

공식 자료 확인일은 2026-09-03이다. [출처 목록](docs/SOURCES.md)에 확인한 SDK·정책·AI 지침을 기록했다. 템플릿 버전은 확인 당시의 예시이며 대상 프로젝트의 버전을 우선한다. [LICENSE](LICENSE)는 권리 유보 상태다. 외부 재배포 권한을 부여하는 오픈소스 라이선스는 지정하지 않았으므로 공개 재배포 전 권리자가 결정해야 한다.
