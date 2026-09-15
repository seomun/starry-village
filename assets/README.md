# assets/ — 이미지 규격

게임은 `data/*.json` 의 경로로만 이미지를 찾는다. **여기에 파일을 두면 코드 수정 없이 뜬다.**
없는 파일은 색 박스 플레이스홀더. 무엇이 없는지: `python tools/check_assets.py`.

## 폴더
| 경로 | 내용 | 규격 |
|---|---|---|
| `characters/<id>/_concept/` | GPT 캐릭터 시트 원본 (참조용, 게임이 읽지 않음) | 자유 |
| `characters/<id>/portrait.png` | 대화창 초상 (얼굴 중심, 정면) | 256×256, 투명 배경 |
| `characters/ria/exp_<joy|surprise|shy|angry|sad|love>.png` | 리아 표정 초상 | 256×256, 투명 |
| `characters/ria/game_<body|hair_back|face|hair_front|hair_acc>.png` | 3등신 파츠 레이어 (P2 이후) | 600×1080 공통 캔버스, 투명 |
| `costumes/<cid>/<dress|top|bottom|shoes|bag>.png` | 의상 파츠. 리아 파츠와 **같은 캔버스·같은 포즈** | 600×1080, 투명 |
| `costumes/<cid>/hero.png` | 장면용 전신 일러 (6~7등신, 배경 있어도 됨) | 720×1080 |
| `backgrounds/<place>.png` | 장면 배경 | 720×1280 |

## P1 지름길 (파츠 분리 전)
`game_*` 파츠 없이 **의상별 전신 한 장**을 `costumes/<cid>/dress.png` 로 두면 그 한 장이 인형 자리에 뜬다
(`characters.json` 의 `game_layers` 항목은 파일이 없으면 플레이스홀더로 겹쳐 뜨므로, 이 단계에서는
`game_layers` 값을 `null` 로 바꿔 둔다 — 데이터 변경, 코드 무수정).

## GPT 요청 프롬프트 (리아 게임용 전신, 의상 1벌 = 1장)
```
첨부한 리아 캐릭터 시트와 동일한 캐릭터(긴 갈색 웨이브, 핑크브라운 눈, 왼쪽 별 헤어핀).
3등신 SD, 정면, 팔을 몸에서 살짝 뗀 A포즈, 양발 붙임. 두꺼운 외곽선, 3~4색, 음영 적게.
의상: <의상 이름·색·특징>. 배경 투명(알파 PNG). 캔버스 600×1080, 캐릭터가 세로 90% 차지, 발끝이 캔버스 하단 5% 위.
이전에 만든 기본복 이미지와 얼굴·머리·체형·위치를 완전히 동일하게.
```
표정 초상: "같은 캐릭터, 어깨 위 정면 초상, 표정 <기쁨/놀람/부끄러움/화남/슬픔/설렘>, 256×256, 투명 배경".
