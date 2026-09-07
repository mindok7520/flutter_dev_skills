# 개발 자료의 도입과 지속 개발 개선

## 작업 식별

- 요청: 전체 구성·파일을 점검하고 새 프로젝트 도입, 지속 개발, 저비용 모델 활용, 성능 측정과 README를 개선한다.
- 로컬 작업 ID: `local-20260907-workflow-efficiency`. 원격 이슈는 제공되지 않았으며 생성하지 않았다.
- 브랜치: `codex/local-20260907-workflow-efficiency`, 기준 `develop`, 시작 커밋 `9a8758d`.
- 상태: 로컬 구현·검증 완료. 시작 작업 트리는 깨끗했다. 확인일: 2026-09-07.

## 범위와 수락 기준

1. 추적 파일 전체의 구성·연결·중복을 조사하고 분야별 판단과 개선 근거를 남긴다.
2. 작업별 목표·수락 기준·범위·검증을 명시하는 휴대 가능한 도구와 지침을 제공한다.
3. 프롬프트의 공통 중복과 글자 수 강제를 줄이고 작업별 절차·출력 계약을 검사한다.
4. 제품 문서를 수정한 뒤에도 선택형 도구를 추가 설치할 수 있고 기존 파일을 보존한다.
5. 빠른 로컬 검증과 플랫폼 빌드를 구분하고 결과의 범위를 명시한다.
6. README의 설치·수동 복사·일상 개발·모델 교체·자료 갱신 절차가 실제 도구와 일치한다.
7. 자료 검증, Python 회귀 테스트, 설치 후 링크·명령 검증을 통과한다.

## 조사와 결정

- 초기 추적 파일: 448개. 앱 매니페스트·앱 코드는 없다.
- 초기 검증은 전역 Python에 `markdown_it`이 없어 실패했다. `.venv`에 기존 고정 의존성을 설치해 환경 실패와 코드 실패를 구분한다.
- 프롬프트 1,500자·스킬 1,200자 하한은 품질보다 분량을 강제한다. 구조와 실제 연결을 검증하도록 변경한다.
- 설치기는 이미 작성한 제품 정의와 원본 양식의 차이를 충돌로 처리한다. 선택형 도구만 추가하는 경로가 필요하다.
- 검증기의 재귀 순회는 무시할 디렉터리 안까지 먼저 열거한다. 진입 전에 제외하도록 변경한다.
- 앱 검증은 웹 지원 여부와 무관하게 웹을 빌드한다. 공통 검사와 명시적 플랫폼 빌드를 나눈다.
- 앱 실행 속도와 모델 비용 개선은 별도 측정 대상이다. 문서 분량 감소만으로 모델 정확도나 앱 성능 향상을 주장하지 않는다.
- 원격 등록 없이도 허용된 로컬 작업을 이어갈 수 있도록 로컬 계획 ID를 정하고 PR 제출 전 실제 이슈 연결을 요구한다. 원격 이슈 번호를 만들거나 미등록 PR을 완료했다고 표시하지 않는다.
- 독립적인 문서 사용 검증에서 제품 정의 수정 후 설치·작업 입력 발견 경로·플랫폼 검사 설명을 대조했다. 추가로 발견한 UTF-8 BOM SDK 핀의 설치/CI 불일치는 같은 입력을 Python·Dart에 전달해 수정했다.

## 전체 구성 점검 범위

초기 추적 파일 448개를 UTF-8로 읽고 디렉터리별 책임, 링크·메타데이터·구문·공통 문구·실행 경로를 점검했다. 이 기록은 각 제품의 보안·정책·성능을 실환경에서 인증했다는 뜻이 아니다. 실제 변경은 아래 근거가 있는 경로에 집중했다.

| 구성 | 초기 파일 수 | 판단과 조치 |
| --- | --- | --- |
| 루트 지침·설정·문서·고정 Python 의존성 | 14 | 제품과 자료 저장소 경계 유지, README·작업 지도·변경 기록·로컬 계획 예외 갱신. 의존성 버전 유지 |
| `docs/` | 176 | 분야별 원본·설계/운영 기준·출처·계획 연결 확인. 공통 작업 계약·인계 입력·검증 단계·공식 출처 추가. 과거 완료 계획은 보존 |
| `prompts/` | 63 | 프롬프트 62개 전체의 작업별 절차와 문서 참조를 유지하며 공통 중복 축소. 색인과 언어를 동기화 |
| `.agents/` | 58 | 스킬 29개·메타데이터 확인. 영어 스킬 21개의 중복을 줄이고 동등한 프롬프트는 대체 진입점으로 명시 |
| `.github/`, `.cursor/` | 89 | 프롬프트 어댑터·지침 참조·이슈/PR 양식·CI 점검. 카탈로그와 실제 스킬 연결의 누락을 검증하고 Python 최소 버전·Dart 도구 CI 추가 |
| `config/` | 2 | 필수 파일 목록과 현재 62개 프롬프트·29개 스킬 목록 동기화. 스킬 참조와 역방향 매핑의 차이 검출 |
| `scripts/` | 8 | 설치 충돌·독립 실행·인코딩·경로·탐색 비용 확인. 도구 전용 설치, 작업 입력 생성기, 캐시 진입 전 제외, 가상 환경 실행 추가 |
| `templates/` | 35 | 앱 설정은 선택 병합 원칙 유지. 제품별 검증/소유권/성능 계약 강화. 플랫폼 빌드 선택과 CI SDK 인코딩 정합성 수정 |
| `tests/` | 3 | 기존 19개 테스트 기준선 확인. 설치 후 도구 실행·실제 Dart 명령 선택·실패 중단·BOM·카탈로그·경로 검증 추가 |

## 변경 파일과 결정

- `scripts/task_context.py`, `docs/agent/TASK_PACKET.md`, `tests/test_task_context.py`: 목표·수락 기준·파일·검증을 묶는다. 표준 라이브러리만 사용하며 코드 내용 수집·외부 전송·AI 호출·체크 실행은 하지 않는다. 설치 시 `.agents/`에 생성기와 카탈로그를 함께 배치한다.
- `scripts/install.py`, `scripts/bootstrap.ps1`, `tests/test_install.py`: `--only-tooling`은 제품 정의를 재비교하지 않는다. 도구의 실제 충돌은 계속 전체 복사 전에 거절한다. 잘못된 `.fvmrc` JSON은 설명 가능한 오류로 처리한다.
- `scripts/validate.py`, `tests/test_catalog.py`, `tests/test_policies.py`: 최소 글자 수를 입력·번호 절차·완료 조건 검사로 바꾸고 스킬 매핑의 누락을 검출한다. 캐시/생성 디렉터리 진입을 방지한다.
- `prompts/00-61`, 영어 스킬 21개, 공통 계약·색인·카탈로그: 중복 공통 지침을 줄이고 분야별 절차·안전 경계는 원본 문서와 연결한다. 62개 프롬프트는 영어, 질문·설명·README는 한국어다.
- `templates/flutter/tool/verify.dart`, 검증 래퍼, 앱 CI: 공통 분석/테스트와 명시적 플랫폼 빌드를 구분한다. 잘못된 대상·지원하지 않는 호스트를 명령 실행 전에 거절하고 테스트 실패 후 빌드하지 않는다.
- `tests/test_dart_tooling.py`, `.github/workflows/ci.yml`: 실제 Dart 분석과 명령 기록용 Flutter 대역으로 검증한다. CI에는 Python 3.11/3.13과 독립 Dart SDK 검사를 구성했다. 원격 실행 결과는 아직 없다.
- `README.md`, `templates/README.md`, `AGENTS.md`, `ARCHITECTURE.md`, `PROJECT.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, 제품 양식: 복사 지도·최초/후속 설치·모델 교체·갱신·측정·검증·인계를 실제 코드와 맞췄다.

## 단계와 진행

- 완료: 현재 Git·매니페스트·도구·문서 지도·설치·검증·CI 조사, 기존 의존성 격리 설치.
- 완료: 작업 입력 도구, 프롬프트·스킬 정리, 검증·설치 개선, 사용 안내와 독립적인 스킬 사용 검증.
- 완료: 마지막 전체 검증, 변경 상태와 남은 환경 제한 기록.

## 검증 기록

| 상태 | 명령·환경 | 결과 | 제한 |
| --- | --- | --- | --- |
| 변경 전 | `python scripts/validate.py` | 실패: `markdown_it` 없음 | 환경 미구성 |
| 변경 전 | `python -m unittest discover -s tests -q` | 오류 3건 | 동일 의존성 미설치 |
| 준비 | `python -m venv .venv`, `.venv/Scripts/python -m pip install -r requirements-dev.txt` | 성공 | Python 3.13, Windows |
| 변경 전 기준선 | `.venv/Scripts/python scripts/validate.py`, `.venv/Scripts/python -m unittest discover -s tests -q` | 성공, 19개 테스트 | 28.116초, 앱 검증 아님 |
| 변경 후 | `DART_EXECUTABLE`을 독립 Dart 경로로 지정, `.venv/Scripts/python -m unittest discover -s tests -v` | 성공, 36개 테스트 | 58.344초. 이후 BOM 회귀 1건 추가 |
| BOM 수정 후 | `.venv/Scripts/python -m unittest tests.test_install.InstallTests.test_installed_ci_sdk_readers_accept_the_same_bom_as_the_installer tests.test_dart_tooling -v` | 성공, 7개 테스트 | 11.357초, SDK 핀 읽기와 Dart 도구의 실제 실행 경로 |
| 최종 전체 검사 | `$env:DART_EXECUTABLE = (Resolve-Path '.local/dart-validation/dart-sdk/bin/dart.exe').Path` 후 `./scripts/verify.ps1` | 자료 검증 및 37개 테스트 모두 성공, 건너뜀 없음 | 58.671초, 래퍼의 로컬 가상 환경 선택도 확인 |
| 구조·링크 | `.venv/Scripts/python scripts/validate.py`, `git diff --check` | 성공 | 문서 링크·YAML/JSON·목록·메타데이터·공백 검사 |
| 독립 사용 확인 | `documentation-sync` 스킬로 README와 실제 도구를 읽기 전용 대조 | 설치·입력 생성·인계·검증 설명 일치 | 발견된 BOM 문제를 수정하고 별도 회귀 검증 |

실행 가능한 테스트는 자료 도구의 계약을 검증한다. 실제 Flutter·기기·서명·스토어·서버 검증은 수행하지 않았다. Dart 테스트의 Flutter 대역은 명령을 기록하고 의도된 실패를 반환하므로 실제 앱 빌드 성공을 뜻하지 않는다.

## 분량과 탐색 비용 측정

`git show HEAD:<path>`의 변경 전 UTF-8 문자 수와 현재 파일을 비교했다. 프롬프트 62개는 123,291 → 83,748자(32.1% 감소), 스킬 29개 전체는 63,386 → 50,723자(20.0% 감소)다. 21개 스킬을 수정했으며 8개 기존 스킬은 보존했다. 문자 수는 모델 토큰·비용·정확도의 측정값이 아니다. 새 공통 계약과 필요한 문서를 포함한 실제 요청 단위로 모델별 평가를 해야 한다.

Windows/Python 3.13, 동일 작업 폴더(`.git`, `.venv`, 검증용 Dart SDK가 있는 `.local` 포함)에서 파일 탐색만 7회 비교했다. 두 방식의 반환 파일 집합은 453개로 동일했다. 전체 검증 시간이나 앱 성능의 측정은 아니다. 파일 캐시·디스크·백신에 따라 달라지며 통계적 성능 보증이 아니다.

| 방식 | 7회 원본 시간(ms) | 중앙값(ms) |
| --- | --- | --- |
| 전체 열거 후 제외 | 499.757, 521.354, 442.555, 392.647, 412.730, 397.376, 389.512 | 412.730 |
| 진입 전 제외 | 31.192, 29.257, 28.345, 24.329, 25.400, 25.136, 26.313 | 26.313 |

자료 루트에서 아래 Python 코드를 실행하면 같은 비교 방법을 재현할 수 있다. 현재 폴더의 파일 수와 캐시 상태에 따라 수치는 달라진다.

```python
from pathlib import Path
from statistics import median
from time import perf_counter
from scripts.validate import IGNORED, material_files

root = Path.cwd()

def original_walk():
    return [path for path in sorted(root.rglob('*'))
            if not any(part in IGNORED for part in path.relative_to(root).parts)
            and path.is_file()]

assert set(original_walk()) == set(material_files(root))
for name, walk in [('original', original_walk), ('pruned', lambda: list(material_files(root)))]:
    samples = []
    for _ in range(7):
        start = perf_counter()
        files = walk()
        samples.append((perf_counter() - start) * 1000)
    print(name, len(files), samples, median(samples))
```

## 위험과 복구

Flutter·GitHub CLI는 PATH에 없고, 검증용 독립 Dart 3.13.2는 `.local/dart-validation/dart-sdk/`에만 준비했다. 공식 체크섬 대조 후 사용했으며 원본 SDK 설정이나 제품 의존성은 바꾸지 않았다. `.venv`와 `.local`은 Git 제외 경로다.

모델별 비용·정확도 비교, 실제 앱 빌드·기기 성능, Linux/macOS와 원격 CI 실행은 미검증이다. 생성기는 신뢰된 로컬 작업 폴더용이며 악의적인 동시 파일 시스템 변경에 대한 격리 도구는 아니다. 설치 중 I/O 실패는 부분 복사 상태를 보존하고 설명하므로 상태를 확인한 뒤 동일 파일을 건너뛰어 재시도한다. 자료 업데이트는 자동 병합하지 않는다.

초기 분량 감소와 디렉터리 탐색 측정은 확인한 사실이고, 저비용 모델의 작업 정확도 개선은 명확한 입력·작은 범위·검증에 기반한 운영 가정이다. 모델을 자동 교체하거나 추가 비용을 사용하는 기능은 없다.

## 다음 행동

요청한 로컬 개선은 완료했다. 사용자는 루트 README의 빠른 시작으로 새 앱을 도입할 수 있다. 변경 검토의 첫 명령은 `git diff --stat`, 재검증은 독립 Dart 경로를 설정한 뒤 `./scripts/verify.ps1`이다.

변경은 `codex/local-20260907-workflow-efficiency`의 미커밋 작업 트리에 남겼다. 시작 커밋은 `9a8758d`이고 원격 이슈·PR·푸시·제품 출시는 없다. 나중에 PR을 제출한다면 실제 이슈 연결과 번호 기반 브랜치 전환을 먼저 수행한다. 완료 계획은 자료 설치 대상의 제품 작업 이력에 복사되지 않는다.
