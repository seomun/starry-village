"""자기완결 배포본 dist/ 생성 (앱 패키징용). python tools/build_dist.py
- games/dress-story/index.html 을 dist/index.html 로, CFG.ROOT '../../' → './'
- data/, assets/(컨셉 시트·README 제외), manifest, sw.js 복사. 경로의 '../../' 를 './' 로.
GitHub Pages 는 저장소 루트를 그대로 쓰므로 이 빌드가 필요 없다. Capacitor(안드로이드) 만 dist/ 를 쓴다."""
import os, shutil, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, "dist")
if os.path.exists(D): shutil.rmtree(D)
os.makedirs(D)
def rd(p): return open(os.path.join(ROOT, p), encoding="utf-8").read()
def wr(p, s): open(os.path.join(D, p), "w", encoding="utf-8", newline="\n").write(s)
html = rd("games/dress-story/index.html")
assert "ROOT: '../../'" in html
wr("index.html", html.replace("ROOT: '../../'", "ROOT: './'").replace("../../assets/", "./assets/"))
wr("manifest.webmanifest", rd("games/dress-story/manifest.webmanifest").replace("../../assets/", "./assets/"))
wr("sw.js", rd("games/dress-story/sw.js"))
shutil.copytree(os.path.join(ROOT, "data"), os.path.join(D, "data"))
shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(D, "assets"), ignore=shutil.ignore_patterns("_concept", "README.md", ".gitkeep"))
n = sum(len(f) for _, _, f in os.walk(D)); print("dist:", n, "files")
