# 02. 1호 「Dress Story」 개발 명세 v0.1

목표: **10분 안에 완주 가능한 프로토타입**. Stage 1~3. 플레이스홀더 아트로 시작.
성공 기준은 "코드가 돌아간다"가 아니라 **폰 브라우저에서 NEXT 를 누르고 싶어지는가**.

## 1. 기술
- `games/dress-story/index.html` 단일 파일. vanilla JS, CSS. 외부 라이브러리 0.
- 기준 해상도 360×640 세로. `viewport` 고정, 화면은 letterbox 로 비율 유지.
- 데이터는 `../../data/*.json` 을 fetch. `file://` 로 열면 fetch 가 막히므로
  **개발 시 `python -m http.server 8080`** (프로젝트 루트) 후 `http://localhost:8080/games/dress-story/`.
  배포 시엔 빌드 스크립트(`tools/inline_data.py`, 나중에)로 JSON 을 인라인.
- 저장: localStorage 키 `sv.dressstory.v1` = `{stage, stardust, affection, album[], costumes[]}`.
- 이미지 누락 시 **색 박스 + id 텍스트**로 대체(플레이스홀더 모드). 개발 중 이미지 없이도 완주 가능해야 함.

## 2. 화면 (6개)
| # | 화면 | 요소 |
|---|---|---|
| S0 | Title | 로고 텍스트, [시작], [이어하기](저장 있을 때), 별조각 표시 |
| S1 | Story-Intro | 배경, 별이 아이콘, 상황 1줄, [옷 고르러 가기] |
| S2 | DressUp | 리아 Game Form(파츠 레이어), 하단 의상 카드 3~5(가로 스크롤), 선택 즉시 미리보기, [이 옷으로!] |
| S3 | Scene | 결과 이미지(Hero 자리, 없으면 Game Form 확대), 대사창(이름+한 줄, 탭으로 다음), 등장인물 초상 좌/우 |
| S4 | Reward | 별조각 +N 애니, 호감도 ♥, 히든 발견 시 뱃지, [다음 이야기 →] |
| S5 | Album | 클리어 스테이지 목록, 히든 수집 여부, 재플레이 버튼 |

## 3. 루프
```
S0 → S1(situation) → S2(costume 선택) → S3(dialogue[variant]) → S4(reward) → S1(next)
                                   └ 재플레이 + hidden.condition 충족 → S3 뒤 hidden scene → S4 뱃지
```
S3 대사는 `common_intro` → `variant[costume_id]` (2줄) → `event` → `closing_question` 순.

## 4. 데이터 스키마

### data/characters.json
```json
{ "ria": { "name": "리아", "color": "#F4A7B9", "portrait": "assets/characters/ria/portrait.png",
           "game_layers": { "body": "...", "hair_back": "...", "face": "...", "hair_front": "...", "hair_acc": "..." },
           "expressions": { "joy": "...", "surprise": "...", "shy": "...", "angry": "...", "sad": "...", "love": "..." } },
  "prince": { "name": "???", "reveal_name": "루안", "color": "#2E3A59", "portrait": "..." } }
```
왕자는 `name` 이 "???" 이고 특정 스테이지(`reveal_stage`) 이후 `reveal_name` 으로 바뀐다.

### data/costumes.json
```json
{ "c001": { "name": "크림 원피스", "tags": ["basic"], "price": 0,
            "layers": { "dress": "assets/costumes/c001/dress.png", "shoes": "...", "bag": null },
            "hero": "assets/costumes/c001/hero.png", "color": "#FFF4E0" } }
```

### data/stages/stage_001.json
```json
{ "id": 1, "title": "첫 번째 별빛 파티", "place": "studio",
  "background": "assets/backgrounds/studio.png",
  "situation": "오늘 밤은 별빛 파티! 리아, 입고 갈 옷이 없어…",
  "costume_choices": ["c001", "c002", "c003"],
  "dialogue": {
    "common_intro": [ { "who": "star", "text": "와, 리아! 오늘 진짜 예쁘다!" } ],
    "variant": {
      "c001": [ { "who": "goofy", "text": "그… 그 옷! 내가 본 적 있는데?!" },
                { "who": "ria",   "text": "…어디서?" } ],
      "c002": [ { "who": "rival", "text": "흥. 그 드레스, 어디서 났어?" },
                { "who": "ria",   "text": "비밀이야." } ],
      "c003": [ { "who": "prince","text": "오늘… 조금 달라 보이네요." },
                { "who": "ria",   "text": "…누구세요?" } ] },
    "event": [ { "who": "star", "text": "그때, 파티장의 불이 꺼졌다!" },
               { "who": "prince","text": "괜찮아요. 잠깐이면 돼요." } ],
    "closing_question": "…저 사람, 왜 이렇게 침착하지?" },
  "reward": { "stardust": 100, "affection": 1, "unlock_costume": "c004" },
  "hidden": { "condition": { "replay": true, "costume": "c003" },
              "scene": [ { "who": "prince", "text": "(혼잣말) 아직 아무것도 모르는군." } ],
              "badge": "prince_secret_01" },
  "next": 2 }
```
`who` 는 characters.json 의 id. 텍스트 규칙(40자/6줄)은 `tools/check_stage.py` 로 검사.

### Stage 1~3 골자 (대사는 위 규칙대로 채운다)
| Stage | 장소 | 사건 | 등장 | 떡밥 |
|---|---|---|---|---|
| 1 첫 번째 별빛 파티 | 스튜디오→광장 | 파티 불이 꺼짐, 낯선 남자가 침착하게 해결 | 별이·허당·엘라·왕자 | 왜 침착하지? |
| 2 카페에서의 우연 | 문라이트 카페 | 남자가 물건을 떨어뜨리고 리아가 주워줌. 회중시계 | 별이·왕자·엘라(스쳐감) | 시계에 왕궁 문양? |
| 3 이름을 아는 남자 | 플라워 가든 | 남자가 리아의 이름을 부름. 리아는 말한 적 없음 | 별이·왕자·허당 | 왜 내 이름을? → TO BE CONTINUED |

## 5. UI 규칙
- 터치 목표 최소 48px. NEXT 버튼은 화면 하단 전폭, 가장 눈에 띄는 색(골드).
- 대사창: 화면 하단 1/3, 탭으로 진행, 자동 진행 없음. 한 줄 40자 초과 시 콘솔 경고.
- 폰트: 시스템 sans-serif(외부 폰트 로드 없음). 제목만 굵게.
- 색: 배경 크림 `#FFF8F0`, 포인트 로즈핑크 `#F4A7B9`, 골드 `#F5C542`, 텍스트 `#3A2E39`.

## 6. 코드 구조 (index.html 내부 섹션, 이 순서로)
```
<!-- 1. CONFIG -->      상수, 경로, 저장키
<!-- 2. DATA LOAD -->   characters/costumes/stages fetch + 플레이스홀더 폴백
<!-- 3. STATE -->       game state, save/load
<!-- 4. RENDER -->      screen 별 render 함수 (renderTitle, renderDressUp, …)
<!-- 5. FLOW -->        goto(screen), nextStage(), replay()
<!-- 6. DIALOGUE -->    라인 큐, 탭 진행, variant 선택
<!-- 7. ADS -->         showRewardedAd(cb) 스텁 — 즉시 cb(true)
<!-- 8. BOOT -->
```
함수 하나 = 화면 하나. 전역은 `G`(state) 와 `D`(data) 두 개만.

## 7. 완료 기준 (P1)
- [ ] `http.server` 로 열어 Stage 1→3 완주, 저장 후 새로고침해도 이어하기 됨
- [ ] 이미지 0장 상태에서도 플레이스홀더로 완주 가능
- [ ] 의상 3개 각각 골랐을 때 variant 대사만 다르고 보상 동일
- [ ] Stage 1 재플레이 + c003 선택 시 히든 장면 + 앨범 뱃지
- [ ] 폰(안드로이드 크롬) 실기 확인 스크린샷 3장 → `notes/`
- [ ] `tools/check_stage.py` 통과 (40자/6줄/who 유효/costume 존재)

## 8. 하지 않는 것 (v0.1)
IAP, 실제 광고 SDK, 서버 저장, 스토리 분기, 음악(효과음 1~2개는 가능), 다국어, 30스테이지.
