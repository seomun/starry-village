# 현재 상태 — Starry Village

갱신 2026-09-15. 폴더 `C:\projects\starry-village`. 먼저 `CLAUDE.md` 를 읽을 것.

## 지금 있는 것
- 문서 5개(`docs/00~04`), 데이터 스키마 + Stage 1~3 JSON 샘플, 폴더 골격.
- 코드 0줄. 이미지 0장 (리아 AI 컨셉 이미지는 ChatGPT 세션에 있음 → `assets/characters/ria/_concept/` 로 옮길 것).

## 다음 할 일 (순서대로)
1. `games/dress-story/index.html` 첫 버전 — `docs/02_GAME01_SPEC.md` §6 구조대로, 플레이스홀더 모드로 Stage 1~3 완주.
2. `tools/check_stage.py` — 40자/6줄/who/costume 검사. `python tools/check_stage.py` 로 3개 통과.
3. 폰 실기 확인(`python -m http.server 8080` → 같은 와이파이) 스크린샷 → `notes/2026-MM-DD_p1_phone.md`.
4. 리아 7종 이미지 세트 제작(01 §4 프롬프트) → 파츠 PNG 로 분리 → data 경로에 배치. 코드 수정 없이 보여야 함.
5. 왕자·엘라 초상 → Stage 4~6 시드 작성(`content/seeds/`).

## 열린 질문
- 왕자·허당남 이름 확정(현재 가칭 루안/토토). 리아 Hero 이미지 최종 선택.
- 쇼츠 제작 툴.

## PC 에서 처음 할 것
```
cd C:\projects\starry-village
claude --remote-control        # 폰에서 이어보기
python -m http.server 8080     # 게임 테스트용 (별도 터미널)
```
