# Flutter AI Development Base

새 Flutter 프로젝트에 **필요한 파일을 가져다 넣고 개발을 시작하기 위한 자료 저장소**다. 실행 앱이나 제품 예제는 포함하지 않는다. AI 지침, 분야별 문서, 작업 프롬프트 54개, 스킬 24개, 협업 양식과 선택적으로 도입할 설정·CI·개발 도구 템플릿을 제공한다.

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
