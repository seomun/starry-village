# 현재 상태 — Starry Village

갱신 2026-09-15 (index.html v0.1 후). 폴더 `C:\projects\starry-village`. 먼저 `CLAUDE.md` 를 읽을 것.

## 지금 있는 것
- 문서 5개(`docs/00~04`), 데이터 스키마 + Stage 1~3 JSON 샘플, 폴더 골격.
- `games/dress-story/index.html` v0.1 (2026-09-15). 스펙 §6 섹션 순서 그대로. 플레이스홀더 모드로 Stage 1~3 완주,
  저장/이어하기, 첫 클리어 보상, 별조각 의상 해금, 재플레이 히든 장면+뱃지, 앨범 동작 확인
  (헤드리스 크롬 자동 플레이 스크린샷: `notes/2026-09-15_p1_headless_playthrough.png`).
- 구현 결정: 보상(별조각·호감도·해금)은 **첫 클리어에만**. 재플레이는 앨범의 "입은 옷" 기록과 히든 뱃지만 갱신.
- 이미지 0장. GPT 캐릭터 시트(리아 2장, 레오 1장, 5인 세트 1장)는 채팅에만 있음 → `assets/characters/<id>/_concept/` 로 옮길 것.
- `tools/check_stage.py` 3개 통과.

## 다음 할 일 (순서대로)
1. 폰 실기 확인(`python -m http.server 8080` → 같은 와이파이) 스크린샷 → `notes/2026-MM-DD_p1_phone.md`.
2. **캐릭터 정본 결정**: GPT 시트(레오·예나·현·소라, 백발 왕자)와 docs/data(루안·엘라·토토·별이, 흑발 왕자)가 다름.
   시트를 따르면 `data/characters.json` + `docs/01` 만 고치면 됨(코드 무수정).
3. 리아 게임용 이미지: 시트의 3등신 전신 그림을 의상별로 잘라 **한 장짜리 전신 PNG**(투명 배경)로 → `costumes.json` 의 `dress` 경로에 넣으면 바로 보임. 파츠 분리는 그 다음.
4. 왕자·라이벌 초상 → Stage 4~6 시드 작성(`content/seeds/`).

## 열린 질문
- 왕자·허당남 이름 확정(현재 가칭 루안/토토). 리아 Hero 이미지 최종 선택.
- 쇼츠 제작 툴.

## PC 에서 처음 할 것
```
cd C:\projects\starry-village
claude --remote-control        # 폰에서 이어보기
python -m http.server 8080     # 게임 테스트용 (별도 터미널)
```
