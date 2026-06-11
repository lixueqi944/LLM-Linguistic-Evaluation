import json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")

with open("data/test_sentences.json", "r", encoding="utf-8") as f:
    test_sentences = json.load(f)
with open("config/manual_results.json", "r", encoding="utf-8") as f:
    manual_data = json.load(f)

# Load Doubao auto results from _last_results.json
doubao_results = {}
if os.path.exists("reports/_last_results.json"):
    with open("reports/_last_results.json", "r", encoding="utf-8") as f:
        all_auto = json.load(f)
    for name, data in all_auto.items():
        if data.get("status") == "completed":
            doubao_results[name] = data
            dname = data.get("display", name)
            dacc = data.get("accuracy", 0)
            print(f"Loaded auto results: {dname} ({dacc:.1f} percent)")


def score_response(s, response):
    resp_lower = response.lower().strip()
    scores = {}
    def get_letters_in_order(resp):
        result = []
        for line in resp.splitlines():
            for c in line.strip().upper():
                if c in "ABCD":
                    result.append(c)
                    break
        return result
    def contains_text(text):
        t = text.lower().strip()
        return t in resp_lower or resp_lower in t
    def correct_letter_for_task(task):
        if not task.get("options"):
            return None
        try:
            idx = task["options"].index(task["expected"])
            return chr(ord("A") + idx)
        except ValueError:
            return None
    if s["phenomenon"] == "双重否定":
        t = s["task"]
        if contains_text(t["expected"]):
            scores[t["type"]] = 1
        elif t.get("options"):
            correct_letter = correct_letter_for_task(t)
            scores[t["type"]] = 1 if correct_letter and correct_letter.lower() in resp_lower else 0
        else:
            scores[t["type"]] = 0
    elif s["phenomenon"] in ["相互代词", "双重属格"]:
        letters = get_letters_in_order(response)
        resp_lines = response.splitlines()
        for i, task in enumerate(s["tasks"]):
            task_line = resp_lines[i].lower().strip() if i < len(resp_lines) else ""
            exp = task["expected"].lower().strip()
            if exp in task_line or task_line in exp:
                scores[task["type"]] = 1
            elif task.get("options"):
                correct_letter = correct_letter_for_task(task)
                if not correct_letter:
                    scores[task["type"]] = 0
                elif i < len(letters) and letters[i] == correct_letter:
                    scores[task["type"]] = 1
                elif correct_letter.lower() in task_line:
                    scores[task["type"]] = 1
                else:
                    scores[task["type"]] = 0
            else:
                scores[task["type"]] = 0
    else:
        for task in s.get("tasks", []):
            scores[task["type"]] = 1 if contains_text(task["expected"]) else 0
    return scores

def parse_full_response(text):
    """Parse a model full response into {id: text}."""
    lines = text.strip().split(chr(10))
    result = {}
    all_ids = [x["id"] for x in test_sentences]
    # Strategy 1: line starts with known ID
    cid = None; cl = []
    for line in lines:
        ls = line.strip()
        if not ls: continue
        found = None
        for sid in all_ids:
            if ls.startswith(sid) or ls.startswith(sid + ":") or ls.startswith(sid + " "):
                found = sid; break
        if found:
            if cid and cl: result[cid] = chr(10).join(cl).strip()
            cid = found
            after = ls[len(found):].lstrip(": ")
            cl = [after] if after else []
        elif cid: cl.append(ls)
    if cid and cl: result[cid] = chr(10).join(cl).strip()
    if len(result) >= 20: return result
    # Strategy 2: "--- Item N: ID ---"
    import re as _re
    r2 = {}; cid = None; cl = []
    ip = _re.compile(r"---\s*Item\s+\d+\s*:\s*([A-Z]{2}-\d+)\s*---")
    for line in lines:
        ls = line.strip()
        if not ls: continue
        m = ip.match(ls)
        if m:
            if cid and cl: r2[cid] = chr(10).join(cl).strip()
            cid = m.group(1); cl = []
        elif cid: cl.append(ls)
    if cid and cl: r2[cid] = chr(10).join(cl).strip()
    if len(r2) >= 20: return r2
    # Strategy 2b: "Item N: answer" format
    r2b = {}
    item_pat = _re.compile(r"Item\s+(\d+)\s*:\s*(.+)")
    for line in lines:
        ls = line.strip()
        if not ls: continue
        m = item_pat.match(ls)
        if m:
            num = int(m.group(1))
            ans = m.group(2).strip()
            if 1 <= num <= len(test_sentences):
                if " / " in ans:
                    parts = ans.split(" / ")
                    r2b[test_sentences[num-1]["id"]] = chr(10).join(p.strip() for p in parts)
                else:
                    r2b[test_sentences[num-1]["id"]] = ans
    if len(r2b) >= 20: return r2b
    
    # Strategy 3: sequential
    ne = [l.strip() for l in lines if l.strip()]
    ne = [l for l in ne if not ip.match(l)]
    if len(ne) >= 26:
        idx = 0; r3 = {}
        for s in test_sentences:
            if idx >= len(ne): break
            if s["phenomenon"] == "双重否定":
                r3[s["id"]] = ne[idx]; idx += 1
            else:
                nt = len(s["tasks"])
                if idx + nt <= len(ne):
                    r3[s["id"]] = chr(10).join(ne[idx:idx+nt]); idx += nt
                else: break
        if len(r3) >= 20: return r3
    return result if len(result) >= len(r2) else r2

# ===== MAIN =====
print("=" * 60)
print("IMPORTING MANUAL RESULTS")
print("=" * 60)

all_model_results = {}

for model_key, model_info in manual_data["models"].items():
    display = model_info["display"]
    full_resp = model_info.get("full_response", "").strip()
    existing = model_info.get("responses", {})
    print(f"\n--- {display} ---")
    parsed = {}
    if full_resp:
        parsed = parse_full_response(full_resp)
        print(f"  Parsed {len(parsed)}/{len(test_sentences)} items")
    for sid in existing:
        if existing[sid].strip(): pass
        elif sid in parsed and parsed[sid]:
            existing[sid] = parsed[sid]
    filled = sum(1 for v in existing.values() if v.strip())
    print(f"  Filled: {filled}/{len(existing)}")
    if filled == 0:
        print("  No results. Skipping.")
        all_model_results[model_key] = {"status": "pending", "display": display}
        continue
    results = []; total_tasks = 0; correct = 0
    for s in test_sentences:
        resp = existing.get(s["id"], "").strip()
        if not resp: continue
        scores = score_response(s, resp)
        results.append({"id": s["id"], "response": resp, "scores": scores})
        for v in scores.values(): total_tasks += 1; correct += v
    acc = (correct / total_tasks * 100) if total_tasks > 0 else 0
    all_model_results[model_key] = {"status": "completed", "display": display, "results": results, "accuracy": acc, "correct": correct, "total": total_tasks}
    print(f"  Accuracy: {correct}/{total_tasks} = {acc:.1f}%")

with open("config/manual_results.json", "w", encoding="utf-8") as f:
    json.dump(manual_data, f, ensure_ascii=False, indent=2)
print("\nUpdated manual_results.json.")

# Add auto results (Doubao) to the comparison
for name, data in doubao_results.items():
    all_model_results[name] = data

completed = {k: v for k, v in all_model_results.items() if v.get("status") == "completed"}
if completed:
    print("\nGenerating comparison report...")
    ts = time.strftime("%Y%m%d_%H%M%S")
    fname = f"reports/evaluation_report_full_{ts}.md"
    lines = [
        "# Linguistic Competence Across Four LLMs: An Evaluation Report",
        f"- Generated: {time.strftime('%Y-%m-%d %H:%M')}",
        f"- Models: {', '.join(v['display'] for v in completed.values())}",
        "",
        "## Results Summary",
        "| Model | Type | Accuracy | Correct / Total |",
        "|---|---|---|---|",
    ]
    for name, data in completed.items():
        model_type = "Auto (API)" if name in doubao_results else "Manual"
        lines.append(f"| {data.get("display")} | {model_type} | {data.get("accuracy",0):.1f}% | {data.get("correct",0)}/{data.get("total",0)} |")
    lines.append("")
    for pk, pn in [("双重否定","Double Negation"),("相互代词","Reciprocal Pronouns"),("双重属格","Double Genitive")]:
        ps = [s for s in test_sentences if s["phenomenon"] == pk]
        if not ps: continue
        lines.append(f"### {pn}")
        for name, data in completed.items():
            lines.append(f"**{data.get("display")}**:")
            lines.append("| ID | Sentence (abbreviated) | Expected Answer | Model Response | Correct? |")
            lines.append("|---|---|---|---|---|")
            for r in data["results"]:
                s = next((x for x in ps if x["id"] == r["id"]), None)
                if not s: continue
                if pk == "双重否定":
                    exp = s["task"]["expected"]
                    sc = chr(10003) if r["scores"].get(s["task"]["type"], 0) == 1 else chr(10007)
                    lines.append(f"| {r['id']} | {s['sentence'][:50]}... | {exp} | {r['response'][:40]} | {sc} |")
                else:
                    exp = "; ".join(t["expected"] for t in s.get("tasks", [s.get("task")]))
                    all_ok = all(v == 1 for v in r["scores"].values())
                    sc = chr(10003) if all_ok else chr(10007)
                    lines.append(f"| {r['id']} | {s['sentence'][:50]}... | {exp} | {r['response'][:40]} | {sc} |")
            lines.append("")
    lines.append("---")
    lines.append("*Report structure adapted from linguistic evaluation methodology*")
    lines.append(f"*{time.strftime('%Y-%m-%d %H:%M')}*")
    with open(fname, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  Report saved to: {fname}")
# Add auto results (Doubao) to the comparison
for name, data in doubao_results.items():
    all_model_results[name] = data

leted = {k: v for k, v in all_model_results.items() if v.get("status") == "completed"}
if not completed:
        print("\nNo completed results to report.")

print("Done!")
