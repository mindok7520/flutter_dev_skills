# 공개 저장소 조사와 적용 결정

확인일: **2026-09-03**. 사용자가 언급한 `superpower`는 `obra/superpowers`로 해석했다. 저장소 설명뿐 아니라 아래에 연결한 실제 파일을 확인했다. 이 목록은 인기 순위나 모든 라이브러리의 도입 권장이 아니다.

## 읽는 순서

- 조사 범위와 버전 구분
- 저장소별 확인 지점
- 적용과 제외 결정
- 공식 문서와 언어 정책

## 조사 범위와 버전 구분

이 자료 저장소에는 실행할 Flutter 앱과 설치된 상태관리·애니메이션 패키지가 없다. 아래 커밋은 조사한 원본을 재현하기 위한 참조이며 대상 프로젝트의 의존성을 고정하거나 최신 버전으로 변경하지 않는다. 대상 앱의 매니페스트·잠금 파일·SDK 설정을 먼저 확인한다.

각 원본의 전체 커밋, 커밋 날짜, 확인일, 확인 당시 보관 상태, 라이선스 메타데이터와 파일 링크는 [구조화한 조사 기록](references/repositories.json)에 있다. API 메타데이터의 `NOASSERTION`은 해당 정보만으로 라이선스를 확정하지 못했다는 뜻이다. 코드나 에셋을 실제로 복사할 때는 해당 파일에 적용되는 조건을 별도로 확인한다.

이번 변경은 필요한 개념을 이 저장소의 목적에 맞게 독자적으로 작성했다. 외부 스킬이나 실행 코드를 설치하지 않았고, 외부 프롬프트의 명령을 현재 작업의 권한으로 취급하지 않는다. 표의 커밋은 조사 시점의 스냅샷이며 이후 변경 여부는 다시 확인해야 한다.

## 저장소별 확인 지점

| 저장소 | 확인한 커밋 | 참고 분야 |
| --- | --- | --- |
| [anthropics/skills](https://github.com/anthropics/skills) | `53048666b0` | 디자인 방향·실제 문구·색과 글꼴 역할·비평 |
| [felangel/bloc](https://github.com/felangel/bloc) | `8fcf54dfea` | 명시적 상태 전이와 이벤트 처리 정책 |
| [flutter/devtools](https://github.com/flutter/devtools) | `c9c5bc8e93` | 프로파일링·메모리·프레임 증거 |
| [flutter/samples](https://github.com/flutter/samples) | `463e365e48` | Compass의 제품 규모 설계 사례 |
| [gskinner/flutter_animate](https://github.com/gskinner/flutter_animate) | `62c12040b1` | 효과 조합·타임라인·컨트롤러 |
| [gskinnerTeam/flutter-wonderous-app](https://github.com/gskinnerTeam/flutter-wonderous-app) | `747b945a7e` | 브랜드 표현·글꼴 역할·간격·모션 사례 |
| [jonahwilliams/flutter_shaders](https://github.com/jonahwilliams/flutter_shaders) | `9d99a2ff20` | 셰이더 자산·샘플러·uniform 계약 |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | `58c220ff9d` | 제품·사용자·스타일 맥락과 디자인 시스템 기록 |
| [obra/superpowers](https://github.com/obra/superpowers) | `b36e0829c6` | 질문·설계 합의·실행 계획·완료 증거 |
| [rive-app/rive-flutter](https://github.com/rive-app/rive-flutter) | `9bb8f7f4a0` | 상태를 가진 그래픽·렌더러·리소스 수명 |
| [rrousselGit/riverpod](https://github.com/rrousselGit/riverpod) | `693a2dbc59` | 상태 범위·자동 해제·캐시·정리 |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | `71e50952fb` | 일관된 컴포넌트 조합과 실제 소스 활용 |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | `063bee94c3` | AI가 참고할 검토 기준 연결 |
| [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) | `e3d624baaf` | 접근성·포커스·입력·문구·실패 상태 |
| [widgetbook/widgetbook](https://github.com/widgetbook/widgetbook) | `66c1eb2f00` | 실제 위젯의 상태별 카탈로그 |

## 적용과 제외 결정

### anthropics/skills

제품 맥락과 명시적 시각 방향, 구현 전 계획과 구현 후 화면 검토를 참고한다. 특정 색·폰트의 일괄 금지나 모든 제품에 강한 장식을 요구하는 규칙은 적용하지 않는다.

검토한 파일: [skills/frontend-design/SKILL.md](https://github.com/anthropics/skills/blob/53048666b05b4799081517d00e09e0a2dd688678/skills/frontend-design/SKILL.md), [skills/frontend-design/LICENSE.txt](https://github.com/anthropics/skills/blob/53048666b05b4799081517d00e09e0a2dd688678/skills/frontend-design/LICENSE.txt).

### felangel/bloc

동시·순차·중복 무시·최신 요청 우선의 의미를 작업별로 비교한다. 핸들러 취소가 서버 변경을 되돌리거나 한 이벤트의 직렬화가 전체 이벤트를 직렬화한다고 가정하지 않는다.

검토한 파일: [README.md](https://github.com/felangel/bloc/blob/8fcf54dfea7ba51ef04c091d1a27e0da498b29f0/README.md), [packages/bloc_concurrency/README.md](https://github.com/felangel/bloc/blob/8fcf54dfea7ba51ef04c091d1a27e0da498b29f0/packages/bloc_concurrency/README.md).

### flutter/devtools

원본 측정, 실행 환경, 비용 위치를 확인하는 절차를 반영한다. 도구 설치나 한 번의 수치 확인을 성능 개선 완료로 간주하지 않는다.

검토한 파일: [README.md](https://github.com/flutter/devtools/blob/c9c5bc8e936a3f8521c2296604778c8ca49a9ade/README.md), [packages/devtools_app/README.md](https://github.com/flutter/devtools/blob/c9c5bc8e936a3f8521c2296604778c8ca49a9ade/packages/devtools_app/README.md).

### flutter/samples

공식 설계 설명과 함께 역할 경계, 데이터와 UI 분리, 테스트 가능한 외부 경계를 참고한다. 샘플 앱을 현재 자료 저장소에 복사하거나 예제의 패키지 구성을 모든 제품에 강제하지 않는다.

검토한 파일: [README.md](https://github.com/flutter/samples/blob/463e365e4842f252ffab9c6198594a504d69469f/README.md), [compass_app/README.md](https://github.com/flutter/samples/blob/463e365e4842f252ffab9c6198594a504d69469f/compass_app/README.md).

### gskinner/flutter_animate

병렬 효과와 순서 구성, 컨트롤러·어댑터 선택을 구분한다. 편리한 애니메이션 문법을 성능 우위의 근거로 삼지 않는다.

검토한 파일: [README.md](https://github.com/gskinner/flutter_animate/blob/62c12040b1e3f80403b4fbfa48649155df006eb5/README.md).

### gskinnerTeam/flutter-wonderous-app

실제 스타일 파일의 역할 분리와 제품별 시각 표현을 참고한다. 예제의 최소 화면 크기, 글로벌 접근 방식, 모든 효과를 베이스의 필수 규칙으로 복사하지 않는다.

검토한 파일: [README.md](https://github.com/gskinnerTeam/flutter-wonderous-app/blob/747b945a7e5239356bf2664261aa2f3b020b8898/README.md), [lib/styles/styles.dart](https://github.com/gskinnerTeam/flutter-wonderous-app/blob/747b945a7e5239356bf2664261aa2f3b020b8898/lib/styles/styles.dart).

### jonahwilliams/flutter_shaders

픽셀 효과의 입력, 샘플링 영역, 샘플러와 숫자 입력의 계약을 참고한다. GPU 효과가 항상 빠르다고 가정하지 않으며 미지원 환경의 대체 표현을 요구한다.

검토한 파일: [README.md](https://github.com/jonahwilliams/flutter_shaders/blob/9d99a2ff207a3ce3552a6bffd724402bd3a3e05f/README.md).

### nextlevelbuilder/ui-ux-pro-max-skill

사용자 맥락 및 실제 스택 확인, 공통 규칙과 화면별 예외의 분리를 참고한다. 검색 결과를 정답으로 취급하거나 패키지 설치·외부 코드 실행을 자동 수행하지 않는다.

검토한 파일: [README.md](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/58c220ff9d02be80523b06c03471925c52e8ab5d/README.md), [.claude/skills/ui-ux-pro-max/SKILL.md](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/58c220ff9d02be80523b06c03471925c52e8ab5d/.claude/skills/ui-ux-pro-max/SKILL.md).

### obra/superpowers

질문을 통한 요구 정리, 범위에 맞는 설계 기록, 검증 근거를 적용한다. 모든 작업의 반복 승인, 무조건적인 하위 에이전트 실행, 모든 변경에 대한 동일한 테스트 절차는 그대로 도입하지 않는다.

검토한 파일: [README.md](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/README.md), [skills/brainstorming/SKILL.md](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/brainstorming/SKILL.md), [skills/writing-plans/SKILL.md](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/writing-plans/SKILL.md), [skills/verification-before-completion/SKILL.md](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/verification-before-completion/SKILL.md).

### rive-app/rive-flutter

인터랙티브 에셋이 필요한 경우의 후보로 다루고 실제 런타임 버전과 해제 책임을 확인한다. 오래된 README의 플래그를 현재 SDK에 무조건 적용하지 않으며 애니메이션 상태를 결제·권한 상태의 근거로 쓰지 않는다.

검토한 파일: [README.md](https://github.com/rive-app/rive-flutter/blob/9bb8f7f4a06db6c1472eb073eb39837ea2a81a86/README.md).

### rrousselGit/riverpod

상태 소유권과 수명, 무효화, 정리 훅, 캐시 상한을 검토한다. 자동 해제를 외부 요청 취소의 증거로 보거나 기존 상태관리의 무조건적 교체를 요구하지 않는다.

검토한 파일: [README.md](https://github.com/rrousselGit/riverpod/blob/693a2dbc59db145f1258449dfea8f417810a2404/README.md), [website/docs/concepts2/auto_dispose.mdx](https://github.com/rrousselGit/riverpod/blob/693a2dbc59db145f1258449dfea8f417810a2404/website/docs/concepts2/auto_dispose.mdx).

### shadcn-ui/ui

AI가 실제 컴포넌트와 사용 예제를 읽고 기존 규칙으로 조합하도록 한다. 웹 컴포넌트나 React 상태관리 코드를 Flutter 프로젝트에 이식하지 않는다.

검토한 파일: [README.md](https://github.com/shadcn-ui/ui/blob/71e50952fbb7eda2c992660d36cd58671a2edf42/README.md).

### vercel-labs/agent-skills

작업 범위와 관련 기준을 읽고 근거가 있는 발견을 보고하는 구조를 참고한다. 외부 문서가 사용자 지시보다 우선하거나 자동으로 추가 권한을 부여하지 않는다.

검토한 파일: [skills/web-design-guidelines/SKILL.md](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/web-design-guidelines/SKILL.md).

### vercel-labs/web-interface-guidelines

의미 있는 이름, 입력 보존, 포커스, 긴 콘텐츠, 모션 감소를 Flutter의 의미 정보와 입력 체계에 맞게 반영한다. DOM·ARIA·CSS 전용 구현, 고정된 목록 길이 기준, 애니메이션 속성 규칙을 Flutter에 그대로 복제하지 않는다.

검토한 파일: [command.md](https://github.com/vercel-labs/web-interface-guidelines/blob/e3d624baaf29dc1fc645aff3e38f03e564d2d6b1/command.md).

### widgetbook/widgetbook

반복 사용하는 실제 컴포넌트로 결정적인 상태 예제를 만들도록 한다. 별도 시연용 위젯이나 유료 호스팅 서비스를 필수로 도입하지 않는다.

검토한 파일: [README.md](https://github.com/widgetbook/widgetbook/blob/66c1eb2f002aab2c90cceddff9f7a84db1959dc2/README.md).

## 공식 문서와 언어 정책

다음 공식 자료도 확인했다. 일부 Flutter 문서는 3.44.7 기준이라고 표시되어 있고, 원본 베이스에 포함된 SDK 설정 예시는 3.47.2다. 이 차이를 실제 앱의 호환성 검증으로 대체하지 않는다. API 사용 시 대상 버전의 공식 문서와 실행 결과가 우선한다.

- [Flutter 아키텍처 권장 사항](https://docs.flutter.dev/app-architecture/recommendations): 역할 분리와 조건부 도메인 계층, 상태관리 선택의 적용 조건.
- [Flutter 성능 지침](https://docs.flutter.dev/perf/best-practices): 실제 비용 측정, 빌드·레이아웃·그리기·레이어 비용의 구분.
- [Flutter 프래그먼트 셰이더](https://docs.flutter.dev/ui/design/graphics/fragment-shaders): 입력 계약·좌표·성능 및 Canvas와 ImageFilter 사용 조건 구분.
- [Flutter 격리 실행](https://docs.flutter.dev/perf/isolates): 실행 비용과 웹의 compute 동작 차이.
- [Flutter 적응형 설계](https://docs.flutter.dev/ui/adaptive-responsive/best-practices): 가용 공간·입력·상태 보존.
- [Flutter 접근성](https://docs.flutter.dev/ui/accessibility-and-internationalization/accessibility), [WCAG 2.2 빠른 참조](https://www.w3.org/WAI/WCAG22/quickref/): 의미 정보·입력·대비·크기·모션 관련 검토 기준. 자동 검사 통과를 법적 준수 보증으로 표현하지 않는다.
- [Rive Flutter 런타임](https://rive.app/docs/runtimes/flutter/flutter), [파일 수명](https://rive.app/docs/runtimes/caching-a-rive-file): 설치한 버전과 리소스 소유권을 확인하는 근거.

**영어의 보편적 우위는 검증하지 않았다.** 개정한 실행 본문을 영어로 쓴 이유는 기술 용어와 원본 대조를 일관되게 하고 중복 번역으로 생기는 정책 차이를 줄이기 위해서다. 사용자 질문·설명·README는 한국어이며 제품 문구는 제품 언어를 따른다. 실제 지침의 효과는 구조 검사 외에 사용자 요청 형태의 스킬 적용으로 확인하고 한계를 기록한다.

새 디자인의 실행 순서는 [디자인 작업 절차](design/DESIGN_WORKFLOW.md), 파일별 사용법은 [프롬프트 지도](../prompts/README.md)에서 확인한다.
