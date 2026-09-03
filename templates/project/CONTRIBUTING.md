# 프로젝트 협업 방법

`AGENTS.md`와 `docs/workflow/DEVELOPMENT_WORKFLOW.md`를 읽는다. 이슈에 문제·수락 기준·범위를 정하고 develop에서 이슈 번호가 포함된 작업 브랜치를 만든다. master·develop에는 직접 커밋하지 않고 PR로 통합한다.

기존 도구 체인과 테스트 명령을 우선한다. 선택형 개발 도구를 설치했다면 `dart run tool/verify.dart`를 사용한다. 플랫폼·결제·보안 변경은 해당 기기·서버 검증을 추가한다. 검증하지 않은 항목은 성공으로 표시하지 않는다.

PR에는 이슈·실행 계획·변경 결과·판단 이유·명령과 결과·남은 위험·복구 방법을 적는다. 비밀과 개인정보를 커밋하지 않는다. 여러 세션의 작업은 `docs/exec-plans/active/`에 기록하고 완료 후 completed로 이동한다.
