"""data/*.json 이 참조하는 이미지 파일 존재 여부. python tools/check_assets.py
없는 파일은 게임에서 플레이스홀더로 뜬다. 목록을 보고 assets/ 에 채우면 코드 수정 없이 반영."""
import json, os, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def load(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f: return json.load(f)
refs = []  # (출처, 경로)
for cid, c in load("data/characters.json").items():
    if c.get("portrait"): refs.append((f"characters.{cid}.portrait", c["portrait"]))
    for k, v in (c.get("game_layers") or {}).items(): refs.append((f"characters.{cid}.game_layers.{k}", v))
    for k, v in (c.get("expressions") or {}).items(): refs.append((f"characters.{cid}.expressions.{k}", v))
for cid, c in load("data/costumes.json").items():
    for k, v in (c.get("layers") or {}).items():
        if v: refs.append((f"costumes.{cid}.layers.{k}", v))
    if c.get("hero"): refs.append((f"costumes.{cid}.hero", c["hero"]))
for fp in sorted(glob.glob(os.path.join(ROOT, "data/stages/stage_*.json"))):
    s = load(os.path.relpath(fp, ROOT))
    if s.get("background"): refs.append((f"stage_{s['id']:03d}.background", s["background"]))
seen, ok, missing = set(), 0, []
for src, p in refs:
    if p in seen: continue
    seen.add(p)
    if os.path.exists(os.path.join(ROOT, p)): ok += 1
    else: missing.append((src, p))
print(f"있음 {ok} / 없음 {len(missing)}")
for src, p in missing: print(f"  [없음] {p}   ← {src}")
