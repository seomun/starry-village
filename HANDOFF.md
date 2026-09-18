# 현재 상태 — Starry Village

갱신 2026-09-18 (출시 준비 완료). 폴더 `C:\projects\starry-village`. 먼저 `CLAUDE.md` 를 읽을 것.

## 출시 상태 (2026-09-18)
- **웹**: https://seomun.github.io/starry-village/ (GitHub Pages, main 브랜치 루트). PWA — 폰에서 "홈 화면에 추가" 가능.
- **안드로이드**: 서명된 릴리스 AAB `android/app/build/outputs/bundle/release/app-release.aab` (versionCode 1). Play Console 에 올리기만 하면 됨 — 절차 `docs/05_STORE_RELEASE.md`.
- **서명 키**: `C:/Users/gurud/.keys/dressstory-upload.jks` + `.properties`. **다른 곳에 백업할 것.** git 에 없음.
- **iOS**: Mac 없음 → 보류. `docs/05` §2.
- 개인정보 처리방침: https://seomun.github.io/starry-village/privacy.html
- 사람이 할 일: Play Console 계정($25) → 앱 생성 → 정책 설문 → AAB 업로드. 스토어 설명문은 직접 쓴다.

## 지금 있는 것
- 문서 5개(`docs/00~04`), 데이터 스키마 + Stage 1~3 JSON 샘플, 폴더 골격.
- `games/dress-story/index.html` v0.1 (2026-09-15). 스펙 §6 섹션 순서 그대로. 플레이스홀더 모드로 Stage 1~3 완주,
  저장/이어하기, 첫 클리어 보상, 별조각 의상 해금, 재플레이 히든 장면+뱃지, 앨범 동작 확인
  (헤드리스 크롬 자동 플레이 스크린샷: `notes/2026-09-15_p1_headless_playthrough.png`).
- 구현 결정: 보상(별조각·호감도·해금)은 **첫 클리어에만**. 재플레이는 앨범의 "입은 옷" 기록과 히든 뱃지만 갱신.
- 이미지: GPT 시트 4장 `assets/characters/{ria,prince}/_concept/`, `assets/characters/_concept/cast_sheet.png`.
  시트에서 잘라 넣음(rembg `isnet-anime` 로 배경 제거): 초상 5 + 리아 표정 6 + 의상 전신 7(c001~c007) + hero 4. 배경 3장(`assets/backgrounds/`, GPT 3연작 시트를 3등분, 원본 `_concept/backgrounds_sheet.png`). `python tools/check_assets.py` → 배경 2장 없음(post_office, star_house — 플레이스홀더로 돌아감).
- P1 지름길 적용: `characters.json.game_layers` 전부 null, 의상은 `layers.dress` 전신 한 장. 파츠 분리는 P2.
- 의상 매핑(시트 기준): c001 크림 원피스(A 게임용 캐릭터) · c002 핑크 파티(B 파티룩) · c003 네이비 리본룩(B 학교룩) · c004 카페 캐주얼(B 기본복) ·
  c005 가든 플라워룩(A 기본복) · c006 하늘빛 여행룩(B 여행룩, 캐리어 포함, 200★) · c007 별꿈 잠옷(B 잠옷룩, 200★). c007 은 S4 보상, c006 은 S5 보상.
- 자르기 스크립트는 세션 스크래치에만 있었음. 다시 자를 일 있으면 좌표는 DEVLOG 2026-09-15 참고 없이 시트를 보고 새로 잡는다.
- Stage 1~6 (`data/stages/`, 시드 `content/seeds/seed_004~006.md`). 시즌 1-1 = S6 「시계탑 아래에서」에서 TO BE CONTINUED. `check_stage.py` 6개 통과.
  S4 우체국(편지·별 문양 도장) → S5 파자마 파티(시계탑 불빛 신호) → S6 시계탑(손수건, 레오 "못 봤군"). 정체는 아직 안 드러남(S07 무심한 해결, S12 예나 알아봄 페이스 유지).

## 다음 할 일 (순서대로) — D10: 빠른 출시가 목표. 스테이지 추가보다 배포 먼저
1. 폰 실기 확인(`python -m http.server 8080` → 같은 와이파이) 스크린샷 → `notes/2026-MM-DD_p1_phone.md`.
2. Play Console 제출(사람). 기능 그래픽 1024×500 + 스크린샷 1080×1920 은 요청하면 만들어 줌.
3. 배경 2장 GPT 생성 → `assets/backgrounds/post_office.png`, `star_house.png` (프롬프트 `assets/README.md`).
4. S7 시드: 「카페의 새 아르바이트생」 — 레오가 카페 알바로 등장, 밀린 주문을 무심한 한마디로 해결(정체 페이스 S07). 쇼츠 대본 첫 2개(S1, S5 현 화단).
5. (P2) 리아 파츠 분리 → `game_layers` 채우기.
6. (품질) 배경은 가로 941×549 라 폰에서 가운데 1/3 만 보임 + 하단에 그려진 대사창 틀. 나중에 세로 720×1280·틀 없이 재생성.

## 열린 질문
- 리아 Hero 이미지 최종 선택 (시트 2장 중).
- 쇼츠 제작 툴.

## PC 에서 처음 할 것
```
cd C:\projects\starry-village
claude --remote-control        # 폰에서 이어보기
python -m http.server 8080     # 게임 테스트용 (별도 터미널)
```
