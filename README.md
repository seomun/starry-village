# Starry Village — HTML5 꾸미기 연속극 IP 프로젝트

여아 타깃 드레스업 + 짧은 스토리 → 쇼츠/블로그 파생 → 캐릭터 IP. 상세는 `CLAUDE.md`, `docs/00_MASTER.md`.

## 파일 역할
| 경로 | 역할 |
|---|---|
| `CLAUDE.md` | 원칙·구조·작업 방식 (진입점) |
| `HANDOFF.md` | 현재 상태·다음 할 일 |
| `docs/00_MASTER.md` | IP 전략·세계관·라인업·단계·KPI·툴 종합 |
| `docs/01_WORLD_BIBLE.md` | 세계관·캐릭터 DNA·아트 3단 규칙·프롬프트 템플릿·텍스트 규칙 |
| `docs/02_GAME01_SPEC.md` | 1호 Dress Story 화면·루프·스키마·완료조건 |
| `docs/03_CONTENT_PIPELINE.md` | Story Seed → 게임/일러/쇼츠/블로그 |
| `docs/04_ANTIGRAVITY_HANDOFF.md` | 다른 코딩 툴로 넘기는 절차 |
| `data/characters.json` | 캐릭터 id·색·이미지 경로 |
| `data/costumes.json` | 의상 id·파츠 레이어·Hero 이미지 |
| `data/stages/stage_NNN.json` | 스테이지(상황·의상·대사 variant·사건·보상·히든·다음) |
| `games/dress-story/index.html` | 1호 게임(단일 파일) |
| `assets/` | 이미지(id 로만 참조) |
| `content/` | 시드·쇼츠·블로그·일러 |
| `tools/check_stage.py` | 스테이지 JSON 규칙 검사 |
| `DECISIONS.md` / `DEVLOG.md` / `bugs_log.csv` | 결정·일지·버그 |

## 실행
```
python -m http.server 8080
# → http://localhost:8080/games/dress-story/   (폰: http://<PC IP>:8080/games/dress-story/)
python tools/check_stage.py
```
