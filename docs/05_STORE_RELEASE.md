# 05. 스토어 출시 절차 (Google Play · App Store)

목표: "그냥 올려본다". 6스테이지, 광고·결제·서버 없음. 이게 정책상 가장 쉬운 형태다.

## 0. 산출물 (이 PC 에서 만들어짐)
| 것 | 위치 | 만드는 명령 |
|---|---|---|
| 웹(PWA) | 저장소 루트 → GitHub Pages | push 만 하면 됨 |
| 자기완결 dist | `dist/` | `python tools/build_dist.py` |
| 안드로이드 프로젝트 | `android/` (Capacitor) | `npx cap sync android` |
| 디버그 APK | `android/app/build/outputs/apk/debug/app-debug.apk` | `cd android && ./gradlew assembleDebug` |
| **릴리스 AAB** (Play 제출용) | `android/app/build/outputs/bundle/release/app-release.aab` | `cd android && ./gradlew bundleRelease` |
| 서명 키 | `C:\Users\gurud\.keys\dressstory-upload.jks` + `dressstory-keystore.properties` | 생성 완료. **백업 필수**(잃으면 앱 업데이트 불가) |

게임 내용을 고친 뒤: `python tools/build_dist.py` → `npx cap sync android` → `bundleRelease`. `versionCode` 를 `android/app/build.gradle` 에서 +1.

## 1. Google Play (이 PC 에서 끝까지 가능)
1. https://play.google.com/console — 개발자 계정(1회 $25).
2. 앱 만들기: 이름 "Dress Story", 기본 언어 한국어, 앱, 무료.
3. **정책 설문** (드레스업 = 아동 지향 판단 요소, CLAUDE.md 1-8):
   - 타깃 연령: "13세 미만 포함" 선택 → **Families 정책** 적용됨. 광고·결제 없으므로 통과 가능.
   - 광고: 없음. 데이터 안전: "수집 없음, 공유 없음". 개인정보 처리방침 URL: Pages 의 `privacy.html`.
   - 콘텐츠 등급 설문(IARC): 폭력·성·약물 없음 → 전체이용가.
   - "교사 승인(Teacher Approved)" 은 선택 심사, 나중에.
4. 스토어 등록정보: 아이콘 512(`assets/ui/icons/icon-512.png`), 기능 그래픽 1024×500(만들 것), 스크린샷 폰 2장 이상(`notes/` 헤드리스 스크린샷을 1080×1920 으로 리스케일).
   짧은 설명 80자, 전체 설명 4000자 — **사람이 쓴다.**
5. 프로덕션 → 새 버전 → `app-release.aab` 업로드 → 검토 제출. 신규 계정은 비공개 테스트 20명·14일 조건이 붙을 수 있음(2023~ 정책). 그 경우 내부 테스트 트랙으로 먼저.

## 2. App Store (Mac 필요)
- Capacitor iOS: `npm i @capacitor/ios && npx cap add ios` → `ios/` 생성은 이 PC 에서 되지만 **빌드·업로드는 Xcode(Mac)** 만 가능.
- Apple Developer $99/년. Kids Category 로 넣으면 광고·외부링크·추적 금지(우린 해당 없음 → 유리).
- 대안: Mac 없이 클라우드 Mac(Codemagic/MacStadium) 또는 지인 Mac 1회 빌드. 결정 보류 — Play 반응 먼저 본다.

## 3. 웹(PWA) — 지금 바로
GitHub Pages: `https://seomun.github.io/starry-village/` → 게임으로 리다이렉트. 폰 브라우저 "홈 화면에 추가"로 앱처럼 실행. 오프라인 재플레이 가능(sw.js).
