# 04. Antigravity(또는 다른 코딩 에이전트)로 넘기는 절차

넘기는 시점: 반복 코딩량이 커질 때(스테이지 대량 추가, UI 폴리싱 반복). 설계는 넘기지 않는다.

## 1. 전제
- 진실은 `docs/` + `data/` 에만 있다. 어떤 툴이든 여기서 시작하면 같은 결과가 나와야 한다.
- 이 폴더를 그대로 Antigravity 워크스페이스로 연다. 복사본 만들지 않는다(두 진실 금지).

## 2. 첫 프롬프트 (그대로 붙여넣기)
```
이 폴더의 CLAUDE.md, HANDOFF.md, docs/02_GAME01_SPEC.md 를 읽어라.
코딩하지 말고 먼저 구현 계획을 Artifact 로 작성해라. 계획에는 (1) 수정할 파일 (2) 건드리지 않을 파일
(3) 검증 방법이 있어야 한다. 원칙: 단일 HTML, 외부 라이브러리 0, 서버 0, 데이터는 data/*.json 만,
이미지 경로 하드코딩 금지. 승인 후에만 구현한다.
```
## 3. 금지 목록 (Antigravity 가 자주 하는 것)
React/Vite 도입, npm init, 서버·DB·로그인 추가, 폴더 구조 변경, data 스키마 임의 변경, 문서 삭제.

## 4. 돌아올 때
Antigravity 작업 후 Claude Code 에서 `tools/check_stage.py` + 브라우저 완주 확인 → `DEVLOG.md` 한 줄 → 계속.

## 5. Claude Code ↔ Antigravity 분담 예
| 작업 | 담당 |
|---|---|
| 스펙·데이터 스키마 변경 | Claude Code |
| 스테이지 JSON 10개 일괄 생성 | Antigravity |
| 버그 원인 분석 | Claude Code |
| CSS 폴리싱 반복 | Antigravity |
