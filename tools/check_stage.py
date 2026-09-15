"""스테이지 JSON 규칙 검사. python tools/check_stage.py [stage_file...]
규칙: 대사 한 줄 40자 이내, 스테이지당 대사 6줄 이내(intro+variant 1개+event 기준),
who 는 characters.json 에 있어야, costume 은 costumes.json 에 있어야, closing_question 필수."""
import json, sys, glob, os
sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def load(p):
    with open(p, encoding="utf-8") as f: return json.load(f)
chars = load(os.path.join(ROOT, "data/characters.json"))
costumes = load(os.path.join(ROOT, "data/costumes.json"))
files = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, "data/stages/stage_*.json")))
bad = 0
for fp in files:
    s = load(fp); errs = []
    d = s.get("dialogue", {})
    def lines(seq, tag):
        for i, l in enumerate(seq):
            if l["who"] not in chars: errs.append(f"{tag}[{i}] who '{l['who']}' 없음")
            if len(l["text"]) > 40: errs.append(f"{tag}[{i}] {len(l['text'])}자 > 40")
    lines(d.get("common_intro", []), "intro"); lines(d.get("event", []), "event")
    for cid in s.get("costume_choices", []):
        if cid not in costumes: errs.append(f"costume '{cid}' 없음")
        v = d.get("variant", {}).get(cid)
        if v is None: errs.append(f"variant '{cid}' 없음")
        else:
            lines(v, f"variant[{cid}]")
            n = len(d.get("common_intro", [])) + len(v) + len(d.get("event", []))
            if n > 6: errs.append(f"variant[{cid}] 총 {n}줄 > 6")
    if not d.get("closing_question"): errs.append("closing_question 없음")
    for l in s.get("hidden", {}).get("scene", []):
        if l["who"] not in chars: errs.append(f"hidden who '{l['who']}' 없음")
    uc = s.get("reward", {}).get("unlock_costume")
    if uc and uc not in costumes: errs.append(f"unlock_costume '{uc}' 없음")
    name = os.path.basename(fp)
    if errs: bad += 1; print(f"[FAIL] {name}"); [print("   -", e) for e in errs]
    else: print(f"[ OK ] {name}")
sys.exit(1 if bad else 0)
